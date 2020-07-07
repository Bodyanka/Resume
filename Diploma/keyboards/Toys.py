import gspread
from telegram import *

import Diploma.Get_all as Ga
import Diploma.Functions as Kb_func

from oauth2client.service_account import ServiceAccountCredentials

order_toys = {0: '', 1: '', 2: '', 3: '', 4: '', 5: ''}
dict_list = ['Your pet:', 'Toy`s type:', 'Toy`s producer:', 'Toy`s size:', 'Toy`s amount:']
toys_num_of_filters = 5


# mass_o = [pet_o, type_o, producer_o, size_o, amount_o, price_o]

def toys_order(q, b, chat_id, mass_o, adding_time):
    creds_n = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', ['https://www.googleapis.com/auth/drive'])
    client_n = gspread.authorize(creds_n)

    customers_n = client_n.open('Diploma').worksheet("Customers")
    toys_n = client_n.open('Diploma').worksheet("Toys")

    # getting line of order
    pos = Ga.get_all_new([mass_o[0], mass_o[1], mass_o[2], mass_o[3], mass_o[4]], Ga.toys, toys_num_of_filters)[3]

    cur_am = toys_n.cell(pos + 1, 5).value
    cur_res = toys_n.cell(pos + 1, 7).value
    if cur_res == '':
        cur_res = 0

    toys_n.update_cell(pos + 1, 5, int(cur_am) - int(mass_o[4]))
    toys_n.update_cell(pos + 1, 7, int(cur_res) + int(mass_o[4]))

    id_list = customers_n.col_values(1)
    msg_id = 0

    for i in range(len(id_list)):
        if id_list[i] == str(chat_id):
            msg_id = customers_n.cell(i + 1, 5).value

            customers_n.insert_row(
                ['', '', '', '', '', '', '', adding_time,
                 mass_o[0], mass_o[1], mass_o[2], mass_o[3], mass_o[4], int(mass_o[5]) * int(mass_o[4])], i + 2)

    b.deleteMessage(chat_id=q['message']['chat']['id'], message_id=q['message']['message_id'])

    b.send_message(chat_id=q['message']['chat']['id'],
                   text='Thanks, your order is being processed!',
                   reply_markup=InlineKeyboardMarkup(
                       [[InlineKeyboardButton('New order', callback_data='New order')]]))

    b.send_message(chat_id=341219282,
                   text='===New order===\n' +
                        'Pet: ' + mass_o[0] + '\n' +
                        'Type: ' + mass_o[1] + '\n' +
                        'Producer: ' + mass_o[2] + '\n' +
                        'Size: ' + mass_o[3] + '\n' +
                        'Amount: ' + mass_o[4] + '\n' +
                        'Price: ' + str(int(mass_o[5]) * int(mass_o[4])) + '\n' +
                        'Chat_id: ' + str(chat_id))

    b.forward_message(chat_id=341219282,
                      from_chat_id=chat_id,
                      message_id=msg_id)

    Ga.toys = client_n.open('Diploma').worksheet("Toys").get_all_values()


def toys(q, d, b, chat_id, mass_o, adding_time):
    if d == "toys":
        Kb_func.ty = 1
        Kb_func.fd = 0
        Kb_func.forward(q, d, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 0)

    elif d in Ga.t_pet and Kb_func.ty == 1:
        Kb_func.forward(q, d, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 1)

    elif d in Ga.t_type and Kb_func.ty == 1:
        Kb_func.forward(q, d, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 2)

    elif d in Ga.t_producer and Kb_func.ty == 1:
        Kb_func.forward(q, d, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 3)

    elif d in Ga.t_size and Kb_func.ty == 1:
        Kb_func.forward(q, d, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 4)

    elif d in [str(x) for x in range(1, Ga.get_max(Ga.toys, 4) + 1)] and Kb_func.ty == 1:
        Kb_func.forward(q, d, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 5, 'add_toys', 't_6')

    elif d == 'add_toys' and Kb_func.ty == 1:
        toys_order(q, b, chat_id, mass_o, adding_time)
        Kb_func.ty = 0

    elif d == 't_1':
        Kb_func.back(q, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, -1)

    elif d == 't_2':
        Kb_func.back(q, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 0)

    elif d == 't_3':
        Kb_func.back(q, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 1)

    elif d == 't_4':
        Kb_func.back(q, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 2)

    elif d == 't_5':
        Kb_func.back(q, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 3)

    elif d == 't_6':
        Kb_func.back(q, b, Ga.toys, toys_num_of_filters, order_toys, dict_list, 4)

import time
import gspread
from telegram import *
import Diploma.Get_all as Ga
from oauth2client.service_account import ServiceAccountCredentials

admins = ['341219282']
promo_code = 'promo'

fd = 0
ty = 0


def new_customer(cus, chat_id, name, second_name, username, phone_number="", adding_time=time.asctime()):
    exist = 'not exist'

    id_list = cus.col_values(1)

    for i in range(len(id_list)):
        if id_list[i] == '':
            id_list[i] = '0'

    for customers_id in id_list[4:]:
        if int(customers_id) == int(chat_id):
            print('User exist: ' + str(username))
            exist = 'exist'

    if exist == 'not exist':  # если не входит - добавить нового покупателя
        print('New user: ' + str(username))
        cus.insert_row([chat_id, name, second_name, username, '', phone_number, adding_time], 5)


def do_start(bot: Bot, update: Update, optional='no'):
    global promo_code

    scope_n = ['https://www.googleapis.com/auth/drive']
    creds_n = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope_n)
    client_n = gspread.authorize(creds_n)

    customers_n = client_n.open('Diploma').sheet1

    new_customer(customers_n,
                 chat_id=update['message']['chat']['id'],
                 name=update['message']['chat']['first_name'],
                 second_name=update['message']['chat']['last_name'],
                 username=update['message']['chat']['username'],
                 adding_time=time.asctime())

    chat_id = update['message']['chat']['id']
    msg_id = update['message']['message_id']

    id_list = customers_n.col_values(1)

    for i in range(len(id_list)):
        if id_list[i] == str(chat_id):
            customers_n.update_cell(i + 1, 5, msg_id)

    if optional == promo_code:
        for j in range(len(id_list)):
            if id_list[j] == str(chat_id):
                if customers_n.cell(j + 1, 15).value != promo_code:
                    bot.send_message(chat_id=chat_id, text='Promo code activated!')
                    customers_n.update_cell(j + 1, 15, optional)
                else:
                    bot.send_message(chat_id=chat_id, text='This promo code has already been activated!')

    bot.send_message(chat_id=chat_id, text="Choose a category:", reply_markup=Ga.category())


def contact_callback(bot: Bot, update: Update):
    print('contact')
    scope_n = ['https://www.googleapis.com/auth/drive']
    creds_n = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope_n)
    client_n = gspread.authorize(creds_n)

    customers_n = client_n.open('Diploma').sheet1

    contact = update.effective_message.contact
    phone = contact.phone_number

    chat_id = update['message']['chat']['id']
    id_list = customers_n.col_values(1)

    for i in range(len(id_list)):
        if id_list[i] == str(chat_id):
            customers_n.update_cell(i + 1, 6, phone)


def text(bot: Bot, update: Update):
    global promo_code

    idi = str(update['message']['chat']['id'])
    texto = update['message']['text']
    mytext = texto.split('|')

    print(texto)

    if mytext[0] == 'send' and idi in admins:
        bot.send_message(chat_id=mytext[1], text=str(mytext[2][1:]))
        print(mytext)

    elif mytext[0] == promo_code:
        do_start(bot, update, promo_code)

    else:
        do_start(bot, update)


def do_help(bot: Bot, update: Update):
    texto = '/start - start of product selection\n'
    texto += '⬅️ - previous menu\n'
    texto += '🛒 - order approvement\n'
    texto += '⚠️ If your profile is hidden, please send your mobile number for communication ' \
             'using special button from smartphone'

    bot.send_message(chat_id=update.message.chat_id, text=texto)


def do_card(bot: Bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text='1234 5678 8765 4321')


def forward(q, d, b, mass, num_of_fil, dict_my, list_my, num, tp='', pp=''):

    temp = []
    for j in dict_my.values():
        temp.append(j)

    x = [temp[i] for i in range(num-1)]
    x.append(d)

    # first()
    if num == 0:
        x.pop()

    if num != num_of_fil:
        q.edit_message_text(text=list_my[num], reply_markup=Ga.get_all_new(x, mass, num_of_fil)[1])

    # обновление массива  order_feed
    if num != 0:
        dict_my[num-1] = d

    if num == num_of_fil:
        b.deleteMessage(chat_id=q['message']['chat']['id'], message_id=q['message']['message_id'])

        b.send_photo(chat_id=q['message']['chat']['id'],
                     photo=Ga.get_all_new(x, mass, num_of_fil)[1],

                     caption=Ga.get_all_new(x, mass, num_of_fil)[0],

                     reply_markup=InlineKeyboardMarkup([
                         [InlineKeyboardButton('🛒', callback_data=tp),
                          InlineKeyboardButton('⬅', callback_data=pp)]
                     ])
                     )

        dict_my[num-1] = d
        dict_my[num] = Ga.get_all_new(x, mass, num_of_fil)[2]


def back(q, b, mass, num_of_fil, dict_my, list_my, num):

    temp = []
    for j in dict_my.values():
        temp.append(j)

    x = [temp[i] for i in range(num)]

    if num == -1:
        q.edit_message_text(text='Choose a category:', reply_markup=Ga.category())

    elif -1 < num < num_of_fil - 1:
        q.edit_message_text(text=list_my[num], reply_markup=Ga.get_all_new(x, mass, num_of_fil)[1])

    else:
        b.deleteMessage(chat_id=q['message']['chat']['id'], message_id=q['message']['message_id'])
        b.send_message(chat_id=q['message']['chat']['id'],
                       text=list_my[num],
                       reply_markup=Ga.get_all_new(x, mass, num_of_fil)[1])

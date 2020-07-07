import gspread
from telegram import *
from oauth2client.service_account import ServiceAccountCredentials

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', ['https://www.googleapis.com/auth/drive'])
client = gspread.authorize(creds)

table = client.open('Diploma')

customers = table.worksheet("Customers").get_all_values()
feed = table.worksheet("Feed").get_all_values()
toys = table.worksheet("Toys").get_all_values()


def get_all_new(mass, source, num_of_filters):

    pos = 0
    result = []
    state = True
    a = [str(x) for x in range(1, int(get_max(source, num_of_filters-1)) + 1)]

    for i in source[4:]:
        for j in range(len(mass)):

            if i[j] == mass[j] or str(i[j]) in a:
                state = True
            else:
                state = False
                break

        if state and i[len(mass)] not in result and i[len(mass)] != '':
            result.append(i[len(mass)])
            pos = source.index(i)

    if len(mass) < num_of_filters:
        keyboard = []
        amount = source[pos][len(mass)]

        if len(mass) == num_of_filters - 1:
            for i in range(1, int(amount) + 1):
                keyboard.append([InlineKeyboardButton(i, callback_data=i)])
        else:
            for i in list(result):
                keyboard.append([InlineKeyboardButton(i, callback_data=i)])

        keyboard.append([InlineKeyboardButton('⬅', callback_data=str(source[0][len(mass)]))])
        return mass, InlineKeyboardMarkup(keyboard)

    elif len(mass) == num_of_filters:
        res_txt = ''

        for i in mass:
            res_txt += i + '\n'

        res_txt += str(int(source[pos][num_of_filters])*int(mass[-1]))
        img = source[pos][num_of_filters + 2]
        price = source[pos][num_of_filters]
        return res_txt, img, price, pos


def get_max(source, num):
    temp_list = []
    for n in source[4:]:
        if n[num] != '':
            temp_list.append(int(n[num]))
    return max(list(set(temp_list)))


def get_lists(source, num):
    temp_list = []
    for n in source[4:]:
        if n[num] != '':
            temp_list.append(n[num])
    return list(set(temp_list))


f_pet = get_lists(feed, 0)
f_type = get_lists(feed, 1)
f_producer = get_lists(feed, 2)
f_weight = get_lists(feed, 3)

t_pet = get_lists(toys, 0)
t_type = get_lists(toys, 1)
t_producer = get_lists(toys, 2)
t_size = get_lists(toys, 3)


def category():
    keyboard = [[InlineKeyboardButton('Feed', callback_data="feed"),
                 InlineKeyboardButton('Toys', callback_data="toys")]]
    return InlineKeyboardMarkup(keyboard)


# a = get_all_new(['Cat', 'Liquid', 'Royal Canin', '1.0', '10'], feed)
# print(a)

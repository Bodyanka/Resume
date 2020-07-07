import time
from telegram import *

import Diploma.Get_all as ga
import Diploma.keyboards.Feed as kbf
import Diploma.keyboards.Toys as kbt


# обработчик всех кнопок со всех клавиатур
def keyboards_callback_handler(bot: Bot, update: Update, chat_data=None, **kwargs):
    query = update.callback_query
    data = query.data

    kbf.feed(query, data, bot,
             query['message']['chat']['id'],
             [kbf.order_feed[0], kbf.order_feed[1], kbf.order_feed[2],
              kbf.order_feed[3], kbf.order_feed[4], kbf.order_feed[5]],
             time.asctime())

    kbt.toys(query, data, bot,
             query['message']['chat']['id'],
             [kbt.order_toys[0], kbt.order_toys[1], kbt.order_toys[2],
              kbt.order_toys[3], kbt.order_toys[4], kbt.order_toys[5]],
             time.asctime())

    # print('query from')
    # print(query['message']['message_id'])

    if data == 'New order':
        query.edit_message_text(text='Choose a category:',
                                reply_markup=ga.category())

from telegram import *
from telegram.ext import *

import Diploma.Functions as ft
import Diploma.Keyboards as kb

from telegram.utils.request import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    request = Request(con_pool_size=20)
    bot = Bot(token='1161675658:AAEA3Tj1LaX-iqFVpP8IE3cstBRxWR5iKmE', request=request)
    updater = Updater(bot=bot)

    updater.dispatcher.add_handler(MessageHandler(Filters.contact, ft.contact_callback))
    updater.dispatcher.add_handler(CommandHandler("start", ft.do_start))
    updater.dispatcher.add_handler(CommandHandler("help", ft.do_help))
    updater.dispatcher.add_handler(CommandHandler("card", ft.do_card))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, ft.text))

    updater.dispatcher.add_handler(CallbackQueryHandler(callback=kb.keyboards_callback_handler, pass_chat_data=True))

    updater.dispatcher.add_error_handler(error)

    updater.start_polling(poll_interval=1)
    updater.idle()


if __name__ == '__main__':
    main()

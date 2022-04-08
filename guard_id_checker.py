import logging
from cnid_checker import checkID as cnid_checker

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

'''
Replace TELEGRAM_ID with the Telegram ID of Telegram client account(s) that is going to use this bot
'''
authorized = [TELEGRAM_ID]

'''
Replace API_TOKEN with the API token of your telegram bot
'''
api_token = "API_TOKEN"

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print(user)
    update.message.reply_markdown_v2(
        f'Welcome\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        f"Type this string to check a Chinese ID Card:\n\n[CNID]-CNID_NUMBER-CHN_NAME"
    )


def checkCNID(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    if (user["id"] not in authorized):
        update.message.reply_text("Not authorized")
        return
    else:
        update.message.reply_text("Please wait...")
        raw = update.message.text.split('-')
        result = cnid_checker(raw[1],raw[2])
        if (result == "err" or result["status"] == "202"):
            msg = "Unable to check this ID"
        else:
            if (result["status"] == "01"):
                msg = f"实名认证通过 Real-name verification passed!\n"+result["idCard"]+"\n"+result["name"]+"\n"+result["area"]
            elif (result["status"] == "02"):
                msg = f"实名认证失败 Real-name verification failed!"
            elif (result["status"] == "204"):
                msg = f"姓名格式不正确 Incorrect name format!"
            elif (result["status"] == "205"):
                msg = f"身份证格式不正确 Incorrect ID format!"
            elif (result["status"] == "9999"):
                msg = f"系统维护 System maintenance"
        update.message.reply_text(msg)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(api_token,use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.regex("^(\[CNID\])-(\d{17})(\d{1}|X|x)-"), checkCNID))

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
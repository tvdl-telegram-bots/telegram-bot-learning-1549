# Copied from https://github.com/python-telegram-bot/python-telegram-bot/blob/v20.0a0/examples/echobot.py

#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from distutils.log import info
import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CallbackContext, CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

dict = {}

async def setkey(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    user_mess = (update.message.text)
    i = user_mess.find('=')
    key = user_mess[5:i]
    value = user_mess[i+1:]
    dict.update({key : value})
    print(key, value)
    print(i)

async def getkey(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
        user_mess = (update.message.text)
        x = user_mess.split(' ')
        i = dict.get(x[1])
        try: 
            await update.message.reply_text(i)
        except:
            await update.message.reply_text("key not found")

async def delkey(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    user_mess = (update.message.text)
    x = user_mess.split(' ')
    i = dict.get(x[1])
    try:
        del dict[x[1]]
        await update.message.reply_text("Delete sucess")
    except:
        await update.message.reply_text("Key not found")
        
        

async def info(update: Update, context: CallbackContext.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Your id is : " + str(update.message.chat.id))
    await update.message.reply_text("Your first name is : " + str(update.message.chat.first_name))
    await update.message.reply_text("Your last name is : " + str(update.message.chat.last_name))

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5400071880:AAH5dhWMOtr1cd4-PaqeAVx1K2X2r6GMEuc").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("set", setkey))
    application.add_handler(CommandHandler("get", getkey))
    application.add_handler(CommandHandler("del", delkey))


    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()



if __name__ == "__main__":
    main()

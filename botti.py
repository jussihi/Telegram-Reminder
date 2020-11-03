#!/usr/bin/env python

import string
import logging
import telegram
from telegram import Update
from telegram.error import NetworkError, Unauthorized
from telegram.ext import Updater, CommandHandler, CallbackContext
import remindme



def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    u = Updater('TOKEN', use_context=True)
    
 
    # Get the dispatcher to register handlers
    dp = u.dispatcher
 
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("remindme", remindme.remind))
 
    # Start the Bot
    u.start_polling()
 
    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    u.idle()



if __name__ == '__main__':
    main()

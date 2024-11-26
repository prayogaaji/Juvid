from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Define a function to start the bot and send a welcome message
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello, I am your bot! Type any message to see my response.")

# Define a function that replies to user messages
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    print(update)
    response = f"You said: {user_message}"
    await update.message.reply_text(response)

# Main function to set up the bot
def main():
    # Replace 'YOUR_API_TOKEN' with the token you got from BotFather
    bot_token = "8172713456:AAEsmglzd1-IJDrjazzE-c_d9IBRG0t2eV0"

    # Create an Application instance (used in python-telegram-bot v20+)
    application = Application.builder().token(bot_token).build()

    # Add a command handler for the '/start' command
    application.add_handler(CommandHandler("start", start))

    # Add a message handler for text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

# Run the bot
if __name__ == "__main__":
    main()

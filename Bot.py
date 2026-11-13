import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "9152560642:AAEsdoXHrL9T9oByYhfNTzqn9R_Pi2N80OQ"
MONETAG_LINK = "https://uplcm.com/4/12252447"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("🔥 Click Here to Earn & Watch 🔥", url=MONETAG_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "স্বাগতম! নিচে ক্লিক করে আমাদের স্পন্সর লিংক ভিজিট করুন এবং আয় করুন:",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    port = int(os.environ.get("PORT", "8080"))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}"
    )

if __name__ == "__main__":
    main()

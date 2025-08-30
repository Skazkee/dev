import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
MY_USER_ID = int(os.getenv("MY_USER_ID", "0"))

KEYWORDS = ["спам", "оплата", "взлом", "жалоба", "Куплю", "Продам", "продам"]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    message_text = update.message.text.lower()
    sender = update.message.from_user

    if any(word in message_text for word in KEYWORDS):
        alert = (
            f"🚨 Обнаружено ключевое слово!\n"
            f"👤 От: {sender.full_name} (@{sender.username})\n"
            f"🗨 Сообщение: {update.message.text}"
        )
        await context.bot.send_message(chat_id=MY_USER_ID, text=alert)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

OWNER_ID = 861087987

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(
        "Привет, я бот, который поможет тебе связаться со мной, если у тебя спам-блокировка. "
        "Напиши свою просьбу и в конце укажи свой юзернейм, чтобы я мог тебе ответить.",
        reply_markup=ForceReply(selective=True),
    )

def forward_to_owner(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_info = (
        f"Сообщение от пользователя: @{update.effective_user.username}\n"
        f"ID: {update.effective_user.id}\n"
        f"Текст: {user_message}"
    )
    
    context.bot.send_message(
        chat_id=OWNER_ID,
        text=user_info
    )
    
    update.message.reply_text("✅ Твоё сообщение отправлено владельцу. Ожидай ответа.")

def main() -> None:
    updater = Updater("7793603582:AAF_70OhZL6lvM757cVhxrri2pZLwo781To")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_owner))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

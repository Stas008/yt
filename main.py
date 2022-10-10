from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_com import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5797756682:AAHh0XQb2_kILdxDFhCH5mMJqbVAu0ijV3w").build()
print("ok")
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("tube", tube))

app.run_polling()


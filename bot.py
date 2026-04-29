import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

OLD_USERNAME = "@MovSerColX"
NEW_USERNAME = "@The_Wolverine_Channel"

TOKEN = os.getenv("BOT_TOKEN")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    caption = msg.caption

    if (msg.video or msg.document) and caption:
        new_caption = caption.replace(OLD_USERNAME, NEW_USERNAME)

        file = await msg.effective_attachment.get_file()
        path = await file.download_to_drive()

        with open(path, 'rb') as vid:
            await context.bot.send_video(
                chat_id=msg.chat.id,
                video=vid,
                caption=new_caption,
                parse_mode='HTML'
            )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video))

print("Bot running...")
app.run_polling()

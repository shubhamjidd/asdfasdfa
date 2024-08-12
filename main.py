from telegram import Update # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes,MessageHandler,filters # type: ignore
import os
from Qrcode import generateQrWithText,welcomeMsg,decodeQrImg

# bot token
API_TOKEN = "7227224228:AAH6J32_sXkBLBiWK9u_LOBuCc2744mfgII"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    firstName =update.message.chat["first_name"]
    await update.message.reply_text(welcomeMsg(firstName),parse_mode="HTML")

# generate qr code 
async def generateQr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    textInput= " ".join(update.message.text.split(" ")[1:])
    if textInput:
        try:
            generateQrWithText(textInput)
            ls = await update.message.reply_photo(photo=open("msg.png", "rb"))
            if ls:
                os.remove("msg.png")
        except Exception as e:
            print(f"Error in generating QR code: {e}")
    else :
        await update.message.reply_text('Please provide some text to generate a QR code.')           
    

# read qr code
async def readQrCode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message and update.message.reply_to_message.photo:
        try:
            photo_file_id = update.message.reply_to_message.photo[-1].file_id 
            photo_file = await context.bot.get_file(photo_file_id)
            await photo_file.download_to_drive('received_photo.jpg')
            decodedText=decodeQrImg("received_photo.jpg")
            await update.message.reply_text(decodedText)
            os.remove("received_photo.jpg")
        except Exception as e:
            print(f"Error in receiving photo: {e}")
            await update.message.reply_text('Failed to receive the photo.')
    else:
        await update.message.reply_text('Reply to a photo to use this command.')

def main() -> None:
    
    application = Application.builder().token(API_TOKEN).build()
    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate", generateQr))
    application.add_handler(CommandHandler("read", readQrCode))
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()

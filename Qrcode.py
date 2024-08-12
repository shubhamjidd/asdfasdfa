import qrcode # type: ignore
from PIL import Image # type: ignore
from pyzbar.pyzbar import decode # type: ignore

# generate QR Code 
def generateQrWithText(Data:str)-> None:
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(Data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("msg.png")
    except Exception as e:
        # Log the exception or handle it as needed
        print(f"An error occurred in generate image : {e}")


# decode qr code image

def decodeQrImg(fileName:str)->str:
    try:
        image = Image.open(fileName)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            return qr_data
    except Exception as e:
        # Log the exception or handle it as needed
        print(f"An error occurred in decode image : {e}")


# welcome Msg 
def welcomeMsg(firstName:str)->str:
    return f"""
Hello {firstName}\n\n
<b>Welcome to QR Bot!</b>\n
<i>Hello! I am your QR code assistant. With me, you can easily generate and read QR codes.</i>\n\n
<b>Here's what I can do for you:</b>\n
<b>• Generate QR Codes:</b> Create a QR code from any text or URL quickly and effortlessly.\n
<b>• Read QR Codes:</b> Decode QR codes from images and retrieve the embedded information.\n\n
<b>To get started, simply send me a command:</b>\n
<b>• /generate</b> - Generate a QR code. Provide the text or URL you want to encode.
<i>• <code>/generate Some Text</code></i>\n
<b>• /read</b> - Read a QR code from an image. Upload the image and I’ll extract the data for you.
<i>• Send an image and then reply to that image by type <code>/read</code></i>\n\n
<b>Enjoy using QR Bot!</b>
"""
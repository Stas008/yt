
from fileinput import filename
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pathlib import Path
from pytube import YouTube
import time

def YT_to_teleg(input_url):
    my_video = YouTube(input_url)
    print(input_url)
    YouTube(input_url).streams.get_highest_resolution().download(filename="1.mp4")
    

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Для того чтобы узнать погоду введите /weather Город')

async def tube(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    new_url=msg[6:]
    print(new_url)

    

    await update.message.reply_text("Please wait")
    YT_to_teleg(new_url)
    await update.message.reply_text("Video has been downloaded to server")
    flag=False
    
    my_file = Path("1.mp4")

    while (flag==False):
        if my_file.is_file():
            flag=True
    else:
        print("wait")
        time.sleep(2)
    vid = open ("1.mp4","rb")
    await update.message.reply_video(vid)
    # await update.message.reply_text("enjoy your video, see you soon")




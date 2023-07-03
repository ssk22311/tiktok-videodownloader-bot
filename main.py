import telebot
from telebot import types
from video_downloader import downloadVideo
import os
from dotenv import load_dotenv
import logging

 # Read .env file
load_dotenv()

    # Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )
logging.getLogger("httpx").setLevel(logging.WARNING)
token = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome! I am a TikTok video downloader bot. Send me a TikTok video link and I will download the video for you.')

@bot.message_handler(func=lambda message: True)
def tiktok_downloader(message):
    url = message.text
    if 'tiktok' in url:
        bot.reply_to(message, 'Downloading your TikTok video...')
        
        downloadVideo(url, 'index')

        bot.send_video(message.chat.id, video=open(f'index.mp4', 'rb'))
        bot.reply_to(message, 'Video downloaded and sent!')
    else:
        bot.reply_to(message, 'Please send a valid TikTok video link')

bot.polling()
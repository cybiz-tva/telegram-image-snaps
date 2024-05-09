import requests
import json
from telegram import Bot

# Replace with your Telegram bot token and channel ID

TELEGRAM_BOT_TOKEN = ''
# Telegram channel ID
TELEGRAM_CHANNEL_ID = ''

async def send_image_to_telegram(image_file):
    # Send image to Telegram channel
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_photo(chat_id=TELEGRAM_CHANNEL_ID, photo=open(image_file, 'rb'))

async def generate_chart_image_and_send_to_telegram(layout_id, api_key, symbol, interval, height, width):
    # Generate chart image using API
    url = f"https://api.chart-img.com/v2/tradingview/layout-chart/{layout_id}"
    headers = {
        "x-api-key": api_key,
        "content-type": "application/json"
    }
    payload = {
        "symbol": symbol,
        "interval": interval,
        "height": height,
        "width": width
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Save chart image
        with open("chart-img-03.png", "wb") as f:
            f.write(response.content)
        
        # Send chart image to Telegram
        await send_image_to_telegram("chart-img-03.png")
        print("Chart image sent to Telegram channel")
    else:
        print(f"Failed to fetch chart image. Status code: {response.status_code}")

# Replace placeholders with your actual values
LAYOUT_ID = ''
API_KEY = ''
SYMBOL = 'FOREXCOM:XAUUSD'
INTERVAL = '15m'
HEIGHT = 1080
WIDTH = 1920

await generate_chart_image_and_send_to_telegram(LAYOUT_ID, API_KEY, SYMBOL, INTERVAL, HEIGHT, WIDTH)

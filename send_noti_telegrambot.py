import asyncio
from telegram import Bot
from send_getcode_exportcode import get_code
from sys import platform
from get_env import get as get_env

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) if 'win' in platform else None


async def send_message(message: str, bot_token: str, chat_id: str):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


def send_telegram_main(message: str):
    TELEGRAM_BOT_TOKEN = get_env('TELEGRAM_BOT_TOKEN', True)
    TELEGRAM_CHAT_ID = get_env('TELEGRAM_CHAT_ID', True)
    
    asyncio.run(send_message(message, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID))


if __name__ == '__main__':
    telegram_codes = get_code()
    try:
        send_telegram_main('TWEET PUBLICADO EXITOSAMENTE')
    except Exception as e:
        print('Error:', e)
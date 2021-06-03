import html
import logging

import telepot
from django.conf import settings

TOKEN = settings.TG_BOT_TOKEN
TG_CHAT_ID = settings.TG_CHAT_ID


def send_msg(office, title, link):
    bot = telepot.Bot(TOKEN)
    log_msg = f"{office}, title： {title}"
    e_title = html.escape(title)
    bot.sendMessage(
        TG_CHAT_ID,
        f'{office}：\n<a href="{link}">{e_title}</a>\n',
        parse_mode="HTML",
        disable_web_page_preview=True,
    )
    logging.info(f"Telegram - office: {log_msg}")

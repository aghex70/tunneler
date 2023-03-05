import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from configuration import TELEGRAM_BOT_TOKEN
from messager.utils import check_access
from proxy.tunnel import create_tunnel, get_public_url, list_tunnels

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def daps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please introduce your email.\nUsage: /daps <email>",
        )
        return

    email = context.args[0]
    if not check_access(email):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You are not allowed to access this bot.",
        )
        return

    # Check if we already have a tunnel active
    tunnels = list_tunnels()
    if tunnels:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="You already have an active tunnel."
        )
        return

    # Create a new tunnel
    tunnel = create_tunnel()
    tunnel_public_url = get_public_url(tunnel)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=tunnel_public_url
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler("daps", daps)

    application.add_handler(start_handler)

    application.run_polling()

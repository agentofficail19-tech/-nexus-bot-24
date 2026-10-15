import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! Render da Environment Variables ni tekshiring!")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🚀 Assalomu alaykum! NEXUS.lab ga xush kelibsiz!\n\n"
        "Biz:\n"
        "🌐 Professional veb-saytlar\n"
        "🤖 Telegram botlar 24/24\n"
        "🎨 Logo va brending qilamiz\n\n"
        "Quyidagi menyudan tanlang:"
    )
    keyboard = [
        [InlineKeyboardButton("🎨 Portfolio", url="https://instagram.com/nexuslab.uz"), InlineKeyboardButton("💼 Xizmatlar", callback_data='services')],
        [InlineKeyboardButton("📩 Buyurtma berish", url="https://t.me/Cosmos_00012")],
        [InlineKeyboardButton("📞 Aloqa", callback_data='contact'), InlineKeyboardButton("🌐 Sayt", url="https://nexuslab.uz")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    else:
        await update.callback_query.message.reply_text(text, reply_markup=reply_markup)

# Tugmalar bosilganda ishlaydigan funksiya
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'services':
        await query.message.reply_text(
            "💼 NEXUS.lab Xizmatlar:\n\n"
            "🌐 Veb-sayt - 500$ dan\n"
            "  • Landing, korporativ, do'kon\n\n"
            "🤖 Telegram bot 24/24 - 300$ dan\n"
            "  • Avto-javob, to'lov, buyurtma\n"
            "  • Telefon o'chiq bo'lsa ham ishlaydi\n\n"
            "🎨 Logo / Brending - 100$ dan\n\n"
            "Buyurtma: @Cosmos_00012"
        )
    elif query.data == 'contact':
        await query.message.reply_text(
            "📞 Aloqa:\n👤 Admin: @Cosmos_00012\n📸 Instagram: @nexuslab.uz\n🌐 Sayt: nexuslab.uz\n📍 Toshkent, 24/24 online!"
        )

async def services_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 NEXUS.lab Xizmatlar:\n\n🌐 Veb-sayt - 500$ dan\n🤖 Telegram bot 24/24 - 300$ dan\n🎨 Logo - 100$ dan\n\nBuyurtma: @Cosmos_00012"
    )

async def contact_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Aloqa: @Cosmos_00012 | @nexuslab.uz | nexuslab.uz")

if __name__ == "__main__":
    print("NEXUS.lab Bot 24/24 ishga tushdi...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("services", services_cmd))
    app.add_handler(CommandHandler("contact", contact_cmd))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

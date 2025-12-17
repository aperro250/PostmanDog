# Version of the code 1.0.10
# Created by Aperro
import json
import telebot
import re

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
# Токен и авторизация бота
TelegramToken = config["Telegram_config"]["TOKEN"]
TgmBot = telebot.TeleBot(TelegramToken)
# Метод бесконечного вызова бота

def run_telegram():
    print("📲 Telegram бот запущен")
    while True:
        try:
            TgmBot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"Ошибка polling: {e}")
            print("Попытка переподключения черкз 5 секунд")
            time.sleep(5)

# ID форума
ForumID = config["Telegram_config"]["Channel_ID"]

# ID топиков
pve = config["Telegram_config"]["pve_topic_id"]
pvp = config["Telegram_config"]["pvp_topic_id"]
ava = config["Telegram_config"]["ava_topic_id"]
anouns = config["Telegram_config"]["anouncement_topic_id"]

#Полное экранирование без замены (для ников авторов колов)
def full_escape_markdown_v2(text: str) -> str:
    escape_chars = r'_*[]()~`>#+-=|{}.!\/'
    return replace_discord_emojis(re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text))
    
def clean_and_escape_for_telegram(text: str) -> str:
    import html  # на случай непечатаемых символов

    # Удаление Discord-форматирования
    text = re.sub(r'``(.*?)``', r'\1', text, flags=re.DOTALL)  # блочный моно
    text = re.sub(r'`([^`\n]+?)`', r'\1', text)                # inline моно
    text = re.sub(r'~~(.*?)~~', r'\1', text)                   # зачёркнутый
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)               # жирный
    text = re.sub(r'__(.*?)__', r'\1', text)                   # подчёркнутый
    text = re.sub(r'\*(\S(?:.*?\S)?)\*', r'\1', text)          # курсив
    text = re.sub(r'_(\S(?:.*?\S)?)_', r'\1', text)            # курсив
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)# заголовки

    # Удаление Discord-упоминаний
    text = re.sub(r'<@!?[0-9]+>', '@user', text)
    text = re.sub(r'<@&[0-9]+>', '@role', text)
    text = re.sub(r'<#[0-9]+>', '#channel', text)

    # Удаление Discord-эмодзи (например, <:tank:123456>)
    text = re.sub(r'<a?:[a-zA-Z0-9_]+:[0-9]+>', '', text)

    # Удаление || скрытого текста || (если не нужен — иначе обернуть как цитату)
    text = re.sub(r'\|\|.*?\|\|', '', text)

    
    # Обработка Эмодзи
    text = replace_discord_emojis(text)
    
    # Экранирование спецсимволов для MarkdownV2
    escape_chars = r'_*[]()~`>#+-=|{}.\!'
    text = re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

    # Обработка HTML-сущностей (если есть)
    text = html.unescape(text)
    
    return text.strip()    
    
import re

def replace_discord_emojis(text: str) -> str:
    emoji_map = {
        ":tank:": "🛡️",
        ":healer:": "💉",
        ":autokill:": "🔫",
        ":amongus_kill:": "⚔️",
        ":pepe_virus:": "☣️",
        ":pepe_trump:": "🧑‍💼",
        ":amongus_t:": "👽",
        ":clown_cry:": "🤡",
        ":pepe_laught:": "😂",
        ":R34:": "🥵",
        ":thinking:": "🤔",
        ":rabbit_mount:": "🐇",
        ":sad:": "😢",
        ":troll_among:": "😈",
        ":okay:": "👍",
        ":durka:": "🏥",
        ":ban:": "⛔",
        ":cat_love_c:": "😻",
        ":loading_smile:": "⌛",
        ":Cat_shy:": "🙈",
        ":pepe_cry:": "😭",
        ":squirtle_cool:": "😎",
        ":BOOM:": "💥",
        ":BRUH:": "🤦",
        ":Surprised:": "😲",
        ":MEE:": "😐",
        ":pepe_nuked:": "☢️",
        ":discord_laugh:": "😆",
        ":stoncks:": "📈"
    }

    # Заменяем известные
    for key, value in emoji_map.items():
        text = text.replace(key, value)

    # Заменяем все оставшиеся :что-то: на 🎯
    text = re.sub(r':[a-zA-Z0-9_]+:', "🎯", text)

    return text
    
# Стартовый хендлер
@TgmBot.message_handler(commands=["start"])
def send_welcome(message):
    TgmBot.reply_to(
        message, clean_and_escape_for_telegram(
        "`Гав🐶!` Я личный бот гилдии *THE COURT* и я *доношу сообщения между участниками сообщества*👥."),
        parse_mode="MarkdownV2"
    )
# Метод подучения актуального ID топиков
def get_topic_id(message_channel: str):
    if message_channel == "pve":
        return pve
    elif message_channel == "pvp":
        return pvp
    elif message_channel == "ava":
        return ava
    elif message_channel == "anouns":
        return anouns
    else:
        return 0
# Функция отправки сообщения
def send_telegram_message(topic_id: int, file_name: str):
    message_path = "texts/" + file_name
    try:
        with open(message_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        TgmBot.send_message(
            chat_id = ForumID, message_thread_id=int(topic_id),
            text=f"Автор: {full_escape_markdown_v2(data['author_name'])}\n\n{clean_and_escape_for_telegram(data['text'])}",
            parse_mode="MarkdownV2"
        )
        print(f"✅ Отправлено сообщение из {message_path} в топик {topic_id}")
    except Exception as e:
        print(f"❌ Ошибка при отправке: {e}")
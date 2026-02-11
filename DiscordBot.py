import os
import discord
from discord.ext import commands
import json
import TelegramBot

# Загрузка конфига
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
# Создание и загрузка переменных
DiscordToken = config["Discord_config"]["TOKEN"]
#pve = config["Discord_config"]["pve_channel_id"]
#pvp = config["Discord_config"]["pvp_channel_id"]
#ava = config["Discord_config"]["ava_channel_id"]
#anouns = config["Discord_config"]["anouncement_channel_id"]
discord = config.get("Discord")
channels_cuantity = discord["channels_cuantity", 0]

# Create a list for the channels id to listen
channels = config["Discord"]["channels"]
listen_channels_id = []
listen_channels_name = []

# Создание папки для хранения текстов
texts = "texts"
if not os.path.exists(texts):
    os.makedirs(texts)
# Сохранение информации. Указывать аргуметы: ID, канал, автор, дата, текст
def save_inf(ID: int, channel: str, author_name: str, date, text: str) -> None:
  
    file_path = os.path.join(texts, f"{author_name} {date}.json")
   
    JsonFile = {
      "ID": ID,
      "channel": channel,
      "author_name": str(author_name),
      "date": str(date),
      "text": text
    }
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(JsonFile, file, ensure_ascii=False, indent=2)

# Указания интентов бота
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.messages = True

# Запуск бота
bot = commands.Bot(command_prefix="!", intents=intents)

# Уведомление о запуске
@bot.event
async def on_ready():
    print(f"🎮 Discord бот запущен как {bot.user}")

# Метод "Прослушки сообщений"
@bot.event
async def on_message(message):
    if str(message.channel.id) in [listen_channels_id] and message.author != bot.user:
        channel = "None"
        #print(message.channel.id)

        # if str(message.channel.id) == pve:
        #     channel = "pve"
        # elif str(message.channel.id) == pvp:
        #     channel = "pvp"
        # elif str(message.channel.id) == ava:
        #     channel = "ava"
        # elif str(message.channel.id) == anouns:
        #     channel = "anouns"


        print(message.channel.id)

        # Obtain the chanels position in the local list to interact later
        id_position = None
        for i in len(listen_channels_id):
            if str(message.channel.id) == listen_channels_id[i]:
                id_position = i
            else:
                pass

        formatted_date = message.created_at.strftime("%d.%m.%Y, %H:%M UTC")  # например: 26.06.2025, 18:31
        save_inf(message.id, channel, message.author.display_name, formatted_date, message.content)
        print(f'💾 Сохранено сообщение ID {message.id} от {message.author} с канала {channel} ({listen_channels_name[id_position]})')
        print('🔄 Попытка отправки в Телеграм')
        telegram_topic_id = TelegramBot.get_topic_id(channel)
        TelegramBot.send_telegram_message(telegram_topic_id, f"{message.author.display_name} {formatted_date}.json")

# Метод запуска бота
def run_discord() -> None :
    bot.run(int(config["Discord_Token"]))

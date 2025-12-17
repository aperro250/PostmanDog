import threading
from TelegramBot import run_telegram
from DiscordBot import run_discord

if __name__ == "__main__":
    tg_thread = threading.Thread(target=run_telegram)
    ds_thread = threading.Thread(target=run_discord)

    tg_thread.start()
    ds_thread.start()

    tg_thread.join()
    ds_thread.join()

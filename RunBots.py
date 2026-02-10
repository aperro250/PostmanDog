import os
import threading
try:
  from TelegramBot import run_telegram
  from DiscordBot import run_discord
except FileNotFoundError:
  pass

config_path = "config.json"
#Check if the config file is created
if os.path.exists(config_path):
  # config.json are alredy excisting
  if __name__ == "__main__":
    print("Starting the bot's")
    # Starts to run the Telegram and Discord bots parallely
    tg_thread = threading.Thread(target=run_telegram)
    ds_thread = threading.Thread(target=run_discord)
      
    tg_thread.start()
    ds_thread.start()
      
    tg_thread.join()
    ds_thread.join()
  # config.json don't excist or can not be found
else:
  # Wana create the config file?
  if input("The config file 'config.json' not fount. Do you want to create it? (Y/N)") in ("Y","y"):
    # Some code
    print ("In work")
  else:
    print("Stoping the program")
    exit()
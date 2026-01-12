import os
import json

# Store the path one level up for future creation of "config.json"
base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))

# Creating a module of config sintaxis

config_model = {

    "DiscordToken": "",
    "TelegramToken": "",

    "Discord": {
        "channel1": {

                # Custom name for a chanel1
                "name": "",
                # The channel id
                "id": "",
                # The list with whos channel are this channel conected. The sidtaxis is Dx for Discord conections and Tx for Telegram conections
                "conectedWith": ""
        },
    },
    "Telegram": {
            "group1": {
                # The telegram group id
                "id": "",

                "channel1": {

                    # The custom name for a channel
                    "name": "",
                    "id": "",
                    "conectedWith": ""

                },

            },
    },

}

def createConfig ():

    print ("Welcome to the config creation assistant")

    while True:
        print ("""
        Please, choose one of the following options:
        1: Telegram config
        2: Discord config
        3: Exit program
        """)

        choice = int(input ())

        if choice == 1:
            # Sending to Telegram config
            telegram_config()
        elif choice == 2:
            # Sending to Discord config
            discord_config()
        elif choice == 3:
            exit()
        else:
            print ("You have introduced the incorect number, please try again")

def telegram_config ():
    print("Telegram_config")

def discord_config ():
    print("Discord_confid")

createConfig()

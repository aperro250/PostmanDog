import os
import json
import clear

# Store the path one level up for future creation of "config.json"
base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
# Store the config derectory
config_path = os.path.join( base_dir,"config.json")

# Create a chose variable for the future work
choice = ""

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
                "name":"",
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


print(config_path)
# Create a config.sjon file if it don't exists
if not os.path.exists(config_path):
	
	print ("creating new config file")
	with open(config_path, "w", encoding="utf-8") as f:
		json.dump(config_model, f, indent=4)
	


# Create a variable for work with config
with open(config_path, "r", encoding="utf-8") as f:

	config = json.load(f)

# Update the config. Writes the local variable "config" into the config.json
def update_config():
	with open (config_path, "w", encoding="utf-8", ensure_ascci=False) as f:
		json.dump(config, f, indent=4)


# ~~~~~~~~~~~~~~~~ GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
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


# ........................ TELEGRAM ...............................
def telegram_config ():
    clear.clear()
    
    telegram = config.get("Telegram")
    print("Telegram_config")
    
    print("""
    What you want to do?
    1: Add a new group
    """)
    # If there are an id for the first group:
    if "id" in telegram.get("group") != "" :
    
    	print("""
    	2: Modife an excisting Telegram group
	3: Add a new channel
    	""")
    	
    choice = input()
    
    if choise == 1:
    	add_telegram_group()
    elif choice == 2:
    	modife_telegram_group()
    elif choice == 3:
    	add_telegram_channel()
    else:
    	print ("You have introduced the incorect number, please try again")
    

def add_telegram_group ():
	input ()
	
def modife_telegram_group ():
	input ()
	
def add_telegram_channel ():
	input ()


# ......................DISCORD ........................
def discord_config ():
    clear.clear()
    print("Discord_confid")
    input()
    
createConfig()

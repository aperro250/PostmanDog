import os
import json
import clear

# Store the path one level up for future creation of "config.json"
base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
# Store the config derectory
config_path = os.path.join(base_dir, "config.json")

# Create a chose variable for the future work
choice = ""

# Creating a module of config sintaxis
config_model = {

    "DiscordToken": "",
    "TelegramToken": "",

    "Discord": {

        "chanels_cuantity": 1,
        "channels": [

            {
                "channel_name": "",
                "channel_id": "",
                "conectedWith": ""
            },
            # Custom name for a chanel1
            #"name": "",
            # The channel id
            #"id": "",
            # The list with whos channel are this channel conected.
            # The sidtaxis is Dx for Discord conections and Tx for Telegram conections
            #"conectedWith": ""
        ],
    },
    "Telegram": {

        "groups_cuantity": 1,
        "groups": [
            # The telegram group id
            #"name": "",
            #"id": "",
            {
                "group_name": "",
                "group_id": "",

                "channels_cuantity": 1,
                "channels": [

                {

                    "channel_name": "",
                    "channel_id": "",
                    "conectedWith": ""
                },
                # The custom name for a channel
                #"name": "",
                #"id": "",
                #"conectedWith": ""
    
                ],
            }
        ],
    },
}


# Create a config.json file if it don't exists
if not os.path.exists(config_path):

    print("creating new config file")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_model, f, indent=4)

# Create a variable for work with config
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# print (config["Discord"]["channel1"]["name"])
# Update the config. Writes the local variable "config" into the config.json
def update_config():
    with open(config_path, "w", encoding="utf-8", ensure_ascii=False) as f:
        json.dump(config, f, indent=4)

# ~~~~~~~~~~~~~~~~ GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createConfig():

    print("Welcome to the config creation assistant")

    while True:
        print("""
        Please, choose one of the following options:
        1: Telegram config
        2: Discord config
        3: Exit program
        """)

        choice = int(input())

        if choice == 1:
            telegram_config()
        elif choice == 2:
            discord_config()
        elif choice == 3:
            exit()
        else:
            print("You have introduced the incorect number, please try again")

# ........................ TELEGRAM ...............................
def telegram_config():
    clear.clear()

#    telegram = config.get("Telegram")
    print("Telegram_config")

    print("""
    What you want to do?
    1: Add a new group
    """)
    #telegram.get("group1", {}).get("id", "")
    if  config["Telegram"]["group1"]["id"] != "":
        print("""
        2: Modife an excisting Telegram group
        3: Add a new channel
        
        """)

    choice = input()

    if choice == "1":
        add_telegram_group()
    elif choice == "2":
        modife_telegram_group()
    elif choice == "3":
        add_telegram_channel()
    else:
        print("You have introduced the incorect number, please try again")

# Add new Telegram group
def add_telegram_group():
    
    # Store the first new group slot available
    group = get_telegram_last_group () + 1
    
    #if config["Telegram"]["group1"]["id"] == "":
        
    #    group = 1
    #else:
        
   
                
    print (f"The new group will be the slot: {group}")
        
    set_Tgroup_id( group, input("Please, enter the id of the group: "))
        
    set_Tgroup_name( group , input("Please, give a name for this channel: "))
        
    print (f"Created a new group in slot {group} with name {config['Telegam'][f'group{group}']['name']}")
        


# Modife an excisting Telegram group
def modife_telegram_group():
    a = True
    while a:
        clear.clear()

        print ("""
            What you wanna do?
            
            1: Modife a group name
            2: Modife a group id
            3: Return
            
            """)

        choice = input ()

        if choice == 1 or 2:
            print()
            
        elif choice == 3:
            a = False
        else:
            print ("Error. Please type one of he fallowing choices")
def add_telegram_channel():
    input()

# Returns the last new telegram group slot number 
def get_telegram_last_group ():
    group = 1
    while True:
            
        try:
            if config["Telegram"][f"group{group}"]["id"] != "":
                group+= 1
            else:                    
                break
        
        except:
        
            break
    
    return group 
    
# Set Telegram group new id. Recives a group number and the new id        
def set_Tgroup_id (group, id):
    config ["Telegram"][f"group{group}"]["id"] = id
    update_config()

# Set Telegram group new name. Recies a group number and the new name
def set_Tgroup_name (group, name):
    config ["Telegram"][f"group{group}"]["name"] = name
    update_config()

# ...................... DISCORD ........................
def discord_config():
    clear.clear()
    print("Discord_config")
    input()

createConfig()

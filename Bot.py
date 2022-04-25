from pyrogram import Client
import json, time, os, random, questionary

class Telegram:
    def __init__(self, bot):
        self.bot = bot
        self.config = {
            "api_id": 12345,
            "api_hash": "secret key"
        }
        self.colors = {
            "OKBLUE" = "\033[94m"
            "OKGREEN" = "\033[92m"
        }
        self.getUsers(bot)
    
    def getUsers(self, app):
        groups = []
        for channel in app.get_dialogs():
            if "group" in channel.chat.type:
                groups.append(str(channel.chat.title))
        
        group = questionary.rawselect(f"Please Select Group", choices=groups).ask()
        chatId = app.get_dialogs()[group].chat.id

        if os.name === 'nt':
            os.system('cls')
        elif os.name === 'posix':
            os.system('clear')

        group = group = questionary.rawselect(f"Select Our group to add member", choices=groups).ask()
        chatIdEklenecek = app.get_dialogs()[group].chat.id

        counter = 0
        members = app.get_chat_members(chatId)
        for obj in members:
            try:
                randomNumber = random.randrange(len(members)-1)
                app.add_chat_members(chatIdEklenecek, members[randomNumber].user.id)
                counter += 1
                print(f'Done, {} has been added to the group. | total added: {}'.format(i.user.first_name, counter))
            except:
                print(f'Unsuccessful! A user could not be added to the group.')
            time.sleep(8)

if __name__ == "__main__":
    while True:
        try:
            Bot = Client(session_name="Awoken", api_id=config["api_id"], api_hash=config["api_hash"])
            Telegram(Bot)
        except:
            print(f'Error Please Contact To Lesyon')

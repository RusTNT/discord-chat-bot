import os

from app.discord.DiscordManager import DiscordManager
from app.json.JsonParser import JsonParser

json = JsonParser('config.json')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json.google().application_credentials

discord_manager = DiscordManager()
discord_manager.run(json.discord().token)

import discord
import random
from app.IntentManager import IntentManager
from app.json.JsonParser import JsonParser
from discord.ext import commands

json = JsonParser('config.json')


class DiscordManager(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.intent_manager = IntentManager(json.google().project_id)
        self.allowed_channels = json.discord().allowed_channels
        self.life_chats = json.discord().life_chats
        self.prefixes = json.discord().prefixes
        self.game = json.discord().gamename
        self.answer = json.discord().answer
        self.custom_emoji_collection = []
    @staticmethod
    def decision(probability):
        return random.random() < probability

    def load_custom_emoji_collection(self):
        self.custom_emoji_collection.clear()
        guilds = list(self.guilds)
        for guild in guilds:
            self.custom_emoji_collection.extend(guild.emojis)
        print("Коллекция кастомных emoji обновлена.")

    async def on_ready(self):
        print('Успешно подключились как ', self.user)
        self.load_custom_emoji_collection()
        game = discord.Game(self.game)
        await self.change_presence(activity=game)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if (message.channel.id not in self.allowed_channels) and (message.channel.id not in self.life_chats):
            return
        my_mention = self.user in message.mentions
        if (my_mention) or (message.channel.id in self.life_chats and self.decision(self.answer)):
            await _send_message(self, json.app().debug, message)


async def _send_message(self, is_debug, message):
    if is_debug:
        await message.channel.trigger_typing()
        result = self.intent_manager.detect_texts(session_id=0, lang=json.dialogflow().lang,
                                                  texts=[_slice_keys(message.content, self.prefixes)])

        embed = discord.Embed()
        embed.add_field(name=result[3], value=f'Intent: {result[1]}')
        embed.set_footer(text=f'Conf: {result[2] * 100}%')
        try:
            await message.channel.send(embed=embed)
        except:
            await message.channel.send(random.choice(self.custom_emoji_collection))
        return
    else:
        await message.channel.trigger_typing()
        result = self.intent_manager.detect_texts(session_id=0, lang=json.dialogflow().lang,
                                                  texts=[_slice_keys(message.content, self.prefixes)])
        try:
            await message.channel.send(result[3])
        except:
            await message.channel.send(random.choice(self.custom_emoji_collection))
        return


def _find_starts_with(message, massive):
    for key in massive[0]:
        if message.startswith(key):
            return True
    return False


def _slice_keys(message, massive):
    for key in massive[0]:
        if message.startswith(key):
            return message[len(key):]
    return message

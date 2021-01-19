import json


class JsonParser:
    def __init__(self, path, data=None):
        self.path = path
        self.data = data
        self._parse()

    def dump(self, data):
        self.data = data
        with open(self.path) as json_data_file:
            self.data = json.dump(data, json_data_file)

    def _parse(self):
        with open(self.path) as json_data_file:
            self.data = json.load(json_data_file)

    def google(self):
        return _Google(
            self.data['GOOGLE']['APPLICATION_CREDENTIALS'],
            self.data['GOOGLE']['PROJECT_ID'],
        )

    def discord(self):
        return _Discord(
            self.data['DISCORD']['ALLOWED_CHANNELS'],
            self.data['DISCORD']['LIFE_CHAT_CHANNELS'],
            self.data['DISCORD']['PREFIX'],
            self.data['DISCORD']['TOKEN'],
            self.data['DISCORD']['GAMENAME'],
            self.data['DISCORD']['LIFE_CHAT_ANSWER']
        )

    def dialogflow(self):
        return _Dialogflow(
            self.data['GOOGLE']['DIALOG_FLOW']['LANG']
        )

    def app(self):
        return _App(
            self.data['APP']['DEBUG-MODE']
        )


class _Discord:
    def __init__(self, allowed_channels, life_chats, prefixes, token, gamename, answer):
        self.life_chats = life_chats
        self.allowed_channels = allowed_channels
        self.prefixes = prefixes
        self.token = token
        self.gamename = gamename
        self.answer = answer


class _Google:
    def __init__(self, application_credentials, project_id):
        self.application_credentials = application_credentials
        self.project_id = project_id


class _Dialogflow:
    def __init__(self, lang):
        self.lang = lang


class _App:
    def __init__(self, debug):
        self.debug = debug

__Discord Chat Bot - Разговорный чат-бот для вашего Discord сервера основаный на *Rapptz's [discord.py](https://github.com/Rapptz/discord.py)* и *[Dialogflow](https://dialogflow.com/)*.__ 
-------------
Бот отвечает пользователю на сообщения, бот работает на одной базе фраз, которые загружены в DialogFlow.
![](https://i.imgur.com/j8XtuOh.png)

*Примечание. Если вы задете сложный вопрос для бота, то бот ответит эмоджи.*

Некоторые из функции, предлагаемые чат-ботом:
* Готовая минимальная база ответов на сообщения людей
* Возможность обучать бота и добавлять кастомные ответы в плоть до команд умного дома
* Повышение актива на вашем сервере
----------
# Инструкция по установке
### Шаг 1 Создать бота в [Discord](https://discord.com/developers)
### Шаг 2 Зарегистрироваться и получить ключ авторизации для Dialogflow
1) Зарегистрироваться на [сайте](https://dialogflow.com/) сервиса.
2) Создать нового агента — нашего бота в DiaologFlow.
3) На вкладке General установить настройку V2 API и перейти по ссылке в поле 'Service Account' в единую панель управления сервисами Google для получения авторизационного ключа.
4) У вашего сервисного аккаунта необходимо создать ключ и скачать его. Этот ключ авторизации необходимо будет использовать для получения ответов от Dialogflow. 
5) Скопировать ключ в папку бота с именем auth.json
### Шаг 3 Заполнить конфигурационный файл
#### Пример *config.json* файла:
```json
{
  "APP": {
    "DEBUG-MODE": false // Режим отладки
  },
  "GOOGLE": {
    "APPLICATION_CREDENTIALS": "auth.json",
    "PROJECT_ID": "small-talk-nqnu", // Название проекта в Dialogflow
    "DIALOG_FLOW": {
      "LANG": "ru"
    }
  },
  "DISCORD": {
    "TOKEN": "токен бота", // Токен нашего дискорд бота
    "PREFIX": ["s."], // Префикс для активации бота
    "ALLOWED_CHANNELS": [513008039511457792, 513009831129513994], # Каналы в которых разрешено работать боту
    "LIFE_CHAT_CHANNELS": [513008039511457792, 513009831129513994], # Каналы которые бот мониторит
    "GAMENAME": "Отвечаю пользователям", // Игровой статус бота
    "LIFE_CHAT_ANSWER": 0.1 // Вероятность ответа на случайное сообщение в чате. 0.1 - 10%, 0.5 - 50% и т.д.

  }
}

```
### Шаг 4 Запустить бота
#### Пример запуска в консоли:
```python
python3 main.py
```
# Требования
Все требуемые модули указаны в файле requirements.txt  
Для установки запустите команду:
```python
python3 pip install -r requirements.txt
```
# Список задач
-------------

- [x] Исправление ошибок!
- [x] Ответ эмоджи на неизвестный вопрос!
- [x] Игровой статус у бота!
- [x] Вероятность случайного ответа от бота!
- [x] Повышение производительности!
- [ ] Обучение бота через Discord!
-------------
# Отдельное спасибо *ovrays* и его [Discordflow](https://github.com/ovrays/Discordflow) за готовую базу для бота которая будет постоянно улучшаться

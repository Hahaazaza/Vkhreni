import vk_api
import random
import json
from vk_api.longpoll import VkLongPoll, VkEventType

main_token = '3bdeca9f85e58b9826bfef94f974854f3ba0a1f138d62817d48d91d95575a4928cb4fc3e733511f1ccb94'
vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
users = {}

def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


main_keyboard = {
    "one_time": True,
    "buttons": [
        [get_but('✋Привет', 'default'), get_but('Как дела❓', 'default'),
         get_but('🎲!Броськубик', 'default'), get_but('🎪сделай цирк', 'default'),
         get_but('💰поддержать автора', 'default')]
    ]
}
main_keyboard = json.dumps(main_keyboard, ensure_ascii=False).encode('utf-8')
main_keyboard = str(main_keyboard.decode('utf-8'))

def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': main_keyboard})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if id not in users:
                users[id] = ''
            if (msg == 'привет') or (msg == '✋привет'):
                sender(id, 'hola amigo, ю хэв э проблем?')
            elif (msg == 'сделай цирк') or (msg == '🎪сделай цирк'):
                sender(id, 'https://goo.su/5c6N')
                users[id] = 'cirk'
            elif users[id] == 'cirk':
                if msg == 'хочухочухочу':
                    sender(id, 'https://www.youtube.com/watch?v=IV5bXvWgs-k')
                elif msg == 'покажи мне что-то ужасное':
                    sender(id, 'https://www.youtube.com/channel/UCybwxopXqi1dcT0LkBlw36g')
            elif msg == 'как делишки?':
                sender(id, 'Я что, не похож на прокурора')
            elif (msg == 'как дела?') or (msg == 'как дела❓'):
                sender(id, 'Дела у прокурора, а у меня делишки')
            elif msg == 'пока':
                sender(id, 'adios amigo')
            elif msg == 'Я уже преисполнился в своем познании настолько,' \
                      'что этот мир мне не интересен':
                sender(id, 'пойди и успокойся, https://gadalkindom.ru/test/na-iq-c-otvetami-i-poyasneniyami.html')
            elif msg == 'что ты можешь сказать про меня?':
                sender(id, 'ответь на вопрос: Мотя хороший?')
                users[id] = '3qestions'
            elif users[id] == '3qestions':
                if msg == 'какой?':
                    sender(id, 'с тобой всё понятно)')
                    users[id] = ''
                elif (msg == 'кншн' or msg == 'да' or msg == 'естественно' or msg == 'конечно' or msg == 'обожаю'):
                    sender(id, 'Молодец, страна таких не забудет')
                    users[id] = ''
                elif (msg == 'хз' or msg == 'не знаю'):
                    sender(id, 'самое время узнать)')
                    users[id] = '2qestions'
                else:
                    sender(id, 'чертов мракобес, пойди убейся головой об стену')
                    users[id] = ''
            elif users[id] == '2qestions':
                if msg == 'узнал':
                    sender(id, 'ну и как?)')
                    users[id] = 'motya'
                else:
                    sender(id, 'Меня такому не обучали, вырвано из контекста')
                    users[id] = ''
            elif users[id] == 'motya':
                if msg == 'мотя хороший':
                    sender(id, 'Молодец, страна таких не забудет')
                    users[id] = ''
                else:
                    sender(id, 'чертов мракобес, пойди убейся головой об стену')
                    users[id] = ''
            elif msg == 'скажи время?':
                sender(id, 'сам посмотри, или спроси, мне лень')
                users[id] = 'time'
            elif users[id] == 'time':
                if msg == 'нет, давай время говори':
                    sender(id, 'чертов мракобес, иди в окно прыгни, и узнаешь')
                    users[id] = 'first_floor'
                else:
                    sender(id, 'Меня такому не обучали, вырвано из контекста')
                    users[id] = ''
            elif users[id] == 'first_floor':
                if msg == 'я живу на первом этаже, мне пофиг':
                    sender(id, 'а ты вниз головой попробуй, так лучше видно')
                    users[id] = ''
                else:
                    sender(id, 'Меня такому не обучали, вырвано из контекста')
                    users[id] = ''
            elif msg == '!хзрандом':
                sender(id, (random.randrange(0, 999999999999999)))
            elif msg == '!1да100':
                sender(id, (random.randrange(1, 100)))
            elif msg == '!1да1000':
                sender(id, (random.randrange(1, 1000)))
            elif msg == 'спасите, убивают':
                sender(id, ('обращайтесь сюда: +7 (495) 224-22-22'))
            elif msg == '!1да1000000':
                sender(id, (random.randrange(1, 1000)))
            elif (msg == '!броськубик') or (msg == '🎲!броськубик'):
                sender(id, f"🎲{random.randrange(1, 7)}")
            elif msg == 'что со мной не так?':
                sender(id, '¯\_(ツ)_/¯, пойди и узнай https://gadalkindom.ru/test/chto-so-mnoj-ne-tak.html')
            elif msg == 'донат':
                sender(id, '💰5599005059226434, всегда пожалуйста')
            elif (msg == 'поддержать автора') or (msg == '💰поддержать автора'):
                sender(id, '💰5599005059226434, всегда пожалуйста')
            elif msg == 'есть лишние деньги':
                sender(id, '💰5599005059226434, всегда пожалуйста')
            elif msg == 'Жизнь скучная':
                sender(id, 'Проблема не в жизни, а в тебе')
            elif msg == 'Я скучный':
                sender(id, 'Не ты такой, жизнь такая')
            elif msg == 'Я скучная':
                sender(id, 'Не ты такая, жизнь такая')
            elif (msg == 'Я застрял в лифте') or (msg == 'я застряла в лифте'):
                sender(id, 'Ищи во всем свои плюсы, у тебя есть время поспать, есть время полениться,'
                           ' или послушать музыку в лифте, если она там есть)))')
            elif (msg == 'я имею лишний вес') or (msg == 'у меня есть лишний вес'):
                sender(id, 'https://yandex.ru/turbo/clinica-opora.ru/s/'
                           'диетология/30-способов-как-похудеть-естественным-с/'
                           '?sign=12766693a22cc54aa41729c8f856d7f5a4016189e3366d3f9b89a2f5761f42de%3A1619647006')
            elif (msg == 'сдохни') or (msg == 'умри') or (msg == 'уйди из жизни') or (msg == 'выйди в окно'):
                sender(id, '😭хныкхнык')
            elif (msg == 'я приемный') or (msg == 'я приемная'):
                sender(id, 'ну шо поделать, на этом мои полномочия всё')
            elif msg == 'до дедлайна 1 минута':
                sender(id, 'сделай вид что ты амёба, или что дедлайна нет')
            else:
                sender(id, 'Меня такому не обучали, вырвано из контекста')

# кукусики
# какой дурак это писал
# зачем я делаю эти комментарии?
# остановите меня, позязя

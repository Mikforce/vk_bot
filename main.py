import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

# Авторизация по токену (ключ доступа)
vk_session = vk_api.VkApi(token='vk1.a.LgZ7ByKhGRg6cp0bi3jbxnhFIv0yhC4STQuxVLNT1gfcOlu3eXCoEs_3npWr7PaaDfhW1AR2DlPNzEK-yNYKl1OcKB0JHMjpKjrftxX61urkDd_8LhRVLfn-ltdsFwI45k1dFcnc3LCKJHTu4L-VJYQvCcSnhe9VqV7n8Qpze6ufhJnlFZoSyelYYPnM3Q5j01ZAHnBv7pLbobJWeeCiUw')

longpoll = VkLongPoll(vk_session)



# Создание клавиатуры
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Цены', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Контакты', color=VkKeyboardColor.PRIMARY)

# Основной цикл бота
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Если пришло сообщение от пользователя
        if event.text.lower() == 'хочу на танцы':
            # Отправляем приветственное сообщение с клавиатурой
            vk_session.method('messages.send', {
                'user_id': event.user_id,
                'message': 'Привет! Что бы вы хотели узнать?',
                'random_id': 0,
                'keyboard': keyboard.get_keyboard()
            })

        # Обработка нажатия на кнопки
        elif event.text.lower() == 'расписание':
            vk_session.method('messages.send', {
                'user_id': event.user_id,
                'message': 'HIP-HOP понедельник среда пятница 18:00 и 19:00, BREAK DANCE понедельник среда пятница 17:00, ЭСТРАДНЫЕ ТАНЦЫ вторник четверг 16:00, вторник четверг 17:00, вторник четверг 19:00, ЦИРКОВАЯ ГИМНАСТИКА ДЛЯ ДЕВОЧЕК понедельник среда пятница 17:00, понедельник среда пятница 18:00, ОСНОВЫ ХОРЕОГРАФИИ вторник четверг 18:00, КАВКАЗСКИЕ НАЦИОНАЛЬНЫЕ ТАНЦЫ вторник четверг 15:00, вторник четверг 16:30, ПАРТЕРНАЯ ХОРЕОГРАФИЯ понедельник среда пятница 19:00, ZUMBA вторник четверг 19:00, STRETCHING понедельник среда пятница 20:00, АКРОБАТИКА ДЛЯ МАЛЬЧИКОВ понедельник среда пятница 16:00, ЗАНЯТИЯ С ПСИХОЛОГОМ понедельник среда пятница 13:00, понедельник среда пятница 14:00, ПАРТЕРНАЯ ХОРЕОГРАФИЯ понедельник среда пятница 19:00',
                'random_id': 0
            })
        elif event.text.lower() == 'цены':
            vk_session.method('messages.send', {
                'user_id': event.user_id,
                'message': 'Абонемент на танцевальные направления: 8 занятий в месяц 1600, на 12 занятий в месяц 2000. Абонемент на зумбу: 8 занятий в месяц 2000. Абонемент на занятия с психологом: 12 занятий в месяц 3000',
                'random_id': 0
            })
        elif event.text.lower() == 'контакты':
            vk_session.method('messages.send', {
                'user_id': event.user_id,
                'message': 'Более подробную информацию вы можете получить позвонив на номер с 15:00 до 19:00 +7 952 838 16 16',
                'random_id': 0
            })
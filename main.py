import telebot
from db import add_message
from db import vivod
bot = telebot.TeleBot("1349894196:AAE0sTRJ2_t_6CdGHjbJBdVY91qxCVaSz7s", parse_mode=None)

user_data = {}

class User:
    def __init__(self, name):
        self.day = name
        self.name = None
        self.list = None
        self.here = None
        self.how = None
        self.ploho = None
        self.covid19 = None
        self.contact = None
        self.another = None
        self.last_name = None


@bot.message_handler(commands=['start'])
def send_w(message):
        msg = bot.send_message(message.chat.id, "Введите дату")
        bot.register_next_step_handler(msg, send_welcome)
def send_welcome(message):
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, "Введите класс")
        bot.register_next_step_handler(msg, process_firstname_step)

def process_firstname_step(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.name = message.text
        msg = bot.send_message(message.chat.id, "Сколько человек по списку?")
        bot.register_next_step_handler(msg, process_list)

def process_list(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.list = message.text
        msg = bot.send_message(message.chat.id, "Сколько присуствуют?")
        bot.register_next_step_handler(msg, process_here)

def process_here(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.here = message.text
        msg = bot.send_message(message.chat.id, "Сколько отсутствуют")
        bot.register_next_step_handler(msg, process_how_step)

def process_how_step(message):
        user_id = message.from_user.id
        how = message.text
        user = user_data[user_id]
        user.how = how
        msg = bot.send_message(message.chat.id, "Сколько по болезни?")
        bot.register_next_step_handler(msg, process_ploho)

def process_ploho(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.ploho = message.text
        msg = bot.send_message(message.chat.id, "Сколько по причине COVID-19?")
        bot.register_next_step_handler(msg, process_covid19)

def process_covid19(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.covid19 = message.text
        msg = bot.send_message(message.chat.id, "Сколько по контакту?")
        bot.register_next_step_handler(msg, process_contact)

def process_contact(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.contact = message.text
        msg = bot.send_message(message.chat.id, "Сколько по иной причине?")
        bot.register_next_step_handler(msg, process_another)

def process_another(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.another = message.text
        msg = bot.send_message(message.chat.id, "Фамилии отсутствующих")
        bot.register_next_step_handler(msg, process_lastname_step)

def process_lastname_step(message):
        user_id = message.from_user.id
        user = user_data[user_id]
        user.lastname = message.text
        msg = bot.send_message(message.chat.id, "Успешно")
      #  print(user.day, user.name, user.list, user.here, user.how, user.ploho, user.covid19, user.contact, user.another, user.lastname)
        add_message(user.name, user.how, user.lastname, user.day, user.list, user.here, user.ploho, user.covid19, user.contact, user.another)
        vivod()



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)




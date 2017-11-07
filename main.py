from googletrans import Translator
import telebot
from telebot import types
import re

bot = telebot.TeleBot("485245927:AAHRvDNPHsj7e6BOYzj8-9GqpdyIVDH9xR4")
translator = Translator()

pattern = re.compile(r"^(\w+) (\w+) (.*)")

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        res = re.findall(pattern, query.query)
        lang_from = res[0][0]
        lang_to = res[0][1]
        text = res[0][2]         
    except Exception as ex:
        return
    try:     
        trans = translator.translate(text, src=lang_from, dest=lang_to)
        ret_text = types.InlineQueryResultArticle(
            id="1", title="Click to send", description=trans.text,
            input_message_content=types.InputTextMessageContent(message_text=trans.text)
        )
        bot.answer_inline_query(query.id, [ret_text])
    except Exception as ex:
        return("Error")
bot.polling(none_stop=True)
from utils.parser.web_requests import PictureGeter
from handlers.vars_for_handlers.vars import get_temp_category
from loader import bot
from aiogram import types

# if int(count_in_message.text) > 100:
#     await count_in_message.answer("Дайте мне немного времени")
# parsed_pictures = PictureGeter.get_list_with_urls_on_pictures(int(count_in_message.text), await get_temp_category())
# for url_link in parsed_pictures:
#     try:
#         await bot.send_photo(chat_id=count_in_message.chat.id, photo=url_link)
#     except InvalidHTTPUrlContent or WrongFileIdentifier or AttributeError:
#         pass
#     except ValueError:
#         await count_in_message.answer("Введите цифру")
#

class ParserManager:
    @staticmethod
    async def process_settings_for_parser(count_in_message):
        try:
            count = int(count_in_message)
            return count
        except TypeError:
            return "Цифру пожалуйста )"

    async def run_parser(self, count: int):
        result = PictureGeter.get_list_with_urls_on_pictures(category=await get_temp_category(), count_of_pictures=count)
        return result
    
    
    async def check_type(self, message):
        print(1)
        print(type(self.process_settings_for_parser(message)))
        if type(self.process_settings_for_parser(message)) == "int":
            print(1)


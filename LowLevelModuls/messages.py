from utils.parser.web_requests import PictureGeter
from handlers.vars_for_handlers.vars import get_temp_category
from loader import bot


async def set_category_for_parser_and_run(message):
    if int(message.text) > 100:
        await message.answer("Дайте мне немного времени")
    parsed_pictures = PictureGeter.get_list_with_urls_on_pictures(int(message.text), await get_temp_category())
    for url_link in parsed_pictures:
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=url_link)
        except InvalidHTTPUrlContent or WrongFileIdentifier or AttributeError:
            pass
        except ValueError:
            await message.answer("Введите цифру")

# TODO: в утилитах создать папку в которой будут 
# только модули работы с хендлерами 

# TODO: в утилитах в другой папке модуль с \ done
# переменными и методами работы с ними (set get) \ done

# TODO: убрать вебреквест в утилиты|done

# TODO: send_picture сделать модулем более высокого уровня \ done

# TODO: бд убрать в дату\done

# TODO: придумать максимально понятные имена модулей и функций\ okay, i will rty to do it as good as i can think =)
# и переменных


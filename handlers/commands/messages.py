async def set_category(message):
    passfor_check = message.text.capitalize()
    yes_no = False
    temp = None
    if for_check in CategoryList:
        text = f"Вы выбрали: {message.text}\nТеперь укажите количество картинок которое хотите получить (не больше 100)"
        temp = for_check
        yes_no = True
    else:
        text = 'Такой категории нет, возможно вы ввели цифру или допустили орфографическую ошибку\nВы можете попробовать снова ;)'

    return (text, yes_no, temp)

# TODO: в утилитах создать папку в которой будут 
# только модули работы с хендлерами 

# TODO: в утилитах в другой папке модуль с 
# переменными и методами работы с ними (set get)

# TODO: убрать вебреквест в утилиты

# TODO: send_picture сделать модулем более высокого уровня

# TODO: бд убрать в дату

# TODO: придумать максимально понятные имена модулей и функций
# и переменных


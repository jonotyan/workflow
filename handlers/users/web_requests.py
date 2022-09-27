from requests import get

CategoryList = [
"Абстрактные",
"Авиация",
"Аниме",
"Архитектура",
"Векторные",
"Весна",
"Винтаж",
"Вода",
"Водопады",
"Города",
"Горы",
"Девушки",
"Деньги",
"Дети",
"Дождь",
"Еда",
"Животные",
"Закаты",
"Земноводные",
"Зима",
"Игры",
"Интерьер",
"Корабли",
"Космос",
"Кошки",
"Лето",
"Лошади",
"Любовь",
"Люди",
"Макро",
"Машины",
"Мосты",
"Мотоциклы",
"Мужчины",
"Музыка",
"Мультфильмы",
"Напитки",
"Насекомые",
"Неоновые",
"Ночь",
"Облака",
"Озёра",
"Океан",
"Осень",
"Пейзажи",
"Подводный мир",
"Природа",
"Птицы",
"Рассвет",
"Рендеринг",
"Ретро автомобили",
"Рисованные",
"Сладости",
"Собаки",
"Спорт",
"Узоры",
"Фантастика",
"Фильмы",
"Фоны",
"Фрукты",
"Цветы"]

class PictureGeter:
    url = "https://7fon.org/Обои/"
    r = get(url)
    start_indx = r.text.find('<div id="cbox">')
    end = r.text.find('<ins class="adsbygoogle"')
    delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
    html_list = r.text[start_indx:end].split(delimetr)
    on_page = 0
    list_of_links: list = []

    @classmethod
    def __reset_url(cls):
        cls.url = "https://7fon.org/Обои/"

    @classmethod
    def __set_category(cls, category: str):
        cls.__reset_url()
        cls.url += category

    @classmethod
    def __open_next_page(cls, category):
        cls.__set_category(category=category)
        cls.on_page += 1
        url_of_new_page = cls.url + f"/{cls.on_page}.html"
        return url_of_new_page

    @classmethod
    def __reset_page_info(cls, cat):
        cls.url = cls.__open_next_page(category=cat)
        r = get(cls.url)
        start_indx = r.text.find('<div id="cbox">')
        end = r.text.find('<ins class="adsbygoogle"')
        delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
        cls.html_list = r.text[start_indx:end].split(delimetr)

    @classmethod
    def __get_links(cls):
        list_with_ready_links = []
        for line in cls.html_list:
            index_img = line.find("<img src=") + 12
            tmp = line[index_img:]
            finish_index = tmp.find('alt=') - 2
            list_with_ready_links.append(tmp[:finish_index])
        return list_with_ready_links

    @classmethod
    def __check_count(cls, count_of_pictures, category):
        cls.__reset_page_info(category)
        cls.list_of_links += cls.__get_links()
        now_count = len(cls.list_of_links)
        if now_count > count_of_pictures:
            return cls.list_of_links[:count_of_pictures]
        else:
            cls.__reset_page_info(category)
            while now_count < count_of_pictures:
                cls.list_of_links += cls.__get_links()[1:]
                now_count = len(cls.list_of_links)
                cls.__reset_page_info(category)
            else:
                return cls.list_of_links[:count_of_pictures]

    @classmethod
    def get_list_with_pictures(cls, count_of_pictures: int, category: str):
        final_result = cls.__check_count(count_of_pictures+1, category=category)
        final_result_ = final_result[1:]
        cls.__reset_url()
        return final_result_

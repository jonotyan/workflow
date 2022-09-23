from requests import get


class PictureGeter:
    url = "https://7fon.org/Обои/Любовь"
    r = get(url)
    start_indx = r.text.find('<div id="cbox">')
    end = r.text.find('<ins class="adsbygoogle"')
    delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
    html_list = r.text[start_indx:end].split(delimetr)
    on_page = 1
    list_of_links = []

    @classmethod
    def __reset_page_info(cls):
        cls.url = cls.__open_next_page()
        r = get(cls.url)
        start_indx = r.text.find('<div id="cbox">')
        end = r.text.find('<ins class="adsbygoogle"')
        delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
        cls.html_list = r.text[start_indx:end].split(delimetr)

    @classmethod
    def __open_next_page(cls):
        def update_var_on_page(on_page):
            page = on_page + 1
            return page

        cls.url = "https://7fon.org/Обои/Любовь"
        new_page = update_var_on_page(on_page=cls.on_page)
        url_of_new_page = cls.url + f"/{new_page}.html"
        cls.on_page = new_page
        return url_of_new_page

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
    def __check_count(cls, count_of_pictures):
        def adding_loop(list_):
            for i in cls.__get_links()[1:]:
                list_.append(i)
            return list_

        list_of_links: list = cls.__get_links()
        now_count = len(list_of_links)
        if now_count > count_of_pictures:
            return list_of_links[:count_of_pictures]
        else:
            cls.__reset_page_info()
            while now_count < count_of_pictures:
                cls.list_of_links = adding_loop(list_of_links)
                now_count = len(cls.list_of_links)
                cls.__reset_page_info()
            else:
                return list_of_links[:count_of_pictures]

    @classmethod
    def return_list_with_pictures(cls, count_of_pictures: int):
        final_result = cls.__check_count(count_of_pictures)
        final_result_ = final_result[1:]
        return final_result_


p = PictureGeter.return_list_with_pictures(701)
a=0
for i in p:
    a+=1
    print(a, i)


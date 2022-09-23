from requests import get


class PictureGeter:
    url = "https://7fon.org/Обои/"
    r = get(url)
    start_indx = r.text.find('<div id="cbox">')
    end = r.text.find('<ins class="adsbygoogle"')
    # end_indx = r.text.rfind('<script async src="')
    delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
    html_list = r.text[start_indx:end].split(delimetr)

    @staticmethod
    def __open_next_page():
        on_page = 0

        def update_var_on_page():
            page = on_page + 1
            return page
        url_of_new_page = url + f"{update_var_on_page()}.html"
        return url_of_new_page

    @classmethod
    def __get_links(cls):
        list_with_ready_links = []
        for line in cls.html_list:
            tmp = line[indx_img:]
            finish_index = tmp.find('alt=') - 2
            list_with_ready_links.append(tmp[:finish_index])
            return list_with_ready_links

    @staticmethod
    def __unpack_list(list_):
        for element in list_:
            yield element

    @classmethod
    def __check_count(cls, count_of_pictures):
        list_of_links: list = cls.__get_links()
        now_count = len(list_of_links)
        while now_count < count_of_pictures:
            new_result = cls.__get_links()
            list_of_links.append(cls.__unpack_list(new_result))
            now_count = len(list_of_links)
        else:
            return list_of_links

    @classmethod
    def return_list_with_pictures(cls, count_of_pictures):
        return cls.__check_count(count_of_pictures)


print(PictureGeter.return_list_with_pictures(7))






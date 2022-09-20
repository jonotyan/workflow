from requests import get


class PictureGeter:
    url = "https://7fon.org/Обои/Дети"
    r = get(url)
    start_indx = r.text.find('<div id="cbox">')
    end = r.text.find('<ins class="adsbygoogle"')
    end_indx = r.text.rfind('<script async src="')
    delimetr = '<div id="tmbox" itemscope itemtype="http://schema.org/ImageObject">'
    html_list = r.text[start_indx:end].split(delimetr)

    @staticmethod
    def __get_links():
        list_with_ready_links = []
        for line in html_list:
            tmp = line[indx_img:]
            finish_index = tmp.find('alt=') - 2
            list_with_ready_links.append(tmp[:finish_index])
            return list_with_ready_links

    @classmethod
    def return_list_with_pictures(cls):
        return __get_links()



import vk_api
from pprint import pprint
import urllib.request
from workshop_blog.models import Article, ArticlePhoto, Vk_data


class BolgWriter:

    def __init__(self):
        self.vk_data = Vk_data.objects.get(id='1')
        print('init')


    def writer(self) -> None:
        print('writer')
        token = self.vk_data.vk_app_token
        vk = vk_api.VkApi(token=token)
        wall = vk.method('wall.get', {'owner_id': -self.vk_data.vk_group_id, 'count': '5'})
        id_articles_list = []
        article_list = self.article_names_list(Article.objects.order_by('id'))
        for i in wall['items']:
            if i['text'] in article_list:
                self.save_material(wall, id_articles_list)
            else:
                id_articles_list.append(i['id'])

    def save_material(self, wall, id_articles_list) -> None:
        print('save_material')
        for attach in wall['items']:
            if attach['id'] in id_articles_list:
                photos = []
                for photo in attach['attachments']:
                    photos.append(self.save_photo(photo['photo']['sizes'][-1]))
                article = Article.create(text=attach['text'])

                article.save()
                for photo in photos:
                    art_photo = ArticlePhoto.create(img=photo, article=article)
                    art_photo.save()

    def save_photo(self, photo) -> str:
        print('save_photo')
        name = str(photo['url'][37:50]) + '.jpg'
        photo = urllib.request.urlretrieve(photo['url'], f"media/{name}")
        return name

    def article_names_list(self, obj)->list:
        print('article_names_list')
        value_list = []
        for i in obj.values():
            value_list.append(i['text'])
        return value_list


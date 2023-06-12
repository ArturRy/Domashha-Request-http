
#                      Задача №1

# from pprint import pprint
# import requests
# import json
# hero_names = ['Hulk', 'Captain America', 'Thanos']
# url = 'https://akabab.github.io/superhero-api/api/all.json'
# responce = requests.get(url)
#
# hero_list = {}
# for hero in responce.json():
#     for name in hero_names:
#         if name in hero['name']:
#             hero_list.update({name: hero['powerstats']['intelligence']})
# print('Самый умный супергерой:', (sorted(hero_list.items(),key=lambda x: x[1])[-1]))

                       # Задача №2

# import pprint
# import requests
# import json
#
# url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
# token = 'OAuth '
# params = {
#     'path': ''
# }
# headers = {
#     'Authorization': token
# }


# class YaUploader:
#
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         file_path = path_to_file
#         params['path'] = 'image/' + file_path.split("\\")[-1]         (Для Windows)
#         params['path'] = 'image/' + file_path.split("/")[-1]          (Для Linux и macOS)
#         responce = requests.get(url, headers=headers, params=params)
#         if 200 <= responce.status_code < 300:
#             url_for_upload = responce.json().get('href', '')
#             with open(file_path, 'rb') as picture:
#                 requests.put(url_for_upload, files={'file': picture})
#
#
# if __name__ == '__main__':
#     path_to_file = r'Путь до файла на компьютере'
#     token = 'OAuth '
#     uploader = YaUploader(token)
#     uploader.upload(path_to_file)

                 # Задача №3
# from pprint import pprint
# import requests
# import json
# import time
#
# todate = round(time.time())
# fromdate = todate - 172800
#
# url = f'https://api.stackexchange.com//2.3/questions?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged=Java&site=stackoverflow'
# responce = requests.get(url)
# questions_list = []
# for questions in responce.json()['items']:
#     questions_list.append([questions['title'], questions['link']])
# pprint(questions_list)

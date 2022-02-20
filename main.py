import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, loadfile, replace=False):
        savefile = os.path.basename(path_to_file)
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        result = requests.get(f'{upload_url}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
        with open(loadfile, 'rb') as f:
            try:
                requests.put(result['href'], files={'file':f})
                print(f'Файл {savefile} успешно сохранен')
            except KeyError:
                print(result)

if __name__ == '__main__':
    token = input('Введите Токен: ')
    path_to_file = input('Введите путь к файлу: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

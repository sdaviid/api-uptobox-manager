import requests

class uptobox(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_api = 'https://uptobox.com'
    def build_url(self, url):
        return f'{self.base_api}{url}?token={self.api_key}'
    def status(self):
        url = self.build_url('/api/user/me')
        try:
            response = requests.get(url)
            if response.status_code == 200:
                if response.json().get('statusCode', -1) == 0:
                    return True
        except Exception as err:
            print(f'uptobox.status exception - {err}')
        return False
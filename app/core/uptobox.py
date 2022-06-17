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
    def upload_remote_server(self):
        url = self.build_url('/api/upload')
        try:
            response = requests.get(url)
            if response.status_code == 200:
                if response.json().get('statusCode', -1) == 0:
                    temp_upload_url = response.json().get('data', {}).get('uploadLink', False)
                    if temp_upload_url:
                        return f'https://{temp_upload_url[2:]}'
        except Exception as err:
            print(f'uptobox.upload_remote_server exception - {err}')
        return False
    def upload_remote(self, link):
        url = self.upload_remote_server()
        if url:
            url = url.replace('upload', 'remote')
            session = requests.Session()
            headers = {
                'content-type': 'application/x-www-form-urlencoded'
            }
            payload = {
                'urls': f'["{link}"]'
            }
            with session.post(url, data=payload, headers=headers, stream=True) as resp:
                for line in resp.iter_lines():
                    if line:
                        print(line)



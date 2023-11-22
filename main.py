import http.server
import socketserver
import urllib.parse
import requests
import json
from api import *

class YandexSearchHandler(http.server.BaseHTTPRequestHandler):
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Results saved to {filename}")

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query = urllib.parse.parse_qs(parsed_path.query)

        if path == '/search_by_name':
            self.search_by_name(query)
        elif path == '/search_by_services':
            self.search_by_services(query)
        elif path == '/search_by_address':
            self.search_by_address(query)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def search_by_name(self, query):
        if 'name' in query:
            name = query['name'][0]
            api_key = yandex_api
            url = f'https://search-maps.yandex.ru/v1/?text={name}&type=biz&lang=ru_RU&apikey={api_key}'

            response = requests.get(url)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response.content)

            self.save_to_json(response.json(), 'result.json')

    def search_by_services(self, query):
        if 'services' in query:
            services = query['services'][0]
            api_key = yandex_api
            url = f'https://search-maps.yandex.ru/v1/?text={services}&type=biz&lang=ru_RU&apikey={api_key}'

            response = requests.get(url)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response.content)

            self.save_to_json(response.json(), 'result.json')

    def search_by_address(self, query):
        if 'organization' in query and 'city' in query and 'street' in query:
            organization = query['organization'][0]
            city = query['city'][0]
            street = query['street'][0]
            api_key = yandex_api
            url = f'https://search-maps.yandex.ru/v1/?text={organization},{city},{street}&type=biz&lang=ru_RU&apikey={api_key}'

            response = requests.get(url)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response.content)

            self.save_to_json(response.json(), 'result.json')

if __name__ == "__main__":
    PORT = 8000
    handler = YandexSearchHandler
    httpd = socketserver.TCPServer(("", PORT), handler)

    print(f"Serving at port {PORT}")
    httpd.serve_forever()

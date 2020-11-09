import requests
from bs4 import BeautifulSoup


anime_list = {
}

user_name = 'M.M'
request_url = f'https://shikimori.one/{user_name}/list/anime/mylist/completed/order-by/ranked/page/'
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

def get_page(request_url):
    return requests.get(request_url, headers=request_headers)

def parse_page(page_number):
    response = get_page(request_url+str(page_number))
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.findAll('a', class_='tooltipped')
    if divs == []:
        return None
    div_a = [div.text for div in divs]
    div_b = [div.get('href') for div in divs]
    for index in range(0,len(div_a)):
        anime_list[div_a[index]] = div_b[index]
    return anime_list


def main():
    page_number = 1
    i = 1
    with open(f'../anime_list.txt', 'w', encoding='utf-8') as f:
        f.write('Название: Ссылка\n')
        while True:
            if parse_page(page_number) == None:
                break
            print(page_number)
            page_number += 1
        for key, value in anime_list.items():
            f.write(f'{i}) {key}: {value}\n')
            i += 1

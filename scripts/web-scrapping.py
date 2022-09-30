import requests
from bs4 import BeautifulSoup

imbd_get = requests.get("https://www.imdb.com/search/keyword/?keywords=marvel&ref_=fn_al_kw_1")
imdb_html = BeautifulSoup(imbd_get.content, 'html.parser')

# print(imdb_html)

movie_list = imdb_html.find('div', {'class': 'lister-list'})
rows = movie_list.findAll('h3')
for row in rows:
    movie_row = row.a # Same as row.find('a')
    movie_title = movie_row.text

    movie_link = f"https://www.imdb.com{movie_row['href']}"
    print(movie_link)
    movie_get = requests.get(movie_link)
    movie_html = BeautifulSoup(movie_get.content, 'html.parser')
    print(movie_html)
    genre_html = movie_html.find('script', type='application/ld+json').text
    # print(genre_html)
    # genre_list = genre_html.findAll('a')
    # print(genre_html)
    if genre_html is not None:
        break

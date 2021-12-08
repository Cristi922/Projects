from bs4 import BeautifulSoup
import lxml
import requests
import html5lib

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_online_site = response.text
soup = BeautifulSoup(empire_online_site, "html.parser")

movie_title = soup.find(name="h3", class_="jsx-4245974604")

print(movie_title)












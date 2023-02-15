import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(URL)
empire_response=response.text
soup=BeautifulSoup(empire_response,'html.parser')
all_movies=soup.find_all(name="h3",class_="title" )
# tt=t.find_all(class_="jsx-3523802742 listicle-item")
# ttt=tt.find_all(class_="jsx-4245974604")

movies_titles=[movie.getText() for movie in all_movies]

movies=movies_titles[::-1]


with open('movies.txt','w') as file:
    for movie in movies:
        file.write(f"{movie}\n")


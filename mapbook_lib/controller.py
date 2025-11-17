from bs4 import BeautifulSoup
import requests
import folium


class User:
    def __init__(self, name:str, location:str, posts:int, img_url:str):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_coordinates()

    def get_coordinates(self):
        from bs4 import BeautifulSoup
        import requests
        url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        return [latitude, longitude]



def user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user.name} z miejscowości {user.location} opublikował {user.posts} postów")


def add_user(users_data: list) -> None:
    name: str = str(input("Podaj imię nowego znajomego: "))
    location: str = str(input("Podaj lokalizację nowego znajomego: "))
    posts: int = int(input("Podaj liczbę postów nowego znajomego: "))
    img_url: str = str(input("Wprowadź adres URL zdjęcia: "))
    users_data.append(User(name, location, posts, img_url))


def remove_user(users_data: list)->None:
    temp_name:str=str(input("Podaj imię użytkownika do usunięcia: "))
    for user in users_data:
        if user.name == temp_name:
            users_data.remove(user)


def update_user(users_data: list)->None:
    temp_name:str=str(input("Podaj imię użytkownika do aktualizacji: "))
    for user in users_data:
        if user.name == temp_name:
            user.name= input("Podaj nowe imię użytkownika: ")
            user.location=input("Podaj nową lokalizację: ")
            user.posts=input("Podaj nową liczbę postów: ")
            user.coords=user.get_cordinates()



def get_map(users_data:list) -> None:
    m = folium.Map(location=[52.23, 21.0], zoom_start=7)
    for user in users_data:
        folium.Marker(
            location=user.coords,
            tooltip=user.name,
            popup=f"<h4>{user.name}</h4> {user.location}, {user.posts}, <img src={user.img_url} alt='jewpiter' />",
            icon=folium.Icon(icon="cloud", color="red", icon_color="blue")
        ).add_to(m)

    m.save("index.html")

if __name__ == "__main__":
    users_data: list=[]
    add_user(users_data)
    remove_user(users_data)
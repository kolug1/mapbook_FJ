from bs4 import BeautifulSoup
import requests
import folium

users: list = [
    {"name": "Filip", "location": "Warszawa", "posts": 67,
     "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRgj9k_XcnXz9UQ0z5xWAqBQO5BxMPXe7QOg&s"},
    {"name": "Krzysiu", "location": "Kraków", "posts": 88,
     "img_url": "https://scontent-vie1-1.xx.fbcdn.net/v/t1.15752-9/574371045_1677000559932459_8926965949219304294_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=E0IwTrLjXDcQ7kNvwFqalft&_nc_oc=AdmhLrHJAFqCVsJyLu0-D1m8Rl4j5Y57yGTC4khgnOwxbl3Q0JcNY4-gTmzZObl0NNE&_nc_zt=23&_nc_ht=scontent-vie1-1.xx&oh=03_Q7cD3wGcUQwkevJCaLrfXd9R5RyU0v2DMYYA_HiPPy45ncEzLA&oe=69301FB0"},
    {"name": "Asia", "location": "Siedlce", "posts": 4,
     "img_url": "https://www.wig.wat.edu.pl/index.php/component/joomgallery/image?view=image&format=raw&type=orig&id=1265"},
    {"name": "Basia", "location": "Kraśnik", "posts": 2137,
     "img_url": "https://data3.cupsell.pl/upload/generator/247026/640x420/5469898_print_1.png?resize=max_sizes&key=55f9a22768eed085006592c1174c0235"},
]

def user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} postów")


def add_user(users_data: list) -> None:
    name: str = str(input("Podaj imię nowego znajomego: "))
    location: str = str(input("Podaj lokalizację nowego znajomego: "))
    posts: int = int(input("Podaj liczbę postów nowego znajomego: "))
    img_url: str = str(input("Wprowadź adres URL zdjęcia: "))
    users_data.append({"name": name, "location": location, "posts": posts, "img_url": img_url})


def remove_user(users_data: list)->None:
    temp_name:str=str(input("Podaj imię użytkownika do usunięcia: "))
    for user in users_data:
        if user["name"] == temp_name:
            users_data.remove(user)


def update_user(users_data: list)->None:
    temp_name:str=str(input("Podaj imię użytkownika do aktualizacji: "))
    for user in users_data:
        if user["name"] == temp_name:
            user["name"]= input("Podaj nowe imię użytkownika: ")
            user["location"]=input("Podaj nową lokalizację: ")
            user["posts"]=input("Podaj nową liczbę postów: ")


def get_cordinates(city_name:str) -> list:
    url: str = f"https://pl.wikipedia.org/wiki/{city_name}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    return [latitude, longitude]


def get_map(users_data:list) -> None:
    m = folium.Map(location=[52.23, 21.0], zoom_start=7)
    for user in users_data:
        folium.Marker(
            location=get_cordinates(user["location"]),
            tooltip=user["name"],
            popup=f"<h4>{user["name"]}</h4> {user["location"]}, {user["posts"]}, <img src={user["img_url"]} alt='jewpiter' />",
            icon=folium.Icon(icon="cloud", color="red", icon_color="blue")
        ).add_to(m)

    m.save("index.html")


while True:
    print("======================MENU=============nigga=========")
    print("0. Wyjście")
    print("1. Wyświetlanie aktywności znajomych")
    print("2. Dodaj znajomego")
    print("3. Usuwabue znajomego")
    print("4. Aktualizacja znajomego")
    print("5. Wyświetlanie mapy znajomych")
    print("=======================================nigga=========")
    temp_choice: int = int(input("Wybierz opcję menu "))
    if temp_choice == 0:
        break
    if temp_choice == 1:
        print("Wybrano funkcję wyświetlania aktywności znajomych")
        user_info(users)
    if temp_choice == 2:
        print("Wybrano funkcję dodawania znajomego")
        add_user(users)
    if temp_choice == 3:
        print("Wybrano funkcję usuwania znajomego")
        remove_user(users)
    if temp_choice == 4:
        print("Wybrano funkcję aktualizacji danych znajomego")
        update_user(users)
    if temp_choice == 5:
        print("Wybrano funkcję wyświetlania mapy")
        get_map(users)

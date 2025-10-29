users: list = [
    {"name": "Filip", "location": "Warszawa", "posts": 67},
    {"name": "Krzysiu", "location": "Radom", "posts": 2137},
    {"name": "Asia", "location": "Siedlce", "posts": 4},
    {"name": "Basia", "location": "Kraśnik", "posts": 88},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} postów")


def add_user(users_data: list) -> None:
    name: str = str(input("Podaj imię nowego znajomego: "))
    location: str = str(input("Podaj lokalizację nowego znajomego: "))
    posts: int = int(input("Podaj liczbę postów nowego znajomego: "))
    users_data.append({"name": name, "location": location, "posts": posts})



def remove_user(users_data)->None:
    temp_name:str=str(input("Podaj imię użytkownika do usunięcia: "))
    for user in users_data:
        if user["name"] == temp_name:
            users_data.remove(user)


while True:
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

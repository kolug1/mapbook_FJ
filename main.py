users: list = [
    {"name": "Filip", "location": "Warszawa", "posts": 67},
    {"name": "Krzysiu", "location": "Radom", "posts": 2137},
    {"name": "Asia", "location": "Siedlce", "posts": 4},
    {"name": "Basia", "location": "Kraśnik", "posts": 88},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} postów")


while True:
    temp_choice: int = int(input("Wybierz opcję menu "))
    if temp_choice == 0:
        break
    if temp_choice == 1:
        print("Wybrano funkcję wyświetlania aktywności znajomych")
        user_info(users)
    if temp_choice == 2:
        print("Wybrano funkcję dodawania znajomego")
    if temp_choice == 3:
        print("Wybrano funkcję usuwania znajomego")
    if temp_choice == 4:
        print("Wybrano funkcję aktualizacji danych znajomego")

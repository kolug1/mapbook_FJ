users: list = [
    {"name": "Filip", "location": "Warszawa", "posts": 67},
    {"name": "Krzysiu", "location": "Radom", "posts": 2137},
    {"name": "Asia", "location": "Siedlce", "posts": 4},
    {"name": "Basia", "location": "Kraśnik", "posts": 88},
]

for user in users:
    print(f"Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} postów")

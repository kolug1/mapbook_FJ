from mapbook_lib.controller import user_info, add_user, remove_user, update_user, get_map
from mapbook_lib.model import users

def main():
    while True:
        print("======================MENU======================")
        print("0. Wyjście")
        print("1. Wyświetlanie aktywności znajomych")
        print("2. Dodaj znajomego")
        print("3. Usuwanie znajomego")
        print("4. Aktualizacja znajomego")
        print("5. Wyświetlanie mapy znajomych")
        print("================================================")
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


if __name__ == "__main__":
    main()
from tkinter import *
import tkintermapview

users: list = []

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


def add_user(users_data: list) -> None:
    name: str = entry_name.get()
    location: str = entry_lokalizacja.get()
    posts: int = int (entry_posty.get())
    img_url: str = entry_imgurl.get()
    users_data.append(User(name, location, posts, img_url))
    print(users_data)
    user_info(users_data)
    entry_name.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_posty.delete(0, END)
    entry_imgurl.delete(0, END)
    entry_name.focus()


def user_info(users_data: list):
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users_data):
        listbox_lista_obiektow.insert(idx, f"{user.name} {user.location} {user.posts}")


def delete_user(users_data: list):
    i = listbox_lista_obiektow.index(ACTIVE)
    users_data.pop(i)
    user_info(users_data)


def user_details(users_data: list):
    i = listbox_lista_obiektow.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=users_data[i].name)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=users_data[i].location)
    label_posty_szczegoly_obiektu_wartosc.config(text=users_data[i].posts)


def edit_user(users_data: list):
    i = listbox_lista_obiektow.index(ACTIVE)
    entry_name.insert(0, users_data[i].name)
    entry_lokalizacja.insert(0, users_data[i].location)
    entry_posty.insert(0, users_data[i].posts)
    entry_imgurl.insert(0, users_data[i].img_url)
    button_dodaj_obiekt.config(text = "Zapisz zmiany", command=lambda: update_user(users, i))


def update_user(users_data: list, i):
    users_data[i].name=entry_name.get()
    users_data[i].location=entry_lokalizacja.get()
    users_data[i].posts=entry_posty.get()
    users_data[i].imgurl=entry_imgurl.get()
    entry_name.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_posty.delete(0, END)
    entry_imgurl.delete(0, END)
    button_dodaj_obiekt.config(text="Dodaj obiekt", command=lambda: add_user(users))
    user_info(users_data)


root = Tk()
root.geometry("1025x760")
root.title("MapBook")

ramka_lista_obiektow=Frame(root)
ramka_formularz = Frame(root)
ramka_szczegolow_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegolow_obiektu.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

#RAMKA_LISTA_OBIEKTOW
label_lista_obiektow = Label(ramka_lista_obiektow, text="Lista obiektów")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)

listbox_lista_obiektow = Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text="Pokaż szczegóły", command=lambda: user_details(users))
button_pokaz_szczegoly.grid(row=2, column=0)

button_usun_obiekt = Button(ramka_lista_obiektow, text="Usuń obiekt", command=lambda: delete_user(users))
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiektow, text="Edytuj obiekt", command=lambda: edit_user(users))
button_edytuj_obiekt.grid(row=2, column=2)



#RAMKA FORMULARZ
label_formularz = Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)

label_imie = Label(ramka_formularz, text="Imię")
label_imie.grid(row=1, column=0, sticky=W)

label_lokalizacja = Label(ramka_formularz, text="Lokalizacja")
label_lokalizacja.grid(row=2, column=0, sticky=W)

label_posty = Label(ramka_formularz, text="Liczba postów")
label_posty.grid(row=3, column=0, sticky=W)

label_imgurl = Label(ramka_formularz, text="Obrazek")
label_imgurl.grid(row=4, column=0, sticky=W)

entry_name = Entry(ramka_formularz)
entry_name.grid(row=1, column=1, sticky=W)

entry_lokalizacja = Entry(ramka_formularz)
entry_lokalizacja.grid(row=2, column=1)

entry_posty = Entry(ramka_formularz)
entry_posty.grid(row=3, column=1)

entry_imgurl = Entry(ramka_formularz)
entry_imgurl.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text="Dodaj obiekt", command=lambda: add_user(users))
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)



#RAMKA SZCZEGÓŁY OBIEKTU
label_szczegoly_obiektu = Label(ramka_szczegolow_obiektu, text="Szczegóły obiektu")
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

label_imie_szczegoly_obiektu = Label(ramka_szczegolow_obiektu, text="Imię: ")
label_imie_szczegoly_obiektu.grid(row=1, column=0)

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegolow_obiektu, text="....")
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegolow_obiektu, text="Lokalizacja: ")
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=2)

label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegolow_obiektu, text="....")
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=3)

label_posty_szczegoly_obiektu = Label(ramka_szczegolow_obiektu, text="Posty: ")
label_posty_szczegoly_obiektu.grid(row=1, column=4)

label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegolow_obiektu, text="....")
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)


#RAMKA MAPY
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1025, height=600)
map_widget.set_position(52.0,21.0)
map_widget.set_zoom(10)
map_widget.grid(row=0, column=0)



root.mainloop()
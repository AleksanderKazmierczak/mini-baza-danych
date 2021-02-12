# import modulow
from tkinter import *


# definicja funkcji zapisywania danych
def save_info():
    # pobranie danych od uzytkownika
    nralbumu_info = nralbumu.get()
    imienazwisko_info = imienazwisko.get()
    wydzial_info = wydzial.get()
    kierunek_info = kierunek.get()
    przedmiot_info = przedmiot.get()
    print(nralbumu_info, imienazwisko_info, wydzial_info, kierunek_info, przedmiot_info)

    # otwarcie/utworzenie pliku tekstowego i dopisanie danych studenta
    file = open("danestudenta.txt", "a")
    file.write("\n" + nralbumu_info + "\n")
    file.write("Imie nazwisko: " + imienazwisko_info + "\n")
    file.write("Wydzial: " + wydzial_info + "\n")
    file.write("Kierunek: " + kierunek_info + "\n")
    file.write("Przedmiot: " + przedmiot_info)
    # zamkniecie pliku tekstowego
    file.close()

    # usuniecie zawartosci pol wejsciowych
    nralbumu_entry.delete(0, END)
    imienazwisko_entry.delete(0, END)
    wydzial_entry.delete(0, END)
    kierunek_entry.delete(0, END)
    przedmiot_entry.delete(0, END)


# definicja funkcji wyswietlajacej dane studenta na podstawie podanego nr albumu
def show_info():
    # pobranie nr albumu na podstawie ktorego funkcja search znajdzie dane okreslonego studenta
    index = (nralbumu.get() + "\n")
    nralbumu_entry.delete(0, END)
    # przypisanie wyniku funkcji search do zmiennej "s" w celu jej wyswietlenia
    s = (search(index))
    text2_text = Label(text=s)
    text2_text.place(x=240, y=140, width="180", height="100")


# definicja funkcji znajdujacej dane okreslonego studenta na podstawie nr albumu
def search(index):
    # otwarcie pliku tekstowego do odczytu
    file2 = open("danestudenta.txt", "r")
    result = ""
    counter = -1
    for line in file2:
        if line == index:
            counter = 1
            result += line
        else:
            if counter > 0:
                result += line
                counter += 1
            if counter == 5:
                return result
    file2.close()


# inicjalizacja okna aplikacji
screen = Tk()
screen.geometry("450x360")
screen.title("Mini baza danych")
theLabel = Label(text="Dane studentów", bg="grey", fg="black", width="500", height="2")
theLabel.pack()

# utworzenie etykiet dla poszczegolnych danych studenta
nralbumu_text = Label(text="Nr albumu: ")
imienazwisko_text = Label(text="Imie Nazwisko: ")
wydzial_text = Label(text="Wydzial: ")
kierunek_text = Label(text="Kierunek: ")
przedmiot_text = Label(text="Przedmiot: ")
text_text = Label(text="Dane studenta: ")

# określenie pozycji etykiet w oknie aplikacji
nralbumu_text.place(x=15, y=50)
imienazwisko_text.place(x=15, y=100)
wydzial_text.place(x=15, y=150)
kierunek_text.place(x=15, y=200)
przedmiot_text.place(x=15, y=250)
text_text.place(x=250, y=120)

# okreslenie typow zmiennych
nralbumu = StringVar()
imienazwisko = StringVar()
wydzial = StringVar()
kierunek = StringVar()
przedmiot = StringVar()
text = StringVar()

# utworzenie pol na dane wejsciowe
nralbumu_entry = Entry(textvariable=nralbumu, width="30")
imienazwisko_entry = Entry(textvariable=imienazwisko, width="30")
wydzial_entry = Entry(textvariable=wydzial, width="30")
kierunek_entry = Entry(textvariable=kierunek, width="30")
przedmiot_entry = Entry(textvariable=przedmiot, width="30")
text_entry = Entry(textvariable=text, width="30")

# okreslenie pozycji pol wejsciowych
nralbumu_entry.place(x=15, y=70)
imienazwisko_entry.place(x=15, y=120)
wydzial_entry.place(x=15, y=170)
kierunek_entry.place(x=15, y=220)
przedmiot_entry.place(x=15, y=270)

# utworzenie przycisku zapisywania danych
zapiszdane = Button(screen, text="Zapisz dane studenta", width="30", height="2", bg="yellow", command=save_info)
zapiszdane.place(x=15, y=300)

# utworzenie przycisku odczytywania danych
odczytajdane = Button(screen, text="Szukaj", width="5", height="1", bg="red", command=show_info)
odczytajdane.place(x=210, y=65)

screen.mainloop()

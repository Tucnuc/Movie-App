import time
import random

# Listy jako vždy
loc = ["menu"]
sluzby = ("Dostupné filmy", "Detaily filmů", "Doporučit film")

# Proměnné
alfa = 62
oddelovac = "=" * alfa

# Textové funkce
def postText(text, zpozdeni=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(zpozdeni)
    print()
def postText2(text, zpozdeni=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(zpozdeni)
def postInput(prompt, zpozdeni=0.03):
    postText2(prompt, zpozdeni)
    user_input = input()
    return user_input

# Slovníky s filmy
hodnoceni_uzivatelu = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "Jméno": "Shawshank Redemption",
    "Hodnocení": "93/100",
    "Rok": 1994,
    "Režisér": "Frank Darabont",
    "Stopáž": 144,
    "Hrají": "Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler, Clancy Brown, Gil Bellows, Mark Rolston, James Whitmore, Jeffrey DeMunn, Larry Brandenburg"
}

film_2 = {
    "Jméno": "The Godfather",
    "Hodnocení": "92/100",
    "Rok": 1972,
    "Režisér": "Francis Ford Coppola",
    "Stopáž": 175,
    "Hrají": "Marlon Brando, Al Pacino, James Caan, Richard S. Castellano, Robert Duvall, Sterling Hayden, John Marley, Richard Conte"
}

film_3 = {
    "Jméno": "The Dark Knight",
    "Hodnocení": "90/100",
    "Rok": 2008,
    "Režisér": "Christopher Nolan",
    "Stopáž": 152,
    "Hrají": "Christian Bale, Heath Ledger, Aaron Eckhart, Michael Caine, Maggie Gyllenhaal, Gary Oldman, Morgan Freeman, Monique Gabriela, Ron Dean, Cillian Murphy"
}

film_4 = {
    "Jméno": "The Prestige",
    "Hodnocení": "85/100",
    "Rok": 2006,
    "Režisér": "Christopher Nolan",
    "Stopáž": 130,
    "Hrají": "Hugh Jackman, Christian Bale, Michael Caine, Piper Perabo, Rebecca Hall, Scarlett Johansson, Samantha Mahurin, David Bowie"
}

filmy = {
    film_1["Jméno"]: film_1,
    film_2["Jméno"]: film_2,
    film_3["Jméno"]: film_3,
    film_4["Jméno"]: film_4
}


# Úvod
# jmeno = postInput("Zadejte prosím vaše jméno: ")
jmeno = "Adam"
# time.sleep(0.5)
# postText2("Zpracovávám")
# time.sleep(0.2)
# postText("...",0.3)
# time.sleep(0.5)
# print("")
# postText2("\033[1mPŘÍSTUP\033[0m",0.05)
# time.sleep(0.2)
# postText("\033[1m POVOLEN\033[0m",0.05)
# time.sleep(0.5)
# print("")
# postText(f"Zdravíme vás, \033[1m{jmeno}\033[0m.")
# time.sleep(1)
# print("")
# loc.append("menu")


while True:


    # Menu
    if "menu" in loc:
        postText(oddelovac, 0.003)
        postText("Vítejte v našem filmovém slovníku.".center(alfa), 0.02)
        postText(oddelovac, 0.003)
        postText(f"{' | '.join(sluzby)}".center(62), 0.02)
        postText(oddelovac, 0.003)
        time.sleep(1)
        print("")
        while True:
            sluzba = postInput(f"Vyberte službu \033[1m[1 - {sluzby[0]}, 2 - {sluzby[1]}, 3 - {sluzby[2]}]\033[0m: ", 0.03)
            time.sleep(0.5)
            print("")
            if sluzba == "1":
                loc.clear()
                loc.append("filmy")
                break
            elif sluzba == "2":
                loc.clear()
                loc.append("detaily")
                break
            elif sluzba == "3":
                loc.clear()
                loc.append("doporuceni")
                break
            else:
                postText2("Špatná odpověď.")
                time.sleep(0.4)
                postText(" Zkuste to znovu.")
                time.sleep(0.5)
                print("")


    # Služba na zobrazení dostupných filmů
    if "filmy" in loc:
        postText("V našem filmovém slovníku najdete:")
        pocetFilmu = 0
        for key, value in filmy.items():
            pocetFilmu += 1
            postText(f"\033[1m{pocetFilmu}.\033[0m {value['Jméno']}")
        pocetFilmu = 0
        time.sleep(1)
        print("")
        loc.clear()
        loc.append("end") 


    # Služba na zobrazení detailů filmů
    if "detaily" in loc:
        postText("Vyberte si film:")
        pocetFilmu = 0
        for key, value in filmy.items():
            pocetFilmu += 1
            postText(f"\033[1m{pocetFilmu}.\033[0m {value['Jméno']}")
        pocetFilmu = 0
        time.sleep(1)
        print("")
        cisloFilmu = postInput("Zadejte odpovídající číslo filmu: ")
        time.sleep(0.5)
        print("")
        while True:
            if cisloFilmu == "1":
                for key, value in film_1.items():
                    postText(f"\033[1m{key}\033[0m: {value}", 0.03)
                time.sleep(1)
                print("")
                loc.clear()
                loc.append("end")
                break
            elif cisloFilmu == "2":
                for key, value in film_2.items():
                    postText(f"\033[1m{key}\033[0m: {value}", 0.03)
                time.sleep(1)
                print("")
                loc.clear()
                loc.append("end")
                break
            elif cisloFilmu == "3":
                for key, value in film_3.items():
                    postText(f"\033[1m{key}\033[0m: {value}", 0.03)
                time.sleep(1)
                print("")
                loc.clear()
                loc.append("end")
                break
            elif cisloFilmu == "4":
                for key, value in film_4.items():
                    postText(f"\033[1m{key}\033[0m: {value}", 0.03)
                time.sleep(1)
                print("")
                loc.clear()
                loc.append("end")
                break
            else:
                postText2("Špatná odpověď.")
                time.sleep(0.4)
                postText(" Zkuste to znovu.")
                time.sleep(0.5)
                print("")


    # Služba na doporučení filmu
    if "doporuceni" in loc:
        print("cs3")
        break


    # Jiná služba nebo ukončení?
    if "end" in loc:
        while True:
            beta = postInput("Chcete aplikaci ukončit nebo vybrat jinou šlužbu? \033[1m[1 - jiná služba, 2 - ukončení]\033[0m: ", 0.03)
            time.sleep(0.5)
            print("")
            if beta == "1":
                loc.clear()
                loc.append("menu")
                break
            elif beta == "2":
                loc.clear()
                loc.append("true-end")
                break
            else:
                postText2("Špatná odpověď.")
                time.sleep(0.4)
                postText(" Zkuste to znovu.")
                time.sleep(0.5)
                print("")
    if "true-end" in loc:
        break
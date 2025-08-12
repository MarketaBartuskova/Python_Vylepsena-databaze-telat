from tkinter import * 
import csv
import os

# import sys

# def resource_path(relative_path):
#     """ Získá absolutní cestu k souboru, funguje pro .py i .exe """
#     try:
#         # při běhu z .exe (PyInstaller)
#         base_path = sys._MEIPASS
#     except Exception:
#         # při běhu z .py
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)


# barvy, fonty
hlavni_font = "Helvetica"
hlavni_barva = "#00747C"
barva_tlacitka = "#F28705"

# První okno, jeho nastavení
okno = Tk()
okno.title("Databaze telat")
okno.minsize(750, 300)
okno.resizable(False, False)
okno.config(bg=hlavni_barva)
# okno.iconbitmap(resource_path("ikona_krava.ico"))
okno.iconbitmap("ikona_krava.ico")

# Funkce přidat tele, nové okno Přidat tele, jeho nastavení
def nove_okno():
    pridat_okno = Toplevel(okno)
    pridat_okno.title("Databáze telat")
    pridat_okno.minsize(550, 450)
    pridat_okno.resizable(False, False)
    pridat_okno.config(bg=hlavni_barva)
    pridat_okno.iconbitmap("ikona_krava.ico")
    # pridat_okno.iconbitmap(resource_path("ikona_krava.ico"))

    Label(pridat_okno, text="Přidat tele", bg=hlavni_barva, fg="black", font=(hlavni_font, 15, "bold", "underline")).pack(pady=10)

    # Vstupní pole
    cislo_vstup = Entry(pridat_okno, font=hlavni_font, width=40)
    datum_vstup = Entry(pridat_okno, font=hlavni_font, width=40)
    pohlavi_vstup = Entry(pridat_okno, font=hlavni_font, width=40)
    vaha_vstup = Entry(pridat_okno, font=hlavni_font, width=40)
    plemeno_vstup = Entry(pridat_okno, font=hlavni_font, width=40)
    matka_vstup = Entry(pridat_okno, font=hlavni_font, width=40)

    # Labely(popisky), nadpisy vstupních polí
    polozky = [
        ("Číslo telete:", cislo_vstup),
        ("Datum narození:", datum_vstup),
        ("Pohlaví:", pohlavi_vstup),
        ("Váha:", vaha_vstup),
        ("Plemeno:", plemeno_vstup),
        ("Číslo matky:", matka_vstup)
    ]

    # Cyklus, vytvoří:label s textem a pod ním vstupní pole 
    for text, vstup in polozky:
        Label(pridat_okno, text=text, bg=hlavni_barva, fg="black", font=(hlavni_font, 13)).pack()
        vstup.pack(pady=2)

    # Funkce načte uživatelem zadané údaje z jednotlivých vstupních polí
    def ulozit_a_zavrit():
        cislo = cislo_vstup.get()
        datum = datum_vstup.get()
        pohlavi = pohlavi_vstup.get()
        vaha = vaha_vstup.get()
        plemeno = plemeno_vstup.get()
        matka = matka_vstup.get()

        # pokud soubor neexistuje nebo je prázdný tak přidá, vytvoří hlavičku souboru
        try:
            velikost = os.stat("telata.csv").st_size
            zapis_hlavičku = velikost == 0
        except:
            zapis_hlavičku = True

        # Zápis do CSV souboru + hlavička
        with open("telata.csv", "a", newline="", encoding="utf-8") as soubor:
            zapis_csv = csv.writer(soubor)
            if zapis_hlavičku:
                zapis_csv.writerow(["Číslo telete", "Datum narození", "Pohlaví", "Váha", "Plemeno", "Číslo matky"])

                # formátování hlavičky, oddělovací čára z ---
                text_pole.delete(0, END)
                text_pole.insert("end", f"{'Číslo telete':<18} {'Datum narození':<20} {'Pohlaví':<14} {'Váha':<12} {'Plemeno':<12} {'Číslo matky':<3}\n")
                text_pole.insert(END, "-" * 115)

            zapis_csv.writerow([cislo, datum, pohlavi, vaha, plemeno, matka])

        # formátování přidaných záznamů
        radek_text = (f"{cislo:<18} {datum:<23} {pohlavi:<17} {vaha:<14} {plemeno:<18} {matka:<20}")
        text_pole.insert(END, radek_text)

        pridat_okno.destroy()

    # Tlačítko
    Button(pridat_okno, text="Uložit a zavřít", bg=barva_tlacitka, borderwidth=2, width=13, height=1, font=(hlavni_font, 13), command=ulozit_a_zavrit).pack(pady=10)


# Funkce která odstraní záznam z textového pole i ze souboru telata.csv
def remove_text_item():
    vybrany_index = text_pole.curselection()
    if not vybrany_index or vybrany_index[0] <= 1: 
        return

    # získá text z řádku podle prvního slova (Číslo telete)
    vybrany_text = text_pole.get(vybrany_index).strip()
    cislo_telete = vybrany_text.split()[0]

    # načte data ze souboru csv
    with open("telata.csv", "r", encoding="utf-8") as soubor:
        radky = list(csv.reader(soubor))

    hlavicka_csv = radky[0]
    telo_csv = radky[1:]

    # Vytvoří nový seznam řádků, které chceme ponechat v CSV souboru
    nove_telo_csv = [
    radek                 
    for radek in telo_csv     
    if radek and radek[0] != cislo_telete  
    ]

    # přepíše starý soubor novým zápisem
    with open("telata.csv", "w", newline="", encoding="utf-8") as soubor:
        zapisovac = csv.writer(soubor)
        zapisovac.writerow(hlavicka_csv)
        zapisovac.writerows(nove_telo_csv)

    # Obnoví textové pole
    text_pole.delete(0, END)
    nacti_zaznamy()

# Funkce upravit záznam, přidání nového okna
def upravit_zvire():
    vybrany_index = text_pole.curselection()
    if not vybrany_index or vybrany_index[0] <= 1:
        return

    vybrany_text = text_pole.get(vybrany_index).strip()

    # Načte soubor csv
    with open("telata.csv", "r", encoding="utf-8") as file:
        radky = list(csv.reader(file))

    hlavicka = radky[0]
    telo = radky[1:]

    # najde řádek odpovídající vybranému zvířeti
    puvodni_radek = None
    for radek in telo:
        if not radek:
            continue
        if radek[0] in vybrany_text:
            puvodni_radek = radek
            break

    if not puvodni_radek:
        return

    # Nové okno, upravit záznam
    upravit_okno = Toplevel(okno)
    upravit_okno.title("Upravit záznam")
    upravit_okno.minsize(550, 450)
    upravit_okno.config(bg=hlavni_barva)
    upravit_okno.iconbitmap("ikona_krava.ico")
    # upravit_okno.iconbitmap(resource_path("ikona_krava.ico"))

    Label(upravit_okno, text="Upravit zvíře", bg=hlavni_barva, fg="black", font=(hlavni_font, 15, "bold", "underline")).pack(pady=10)

    vstupni_pole = []
    popisky = ["Číslo telete", "Datum narození", "Pohlaví", "Váha", "Plemeno", "Číslo matky"]

    for i in range(6):
        Label(upravit_okno, text=popisky[i] + ":", bg=hlavni_barva, fg="black", font=hlavni_font).pack()
        vstup = Entry(upravit_okno, font=hlavni_font, width=40)
        vstup.insert(0, puvodni_radek[i])
        vstup.pack(pady=2)
        vstupni_pole.append(vstup)

    def ulozit_upravy():
        # získá nové udaje ze vstupních polí
        nove_udaje = []
        for entry in vstupni_pole:
            hodnota = entry.get()
            nove_udaje.append(hodnota)

        # přepsání dat v csv souboru
        nove_telo = []
        for radek in telo:
            if radek and radek[0] == puvodni_radek[0]:
                nove_telo.append(nove_udaje)
            else:
                nove_telo.append(radek)
        
        # Zápíše do csv souboru
        with open("telata.csv", "w", newline="", encoding="utf-8") as file:
            zapisovac = csv.writer(file)
            zapisovac.writerow(hlavicka)
            zapisovac.writerows(nove_telo)

        text_pole.delete(0, END)
        nacti_zaznamy()
        upravit_okno.destroy()

    Button(upravit_okno, text="Uložit a zavřít", bg=barva_tlacitka, borderwidth=2, width=13, height=1, font=(hlavni_font, 13), command=ulozit_upravy).pack(pady=10)

# Funkce která načte soubor telata.csv do textového pole
def nacti_zaznamy():
    try:
        with open("telata.csv", "r", encoding="utf-8") as soubor:
            ctecka_csv = csv.reader(soubor)
            radky = list(ctecka_csv)

            if not radky:
                return

            hlavicka = radky[0]
            telo = radky[1:]

            # vypsání hlavičky
            nadpis = (f"{'Číslo telete':<18} {'Datum narození':<20} {'Pohlaví':<14} {'Váha':<12} {'Plemeno':<12} {'Číslo matky':<3}")

            text_pole.insert(END, nadpis)
            text_pole.insert(END, "-" * 115)

            # vypsání dat
            for radek in telo:
                radek_text = f"{radek[0]:<18} {radek[1]:<23} {radek[2]:<17} {radek[3]:<14} {radek[4]:<18} {radek[5]:<20}"
                text_pole.insert(END, radek_text)
    except Exception as chyba:
        print("Chyba při načítání záznamů:", chyba)  

# Hlavní frame, který drží pravou a levou stranu vedle sebe
hlavni_frame = Frame(okno, bg=hlavni_barva)
hlavni_frame.pack(padx=10, pady=10)

# Frame pro tlačítka - vlevo
tlaciko_frame = Frame(hlavni_frame, bg=hlavni_barva)
tlaciko_frame.grid(row=0, column=0, sticky="n")

# Textový frame
textovy_frame = Frame(hlavni_frame, bg=hlavni_barva)
textovy_frame.grid(row=0, column=1, padx=(20,0))

# Scrollbar
text_scrollbar = Scrollbar(textovy_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S)

# Textové pole - v pravo
text_pole = Listbox(textovy_frame, height=9, width=63, borderwidth=2, font=hlavni_font, yscrollcommand=text_scrollbar.set)
text_pole.grid(row=0, column=0)

# Propojení scrollbaru s textovým polem
text_scrollbar.config(command=text_pole.yview)

# Tlačítka - v levo
pridat_tlacitko = Button(tlaciko_frame, text="Přidat tele", borderwidth=2, width=13, height=1, font=(hlavni_font, 13), bg=barva_tlacitka, command=nove_okno)
pridat_tlacitko.grid(row=0, column=0, pady=8)

upravit_tlacitko = Button(tlaciko_frame, text="Upravit záznam", borderwidth=2, width=13, height=1,font=(hlavni_font, 13), bg=barva_tlacitka, command=upravit_zvire) 
upravit_tlacitko.grid(row=1, column=0, pady=8)

smazat_tlacitko = Button(tlaciko_frame, text="Smazat záznam", borderwidth=2, width=13, height=1,font=(hlavni_font, 13), bg=barva_tlacitka, command=remove_text_item)
smazat_tlacitko.grid(row=3, column=0, pady=8)

konec_tlacitko = Button(tlaciko_frame, text="Konec", borderwidth=2, width=13, height=1,font=(hlavni_font, 13), bg=barva_tlacitka, command=okno.destroy)
konec_tlacitko.grid(row=4, column=0, pady=8)

nacti_zaznamy()

# Hlavní cyklus
okno.mainloop()

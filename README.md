# Vylepšená databáze telat

Python aplikace s Tkinterem slouží jako databáze telat.

---

Součástí repozitáře je:
- 'main.py' – hlavní program aplikace  
- 'telata.csv' – soubor s uloženými daty (tabulka telat)  
- 'ikona_krava.ico' – ikona aplikace  
- `images/` – složka se screenshoty aplikace  


---

Funkce:
- Přidání nového telete
- Úprava existujícího záznamu
- Smazání zvířete z databáze
- Zobrazení všech zvířat a detailní zobrazení se vypisuje automaticky v úvodním okně
- Automatické ukládání dat do telata.csv, soubor se sám vytvoří
- Jednoduché grafické rozhraní (Tkinter)

---

Použité technologie a metody:
- Tkinter – pro tvorbu GUI (okna, tlačítka, vstupní pole, seznam)
- csv modul – pro práci se soubory CSV (čtení, zápis, přepis dat)
- os modul – pro kontrolu existence a velikosti souboru
- Listbox + Scrollbar pro zobrazení více záznamů s možností rolování
- Použití try/except pro ošetření chyb při práci se soubory

---

Ukázka:

[Úvodní okno](images/foto1.png) 

[Přidat zvíře](images/foto2.png)

[Upravit zvíře](images/foto3.png)

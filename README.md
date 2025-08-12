# Vylepšená databáze telat

Python aplikace s Tkinterem slouží jako databáze telat.

Součástí repozitáře je také:
- ikona krávy (`ikona_krava.ico`), která je použita jako ikona okna aplikace
- ukázkový soubor `telata.csv`, který aplikace sama vytváří a do kterého ukládá data

Použité technologie a metody:
- Tkinter – pro tvorbu GUI (okna, tlačítka, vstupní pole, seznam)
- csv modul – pro práci se soubory CSV (čtení, zápis, přepis dat)
- os modul – pro kontrolu existence a velikosti souboru
- Listbox + Scrollbar pro zobrazení více záznamů s možností rolování
- Použití try/except pro ošetření chyb při práci se soubory

# Finanšu uzskaites sistēma python valodā
# Dokumentācija

## Projekta mērķis
Projekts ir izstrādāts, lai lietotāji varētu ērti un pēc iespējas ātrāk saglabāt, uzskaitīt savus ienākumus un izdevumus. Programma nodrošina vienkāršu un ērtu saskarni datu ievadei un apskatei. Programmā ievadītus datus var vienkārši nokopēt un glabāt kā rezerves kopiju.

## Izmantotās bibliotēkas

- **csv**: Bibliotēka darbam ar CSV datni. Tā tiek izmantota, lai glabātu informāciju par transakcijām.
- **tkinter**: Grafiskā bibliotēka ērtai un vienkāršai lietotāja saskarnes izveidei.
- **ttk (Tkinter)**: Tkinter paplašinājums, kas tika izmantots koka struktūras veidošanai.
- **datetime**: Bibliotēka darbam ar datumu un laiku. Tā tika izmantota, lai automātiski ievadītu transakcijas datumu.

## Programmas lietošana

1. **Programmas palaišana**: Palaidiet ***"main.py"*** skriptu, un tiks atvērts galvenais programmas logs ar pašreizējo bilanci un transakciju sarakstu.

2. **Jaunas transakcijas pievienošana**:
   - Nospiediet pogu "Pievienot ierakstu", lai atvērtu jaunu transakciju ievades logu.
   - Aizpildiet ievades laukumus (Datums, Apraksts, Tips, Summa).
   - Nospiediet pogu "Saglabāt", lai saglabātu transakciju. Jaunā transakcija tiks pievienota datnē, un dati tiks ielādēti no jauna.

3. **Transakcijas dzēšana**:
   - Iezīmējiet transakciju sarakstā.
   - Nospiediet pogu "Dzēst ierakstu", lai dzēstu izvēlēto transakciju. Transakciju saraksts un bilance tiks atjaunoti.
   - Ja poga tiks nospiesta, neiezīmējot nevienu pozīciju sarakstā, nekas nenotiks.

4. **Iziet no programmas**:
   - Aizveriet galveno programmas logu, lai pabeigtu programmas darbību.

## Brīdinājumi

1. Dažreiz python tekošā mape var atšķirties no faktiskās skripta atrašanās vietas. Ja programma neatrod savu ***.csv*** datni, tā tiek izveidota no jauna. Programmai pievienota testa datne ar testa informāciju. Ja pirmo reizi palaižot programmu, testa dati netiek rādīti, pamēģiniet nomainīt ***"filepath"*** mainīgo skriptā.

2. Esiet uzmanīgi, pievienojot jaunu ierakstu: esošā programmas versija neveic datu validāciju. Ja dati būs nekorekti, pastāv iespēja, ka programmu nevarēs palaist līdz datu manuālai izlabošanai.
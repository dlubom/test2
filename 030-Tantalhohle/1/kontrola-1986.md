# Tantalhöhle 1335/30 · od otworu do Riesenhalle

We wrześniu 1986 r. M. Napirala i H. Frey wykonali ponowny pomiar ciągu od otworu do Riesenhalle. Wydruk Wolfganga Gadermayra z 18 września zawiera 282 odcinki o łącznej długości 4218,35 m. Ostatni punkt ma numer obliczeniowy 282 i odpowiada punktowi 302 z pomiarów G. Abla. [Skan obliczeń, s. 1–13](1335-0030_V_19860918_pol_Vermessung_Eingang-Riesenhalle_Ausarbeitung_Gadermayr.pdf)

## Odczyt

Kolumny `LAEN.`, `NEI` i `RIC` podają długość w metrach, nachylenie i azymut w stopniach. Na wydruku kąty mają pełne stopnie, a składowe wektora `dy, dx, dh` (wschód, północ, wysokość) mają dwa miejsca po przecinku. W plikach dla Survex i Walls przyjęto kąty, które odtwarzają te trzy składowe z dokładnością do zaokrąglenia o 0,005 m. Obejmuje to także półstopnie i upad −12,2° na 219→220. W arkuszu kalkulacyjnym kolumny kątów zachowują wartości drukowane. [Survex](1.svx) · [Walls](1.srv) · [Transkrypcja arkusza](Tantalhohle%20vermessung.xlsx)

| Odcinek | Strona PDF | Korekta względem wcześniejszego pliku Survex |
|---|---:|---|
| 3→4 | 1 | początek w stacji 3 zamiast 2 |
| 12→13 | 2 | 16,40 → 6,40 m |
| 42→43 | 3 | początek w stacji 42 zamiast 41 |
| 93→94 | 5 | zapis +123° przy azymucie 114° daje ujemny rzut poziomy. W plikach pomiarowych równoważny wektor ma upad +57° i azymut 294°. Wcześniej przyjęto +12° i 114° |
| 103→104 | 5 | 7,15 → 17,15 m |
| 136→137 | 7 | 20,00 → 20,20 m |
| 183→184 | 9 | +31° → −31° |
| 214→215 | 10 | azymut 73° → 75° |
| 217→218 | 10 | 20,00 → 20,10 m |
| 228→229 | 11 | 7,00 → 17,00 m |
| 237→238 | 11 | upad −4° → −7° na wydruku, −6,5° według przyrostów |

Na stronie 8 w wierszu 173 wydrukowano 172→172. Wektor prowadzi od współrzędnych stacji 172 do współrzędnych stacji 173, z której wychodzi następny odcinek. W modelu i arkuszu przyjęto 172→173. Pozycje 283–295 na ostatniej stronie to puste wiersze rachunku.

## Sprawdzenie współrzędnych

W lokalnej kompilacji Survex przyjęto początek w (0, 0, 0) i deklinację 0°, zgodnie z układem porównywanych przyrostów. Wszystkie 282 stacje docelowe zgadzają się z wydrukiem do 0,05 m na każdej osi. Wydruk podaje współrzędne stacji z dokładnością do 0,1 m.

| Punkt 282 / 302 w Riesenhalle | Wschód [m] | Północ [m] | Wysokość względna [m] | Różnica 3D od wydruku |
|---|---:|---:|---:|---:|
| Wydruk z 1986 r. | 1734,5 | 1285,7 | −263,1 | |
| Przed korektą | 1748,79 | 1270,90 | −243,36 | 28,51 m |
| Po korekcie | 1734,51 | 1285,72 | −263,06 | 0,046 m |

Porównanie mierzy zgodność rekonstrukcji z rachunkiem archiwalnym. Na pierwszej stronie rzędna otworu VP 1003 wynosi 1703,94 m. Zakotwiczenie współczesnego modelu masywu podaje dla otworu 1710 m.

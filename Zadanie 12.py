liczba_próbek = 50000
rozmiar_batcha = 128
liczba_epok = 50
czas_na_batch = 0.15

l_batchy_na_epokę = liczba_próbek // rozmiar_batcha
pozostałe_próbki = liczba_próbek % rozmiar_batcha

print(f"Liczba pełnych batchy na epokę: {l_batchy_na_epokę}")
print(f"Pozostałe próbki (do niepełnego batcha): {pozostałe_próbki}")

if pozostałe_próbki > 0:
    l_batchy_na_epokę += 1
    print("Dodano 1 batch, bo zostały próbki.")

łączna_liczba_batchy = l_batchy_na_epokę * liczba_epok
łączny_czas_w_sekundach = łączna_liczba_batchy * czas_na_batch

print(f"Łączna liczba batchy: {łączna_liczba_batchy}")
print(f"Całkowity czas treningu (sekundy): {łączny_czas_w_sekundach}")

godziny = int(łączny_czas_w_sekundach // 3600)
minuty = int((łączny_czas_w_sekundach % 3600) // 60)
sekundy = int(łączny_czas_w_sekundach % 60)

print(f"Szacowany czas: {godziny} h {minuty} min {sekundy} s")
# Gra Tetris w Pythonie 🕹️

Ten projekt to klasyczna implementacja gry Tetris w Pythonie, wykorzystująca bibliotekę `pygame` do renderowania grafiki i interakcji z graczem. Umożliwia grę w kultową grę, gdzie możesz obracać i przesuwać klocki, usuwać pełne linie i wiele więcej.

## Spis treści 📜
- [Wstęp](#wstęp)
- [Funkcje](#funkcje)
- [Instalacja](#instalacja)
- [Jak grać](#jak-grać)
- [Sterowanie](#sterowanie)
- [Mechanika gry](#mechanika-gry)
- [Personalizacja](#personalizacja)
- [Licencja](#licencja)
- [Podziękowania](#podziękowania)

## Wstęp 🎮

Tetris to jedna z najbardziej ikonicznych gier w historii, stworzona przez Alexeya Pajitnova w 1984 roku. Celem gry jest obracanie i umieszczanie spadających klocków (tetromino), aby wypełniały całe poziome linie. W tej wersji gry stworzonej w Pythonie za pomocą biblioteki `pygame` odwzorowaliśmy podstawową mechanikę gry.

Gra zawiera kilka funkcji:
- **Podstawowa rozgrywka**: Przesuwaj i obracaj spadające klocki, usuwaj linie, zapobiegaj zapełnieniu ekranu.
- **Funkcja pauzy**: Pauzuj i wznawiaj grę za pomocą spacji.
- **Ekran startowy**: Ekran powitalny, który zachęca gracza do rozpoczęcia gry.
- **Prędkość spadania**: Prędkość spadania klocków rośnie w miarę postępów w grze.

## Funkcje 🎉

Ta wersja gry Tetris w Pythonie zawiera następujące funkcje:
- **Tetromino**: Siedem różnych klocków (I, O, T, S, Z, L, J) o różnych kolorach.
- **Usuwanie linii**: Linie zostają usunięte, gdy są całkowicie wypełnione klockami.
- **Punkty**: Punkty zdobywa się za usuwanie linii.
- **Koniec gry**: Gra kończy się, gdy klocki zapełnią górną część ekranu.
- **Pauza i wznowienie**: Naciśnij spację, aby wstrzymać grę, naciśnij ją ponownie, aby wznowić.
- **Ekran startowy**: Ekran startowy, który zachęca do rozpoczęcia gry.

## Instalacja ⚙️

Aby uruchomić tę grę Tetris na swoim komputerze, wykonaj poniższe kroki.

### Wymagania wstępne

Aby uruchomić grę, potrzebujesz zainstalowanego Pythona (wersja 3.6 lub wyższa) oraz biblioteki `pygame`, która jest używana do renderowania grafiki i obsługi wejścia od gracza.

#### 1. Zainstaluj Pythona

Jeśli jeszcze nie masz Pythona, pobierz go ze strony [https://www.python.org/downloads/](https://www.python.org/downloads/).

#### 2. Zainstaluj bibliotekę pygame

Po zainstalowaniu Pythona, otwórz terminal lub wiersz poleceń i uruchom poniższe polecenie, aby zainstalować bibliotekę `pygame`:

```bash
pip install pygame
```

### Pobranie repozytorium

Po zainstalowaniu Pythona i pygame, pobierz kod źródłowy, klonując repozytorium za pomocą Git. W terminalu uruchom polecenie:

```bash
git clone https://github.com/twojeimie/tetris-python.git
```

Alternatywnie, możesz pobrać plik ZIP z repozytorium na GitHubie i wypakować go w wybranej lokalizacji.

### Uruchamianie gry

Po pobraniu plików, przejdź do folderu, w którym znajdują się pliki gry. Uruchom grę za pomocą Pythona, wpisując w terminalu:

```bash
python tetris.py
```

Po tym poleceniu gra powinna wystartować, a na ekranie pojawi się okno Tetrisa.

## Jak grać 🎯

### Przegląd gry

Tetris to gra logiczna, w której gracz manipuluje spadającymi klockami (tetromino). Celem jest obracanie i przesuwanie klocków, aby wypełniały pełne linie. Gdy linia jest wypełniona, zostaje usunięta, a gracz zdobywa punkty. Gra kończy się, gdy klocki zapełnią całą przestrzeń w górnej części ekranu.

### Instrukcja gry

1. **Rozpocznij grę**: Naciśnij klawisz "Enter" na ekranie startowym, aby rozpocząć grę.
2. **Przesuwanie w lewo/prawo**: Użyj klawiszy strzałek w lewo i w prawo, aby przesunąć klocek w poziomie.
3. **Obracanie**: Użyj klawisza "Strzałka w górę", aby obrócić klocek.
4. **Przyspieszenie spadania**: Naciśnij klawisz "Strzałka w dół", aby przyspieszyć spadanie klocka.
5. **Pauza/Wznów grę**: Naciśnij "Spację", aby zatrzymać grę. Naciśnij ją ponownie, aby wznowić.
6. **Koniec gry**: Gra kończy się, gdy nowe klocki nie mogą zostać umieszczone na górze ekranu, ponieważ jest już pełny.

## Sterowanie 🕹️

Poniżej znajdziesz kontrolki, które pozwalają grać w Tetris:

| Akcja               | Klawisz       |
| ------------------- | ------------- |
| Przesuń w lewo       | Strzałka w lewo|
| Przesuń w prawo      | Strzałka w prawo|
| Obróć klocek         | Strzałka w górę|
| Przyspiesz spadanie  | Strzałka w dół |
| Pauza/Wznów grę      | Spacja        |
| Rozpocznij grę       | Enter         |

## Mechanika gry ⚙️

### Tetromino

W grze Tetris występuje siedem różnych klocków, z których każdy składa się z czterech bloków. Oto ich lista:
- **I**: Prosta linia składająca się z 4 bloków.
- **O**: Kwadrat 2x2.
- **T**: Kształt T, z 3 blokami w poziomie i jednym nad środkiem.
- **S**: Klocki w kształcie "S" skierowane w lewo.
- **Z**: Klocki w kształcie "S" skierowane w prawo.
- **L**: Klocki w kształcie litery "L".
- **J**: Lustrzane odbicie klocka L.

Każdy klocek ma unikalny kolor, co ułatwia rozróżnienie między nimi.

### Siatka

Gra odbywa się na siatce składającej się z bloków. Domyślny rozmiar siatki to 10 kolumn i 20 wierszy. Klocki spadają z góry siatki, a gracz musi je przesuwać i obracać, aby wypełnić linie. Gdy linia zostanie wypełniona, zostaje usunięta, a wszystkie wyższe linie przesuwają się w dół.

### Punkty

Punkty przyznawane są za każdą usuniętą linię. Im więcej linii usuniętych w jednym czasie, tym więcej punktów gracz zdobywa. Wynik jest wyświetlany na górze ekranu.

### Koniec gry

Gra kończy się, gdy klocki nie mogą zostać umieszczone na górze ekranu, ponieważ siatka jest pełna. Po zakończeniu gry pojawi się ekran z wynikiem końcowym.

### Prędkość spadania

Klocki spadają z określoną prędkością, która rośnie wraz z upływem czasu. Oznacza to, że w miarę postępów w grze, klocki będą spadały szybciej, co zwiększa trudność.

### Funkcja pauzy

Naciśnięcie "Spacji" wstrzymuje grę, pozwalając graczowi na przerwę. Naciśnięcie jej ponownie wznawia grę.

## Personalizacja ✨

Gra jest łatwa do personalizacji. Oto niektóre rzeczy, które możesz zmienić w kodzie:

1. **Kolory klocków**: Zmień kolory w liście `SHAPE_COLORS`, aby dostosować wygląd klocków.
2. **Rozmiar siatki**: Zmieniaj rozmiar siatki poprzez dostosowanie zmiennych `SCREEN_WIDTH` i `SCREEN_HEIGHT`.
3. **Prędkość**: Zmień zmienną `fall_speed`, aby kontrolować, jak szybko spadają klocki.
4. **Obracanie klocków**: Jeśli chcesz, możesz zmodyfikować sposób obracania klocków, aby dopasować go do własnych preferencji.

## Licencja 📝

Ten projekt jest dostępny na licencji MIT. Zobacz plik [LICENSE](LICENSE.md), aby uzyskać więcej informacji.

## Podziękowania 🙏

- **pygame**: Gra korzysta z biblioteki `pygame` do renderowania grafiki i obsługi wejścia. Więcej informacji o `pygame` znajdziesz na [pygame.org](https://www.pygame.org/).
- **Tetris**: Oryginalna gra Tetris została stworzona przez Alexeya Pajitnova w 1984 roku.

---

Miłej zabawy w Tetris! 🟦🟧🟨

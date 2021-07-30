# Windows povećalo #

* Autor: Cyrille Bougot
* NVDA kompatibilnost: 2018.3 i novije
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

Ovaj dodatak poboljšava upotrebu Windows povećala s NVDA čitačem.


## Funkcije

* Dozvoljava izvještavanje o rezultatu nekih izvornih tipkovničkih naredbi
  povećala.
* Dozvoljava smanjivanje broja slučajeva, gdje se naredbe za kretanje po
  tablici sukobljavaju s naredbama povećala.
* Dodaje neke prečace na tipkovnici za uključivanje i isključivanje raznih
  opcija povećala.


## Postavke

Ploča za postavljanje dodatka Windows povećala omogućuje konfiguriranje načina na koji NVDA reagira na izvorne naredbe Windows povećala.
Možda želiš da se javlja više ili manje naredbi u skladu s onim što možeš vidjeti.
Ova se ploča može otvoriti odabirom Postavke -> Postavke u NVDA izborniku, a zatim odabirom kategorije Windows Povećalo u prozoru Postavke.
Tipkovni prečac NVDA+Windows+O, zatim O, također omogućuje izravno otvaranje ove ploče s postavkama.

Ploča sadrži sljedeće opcije:

* Javi pomicanja prikaza: određuje što se javlja pri premještanju prikaza
  pomoću naredbi Kontrol+Alt+Strelice. Postoje tri opcije:
  
    * Isključeno: ništa se ne javlja.
    * S govorom: govorna poruka označava položaj uvećanog prikaza na
      dimenziji na kojoj se prikaz pomiče.
    * Sa zvučnim signalima: svira se ton i njegova visina označava položaj
      uvećanog prikaza na dimenziji na kojoj se prikaz pomiče.
  
  Ova opcija vrijedi samo za cjloekranski prikaz.
  
* Uključi ili isključi javljanje: Ako je označeno, javlja se stanje povećala
  kad za uključivanje ili isključivanje koristiš naredbe Windows++ ili
  Windows+Escape.
* Javi uvećanje: Ako je označeno, javlja se razina uvećanja povećala kad
  koristiš naredbe za uvećanje Windows++ ili Windows+-.
* Javi inverziju boje: Ako je označeno, javlja se stanje inverzije boje kad
  koristiš naredbu za uključivanje/isključivanje kontrol+Alt+I.
* Javi promjenu prikaza: Ako je označeno, javlja se vrsta prikaza kad
  koristiš naredbu koja mijenja vrstu prikaza (Kontrol+Alt+M, Kontrol+Alt+F,
  Kontrol+Alt+D, Kontrol+Alt+L)
* Javi mijenjanje veličine leće ili fiksiranog prozora: Ako je označeno,
  javlja se poruka kad koristiš naredbe za mijenjanje veličine
  (Alt+šift+strelice). U načinu fiksiranog prozora javlja se visina ili
  širina. U modusu leće, nova se dimenzija za sada ne može javiti. Čini se
  da ove naredbe za mijenjanje veličine nisu dostupne u svim verzijama
  WIndows sustava; ako ih tvoja verzija Windows sustava ne podržava, nemoj
  označiti ovu opciju.
* U prikazima dokumenata i popisa, proslijedi prečace kontrol+alt+strelice
  Windows povećalu: Postoje tri mogućnosti:
  
    * Nikada: Naredba se ne prosljeđuje Windows povećalu i standardno NVDA
      kretanje tablicom može raditi. Kad se koristi u dokumentima izvan
      tablice, naredba Kontrol+Alt+Strelica javlja poruku o grešci „Nije u
      tablici”. To je standardno ponašanje NVDA čitača bez ovog dodatka.
    * Samo izvan tablice: U prikazima tablice ili popisa, naredbe
      Kontrol+Alt+Strelica izvode standardno kretanje po tablici. Kad se
      koriste u dokumentima izvan tablice, naredbe Kontrol+Alt+Strelica
      izvode standardne naredbe za pomicanje prikaza povećala. Ako i dalje
      želiš pomaknuti prikaz Windows povećala dok se nalaziš u prikazu
      tablice ili popisa, morat ćeš pritisnuti NVDA+F2 prije korištenja
      naredbi Kontrol+Alt+Strelica. Ova je opcija najbolji kompromis, ako
      želiš koristiti Kontrol+Alt+Strelica za povećalo i za kretanje po
      tablici.
    * Uvijek: Naredbe Kontrol+Alt+Strelica u svakom slučaju pomiču prikaz
      povećala. Ova opcija može biti korisna, ako ne koristiš
      Kontrol+Alt+Strelica za kretanje po tablici, npr. jer si promijenio/la
      prečace za kretanje po tablici u NVDA čitaču ili jer za kretanje po
      tablicama isključivo koristiš dodatak [Jednostavno kretanje po
      tablici][5].


## Dodatak dodaje sljedeće naredbe

Osim izvornih naredbi povećala, ovaj dodatak nudi dodatne naredbe koje
omogućuju upravljanje opcijama povećala bez otvaranja njegove stranice
konfiguracije. Sve naredbe koje su dodane za upravljanje opcijama povećala
dostupne su putem naredbe povećala NVDA+Windows+O:

* NVDA+Windows+O, zatim C: Uključuje ili isključuje praćenje kursora.
* NVDA+Windows+O, zatim F: Uključuje ili isključuje praćenje fokusa.
* NVDA+Windows+O, zatim M: Uključuje ili isključuje praćenje miša.
* NVDA+Windows+O, zatim T: Uključuje ili isključuje praćenje globalno.
* NVDA+Windows+O, zatim S: Uključuje ili isključuje zaglađivanje rubova.
* NVDA+Windows+O, zatim R: Prebacuje se između modusa praćenja miša (unutar
  ruba ekrana ili centrirano na ekranu); ova je funkcija dostupna samo u
  Windows 10 gradnja 17643 ili novijoj verziji.
* NVDA+Windows+O, zatim X: Prebacuje se između modusa praćenja miša (unutar
  ruba ekrana ili centrirano na ekranu); ova je funkcija dostupna samo u
  Windows 10 gradnja 18894 ili novijoj verziji.
* NVDA+Windows+O, zatim V: Pomiče kursor miša u središte uvećanog prikaza
  (naredba je dostupna samo u cjeloekranskom prikazu).
* NVDA+Windows+O, zatim O: Otvara postavke dodatka Windows povećala.
* NVDA+Windows+O, zatim H: Prikazuje pomoć za naredbe povećala.

Ne postoji standardna gesta za svaku naredbu, ali ako treba, može je se
normalno dodijeliti u dijaloškom okviru unosa gesta. Na isti je način moguće
i izmijeniti ili izbrisati gestu za pristup povećalu
(NVDA+Windows+O). Međutim, nije moguće mijenjati tipku prečaca pod-naredbi
povećala.


## Izvorne naredbe povećala

S ovim se dodatkom rezultat sljedećih izvornih naredbi povećala izgovara,
ovisno o konfiguraciji:

* Pokreni povećalo: Windows++ (na alfanumeričkoj tipkovnici ili na
  numeričkoj tipkovnici)
* Zatvori povećalo: Windows+Escape
* Uvećaj prikaz: Windows++ (na alfanumeričkoj tipkovnici ili na numeričkoj
  tipkovnici)
* Umanji prikaz: Windows+- (na alfanumeričkoj tipkovnici ili na numeričkoj
  tipkovnici)
* Uključi ili isključi inverziju boje: Kontrol+Alt+I
* Odaberi fiksirani prikaz: Kontrol+Alt+D
* Odaberi cjeloekranski prikaz: Kontrol+Alt+F
* Odaberi prikaz lećom: Kontrol+Alt+L
* Mijenjaj između tri vrste prikaza: Kontrol+Alt+M
* Promijeni veličinu leće tipkovnicom: Šift+Alt+strelica
  Lijevo/Desno/Gore/Dolje. Napomena: iako se čini da ovo nije dokumentirano,
  čini se da je ovaj prečac povučen u novijim verzijama Windowsa, kao što je
  Windows 2004.
* Pomakni uvećani prikaz: Kontrol+Alt+strelice (izvještavanje utječe samo na
  cjeloekranski modus)

Za kraj, evo popis ostalih izvornih naredbi povećala, čisto informativno:

* Kontrol+Alt+kotačić miša: Uvećava i smanjuje prikaz pomoću kotačića miša.
* Kontrol+Windows+M: Otvara prozor s postavkama povećala.
* Kontrol+Alt+R: Mijenja veličinu leće pomoću miša.
* Kontrol+Alt+razmaknica: Brzo prikazuje cijelu radnu površinu pomoću
  cjeloekranskog prikaza.

Nije moguće promijeniti niti jednu izvornu naredbu povećala.


## Napomene

* Za računala opremljena Intelovom grafičkom karticom, prečac
  kontrol+alt+strelica (lijevo/desno/gore/dolje) također služi za okretanje
  ekrana. Ti su prečaci standardno aktivirani i sukobljavaju se s prečacima
  Windows povećala za pomicanje prikaza. Za korištenje povećala, ti se
  prečaci moraju deaktivirati. Deaktiviraju se na Intelovoj upravljačkoj
  ploči ili u Intelovom izborniku u programskoj traci.
* Tipke Alt+šift+strelica prečaci su Windows povećala za mijenjanje veličine
  uvećanog prikaza (leća ili fiksirano). Kad je povećalo aktivno (čak i u
  cjeloekranskom prikazu), povećalo nadvladava ove prečace i ne mogu se
  proslijediti programu, čak i ako se prethodno pritisne NVDA+F2. Za
  upotrebu ovih prečaca u trenutačnom programu, mora se izaći iz povećala
  (Windows+Escape) i nakon toga ponovo ga otvoriti (Windows++). Na primjer,
  u MS wordu, za smanjivanje razine naslova:
  
    * Pritisni Windows+Escape za zatvaranje povećala.
    * Pritisni Alt+šift+strelica desno, za smanjivanje razine naslova.
    * Pritisni Windows++ za ponovno otvaranje povećala.

* Za daljnje informacije o funkcijama i prečacima Windows povećala,
  pregledaj sljedeće stranice:

    * [Korištenje Povećala za lakše gledanje sadržaja na
      zaslonu](https://support.microsoft.com/hr-hr/windows/kori%C5%A1tenje-pove%C4%87ala-za-lak%C5%A1e-gledanje-sadr%C5%BEaja-na-zaslonu-414948ba-8b1c-d3bd-8615-0e5e32204198)
    * [Tipkovni prečaci za pristupačnost u sustavu Windows][4]


## Dnevnik promjena

### Verzija 1.0

* Inicijalno izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/hr-hr/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.hr.html

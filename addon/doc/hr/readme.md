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
* Dodaje neke tipkovničke prečace za uključivanje i isključivanje raznih
  opcija povećala.
* Dozvoli spremanje i obnavljanje parametara konfiguracije povećala.
* Dodaje neke dodatne značajke koje ne pruža Windows povećalo (miš za
  prikaz, prozor povećala nije na vrhu)

## Postavke

Ploča za postavljanje dodatka Windows povećala omogućuje konfiguriranje
načina na koji NVDA reagira na izvorne naredbe Windows povećala. Možda želiš
da se javlja više ili manje naredbi u skladu s onim što možeš vidjeti. Ploča
također sadrži opciju za mijenjanje ponašanja kontrolnog prozora Windows
povećala.

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
  
  Ova opcija ne utječe na usidreni način prikaza.

* Javi rubove ekrana: kontrolira ono što se prijavljuje kad dosegneš rubove
  ekrana tijekom micanja prikaza pomoću naredbi Kontrol+Alt+Strelice. Tri
  opcije su: Isključeno, S govorom i S tonovima. Ova opcija ne utječe na
  usidreni način prikaza.
* Glasnoća tonova za javljanje položaja prikaza: omogućuje definiranje
  glasnoće tonova ako je odabrana mogućnost javljanja premještanja prikaza
  ili rubova ekrana pomoću tonova.
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
      tablici”. To je standardno ponašanje NVDA čitača bez ovog dodatka. I
      dalje možeš koristiti NVDA+Windows+O zatim strelice za pomicanje
      uvećanog prikaza.
    * Samo izvan tablice: U prikazima tablice ili popisa, naredbe
      Kontrol+Alt+Strelica izvode standardno kretanje po tablici. Kad se
      koriste u dokumentima izvan tablice, naredbe Kontrol+Alt+Strelica
      izvode standardne naredbe za pomicanje prikaza povećala. Ako i dalje
      želiš pomaknuti prikaz Windows povećala dok se nalaziš u prikazu
      tablice ili popisa, morat ćeš pritisnuti NVDA+F2 prije korištenja
      naredbi Kontrol+Alt+Strelica ili alternativno NVDA+Windows+O zatim
      strelice. Ova je opcija najbolji kompromis, ako želiš koristiti
      Kontrol+Alt+Strelica za povećalo i za kretanje po tablici.
    * Uvijek: Naredbe Kontrol+Alt+Strelica u svakom slučaju pomiču prikaz
      povećala. Ova opcija može biti korisna, ako ne koristiš
      Kontrol+Alt+Strelica za kretanje po tablici, npr. jer si promijenio/la
      prečace za kretanje po tablici u NVDA čitaču ili jer za kretanje po
      tablicama isključivo koristiš dodatak [Jednostavno kretanje po
      tablici][5].

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## Dodatak dodaje sljedeće naredbe

Osim izvornih naredbi povećala, ovaj dodatak pruža dodatne naredbe:

* Naredbe koje omogućuju upravljanje opcijama povećala bez otvaranja njegove
  konfiguracijske stranice.
* Dodatne naredbe specifične za ovaj dodatak.

Sve ove dodatne naredbe dostupne su putem naredbe sloja povećala
NVDA+Windows+O:

* NVDA+Windows+O, zatim C: Uključuje ili isključuje praćenje kursora.
* NVDA+Windows+O, zatim F: Uključuje ili isključuje praćenje fokusa.
* NVDA+Windows+O, zatim M: Uključuje ili isključuje praćenje miša.
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+Windows+O, zatim S: Uključuje ili isključuje zaglađivanje rubova.
* NVDA+Windows+O, zatim R: Prebacuje se između modusa praćenja kursora miša
  (unutar ruba ekrana ili centrirano na ekranu); ova je funkcija dostupna
  samo u Windows 10 gradnja 17643 ili novijoj verziji.
* NVDA+Windows+O, zatim X: Prebacuje se između modusa praćenja miša (unutar
  ruba ekrana ili centrirano na ekranu); ova je funkcija dostupna samo u
  Windows 10 gradnja 18894 ili novijoj verziji.
* NVDA+Windows+O, zatim šift+P: Sprema aktualne parametre konfiguracije
  povećala u NVDA konfiguraciju.
* NVDA+Windows+O then P: Restores the current configuration parameters of
  the magnifier from NVDA's configuration.  If no configuration parameters
  has been previously saved to NVDA's configuration, the default
  configuration parameters of Windows Magnifier are restored instead.
* NVDA+Windows+O, zatim strelice: Pomakni uvećani prikaz.
* NVDA+Windows+O, zatim V: Pomiče kursor miša u središte uvećanog prikaza
  (naredba nije dostupna u usidrenom načinu prikaza).
* NVDA+Windows+O, zatim W: Uključuje ili isključuje modus omogučujući
  zadržavanje kontrolnog prozora Windows povećala uvijek iznad ostalih. Ova
  je značajka dostupna samo za instalirane NVDA verzije.
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
* Promijeni veličinu leće pomoću tipkovnice: Šift+Alt+strelica
  lijevo/desno/gore/dolje. Napomena: iako ovo nije dokumentirano, čini se da
  je ovaj prečac povučen u novijim verzijama Windows sustava kao što je
  Windows 10 2004.
* Pomakni uvećani prikaz: Kontrol+Alt+strelice

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

* Ovaj dodatak nije testiran u višeekranskom okruženju i neka značajka možda
  neće radi u ovom okruženju. Ako koristiš višeekransko okruženje i ako
  želiš da se to podrži, kontaktiraj me kako bih ga implementirao.
* Općenito, ne ustručavaj se me kontaktirati na [GitHub stranici][3] ovog
  dodatka ili izravno putem e-pošte.


## Dnevnik promjena

### Verzija 3.0

* Pressing the zoom buttons in the Magnifier window (with the keyboard) now
  reports the new zoom level.
* The parameter controlling if Magnifier control window remains always on
  top is now stored in configuration; this means that this parameter is
  remembered when restarting NVDA and can be enabled or not depending on the
  active profile.
* Fixed a bug causing unexpected screen curtain de-activation when using
  move to view or move view commands.
* Option alwaysOnTop setting will now be honoured also when changing
  magnification mode.
* Added ability to save and restore Windows Magnifier's config in NVDA's
  config.
* Kompatibilnost s NVDA verzijom 2023.1.
* Clarify which type of tracking is re-enabled when tracking is toggled on
  again.
* Aktualizirane lokalizacije.

### Verzija 2.0

* Prikaz se može pomicati strelicama dok se nalaziš u sloju Windows
  povećala.
* Mogućnost za održavanje prozora naredbi povećala uvijek na vrhu ili ne.
* Dodana je funkcija „Javi rubove ekrana”.
* Podešavanje glasnoće tonova tijekom korištenja naredbi za pomicanje
  prikaza.
* Izvještavanje o pomicanjima prikaza i o naredbama prikaz mišem su sada
  podržane u modusu leće.
* Kompatibilnost s NVDA 2022.1.
* Ispravljena je greška koja je ponekad netočno javljala da povećalo ne radi
  nakon pozivanja skripta.
* Izdanje se sada izvodi zahvaljujući GitHub radnji umjesto appVeyora.
* Aktualizirane lokalizacije.

### Verzija 1.1

* Dodane su lokalizacije.

### Verzija 1.0

* Inicijalno izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/hr-hr/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.hr.html

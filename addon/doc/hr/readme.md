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
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

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
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the view position: allows to define the
  volume of the tones if you have selected to report view moves or screen
  edges with tones.
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
  
    * Never: The command is not passed to Windows Magnifier and standard
      NVDA table navigation can operate.  When used in documents out of a
      table, the Control+Alt+Arrow command reports a "Not in a table" error
      message.  This is the standard behaviour of NVDA without this add-on.
      You can still use NVDA+Windows+O then arrows to move the magnified
      view.
    * Only when not in table: In table or in list views, Control+Alt+Arrow
      commands perform standard table navigation.  When used in documents
      out of a table, Control+Alt+Arrow commands perform standard Magnifier
      view move commands.  If you still want to move Windows Magnifier view
      while in table or in list view, you will need to press NVDA+F2 before
      using Control+Alt+Arrow commands or alternately use NVDA+Windows+O
      then arrows.  This option is the best compromise if you want to use
      Control+Alt+Arrow for both Magnifier and table navigation.
    * Uvijek: Naredbe Kontrol+Alt+Strelica u svakom slučaju pomiču prikaz
      povećala. Ova opcija može biti korisna, ako ne koristiš
      Kontrol+Alt+Strelica za kretanje po tablici, npr. jer si promijenio/la
      prečace za kretanje po tablici u NVDA čitaču ili jer za kretanje po
      tablicama isključivo koristiš dodatak [Jednostavno kretanje po
      tablici][5].


## Dodatak dodaje sljedeće naredbe

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

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
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode keeping Windows
  Magnifier's control window always on top of the other ones.  This feature
  is only available for installed versions of NVDA.
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
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

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

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Dnevnik promjena

### Version 2.0

* The view can be moved with arrows while in Windows Magnifier layer.
* Capability to keep the Magnifier commands Window always on top or not.
* Added "Report screen edges" feature.
* Volume setting of tones when using move view commands.
* Reporting view moves and mouse to view commands are now supported in Lens
  mode.
* Compatibility with NVDA 2022.1.
* Fixed a bug that sometimes incorrectly reported that the Magnifier was not
  working upon script call.
* The release is now performed thanks to a GitHub action instead of
  appVeyor.
* Updated localizations.

### Version 1.1

* Added localizations.

### Verzija 1.0

* Inicijalno izdanje.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/hr-hr/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.hr.html

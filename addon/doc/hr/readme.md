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

The setting panel of Windows Magnifier add-on allows to configure how NVDA reacts to native Windows Magnifier commands.
You may want to have more or less commands reported according to what you are able to see.
This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

The panel contains the following options:

* Report view moves: controls what is reported when you move the view with
  Control+Alt+Arrows commands. The three options are:
  
    * Off: Nothing is reported.
    * With speech: a speech message indicates the position of the zoomed
      view on the dimension the view is being moved.
    * With tones: a tone is played and its pitch indicates the position of
      the zoomed view on the dimension the view is being moved.
  
  This option only affects full view mode.
  
* Report turn on or off: If checked, the Magnifier's state is reported when
  you use Windows++ or Windows+Escape commands to turn it on or off.
* Report zoom: If checked, the Magnifier's zoom level is reported when you
  use Windows++ or Windows+- zoom commands.
* Report color inversion: If checked, the color inversion state is reported
  when you use the control+Alt+I toggle command.
* Report view change: If checked, the view type is reported when you use a
  command that changes the view type (Control+Alt+M, Control+Alt+F,
  Control+Alt+D, Control+Alt+L)
* Report lens or docked window resizing: If checked, a message is reported
  when you use the resizing commands (Alt+Shift+Arrows).  In docked window
  mode, the height or the width is reported.  In lens mode, the new
  dimension cannot be reported for now.  These resizing command do not seem
  to be available on all versions of Windows; if your Windows version does
  not support them, you should keep this option unchecked.
* In documents and list views, pass control+alt+arrows shortcuts to Windows
  Magnifier: There are three possible choices:
  
    * Never: The command is not passed to Windows Magnifier and standard
      NVDA table navigation can operate.  When used in documents out of a
      table, the Control+Alt+Arrow command reports a "Not in a table" error
      message.  This is the standard behaviour of NVDA without this add-on.
    * Only when not in table: In table or in list views, Control+Alt+Arrow
      commands perform standard table navigation.  When used in documents
      out of a table, Control+Alt+Arrow commands perform standard Magnifier
      view move commands.  If you still want to move Windows Magnifier view
      while in table or in list view, you will need to press NVDA+F2 before
      using Control+Alt+Arrow commands.  This option is the best compromise
      if you want to use Control+Alt+Arrow for both Magnifier and table
      navigation.
    * Always: Control+Alt+Arrow commands moves the Magnifier's view in any
      case.  This option may be useful if you do not use Control+Alt+Arrow
      to navigate in table, e.g. because you have changed table navigation
      shortcuts in NVDA or because you exclusively use [Easy table
      navigator][5] add-on for table navigation.


## Dodatak dodaje sljedeće naredbe

In addition to native Magnifier commands, this add-on provide additional
commands that allow to control Magnifier's options without opening its
configuration page.  All the commands added to control Magnifier options are
accessible through the Magnifier layer command NVDA+Windows+O:

* NVDA+Windows+O zatim C: Uključuje ili isključuje praćenje kursora.
* NVDA+Windows+O zatim F: Uključuje ili isključuje praćenje fokusa.
* NVDA+Windows+O zatim M: Uključuje ili isključuje praćenje miša.
* NVDA+Windows+O zatim T: Uključuje ili isključuje praćenje globalno.
* NVDA+Windows+O zatim S: Uključuje ili isključuje zaglađivanje.
* NVDA+Windows+O, zatim R: Prebacuje se između modusa praćenja miša (unutar
  ruba ekrana ili centrirano na ekranu); ova je funkcija dostupna samo u
  Windows 10 gradnja 17643 ili novijoj verziji.
* NVDA+Windows+O, zatim X: Prebacuje se između modusa praćenja miša (unutar
  ruba ekrana ili centrirano na ekranu); ova je funkcija dostupna samo u
  Windows 10 gradnja 18894 ili novijoj verziji.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command available in full screen view only).
* NVDA+Windows+O zatim O: Otvara postavke dodatka Windows povećala.
* NVDA+Windows+O zatim H: Prikazuje pomoć za naredbe povećala.

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
* Uključi i isključi inverziju boje: Kontrol+Alt+I
* Odaberi usidreni prikaz: Kontrol+Alt+D
* Odaberi cjeloekranski prikaz: Kontrol+Alt+F
* Odaberi prikaz lećom: Kontrol+Alt+L
* Prolazi kroz vrste prikaza stabla: Kontrol+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow.
  Note: although this does not seem to be documented, this shortcut seems to
  have been withdrawn in recent Windows versions such as Windows 2004.
* Move the magnified view: Control+Alt+Arrows (reporting only affects full
  screen mode)

Za kraj, evo popis ostalih izvornih naredbi povećala, čisto informativno:

* Kontrol+Alt+kotiačić miša: Uvećava i smanjuje prikaz pomoću kotačića miša.
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
  uvećanog prikaza (leća ili usidreno). Kad je povećalo aktivno (čak i u
  cjeloekranskom prikazu), povećalo nadvladava ove prečace i ne mogu se
  proslijediti programu, čak i ako se prethodno pritisne NVDA+F2. Za
  upotrebu ovih prečaca u trenutačnom programu, mora se izaći iz povećala
  (Windows+Escape) i nakon toga ponovo ga otvoriti (Windows ++). Na primjer,
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

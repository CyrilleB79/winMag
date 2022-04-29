# Windows Forstørrelsesglas #

* Forfatter: Cyrille Bougot
* NVDA-kompatibilitet: 2018.3 og derover
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse forbedrer brugen af Windows Forstørrelsesglas med NVDA.


## Funktioner

* Giver mulighed for at få oplyst hvad der sker, når du bruger en kommando
  for Windows Forstørrelsesglas
* Gør det muligt at reducere de tilfælde, hvor tabelnavigationskommandoer er
  i konflikt med forstørrelses kommandoer.
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

## indstillinger

Indstillingspanelet for tilføjelsesprogrammet gør det muligt at konfigurere, hvordan NVDA reagerer til de oprindelige kommandoer for Windows Forstørrelsesglas.
Du vil sandsynligvis helst have oplyst, når du udfører flere eller færre kommandoer i henhold til din synsrest.
Dette panel åbnes ved at vælge Opsætning>Indstillinger i NVDA-menuen og derefter vælge kategorien Windows Forstørrelsesglas i vinduet Indstillinger.
Tastaturgenvejen NVDA+Windows+O lader dig også åbne dette indstillingspanel.

Panelet indeholder følgende indstillinger:

* Oplys panorering: styrer, hvad der rapporteres, når du panorere med
  kommandoerne Ctrl+Alt+piletaster. De tre muligheder er:
  
    * Fra: Intet oplyses.
    * Med tale: En talemeddelelse angiver placeringen af den zoomede visning
      på den dimension, der panoreres.
    * Med toner: En tone afspilles, og dens tonehøjde angiver placeringen af
      den zoomede visning på den dimension, der panoreres.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the view position: allows to define the
  volume of the tones if you have selected to report view moves or screen
  edges with tones.
* Oplys, når forstørrelsesglas slås til: Hvis dette er markeret, rapporteres
  Forstørrelsesglasets tilstand, når du bruger kommandoerne Windows++ eller
  Windows+Escape til at slå funktionen til eller fra.
* Oplys zoomniveau: Hvis dette er markeret, rapporteres forstørrelsesglasets
  zoomniveau, når du bruger Windows++ eller Windows+-.
* Oplys farveinvertering: Hvis dette er markeret, rapporteres det, når du
  aktivere eller deaktivere farveinvertering med Alt+Ctrl+I.
* Oplys ændring af visningstype: Hvis dette er markeret, rapporteres
  visningstypen, når du bruger en kommando, der ændrer visningstypen
  (Ctrl+Alt+M, Ctrl+Alt+F, Ctrl+Alt+D, Ctrl+Alt+L)
* Oplys ny størrelse for vinduer i linse- eller forankret visning: Hvis
  dette er markeret, vil du få oplyst, når du bruger kommandoerne til
  ændring af størrelse (Alt+Skift+Piletaster). I forankret visnings
  rapporteres højden eller bredden. Hvis du i stedet benytter linsevisning,
  vil du ikke få denne information oplyst for øjeblikket. Disse kommandoer
  til ændring af størrelse ser ikke ud til at være tilgængelige i alle
  versioner af Windows; hvis din Windows-version ikke understøtter dem, skal
  du ikke aktivere denne indstilling.
* Send tastekombinationerne alt+Ctrl+piletaster til Windows
  Forstørrelsesglas, når NVDA befinder sig i dokumenter og listevisninger:
  Der er tre mulige valg:
  
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
    * Altid: Ctrl+Altpiletasterne vil panorere uanset hvad. Dette kan være
      brugbart, hvis du ikke bruger Ctrl+Alt+piletaster til at navigere i
      tabeller, fordi du har ændret tastekombinationen eller benytter dig af
      tilføjelsen [Easy table navigator][5], når du navigere i tabeller.


## Kommandoer udbudt af denne tilføjelse

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O og derefter C: Slår sporing af tekstmarkøren til og fra.
* NVDA+Windows+O og derefter F: Slår fokussporing til eller fra.
* NVDA+Windows+O og derefter M: Slår musesporing til eller fra.
* NVDA+Windows+O og derefter T: Slår sporing til eller fra globalt.
* NVDA+ Windows+O og derefter S: Slår tekstudglatning til eller fra.
* NVDA+Windows+O og derefter R: Skifter mellem musesporingstilstande
  (indenfor kanten af skærmen eller centreret på skærmen); denne funktion er
  kun tilgængelig på Windows 10 build 17643 eller nyere.
* NVDA+Windows+O og derefter X: Skifter mellem sporingsfunktioner for
  tekstmarkøren(indenfor kanten af skærmen eller centreret på skærmen);
  denne funktion er kun tilgængelig på Windows 10 build 18894 eller nyere.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode keeping Windows
  Magnifier's control window always on top of the other ones.  This feature
  is only available for installed versions of NVDA.
* NVDA+Windows+O og derefter O: Åbner indstillingerne for tilføjelsen.
* NVDA+Windows+O og derefter H: Viser hjælpen for kommandoerne til
  forstørrelseslaget.

Der er ikke tildelt et standardtastetryk til disse kommandoer, men du kan
tildele tastetryk via dialogen "Håndter kommandoer". Du kan også redigere
eller slette kommandoen for forstørrelseslaget (NVDA+Windows+O). Du kan
derimod ikke tildele andre tastetryk til kommandoerne i selve
forstørrelseslaget.


## Oprindelige kommandoer tildelt af Windows til Forstørrelsesglas

Resultatet af følgende indbyggede kommandoer til forstørrelsesglas kan
rapporteres af denne tilføjelse i henhold til dens konfiguration:

* Start Forstørrelsesglas: Windows++ (på alfanumerisk tastatur eller på
  numpad)
* Afslut forstørrelsesglas: Windows+Escape
* Zoom ind: Windows++(på alfanumerisk tastatur eller på numpad)
* Zoom ud: Windows+- (på alfanumerisk tastatur eller på numpad)
* Skift indstilling for farveinvertering: Ctrl+Alt+I
* Vælg forankret visning: Ctrl+Alt+D.
* Vælg fuldskærmsvisning: Ctrl+Alt+F
* Vælg linsevisning: Ctrl+Alt+L.
* Skift mellem de tre visningstyper: Ctrl+Alt+M.
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Yderligere er disse indbyggede kommandoer til rådighed:

* Ctrl+alt+musehjul: Zoomer ind og ud ved hjælp af musens rullehjul.
* Ctrl+Windows+M: Åbner de indbyggede indstillinger for Forstørrelsesglas.
* Ctrl+Alt+R: Tilpasser størrelsen for linsen vha. musen.
* Ctrl+Alt+Mellemrum: Viser kort hele skrivebordet, når fuldskærmsvisning
  benyttes.

Ingen af de indbyggede kommandoer til Forstørrelsesglas kan ændres.


## Bemærkninger

* For computere udstyret med et Intel-grafikkort er Ctrl+alt+piletasterne
  også genveje til at ændre skærmretningen. Disse genveje er aktiveret som
  standard og er i konflikt med Windows-forstørrelsesgenveje, der ellers
  bruges til at panorere. Du bliver nødt til at deaktivere dem for at kunne
  bruge dem til forstørrelsesglas. De kan deaktiveres i Intel-kontrolpanelet
  eller i Intel-menuen i systembakken.
* Afhængigt af din Windows-version er Alt+SKift+PILETASTERNE
  Windows-forstørrelsesgenveje for at ændre størrelsen på den forstørrede
  visning (LINSE ELLER FORANKRET). Når Forstørrelsesglas er aktivt (selv i
  fuldskærmstilstand), fanges disse genveje af Forstørrelsesglas og kan ikke
  videregives til applikationen, selvom du tidligere har trykket på
  NVDA+F2. For at bruge disse genveje i den aktuelle applikation skal du
  afslutte Forstørrelsesglas (Windows+Escape) og åbne den igen bagefter
  (Windows++). For eksempel i MS word, for at ændre overskriftsniveauet:
  
    * Tryk på Windows+Escape for at afslutte Forstørrelsesglas.
    * Tryk på Alt+Skift+Højre pil for at øge det aktuelle overskriftsniveau.
    * Tryk på Windows++ for at aktivere Forstørrelsesglas igen.

* For mere information om de forskellige funktioner og genveje, der tilhører
  Windows Forstørrelsesglas, kan du gå til følgende sider:

    * [Brug Forstørrelsesglas til at gøre tingene på skærmen nemmere at
      se](https://support.microsoft.com/da-DK/windows/use-magnifier-to-make-things-on-the-screen-easier-to-see-414948ba-8b1c-d3bd-8615-0e5e32204198?WT.mc_id=365AdminCSH_gethelp)
    * [Windows-tastaturgenveje som hjælp til handicappede][4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Ændringshistorik

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

### Version 1.0

* Første udgivelse.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://shorturl.at/dezBK

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.da.html

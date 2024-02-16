# Windows Forstørrelsesglas #

* Forfatter: Cyrille Bougot
* NVDA compatibility: 2019.2.1 and beyond
* Download [stabil version][1]

Denne tilføjelse forbedrer brugen af Windows Forstørrelsesglas med NVDA.


## Funktioner

* Giver mulighed for at få oplyst hvad der sker, når du bruger en kommando
  for Windows Forstørrelsesglas
* Gør det muligt at reducere de tilfælde, hvor tabelnavigationskommandoer er
  i konflikt med forstørrelses kommandoer.
* Tilføjer nogle tastaturgenveje, der ændre forskellige
  standardindstillinger for Forstørrelsesglas.
* Allow to save and restore the configuration parameters of the Magnifier.
* Tilføjer nogle ekstra funktioner, der ikke leveres af Windows Forstørrelse
  (mus til visning, forstørrelsesvindue ikke øverst)

## indstillinger

The setting panel of Windows Magnifier add-on allows to configure how NVDA
reacts to native Windows Magnifier commands.  You may want to have more or
less commands reported according to what you are able to see.  The panel
also contains an option to modify the behaviour of Windows Magnifier control
window.

This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

Panelet indeholder følgende indstillinger:

* Oplys panorering: styrer, hvad der rapporteres, når du panorere med
  kommandoerne Ctrl+Alt+piletaster. De tre muligheder er:
  
    * Fra: Intet oplyses.
    * Med tale: En talemeddelelse angiver placeringen af den zoomede visning
      på den dimension, der panoreres.
    * Med toner: En tone afspilles, og dens tonehøjde angiver placeringen af
      den zoomede visning på den dimension, der panoreres.
  
  Denne indstilling påvirker ikke forankret visning.

* Oplys skærmens kanter: styrer, hvad der oplyses, når du når kanterne af
  skærmen, mens du panorere visningen med kommandoerne
  Ctrl+Alt+Piletaster. De tre muligheder er: Fra, Med tale og Med
  toner. Denne indstilling påvirker ikke forankret visning.
* Volume of the tones reporting the position of the view: allows to define
  the volume of the tones if you have selected to report view moves or
  screen edges with tones.
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
  
    * Aldrig: Kommandoen videregives ikke til Windows Forstørrelsesglas, og
      standard NVDA-tabelnavigation vil fungere. Når dette bruges i
      dokumenter udenfor en tabel, oplyser kommandoen fejlmeddelelsen "Ikke
      i en tabelcelle". Dette er NVDAs standardadfærd uden denne
      tilføjelse. Du kan stadig benytte NVDA+Windows+o og derefter
      piletasterne for at panorere den forstørrede visning.
    * Brug kun, hvis udenfor en tabel: I tabeller eller listevisninger
      udfører Ctrl+Alt+piletasterne standardnavigering i tabeller. Når disse
      bruges i dokumenter udenfor en tabel, udfører kommandoerne
      Alt+Ctrl+piletasterne standardkommandoerne for
      forstørrelsesglasset. Hvis du stadig vil panorere, mens du er i en
      tabel eller listevisning, skal du trykke på NVDA+F2, før du bruger
      Ctrl+alt+piletasterne. Du kan også bruge NVDA+Windows+O og derefter
      piletasterne for at panorere visningen. qDenne mulighed er det bedste
      kompromis, hvis du vil bruge kommandoerne til både forstørrelse og
      tabelnavigation.
    * Altid: Ctrl+Altpiletasterne vil panorere uanset hvad. Dette kan være
      brugbart, hvis du ikke bruger Ctrl+Alt+piletaster til at navigere i
      tabeller, fordi du har ændret tastekombinationen eller benytter dig af
      tilføjelsen [Easy table navigator][5], når du navigere i tabeller.

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## Kommandoer udbudt af denne tilføjelse

Ud over de standardkommandoer, der benyttes når du bruger Forstørrelsesglas,
tilføjer denne tilføjelse yderligere kommandoer:

* Kommandoer, der gør det muligt at styre indstillingerne for
  Forstørrelsesglas uden at åbne indstillingspanelet.
* Yderligere kommandoer, der kan bruges med denne tilføjelse.

Alle disse kommandoer er tilglngelige via forstørelseslaget med kommandoen
NVDA+skift+o.

* NVDA+Windows+O og derefter C: Slår sporing af tekstmarkøren til og fra.
* NVDA+Windows+O og derefter F: Slår fokussporing til eller fra.
* NVDA+Windows+O og derefter M: Slår musesporing til eller fra.
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+ Windows+O og derefter S: Slår tekstudglatning til eller fra.
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes
  (within the edge of the screen or centered on the screen); this feature is
  only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O og derefter X: Skifter mellem sporingsfunktioner for
  tekstmarkøren(indenfor kanten af skærmen eller centreret på skærmen);
  denne funktion er kun tilgængelig på Windows 10 build 18894 eller nyere.
* NVDA+Windows+O then shift+P: Saves the current configuration parameters of
  the magnifier to NVDA's configuration.
* NVDA+Windows+O then P: Restores the current configuration parameters of
  the magnifier from NVDA's configuration.  If no configuration parameters
  has been previously saved to NVDA's configuration, the default
  configuration parameters of Windows Magnifier are restored instead.
* NVDA+Windows+O derefter piletasterne: Panorere den forstørrede visning.
* NVDA+Windows+O og derefter V: Flytter musemarkøren i midten af den
  forstørrede visning (kommandoen er ikke tilgængelig i forankret visning).
* NVDA+Windows+O then W: Switches on or off the mode allowing to keep
  Windows Magnifier's control window always on top of the other ones.  This
  feature is only available for installed versions of NVDA.
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
* Tilpas linsens størrelse med tastaturet: Skift+Alt+piletasterne. Bemærk:
  skønt dette ikke ser ud til at være dokumenteret, synes denne genvej at
  være trukket tilbage i de nyeste Windows-versioner som Windows 10 2004.
* Panorer den forstørrede visning: Ctrl+Alt+piletasterne

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

* Denne tilføjelse er ikke blevet testet i miljøer, hvor flere skærme
  benyttes samtidigt, og der er chancer for, at nogle funktioner ikke virker
  i dette miljø. Hvis du bruger flere skærme på én gang og ønsker, at det
  skal understøttes, bedes du kontakte mig for at få det implementeret.
* Tøv desuden ikke med at kontakte mig på [GitHub-siden][3] vedr. denne
  tilføjelse eller direkte via e-mail.


## Ændringshistorik

### Version 3.5

* Prepares compatibility with NVDA 2024.1.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][8]
  when using the add-on with older versions of NVDA. However, it is
  recommended to use NVDA 2023.3.3 or higher.
* Note: From now on, translation updates will not appear anymore in the
  change log.

### Version 3.4

* The "move mouse to view" command works again
* Opdaterede oversættelser.

### Version 3.3

* Compatibility reduced to NVDA 2019.2.1 and beyond.  The last compatible
  versions with NVDA 2018.3 are the [3.2][7] (partially compatible) and
  [1.1][6] (fully compatible)
* Fixed a bug in the settings panel with NVDA 2019.2.1.

### Version 3.2

* Removed the dev channel.
* Opdaterede oversættelser.

### Version 3.1

* Fixed an issue preventing the Magnifier's command window from being
  restored on top.
* Fixed an issue preventing the add-on to run on NVDA 2019.2.1.
* Opdaterede oversættelser.

### Version 3.0

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
* Compatibility with NVDA 2023.1.
* Clarify which type of tracking is re-enabled when tracking is toggled on
  again.
* Opdaterede oversættelser.

### Version 2.0

* Du kan panorere visningen med piletasterne, når du er I
  forstørrelseslaget.
* Mulighed, der gør det muligt at vise vinduet for Forstørelsesglas oven på
  andre vinduer.
* Tilføjet funktion til at oplyse skærmens kanter.
* Lydstyrkeindstilling for toner, når du bruger kommandoer til at panorere
  visningen.
* Kommandoer til at oplyse panorering af visningen, samt kommandoer til at
  flytte musen til visningen, understøttes nu I linsetilstand.
* Kompatibilitet med NVDA 2022.1.
* Rettede en fejl, der nogle gange fejlagtigt rapporterede, at
  forstørrelsesglasset ikke fungerede ved scriptkald.
* Udgivelsen udføres nu takket være en GitHub-handling i stedet for
  appVeyor.
* Opdaterede oversættelser.

### Version 1.1

* Tilføjede oversættelser.

### Version 1.0

* Første udgivelse.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: https://shorturl.at/dezBK

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.da.html

[6]:
https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]:
https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

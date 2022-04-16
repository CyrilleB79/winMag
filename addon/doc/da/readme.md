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
* Tilføjer nogle tastaturgenveje, der ændre forskellige
  forstørrelsesindstillinger.


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
  
  Denne indstilling påvirker kun fuldskærmsvisning.
  
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
      i en tabelcelle". Dette er NVDAs standardadfærd uden denne tilføjelse.
    * Brug kun, hvis udenfor en tabel: I tabeller eller listevisninger
      udfører Ctrl+Alt+piletasterne standardnavigering i tabeller. Når disse
      bruges i dokumenter udenfor en tabel, udfører kommandoerne
      Alt+Ctrl+piletasterne standardkommandoerne for
      forstørrelsesglasset. Hvis du stadig vil panorere, mens du er i en
      tabel eller listevisning, skal du trykke på NVDA+F2, før du bruger
      Ctrl+alt+piletasterne. Denne mulighed er det bedste kompromis, hvis du
      vil bruge kommandoerne til både forstørrelse og tabelnavigation.
    * Altid: Ctrl+Altpiletasterne vil panorere uanset hvad. Dette kan være
      brugbart, hvis du ikke bruger Ctrl+Alt+piletaster til at navigere i
      tabeller, fordi du har ændret tastekombinationen eller benytter dig af
      tilføjelsen [Easy table navigator][5], når du navigere i tabeller.


## Kommandoer udbudt af denne tilføjelse

Ud over de oprindelige kommandoer for Forstørrelsesglas, udbyder denne
tilføjelse yderligere kommandoer, der gør det muligt at ændre funktionens
indstillinger uden at åbne indstillingerne. Alle kommandoer, der er tilføjet
for at ændre forstørrelsesindstillinger er tilgængelige via kommandoen
NVDA+Windows+O, der åbner et Forstørrelseslag til brug af følgende
kommandoer:

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
* NVDA+Windows+O og derefter V: Flytter musemarkøren i midten af den
  forstørrede visning (kommandoen er kun tilgængelig i fuldskærmsvisning).
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
  være trukket tilbage i de nyeste Windows-versioner som Windows 2004.
* Flyt den forstørrede visning: Ctrl+Alt+piletasterne (rapportering påvirker
  kun fuldskærmsvisning)

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


## Ændringshistorik

### Version 1.0

* Første udgivelse.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://shorturl.at/dezBK

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.da.html

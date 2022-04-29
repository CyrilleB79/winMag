# Windows-suurennuslasi #

* Tekijä: Cyrille Bougot
* yhteensopivuus: NVDA 2018.3 ja uudemmat
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tämä lisäosa parantaa Windowsin suurennuslasin käytettävyyttä NVDA:n kanssa.


## Ominaisuudet

* Ilmoittaa joidenkin alkuperäisten suurennuslasinäppäinkomentojen tulokset.
* Vähentää tapauksia, joissa taulukkonavigointikomennot ovat ristiriidassa
  suurennuslasikomentojen kanssa.
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

## Asetukset

Windowsin suurennuslasi -lisäosan asetuspaneelissa voit määrittää, miten NVDA reagoi alkuperäisiin Windows-suurennuslasin komentoihin.
Voit haluta enemmän tai vähemmän komentoja ilmoitettavan riippuen siitä, minkä verran näet.
Tämä paneeli voidaan avata Valitsemalla NVDA-valikosta Asetukset -> Asetukset ja sitten Windowsin suurennuslasi -kategoria.
Näppäinkomento NVDA+Win+O ja sitten O avaa myös tämän asetuspaneelin suoraan.

Paneelissa on seuraavat asetukset:

* Ilmoita näkymän siirtäminen: säätää, mitä ilmoitetaan, kun siirrät näkymää
  Ctrl+Alt+nuolinäppäimillä. Käytettävissä olevat kolme vaihtoehtoa ovat:
  
    * Ei käytössä: Mitään ei ilmoiteta.
    * Puheella: Puhuttu viesti ilmaisee zoomatun näkymän sijainnin
      suunnassa, johon näkymää siirretään.
    * Äänimerkeillä: Toistettava äänimerkki ja sen korkeus ilmaisee zoomatun
      näkymän sijainnin suunnassa, johon näkymää siirretään.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the view position: allows to define the
  volume of the tones if you have selected to report view moves or screen
  edges with tones.
* Ilmoita käyttöön ottaminen tai käytöstä poistaminen: Jos tämä on
  valittuna, suurennuslasin tila ilmoitetaan käyttäessäsi Win++- tai
  Win+Esc-komentoja sen käyttöön ottamiseksi tai käytöstä poistamiseksi.
* Ilmoita zoomauksen taso: Jos tämä on valittuna, suurennuslasin zoomauksen
  taso ilmoitetaan käyttäessäsi zoomauskomentoja Win++ tai Win+-.
* Ilmoita värin inversio: Jos tämä on valittuna, värin inversion tila
  ilmoitetaan käyttäessäsi tilanvaihtokomentoa Ctrl+Alt+I.
* Ilmoita näkymän muuttumisesta: Jos tämä on valittuna, näkymän tyyppi
  ilmoitetaan käyttäessäsi sitä muuttavaa komentoa (Ctrl+Alt+M, Ctrl+Alt+F,
  Ctrl+Alt+D ja Ctrl+Alt+L).
* Ilmaise linssi- tai kiinnitetyn ikkunan koon muuttaminen: Jos tämä on
  valittuna, NVDA antaa ilmoituksen käyttäessäsi koonmuuttamiskomentoja
  (Alt+Vaihto+Nuolinäppäimet). Kiinnitetyn ikkunan tilassa ilmoitetaan
  korkeus tai leveys. Linssitilassa uutta mittaa ei toistaiseksi voida
  ilmoittaa. Nämä koonmuutoskomennot eivät näytä olevan käytettävissä
  kaikissa Windows-versioissa; mikäli Windows-versiosi ei tue niitä, älä
  valitse tätä asetusta.
* Välitä Ctrl+Alt+Nuolet-pikanäppäimet asiakirjoissa ja luettelonäkymissä
  Windows suurennuslasille: Mahdollisia vaihtoehtoja on kolme:
  
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
    * Aina: Ctrl+Alt+Nuoli-komennot siirtävät suurennuslasin näkymää
      kaikissa tapauksissa. Tämä vaihtoehto voi olla hyödyllinen, mikäli et
      käytä Ctrl+Alt+Nuoli-komentoja taulukossa liikkumiseen, esim. koska
      olet vaihtanut NVDA:n taulukkonavigointikomentoja tai koska käytät
      yksinomaan [Helppo taulukossa liikkuminen][5] -lisäosaa taulukossa
      liikkumiseen.


## Lisäosan komennot

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Win+O ja sitten C: Ottaa kohdistimen seurannan käyttöön tai poistaa
  sen käytöstä.
* NVDA+Win+O ja sitten F: Ottaa kohdistuksen seurannan käyttöön tai poistaa
  sen käytöstä.
* NVDA+Win+O ja sitten M: Ottaa hiiren seurannan käyttöön tai poistaa sen
  käytöstä.
* NVDA+Win+O ja sitten T: Ottaa seurannan käyttöön tai poistaa sen käytöstä
  yleisesti.
* NVDA+Win+O ja sitten S: Ottaa pehmennyksen käyttöön tai poistaa sen
  käytöstä.
* NVDA+Win+O ja sitten R: Vaihtaa hiiren seurannan tilaa (ruudun reunassa
  tai keskitettynä). Tämä ominaisuus on käytettävissä vain Windows 10:n
  koontiversiossa 17643 tai uudemmassa.
* NVDA+Win+O ja sitten X: Vaihtaa tekstikohdistimen seurannan tilaa (näytön
  reunassa tai näytön keskellä). Tämä ominaisuus on käytettävissä vain
  Windows 10:n koontiversiossa 18894 tai sitä uudemmassa.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode keeping Windows
  Magnifier's control window always on top of the other ones.  This feature
  is only available for installed versions of NVDA.
* NVDA+Win+O ja sitten O: Avaa tämän lisäosan asetukset.
* NVDA+Win+O ja sitten H: Näyttää suurennuslasin komentokerroskomentojen
  ohjeen.

Komennoilla ei ole oletusarvoisia syötekomentoja, mutta voit halutessasi
määrittää ne normaalisti Syötekomennot-valintaikkunassa. Samalla tavalla
voit myös muuttaa tai poistaa suurennuslasin komentokerroksen
aktivointikomennon (NVDA+Win+O). Komentokerroksen alikomentojen muuttaminen
ei kuitenkaan ole mahdollista.


## Alkuperäiset suurennuslasikomennot

Asetuksista riippuen seuraavien alkuperäisten suurennuslasikomentojen
tulokset puhutaan tätä lisäosaa käytettäessä:

* Käynnistä suurennuslasi: Win++ (numeroriviltä tai numeronäppäimistöltä)
* Lopeta suurennuslasi: Win+Esc
* Lähennä näkymää: Win++ (numeroriviltä tai numeronäppäimistöltä)
* Loitonna näkymää: Win+- (numeroriviltä tai numeronäppäimistöltä)
* Ota käänteiset värit käyttöön tai poista ne käytöstä: Ctrl+Alt+I
* Valitse kiinnitetty näkymä: Ctrl+Alt+D
* Valitse koko ruudun näkymä: Ctrl+Alt+F
* Valitse linssinäkymä: Ctrl+Alt+L
* Vaihda kolmen näkymätyypin välillä: Ctrl+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Tässä on lisäksi luettelo muista Suurennuslasin alkuperäisistä komennoista:

* Ctrl+Alt+Hiiren vieritysrulla: Lähentää ja loitontaa näkymää hiiren
  vieritysrullaa käyttäen.
* Ctrl+Win+M: Avaa suurennuslasin asetusikkunan.
* Ctrl+Alt+R: Muuttaa linssin kokoa hiiren avulla.
* Ctrl+Alt+Väli: Näyttää nopeasti koko työpöydän koko ruudun näkymää
  käytettäessä.

Alkuperäisiä suurennuslasikomentoja ei voi muuttaa.


## Huomautuksia

* Intel-näytönohjaimella varustetuissa tietokoneissa Ctrl+Alt+Nuoli
  vasemmalle/oikealle/ylös/alas ovat myös näytön suunnan muuttamisen
  pikanäppäimiä. Nämä pikanäppäimet ovat oletusarvoisesti käytössä ja
  ristiriidassa Windowsin suurennuslasin näkymänsiirtopikanäppäinten
  kanssa. Sinun on poistettava ne käytöstä, jotta voit käyttää niitä
  suurennuslasissa. Ne voidaan poistaa käytöstä Intelin ohjauspaneelista tai
  ilmaisinalueen Intel-valikosta.
* Windows-versiostasi riippuen Alt+Vaihto+Nuoli-komennot ovat Windowsin
  suurennuslasin pikanäppäimiä suurennetun näkymän koon muuttamiseen linssi-
  tai kiinnitetyssä näkymässä. Kun suurennuslasi on käytössä (jopa koko
  näytön tilassa), se kaappaa nämä pikanäppäimet, eikä niitä voi välittää
  aktiiviselle sovellukselle, vaikka painaisit ensin NVDA+F2. Mikäli haluat
  käyttää näitä pikanäppäimiä nykyisessä sovelluksessa, sinun on suljettava
  suurennuslasi (Win+Esc) ja avattava se uudelleen sen jälkeen
  (Win++). Esimerkiksi MS Wordissa otsikkotason pienentämiseksi:
  
    * Sulje suurennuslasi painamalla Win+Esc.
    * Pienennä nykyistä otsikkotasoa painamalla Alt+Vaihto+Nuoli oikealle.
    * Avaa suurennuslasi uudelleen painamalla Win++.

* Saat lisätietoja Windowsin suurennuslasin ominaisuuksista ja
  pikanäppäimistä seuraavilta sivuilta:

    * [Käytä suurennuslasia nähdäksesi näytön kohteet
      paremmin](https://support.microsoft.com/fi-fi/windows/k%C3%A4yt%C3%A4-suurennuslasia-n%C3%A4hd%C3%A4ksesi-n%C3%A4yt%C3%B6n-kohteet-paremmin-414948ba-8b1c-d3bd-8615-0e5e32204198)
    * [Windowsin helppokäyttötoimintojen pikanäppäimet][4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Muutosloki

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

### Versio 1.0

* Ensimmäinen julkaisu.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]:
https://support.microsoft.com/fi-fi/windows/windowsin-helppok%C3%A4ytt%C3%B6toimintojen-pikan%C3%A4pp%C3%A4imet-021bcb62-45c8-e4ef-1e4f-41b8c1fc87fd

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

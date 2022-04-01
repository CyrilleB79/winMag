# Windows-suurennuslasi #

* Tekijä: Cyrille Bougot
* NVDA compatibility: 2018.3 and beyond
* Download [stable version][1]
* Lataa [kehitysversio][2]

This add-on improves the use of Windows Magnifier with NVDA.


## Ominaisuudet

* Allows to report the result of some native Magnifier keyboard commands.
* Allows to reduce the cases where table navigation commands conflict with
  Magnifier's commands.
* Lisää pikanäppäimiä suurennuslasin eri asetusten muuttamiseen..


## Asetukset

Windowsin suurennuslasi -lisäosan asetuspaneelissa voit määrittää, miten NVDA reagoi natiiveihin Windows-suurennuslasin komentoihin.
Voit haluta enemmän tai vähemmän komentoja ilmoitettavan riippuen siitä, minkä verran näet.
Tämä paneeli voidaan avata Valitsemalla NVDA-valikosta Asetukset -> Asetukset ja sitten Windowsin suurennuslasi -kategoria.
Näppäinkomento NVDA+Win+O ja sitten O avaa myös tämän asetuspaneelin suoraan.

Paneelissa on seuraavat asetukset:

* Ilmoita näkymän liikkeet: säätää, mitä ilmoitetaan, kun siirrät näkymää
  Ctrl+Alt+nuolinäppäimillä. Käytettävissä olevat kolme vaihtoehtoa ovat:
  
    * Ei käytössä: Mitään ei ilmoiteta.
    * Puheella: Puhuttu viesti ilmaisee zoomatun näkymän sijainnin
      suunnassa, johon näkymää siirretään.
    * Äänimerkeillä: Toistettava äänimerkki ja sen korkeus ilmaisee zoomatun
      näkymän sijainnin suunnassa, johon näkymää siirretään.
  
Tämä asetus vaikuttaa vain koko näkymän tilaan.
  
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


## Lisäosan komennot

In addition to native Magnifier commands, this add-on provide additional
commands that allow to control Magnifier's options without opening its
configuration page.  All the commands added to control Magnifier options are
accessible through the Magnifier layer command NVDA+Windows+O:

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
* NVDA+Windows+O then X: Switches between text cursor tracking modes (within
  the edge of the screen or centered on the screen); this feature is only
  available on Windows 10 build 18894 or higher.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command available in full screen view only).
* NVDA+Windows+O then O: Opens Windows Magnifier add-on settings.
* NVDA+Win+O ja sitten H: Näyttää suurennuslasin komentokerroskomentojen
  ohjeen.

There is no default direct gesture for each command, but you can attribute
one normally in the input gesture dialog if you wish.  The same way, You can
also modify or delete the Magnifier layer access gesture (NVDA+Windows+O).
Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.


## Natiivit suurennuslasikomennot

The result of the following Magnifier native commands may be reported by
this add-on, according to its configuration:

* Käynnistä suurennuslasi: Win++ (numeroriviltä tai numeronäppäimistöltä)
* Lopeta suurennuslasi: Win+Esc
* Lähennä näkymää: Win++ (numeroriviltä tai numeronäppäimistöltä)
* Loitonna näkymää: Win+- (numeroriviltä tai numeronäppäimistöltä)
* Ota käänteiset värit käyttöön tai poista ne käytöstä: Ctrl+Alt+I
* Valitse kiinnitetty näkymä: Ctrl+Alt+D
* Valitse koko ruudun näkymä: Ctrl+Alt+F
* Valitse linssinäkymä: Ctrl+Alt+L
* Vaihda kolmen näkymätyypin välillä: Ctrl+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow.
  Note: although this does not seem to be documented, this shortcut seems to
  have been withdrawn in recent Windows versions such as Windows 2004.
* Move the magnified view: Control+Alt+Arrows (reporting only affects full
  screen mode)

Here is also a list of other Magnifier native commands, just for
information:

* Ctrl+Alt+Hiiren vieritysrulla: Lähentää ja loitontaa näkymää hiiren
  vieritysrullaa käyttäen.
* Ctrl+Win+M: Avaa suurennuslasin asetusikkunan.
* Ctrl+Alt+R: Muuttaa linssin kokoa hiiren avulla.
* Ctrl+Alt+Väli: Näyttää nopeasti koko työpöydän koko ruudun näkymää
  käytettäessä.

Natiiveja suurennuslasikomentoja ei voi muuttaa.


## Huomautuksia

* For computers equipped with an Intel graphic card, control+alt+arrow
  (left/right/up/down) are also shortcuts to modify the orientation of the
  screen.  These shortcut are enabled by default and conflict with Windows
  Magnifiers shortcuts to move the view.  You will need to disable them to
  be able to use them for the Magnifier.  They can be disabled in the Intel
  control panel or in the Intel menu present in the system tray.
* Depending on your Windows version, Alt+Shift+Arrow are Windows Magnifier
  shortcuts to resize the magnified view (lens or docked).  When Magnifier
  is active (even in full screen mode), these shortcuts are captured by
  Magnifier and cannot be passed to the application, even if you press
  NVDA+F2 before.  To use these shortcuts in the current application, you
  need to quit the Magnifier (Windows+Escape) and re-open it after
  (Windows++).  For example in MS word, to decrease title level:
  
    * Press Windows+Escape to quit Magnifier.
    * Press Alt+Shift+RightArrow to decrease current title level.
    * Press Windows++ to re-open the Magnifier.

* For more information about Windows Magnifier's features and shortcuts, you
  may want to consult the following pages:

    * [Use Magnifier to make things on the screen easier to
      see](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows keyboard shortcuts for accessibility][4]


## Change log

### Version 1.0

* Initial release.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

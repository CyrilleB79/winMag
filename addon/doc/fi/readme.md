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
* Lisää pikanäppäimiä suurennuslasin eri asetusten muuttamiseen..


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
  
    * Ei koskaan: Komentoa ei välitetä Windows suurennuslasille, ja
      tavalliset NVDA:n taulukossa liikkuminen toimii.  Käytettäessä
      asiakirjoissa olevien taulukoiden ulkopuolella
      Ctrl+Alt+Nuolinäppäin-komento ilmoittaa virheen "Ei taulukossa". NVDA
      toimii näin ilman tätä lisäosaa.
    * Vain, kun ei taulukossa: Taulukko- tai luettelonäkymissä
      Ctrl+Alt+Nuoli-komentoja voidaan käyttää tavalliseen taulukossa
      liikkumiseen.  Käytettäessä asiakirjoissa olevien taulukoiden
      ulkopuolella Ctrl+Alt+Nuoli-komennot suorittavat tavallisia
      suurennuslasin näkymänsiirtokomentoja. Mikäli haluat silti siirtää
      suurennuslasin näkymää taulukko- tai luettelonäkymässä, sinun on
      painettava NVDA+F2 ennen kuin käytät Ctrl+Alt+Nuoli-komentoja. Tämä
      vaihtoehto on paras kompromissi, jos haluat käyttää
      Ctrl+Alt+Nuoli-näppäinyhdistelmää sekä suurennuslasissa että
      taulukossa liikkumiseen.
    * Aina: Ctrl+Alt+Nuoli-komennot siirtävät suurennuslasin näkymää
      kaikissa tapauksissa. Tämä vaihtoehto voi olla hyödyllinen, mikäli et
      käytä Ctrl+Alt+Nuoli-komentoja taulukossa liikkumiseen, esim. koska
      olet vaihtanut NVDA:n taulukkonavigointikomentoja tai koska käytät
      yksinomaan [Helppo taulukossa liikkuminen][5] -lisäosaa taulukossa
      liikkumiseen.


## Lisäosan komennot

Alkuperäisten suurennuslasikomentojen lisäksi tämä lisäosa tarjoaa
lisäkomentoja, joiden avulla voit hallita suurennuslasin asetuksia avaamatta
sen asetussivua. Kaikki komennot, jotka on lisätty ohjaamaan suurennuslasin
asetuksia, ovat käytettävissä suurennuslasin komentokerroskomennolla
NVDA+Win+O:

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
* NVDA+Win+O ja sitten V: Siirtää hiirikohdistimen suurennetun näkymän
  keskelle (komento käytettävissä vain koko näytön näkymässä).
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
* Muuta linssin kokoa näppäimistöllä: Vaihto+Alt+Nuoli
  vasemmalle/oikealle/ylös/alas. Huom: Tämä pikanäppäin näyttää olevan
  poistettu viimeisimmistä Windows-versioista, kuten Windows 10 2004,
  vaikkei sitä ole dokumentoitu missään.
* Siirrä suurennettua näkymää: Ctrl+Alt+Nuolet (ilmoittaminen vaikuttaa vain
  koko näytön tilaan)

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


## Muutosloki

### Versio 1.0

* Ensimmäinen julkaisu.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]:
https://support.microsoft.com/fi-fi/windows/windowsin-helppok%C3%A4ytt%C3%B6toimintojen-pikan%C3%A4pp%C3%A4imet-021bcb62-45c8-e4ef-1e4f-41b8c1fc87fd

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

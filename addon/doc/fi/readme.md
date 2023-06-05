# Windowsin suurennuslasi #

* Tekijä: Cyrille Bougot
* yhteensopivuus: NVDA 2018.3 ja uudemmat
* Lataa [vakaa versio][1]

Tämä lisäosa parantaa Windowsin suurennuslasin käytettävyyttä NVDA:n kanssa.


## Ominaisuudet

* Ilmoittaa joidenkin alkuperäisten suurennuslasinäppäinkomentojen tulokset.
* Vähentää tapauksia, joissa taulukkonavigointikomennot ovat ristiriidassa
  suurennuslasikomentojen kanssa.
* Lisätty joitakin pikanäppäimiä suurennuslasin useiden alkuperäisten
  asetusten muuttamiseen.
* Mahdollistaa suurennuslasin asetusten tallentamisen ja palauttamisen.
* Lisää joitain lisäominaisuuksia, joita Windowsin suurennuslasi ei tarjoa
  (siirrä hiiri näkymään, suurennuslasi ei päällimmäisenä)

## Asetukset

Windowsin suurennuslasi -lisäosan asetuspaneelissa voit määrittää, miten
NVDA reagoi suurennuslasin alkuperäisiin komentoihin. Voit haluta enemmän
tai vähemmän komentoja ilmoitettavan riippuen siitä, minkä verran
näet. Paneelissa on myös asetus, jolla voidaan muokata suurennuslasin
säädinikkunan toimintaa.

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
  
Tämä asetus ei vaikuta kiinnitetyn näkymän tilaan.

* Ilmoita näytön reunat: säätää, mitä ilmoitetaan, kun saavutat näytön
  reunan siirtäessäsi näkymää Ctrl+Alt+nuolinäppäimillä. Käytettävissä
  olevat kolme vaihtoehtoa ovat: Ei käytössä, Puheella ja
  Äänimerkeillä. Tämä asetus ei vaikuta kiinnitetyn näkymän tilaan.
* Näkymän sijainnin ilmoittavien äänimerkkien voimakkuus: Mahdollistaa
  äänimerkkien voimakkuuden määrittämisen, mikäli olet valinnut näkymän
  siirtämisen tai näytön reunojen ilmoittamisen äänimerkeillä.
* Ilmoita käyttöön ottaminen tai käytöstä poistaminen: Jos tämä on
  valittuna, suurennuslasin tila ilmoitetaan käyttäessäsi Win++- tai
  Win+Esc-komentoja sen käyttöön ottamiseksi tai käytöstä poistamiseksi.
* Ilmoita zoomauksen taso: Jos tämä on valittuna, suurennuslasin zoomauksen
  taso ilmoitetaan käyttäessäsi zoomauskomentoja Win++ tai Win+-.
* Ilmoita värin inversio: Jos tämä on valittuna, värin inversion tila
  ilmoitetaan käyttäessäsi tilanvaihtokomentoa Ctrl+Alt+I.
* Ilmoita näkymän vaihtaminen: Jos tämä on valittuna, näkymän tyyppi
  ilmoitetaan käyttäessäsi sitä vaihtavaa komentoa (Ctrl+Alt+M, Ctrl+Alt+F,
  Ctrl+Alt+D ja Ctrl+Alt+L).
* Ilmaise linssi- tai kiinnitetyn ikkunan koon muuttaminen: Jos tämä on
  valittuna, NVDA antaa ilmoituksen käyttäessäsi koonmuuttamiskomentoja
  (Alt+Vaihto+Nuolinäppäimet). Kiinnitetyn ikkunan tilassa ilmoitetaan
  korkeus tai leveys. Linssitilassa uutta mittaa ei toistaiseksi voida
  ilmoittaa. Nämä koonmuutoskomennot eivät näytä olevan käytettävissä
  kaikissa Windows-versioissa; mikäli Windows-versiosi ei tue niitä, älä
  valitse tätä asetusta.
* Välitä Ctrl+Alt+Nuolet-pikanäppäimet asiakirjoissa ja luettelonäkymissä
  Windowsin suurennuslasille: Mahdollisia vaihtoehtoja on kolme:
  
    * Ei koskaan: Komentoa ei välitetä Windowsin suurennuslasille, ja
      tavallinen NVDA:n taulukossa liikkuminen toimii. Käytettäessä
      asiakirjoissa olevien taulukoiden ulkopuolella
      Ctrl+Alt+Nuolinäppäin-komento ilmoittaa virheen "Ei taulukossa". NVDA
      toimii näin ilman tätä lisäosaa. Voit edelleen käyttää NVDA+Win+O:ta
      ja sitten nuolinäppäimiä suurennetun näkymän siirtämiseen.
    * Vain, kun ei taulukossa: Taulukko- tai luettelonäkymissä
      Ctrl+Alt+Nuoli-komentoja voidaan käyttää tavalliseen taulukossa
      liikkumiseen.  Käytettäessä asiakirjoissa olevien taulukoiden
      ulkopuolella Ctrl+Alt+Nuoli-komennot suorittavat tavallisia
      suurennuslasin näkymänsiirtokomentoja. Mikäli haluat silti siirtää
      Windowsin suurennuslasin näkymää taulukko- tai luettelonäkymässä,
      sinun on painettava NVDA+F2 ennen kuin käytät
      Ctrl+Alt+Nuoli-komentoja, tai käytä vaihtoehtoisesti NVDA+Win+O:ta ja
      sitten nuolinäppäimiä. Tämä vaihtoehto on paras kompromissi, jos
      haluat käyttää Ctrl+Alt+Nuoli-näppäinyhdistelmää sekä suurennuslasissa
      että taulukossa liikkumiseen.
    * Aina: Ctrl+Alt+Nuoli-komennot siirtävät suurennuslasin näkymää
      kaikissa tapauksissa. Tämä vaihtoehto voi olla hyödyllinen, mikäli et
      käytä Ctrl+Alt+Nuoli-komentoja taulukossa liikkumiseen, esim. koska
      olet vaihtanut NVDA:n taulukkonavigointikomentoja tai koska käytät
      yksinomaan [Helppo taulukossa liikkuminen][5] -lisäosaa taulukossa
      liikkumiseen.

* Pidä Windowsin suurennuslasin komentoikkuna aina päällimmäisenä: Jos tämä
  ei ole valittuna, suurennuslasin säädinikkunaa ei pidetä aina muiden
  ikkunoiden päällä.

## Lisäosan komennot

Alkuperäisten suurennuslasikomentojen lisäksi Tämä lisäosa tarjoaa
lisäkomentoja:

* Komentoja, joiden avulla voi hallita suurennuslasin asetuksia avaamatta
  sen asetussivua.
* Tämän lisäosan lisäkomennot.

Kaikki nämä lisäkomennot ovat käytettävissä suurennuslasin komentokerroksen,
NVDA+Win+O, kautta:

* NVDA+Win+O ja sitten C: Ottaa kohdistimen seurannan käyttöön tai poistaa
  sen käytöstä.
* NVDA+Win+O ja sitten F: Ottaa kohdistuksen seurannan käyttöön tai poistaa
  sen käytöstä.
* NVDA+Win+O ja sitten M: Ottaa hiiren seurannan käyttöön tai poistaa sen
  käytöstä.
* NVDA+Win+O ja sitten T: Ottaa käyttöön seurannan tai poistaa sen käytöstä
  järjestelmänlaajuisesti. Kun seuranta otetaan uudelleen käyttöön, käytössä
  on ennen sen käytöstä poistamista aktiivisena ollut asetus.
* NVDA+Win+O ja sitten S: Ottaa pehmennyksen käyttöön tai poistaa sen
  käytöstä.
* NVDA+Win+O ja sitten R: Vaihtaa hiiren osoittimen seurannan tilaa (näytön
  reunojen sisäpuolella tai näytöllä keskitettynä). Tämä ominaisuus on
  käytettävissä vain Windows 10:n koontiversiossa 17643 tai sitä uudemmassa.
* NVDA+Win+O ja sitten X: Vaihtaa tekstin kohdistimen seurannan tilaa
  (näytön reunojen sisäpuolella tai näytöllä keskitettynä). Tämä ominaisuus
  on käytettävissä vain Windows 10:n koontiversiossa 18894 tai sitä
  uudemmassa.
* NVDA+Win+O ja sitten Vaihto+P: Tallentaa nykyiset suurennuslasin asetukset
  NVDA:n asetuksiin.
* NVDA+Win+O ja sitten P: Palauttaa suurennuslasin nykyiset asetukset NVDA:n
  asetuksista. Mikäli asetuksia ei ole aiemmin tallennettu, Windowsin
  suurennuslasin oletusasetukset palautetaan.
* NVDA+Win+O ja sitten nuolinäppäimet: Siirrä suurennettua näkymää.
* NVDA+Win+O ja sitten V: Siirtää hiirikohdistimen suurennetun näkymän
  keskelle (komento ei käytettävissä kiinnitetyn näkymän tilassa).
* NVDA+Win+O ja sitten W: Ottaa käyttöön tai poistaa käytöstä tilan, joka
  pitää Windowsin suurennuslasin ikkunan muiden ikkunoiden päällä. Tämä
  ominaisuus on käytettävissä vain NVDA:n asennetuissa versioissa.
* NVDA+Win+O ja sitten O: Avaa Windowsin suurennuslasi -lisäosan asetukset.
* NVDA+Win+O ja sitten H: Näyttää suurennuslasin komentokerroskomentojen
  ohjeen.

Komennoilla ei ole oletusarvoisia näppäinkomentoja, mutta voit halutessasi
määrittää ne normaalisti Näppäinkomennot-valintaikkunassa. Samalla tavalla
voit myös muuttaa tai poistaa suurennuslasin komentokerroksen
aktivointikomennon (NVDA+Win+O). Komentokerroksen alikomentojen muuttaminen
ei kuitenkaan ole mahdollista.


## Alkuperäiset suurennuslasikomennot

Asetuksista riippuen seuraavien alkuperäisten suurennuslasikomentojen
tulokset puhutaan tätä lisäosaa käytettäessä:

* Käynnistä suurennuslasi: Win++ (numeroriviltä tai numeronäppäimistöltä)
* Lopeta suurennuslasi: Win+Esc
* Zoomaa lähemmäs: Win++ (numeroriviltä tai laskinnäppäimistöltä)
* Zoomaa loitommas: Win+- (numeroriviltä tai laskinnäppäimistöltä)
* Ota käänteiset värit käyttöön tai poista ne käytöstä: Ctrl+Alt+I
* Valitse kiinnitetty näkymä: Ctrl+Alt+D
* Valitse koko ruudun näkymä: Ctrl+Alt+F
* Valitse linssinäkymä: Ctrl+Alt+L
* Vaihda kolmen näkymätyypin välillä: Ctrl+Alt+M
* Muuta linssin kokoa näppäimistöllä: Vaihto+Alt+Nuoli
  vasemmalle/oikealle/ylös/alas. Huom: Tämä pikanäppäin näyttää olevan
  poistettu viimeisimmistä Windows-versioista, kuten Windows 10 2004,
  vaikkei sitä ole dokumentoitu missään.
* Siirrä suurennettua näkymää: Ctrl+Alt+Nuolinäppäimet

Tässä on lisäksi luettelo muista Suurennuslasin alkuperäisistä komennoista:

* Ctrl+Alt+Hiiren vieritysrulla: Zoomaa lähemmäs tai loitommas hiiren
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
  kanssa. Ne on poistettava käytöstä, jotta voit käyttää niitä
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

* Tätä lisäosaa ei ole testattu moninäyttöympäristössä, ja on mahdollista,
  että jokin ominaisuus ei toimi sitä käytettäessä. Mikäli käytät
  moninäyttöympäristöä ja haluat, että sitä tuetaan, ota minuun yhteyttä.
* Yleisemmin ottaen älä epäröi ottaa minuun yhteyttä tämän lisäosan
  [GitHub-sivulla][3] tai suoraan sähköpostitse.


## Muutosloki

### Versio 3.2

* Dev-kanava poistettu.
* Lokalisointeja päivitetty.

### Versio 3.1

* Korjattu ongelma, joka esti suurennuslasin komentoikkunan palauttamista
  päällimmäiseksi.
* Korjattu ongelma, joka esti lisäosan suorittamisen NVDA 2019.2.1:ssä.
* Lokalisointeja päivitetty.

### Versio 3.0

* Uusi zoomauksen taso ilmoitetaan nyt painettaessa suurennuslasin ikkunassa
  olevia Zoomauspainikkeita näppäimistöltä.
* Suurennuslasin säädinikkunan päällimmäisenä olemista määrittävä asetus
  tallennetaan nyt asetuksiin. Tämä tarkoittaa, että asetuksen tila
  muistetaan NVDA:ta uudelleenkäynnistettäessä, ja asetus voidaan ottaa
  käyttöön tai poistaa käytöstä aktiivisesta profiilista riippuen.
* Korjattu bugi, joka aiheutti odottamattoman näyttöverhon käytöstä
  poistamisen Siirry näkymään- tai Siirrä näkymää -komentoja käytettäessä.
* Aina päällimmäisenä -asetusta noudatetaan nyt myös suurennuksen tilaa
  vaihdettaessa.
* Lisätty mahdollisuus Windowsin suurennuslasin asetusten tallentamiseen ja
  palauttamiseen.
* Yhteensopivuus NVDA 2023.1:n kanssa.
* Selvennetty, mikä asetus on käytössä, kun seuranta otetaan uudelleen
  käyttöön.
* Lokalisointeja päivitetty.

### Versio 2.0

* Näkymää voidaan siirtää nuolinäppäimillä Windows-suurennuslasin
  komentokerroksessa oltaessa.
* Mahdollisuus pitää suurennuslasin komentoikkuna aina päällimmäisenä.
* Lisätty "Ilmoita näytön reunat" -ominaisuus.
* Äänimerkkien voimakkuusasetus näkymänsiirtämiskomentoja käytettäessä.
* Näkymän siirtämis- ja Siirrä hiiri näkymään -komentojen ilmoittamista
  tuetaan nyt linssitilassa.
* Yhteensopivuus NVDA 2022.1:n kanssa.
* Korjattu virhe, joka joskus ilmoitti virheellisesti, että suurennuslasi ei
  toiminut skriptiä kutsuttaessa.
* Julkaisu suoritetaan nyt appVeyorin sijasta GitHub-toiminnolla.
* Lokalisointeja päivitetty.

### Versio 1.1

* Lokalisointeja lisätty.

### Versio 1.0

* Ensimmäinen julkaisu.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]:
https://support.microsoft.com/fi-fi/windows/windowsin-helppok%C3%A4ytt%C3%B6toimintojen-pikan%C3%A4pp%C3%A4imet-021bcb62-45c8-e4ef-1e4f-41b8c1fc87fd

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

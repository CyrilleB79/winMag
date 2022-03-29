# Windows-Lupe #

* Autor: Cyrille Bougot
* NVDA-Kompatibilität: 2018.3 und neuer
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

Diese Erweiterung verbessert die Verwendung von Windows-Lupe mit NVDA.


## Features

* Ermöglicht es, das Ergebnis einiger nativer Tastaturbefehle der Lupe
  anzusagen.
* Ermöglicht die Reduzierung der Fälle, in denen die Befehle für die
  Tabellen-Navigation mit den Befehlen der Lupe in Konflikt stehen.
* Fügt einige Tastaturkürzel hinzu, um verschiedene Lupenoptionen
  umzuschalten.


## Die Einstellungen

Im Einstellungsfeld der Erweiterung für die Windows-Lupe können Sie konfigurieren, wie NVDA auf native Befehle für die Windows_lupe reagiert.
Möglicherweise möchten Sie mehr oder weniger Befehle angesagt bekommen, je nachdem, was Sie sehen können.
Dieses Fenster kann geöffnet werden, indem Sie im NVDA-Menü Einstellungen -> Optionen auswählen und dann im Einstellungsfenster die Kategorie "Windows-Lupe" auswählen.

Die Tastenkombination NVDA+Windows+O dann O öffnet auch dieses Einstellungsfenster direkt.

Das Panel enthält die folgenden Optionen:

* Verschieben der Berichtsansicht: Steuert, was mitgeteilt wird, wenn Sie
  die Ansicht mit den Befehlen Strg+Alt+Pfeil verschieben. Die drei Optionen
  sind:
  
    * Aus: Es wird nichts angesagt.
    * Mit Sprachausgabe: Via Sprachausgabe wird die Position der gezoomten
      Ansicht in der Dimension angesagt, in der die Ansicht verschoben wird.
    * Mit Signaltöne: Ein Signalton wird wiedergegeben und dessen Tonhöhe
      gibt die Position der gezoomten Ansicht auf der Dimension an, in der
      die Ansicht verschoben wird.
  
  Diese Option betrifft nur den Vollbild-Modus.
  
* Ansage ein- oder ausschalten: Wenn diese Option aktiviert ist, wird der
  Status der Lupe gemeldet, wenn Sie Windows+Plus or Minus oder
  Windows+Escape verwenden, um sie ein- oder auszuschalten.
* Zoom-Faktor ansagen: Wenn diese Option aktiviert ist, wird die Zoom-Faktor
  der Lupe gemeldet, wenn Sie die Zoombefehle von Windows+Plus oder
  Windows+Minus verwenden.
* Invertierte Farben ansagen: Wenn diese Option aktiviert ist, wird der
  Status der Farbumkehrung angesagt, wenn Sie den Umschalt-Befehl Strg+Alt+I
  verwenden.
* Ansichtsänderung ansagen: Wenn aktiviert, wird der Ansichtstyp angesagt,
  wenn Sie einen Befehl verwenden, der den Ansichtstyp ändert (Strg+Alt+M,
  Strg+Alt+F, Strg+Alt+D, Strg+Alt+L)
* Größenänderung der Linse oder des angedockten Fensters ansagen: Wenn diese
  Option aktiviert ist, wird eine Meldung ausgegeben, wenn Sie die
  Größenänderungsbefehle verwenden (Alt+Umschalt+Pfeil). Im angedockten
  Fenstermodus wird die Höhe oder die Breite gemeldet. Im Objektivmodus kann
  die neue Dimension vorerst nicht gemeldet werden. Diese
  Größenänderungsbefehle scheinen nicht in allen Windows-Versionen verfügbar
  zu sein; Wenn Ihre Windows-Version sie nicht unterstützt, sollten Sie
  diese Option deaktiviert lassen.
* In Dokumenten und Listenansichten die Tastenkombinationen
  Strg+Alt+Pfeiltasten an die Windows-Lupe durchreichen: Es gibt drei
  Möglichkeiten:
  
    * Nie: Der Befehl wird nicht an die Windows-Lupe übergeben und die
      standardmäßige Tabellen-Navigation in NVDA kann ausgeführt werden. Bei
      Verwendung in Dokumenten außerhalb einer Tabelle meldet der Befehl
      Strg+Alt+Pfeiltasten die Fehlermeldung "Nicht in einer Tabelle". Dies
      ist das Standardverhalten von NVDA ohne dieser Erweiterung.
    * Nur außerhalb von Tabellen: In Tabellen- oder Listenansichten führen
      die Befehle Strg+Alt+Pfeiltasten die Standardtabellennavigation
      durch. Bei Verwendung in Dokumenten aus einer Tabelle führen die
      Befehle Strg+Alt+Pfeiltasten die Standardbefehle zum Verschieben der
      Lupenansicht aus. Wenn Sie die Windows-Lupe weiterhin in der Tabellen-
      oder Listenansicht verschieben möchten, müssen Sie NVDA+F2 drücken,
      bevor Sie die Befehle Strg+Alt+Pfeiltasten verwenden. Diese Option ist
      der beste Kompromiss, wenn Sie Strg+Alt+Pfeiltasten sowohl für die
      Lupen- als auch die Tabellennavigation verwenden möchten.
    * Immer: Strg+Alt+Pfeiltasten verschieben die Ansicht der Lupe in jedem
      Fall. Diese Option kann nützlich sein, wenn Sie nicht
      Strg+Alt+Pfeiltasten zum Navigieren in der Tabelle verwenden,
      z. B. weil Sie die Tastenkombination für die Tabellen-Navigation in
      NVDA geändert haben oder weil Sie ausschließlich die Erweiterung
      [Einfache Tabellen-Navigation][5] für die Tabellen-Navigation
      verwenden.


## Befehle

Zusätzlich zu den nativen Lupenbefehlen bietet dieser Erweiterung weitere
Befehle, mit denen die Optionen der Lupe gesteuert werden können, ohne die
Konfigurationsseite zu öffnen. Alle Befehle, die zur Steuerung der
Lupenoptionen hinzugefügt wurden, sind über den Befehl NVDA+Windows+O
zugänglich:

* NVDA+Windows+O, dann C: Schaltet die Verfolgung des System-Cursors ein
  oder aus.
* NVDA+Windows+O, dann F: Schaltet die Verfolgung des Cursors ein oder aus.
* NVDA+Windows+O, dann M: Schaltet die Verfolgung der Maus ein oder aus.
* NVDA+Windows+O, dann T: Schaltet die Verfolgung global ein oder aus.
* NVDA+Windows+O, dann S: Schaltet die Kantenglättung ein oder aus.
* NVDA+Windows+O, dann R: Schaltet zwischen den Verfolgungsmodi der Maus um
  (am Rand des Bildschirms oder zentriert auf dem Bildschirm). Diese
  Funktion ist nur unter Windows 10 Build 17643 oder neuer verfügbar.
* NVDA+Windows+O dann X: Wechselt zwischen den Textcursor-Tracking-Modi
  (innerhalb des Bildschirmrands oder zentriert auf dem Bildschirm); Diese
  Funktion ist nur unter Windows 10 Build 18894 oder neuer verfügbar.
* NVDA+Windows+O, dann V: Bewegt den Mauszeiger in die Mitte der
  vergrößerten Ansicht (Befehl nur in der Vollbild-Ansicht verfügbar).
* NVDA+Windows+O, dann O: Öffnet die Einstellungen der Erweiterung für die
  Windows-Lupe.
* NVDA+Windows+O, dann H: Zeigt die Hilfe zu Befehlen des Levels der Lupe
  an.

Es gibt keine standardmäßige direkte Tastenkombination für jeden Befehl,
aber Sie können eine normale Tastenkombination im Dialogfeld für die
Tastenbefehle zuweisen, wenn Sie möchten. Auf die gleiche Weise können Sie
auch die Tastenkombination für den Zugriff (NVDA+Windows+O) ändern oder
löschen. Sie können die Tastenkombination der Unterbefehle jedoch nicht
ändern.


## Befehle für die Windows-Lupe

Das Ergebnis der folgenden nativen Lupenbefehle kann von dieser Erweiterung
entsprechend dessen Konfiguration angesagt werden:

* Windows-Lupe starten: Windows+Plus-Taste
* Windows-Lupe beenden: Windows+Escape-Taste
* Vergrößern: Windows+Plus (auf alphanumerischer Tastatur oder auf dem
  Nummernblock)
* Verkleinern: Windows+Minus (auf alphanumerischer Tastatur oder auf dem
  Nummernblock)
* Farbinversion umschalten: Steuerung+Alt+I
* Angedockte Ansicht auswählen: Steuerung+Alt+D
* Vollbildansicht auswählen: Steuerung+Alt+F
* Objektivansicht auswählen: Steuerung+Alt+L
* Zwischen 3 Ansichtstypen (umschalten: Steuerung+Alt+M
* Ändern Sie die Größe des Objektivs mit der Tastatur:
  Umschalt+Alt+Pfeiltasten. Hinweis: Obwohl dies nicht dokumentiert zu sein
  scheint, scheint diese Verknüpfung in neueren Windows-Versionen wie
  Windows 10 Version 2004 entfernt worden zu sein.
* Verschieben der vergrößerten Ansicht: Strg+Alt+Pfeil (die
  Berichterstellung betrifft nur den Vollbild-Modus)

Es gibt auch eine Liste weitere nativer Befehle der Lupe, nur zur
Information:

* Steuerung+Alt+Mausrad: verkleinern und vergrößern mittels Mausrad.
* Steuerung+Windows+m: öffnet das Lupen-Einstellungsfenster.
* Strg+Alt+R: Ändert die Größe des Objektivs mit der Maus.
* Strg+Alt+Leertaste: Zeigt bei Verwendung der Vollbildansicht schnell den
  gesamten Desktop an.

Keiner der Tastenkombinationen für die Windows-Lupe können geändert werden.


## Anmerkungen

* Bei Computern, die mit einer Intel-Grafikkarte ausgestattet sind, sind
  Strg+Alt+Pfeiltasten auch Verknüpfungen zum Ändern der
  Bildschirmausrichtung. Diese Verknüpfungen sind standardmäßig aktiviert
  und stehen in Konflikt mit den Verknüpfungen der Windows-Lupe zum
  Verschieben der Ansicht. Sie müssen sie deaktivieren, um sie für die Lupe
  verwenden zu können. Sie können in der Intel-Systemsteuerung oder im
  Intel-Menü in der Taskleiste deaktiviert werden.
* Abhängig von Ihrer Windows-Version sind Alt+Umschalt+Pfeiltasten für die
  Windows-Lupe, um die Größe der vergrößerten Ansicht (Objektiv oder
  angedockt) zu ändern. Wenn die Bildschirmlupe aktiv ist (auch im
  Vollbild-Modus), werden diese Verknüpfungen von der Bildschirmlupe erfasst
  und können nicht an die Anwendung weitergegeben werden, selbst wenn Sie
  zuvor NVDA+F2 drücken. Um diese Verknüpfungen in der aktuellen Anwendung
  zu verwenden, müssen Sie die Lupe beenden (Windows+Escape) und
  anschließend erneut öffnen (Windows+Plus). Zum Beispiel in Microsoft Word,
  um die Titelebene zu verringern:
  
    * Drücken Sie Windows+Escape-Taste, um die Lupe zu beenden.
    * Drücken Sie Alt+Umschalt+Pfeiltaste nach rechts, um die aktuelle
      Titelstufe zu verringern.
    * Drücken Sie Windows+Plustaste, um die Lupe wieder zu öffnen.

* Weitere Informationen über die Funktionen und Tastenkombinationen der
  Windows-Lupe finden Sie auf den folgenden Seiten:

    * [Die Lupe verwenden, um die Anzeige auf dem Bildschirm zu
      verbessern](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows-Tastaturbefehle für Barrierefreiheit][4]


## Änderungen

### Version 1.0

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

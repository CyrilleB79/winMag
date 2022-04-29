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
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

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
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the view position: allows to define the
  volume of the tones if you have selected to report view moves or screen
  edges with tones.
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
    * Immer: Strg+Alt+Pfeiltasten verschieben die Ansicht der Lupe in jedem
      Fall. Diese Option kann nützlich sein, wenn Sie nicht
      Strg+Alt+Pfeiltasten zum Navigieren in der Tabelle verwenden,
      z. B. weil Sie die Tastenkombination für die Tabellen-Navigation in
      NVDA geändert haben oder weil Sie ausschließlich die Erweiterung
      [Einfache Tabellen-Navigation][5] für die Tabellen-Navigation
      verwenden.


## Befehle

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

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
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode keeping Windows
  Magnifier's control window always on top of the other ones.  This feature
  is only available for installed versions of NVDA.
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
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

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

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Änderungen

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

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

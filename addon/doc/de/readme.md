# Windows-Lupe #

* Autor: Cyrille Bougot
* NVDA-Kompatibilität: 2018.3 und neuer
* [Stabile Version herunterladen][1]

Diese Erweiterung verbessert die Verwendung von Windows-Lupe mit NVDA.


## Features

* Ermöglicht es, das Ergebnis einiger nativer Tastaturbefehle der Lupe
  anzusagen.
* Ermöglicht die Reduzierung der Fälle, in denen die Befehle für die
  Tabellen-Navigation mit den Befehlen der Lupe in Konflikt stehen.
* Fügt einige Tastenkombinationen zum Umschalten verschiedener Optionen der
  Lupe hinzu.
* Allow to save and restore the configuration parameters of the Magnifier.
* Fügt einige zusätzliche Funktionen hinzu, die die Windows-Lupe nicht
  anbietet (Maus zum Betrachten, Lupenfenster nicht im Vordergrund)

## Die Einstellungen

The setting panel of Windows Magnifier add-on allows to configure how NVDA
reacts to native Windows Magnifier commands.  You may want to have more or
less commands reported according to what you are able to see.  The panel
also contains an option to modify the behaviour of Windows Magnifier control
window.

This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

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
  
  Diese Option wirkt sich nicht auf den angedockten Ansichtsmodus aus.

* Bildschirmränder mitteilen: Steuert, was gemeldet wird, wenn Sie beim
  Verschieben der Ansicht mit den Befehlen Strg+Alt+Pfeile die
  Bildschirmränder erreichen.  Die drei Optionen sind: Deaktiviert, mit
  Sprachausgabe oder mit Signaltönen. Diese Option wirkt sich nicht auf den
  angedockten Ansichtsmodus aus.
* Volume of the tones reporting the position of the view: allows to define
  the volume of the tones if you have selected to report view moves or
  screen edges with tones.
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
  
    * Niemals: Der Befehl wird nicht an die Windows-Lupe weitergegeben und
      die Standard-Tabellen-Navigation in NVDA kann funktionieren. Wenn der
      Befehl Strg+Alt+Pfeiltasten in Dokumenten außerhalb einer Tabelle
      betätigt werden, wird eine Fehlermeldung "Nicht in einer Tabelle"
      angezeigt. Dies ist das standardmäßige Verhalten von NVDA ohne diese
      Erweiterung. Sie können weiterhin NVDA+Windows+O und dann die
      Pfeiltasten betätigen, um die vergrößerte Ansicht zu verschieben.
    * Nur wenn nicht in einer Tabelle: In Tabellen- oder Listenansichten
      führt Strg+Alt+Pfeiltasten die Standard-Tabellen-Navigation aus. In
      Dokumenten außerhalb einer Tabelle führt Strg+Alt+Pfeiltasten die
      Standardbefehle zum Verschieben der Lupenansicht aus. Wenn Sie die
      Windows-Lupenansicht in der Tabellen- oder Listenansicht dennoch
      verschieben möchten, müssen Sie vor der Verwendung von dem Drücken von
      Strg+Alt+Pfeiltasten einmal NVDA+F2 drücken oder alternativ
      NVDA+Windows+O und dann die Pfeiltaste betätigen. Diese Option ist der
      beste Kompromiss, wenn Sie Strg+Alt+Pfeiltasten sowohl für die Lupen-
      als auch für die Tabellen-Navigation verwenden möchten.
    * Immer: Strg+Alt+Pfeiltasten verschieben die Ansicht der Lupe in jedem
      Fall. Diese Option kann nützlich sein, wenn Sie nicht
      Strg+Alt+Pfeiltasten zum Navigieren in der Tabelle verwenden,
      z. B. weil Sie die Tastenkombination für die Tabellen-Navigation in
      NVDA geändert haben oder weil Sie ausschließlich die Erweiterung
      [Einfache Tabellen-Navigation][5] für die Tabellen-Navigation
      verwenden.

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## Befehle

Zusätzlich zu den nativen Befehlen der Windows-Lupe bietet diese Erweiterung
weitere Befehle:

* Befehle, die die Optionen für die Windows-Lupe steuern, ohne die
  Konfigurationsseite zu öffnen.
* Zusätzliche Befehle speziell für diese Erweiterung.

Alle diese zusätzlichen Befehle sind über die Tastenkombination
NVDA+Windows+O zu erreichen:

* NVDA+Windows+O, dann C: Schaltet die Verfolgung des System-Cursors ein
  oder aus.
* NVDA+Windows+O, dann F: Schaltet die Verfolgung des Cursors ein oder aus.
* NVDA+Windows+O, dann M: Schaltet die Verfolgung der Maus ein oder aus.
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+Windows+O, dann S: Schaltet die Kantenglättung ein oder aus.
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes
  (within the edge of the screen or centered on the screen); this feature is
  only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O dann X: Wechselt zwischen den Textcursor-Tracking-Modi
  (innerhalb des Bildschirmrands oder zentriert auf dem Bildschirm); Diese
  Funktion ist nur unter Windows 10 Build 18894 oder neuer verfügbar.
* NVDA+Windows+O then shift+P: Saves the current configuration parameters of
  the magnifier to NVDA's configuration.
* NVDA+Windows+O then P: Restores the current configuration parameters of
  the magnifier from NVDA's configuration.  If no configuration parameters
  has been previously saved to NVDA's configuration, the default
  configuration parameters of Windows Magnifier are restored instead.
* NVDA+Windows+O und dann Pfeiltasten: Verschieben Sie die damit vergrößerte
  Ansicht.
* NVDA+Windows+O dann V: Bewegt den Mauszeiger in die Mitte der vergrößerten
  Ansicht (Befehl nicht verfügbar im angedockten Ansichtsmodus).
* NVDA+Windows+O then W: Switches on or off the mode allowing to keep
  Windows Magnifier's control window always on top of the other ones.  This
  feature is only available for installed versions of NVDA.
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
  Umschalt+Alt+Pfeiltasten nach oben/unten/links/rechts - Hinweis: Obwohl
  dies nicht dokumentiert zu sein scheint, scheint diese Tastenkombination
  in neueren Windows-Versionen wie Windows 10 Version 2004 zurückgekehrt zu
  sein.
* Verschieben Sie die vergrößerte Ansicht: Strg+Alt+Pfeiltasten

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

* Diese Erweiterung wurde nicht mit mehreren Bildschirm getestet und es
  besteht die Möglichkeit, dass einige Funktionen in dieser Umgebung nicht
  funktionieren.  Wenn Sie eine mehrere Bildschirme gleichzeitig verwenden
  und möchten, dass es unterstützt wird, kontaktieren Sie mich bitte, damit
  es implementiert werden kann.
* Im Allgemeinen zögern Sie nicht, mich auf der [GitHub-Seite][3] diese
  Erweiterung oder direkt per E-Mail zu kontaktieren.


## Änderungen

### Version 3.2

* Removed the dev channel.
* Übersetzungen aktualisiert.

### Version 3.1

* Fixed an issue preventing the Magnifier's command window from being
  restored on top.
* Fixed an issue preventing the add-on to run on NVDA 2019.2.1.
* Übersetzungen aktualisiert.

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
* Übersetzungen aktualisiert.

### Version 2.0

* In der Ansicht kann die Vergrößerungsstufe der Windows-Lupe mit den
  Pfeiltasten eingestellt werden.
* Möglichkeit geschaffen, das Fenster mit den Befehlen für die Windows-Lupe
  immer im Vordergrund zu halten oder nicht.
* Funktion zum Mitteilen der Bildschirmränder hinzugefügt.
* Einstellung der Lautstärke von Signaltönen bei der Verwendung von Befehlen
  zur Verschiebung der Ansicht.
* Die Mitteilung zum Verschieben der Ansichten und Befehle zum Verschieben
  von Ansichten mit der Maus werden auch im Objektivmodus unterstützt.
* Kompatibilität mit NVDA 2022.1.
* Ein Fehler wurde behoben, der manchmal fälschlicherweise meldete, dass die
  Windows-Lupe beim Skriptaufruf nicht funktionierte.
* Die Freigabe erfolgt nun über eine GitHub-Aktion anstelle von appVeyor.
* Übersetzungen aktualisiert.

### Version 1.1

* Übersetzungen hinzugefügt.

### Version 1.0

* Erstveröffentlichung.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

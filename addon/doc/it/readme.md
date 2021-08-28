# Windows Magnifier #

* Autore: Cyrille Bougot
* NVDA compatibility: 2018.3 and beyond
* Download [stable version][1]
* Scarica la [versione in sviluppo][2]

This add-on improves the use of Windows Magnifier with NVDA.


## Funzionalità

* Allows to report the result of some native Magnifier keyboard commands.
* Allows to reduce the cases where table navigation commands conflict with
  Magnifier's commands.
* Aggiunge alcuni tasti rapidi per attivare o disattivare alcune opzioni di
  ingrandimento.


## Settings

The setting panel of Windows Magnifier add-on allows to configure how NVDA reacts to native Windows Magnifier commands.
You may want to have more or less commands reported according to what you are able to see.
This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

The panel contains the following options:

* Report view moves: controls what is reported when you move the view with
  Control+Alt+Arrows commands. The three options are:
  
    * Off: Nothing is reported.
    * With speech: a speech message indicates the position of the zoomed
      view on the dimension the view is being moved.
    * With tones: a tone is played and its pitch indicates the position of
      the zoomed view on the dimension the view is being moved.
  
  This option only affects full view mode.
  
* Report turn on or off: If checked, the Magnifier's state is reported when
  you use Windows++ or Windows+Escape commands to turn it on or off.
* Report zoom: If checked, the Magnifier's zoom level is reported when you
  use Windows++ or Windows+- zoom commands.
* Report color inversion: If checked, the color inversion state is reported
  when you use the control+Alt+I toggle command.
* Report view change: If checked, the view type is reported when you use a
  command that changes the view type (Control+Alt+M, Control+Alt+F,
  Control+Alt+D, Control+Alt+L)
* Report lens or docked window resizing: If checked, a message is reported
  when you use the resizing commands (Alt+Shift+Arrows).  In docked window
  mode, the height or the width is reported.  In lens mode, the new
  dimension cannot be reported for now.  These resizing command do not seem
  to be available on all versions of Windows; if your Windows version does
  not support them, you should keep this option unchecked.
* In documents and list views, pass control+alt+arrows shortcuts to Windows
  Magnifier: There are three possible choices:
  
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


## Comandi aggiunti da questo add-on

In addition to native Magnifier commands, this add-on provide additional
commands that allow to control Magnifier's options without opening its
configuration page.  All the commands added to control Magnifier options are
accessible through the Magnifier layer command NVDA+Windows+O:

* NVDA+Windows+O, quindi c: attiva o disattiva il tracciamento del cursore
  di scrittura.
* NVDA+Windows+O, quindi f: attiva o disattiva il tracciamento del focus.
* NVDA+Windows+O, quindi m: attiva o disattiva il tracciamento del mouse.
* NVDA+Windows+O, quindi t: attiva o disattiva il tracciamento globale.
* NVDA+Windows+O, quindi s: attiva o disattiva il livellamento (in inglese
  smoothing).
* NVDA+Windows+O, quindi r: cicla tra le modalità di tracciamento del mouse
  (tra i bordi dello schermo o centrata sullo schermo); questa funzione è
  disponibile solo in Windows 10 build 17643 o successiva.
* NVDA+Windows+O then X: Switches between text cursor tracking modes (within
  the edge of the screen or centered on the screen); this feature is only
  available on Windows 10 build 18894 or higher.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command available in full screen view only).
* NVDA+Windows+O then O: Opens Windows Magnifier add-on settings.
* NVDA+Windows+O, poi H: mostra la guida sui comandi a livelli dell'add-on.

There is no default direct gesture for each command, but you can attribute
one normally in the input gesture dialog if you wish.  The same way, You can
also modify or delete the Magnifier layer access gesture (NVDA+Windows+O).
Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.


## Comandi nativi dell'ingranditore

The result of the following Magnifier native commands may be reported by
this add-on, according to its configuration:

* Avviare l'ingranditore: Windows++ (della tastiera centrale o del
  tastierino numerico)
* Chiudere l'ingranditore: Windows+Escape
* Ingrandire: Windows++ (della tastiera centrale o del tastierino numerico)
* Rimpicciolire: Windows+- (della tastiera centrale o del tastierino
  numerico)
* Attivare o disattivare l'inversione dei colori: Control+Alt+I
* Selezionare la visualizzazione bloccata: Control+Alt+D
* Selezionare la modalità a tutto schermo: Control+Alt+F
* Selezionare la visualizzazione a lente: Control+Alt+L
* Ciclare tra le tre visualizzazioni precedenti: Control+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow.
  Note: although this does not seem to be documented, this shortcut seems to
  have been withdrawn in recent Windows versions such as Windows 2004.
* Move the magnified view: Control+Alt+Arrows (reporting only affects full
  screen mode)

Here is also a list of other Magnifier native commands, just for
information:

* Control+Alt+rotellina del mouse: ingrandisce o rimpicciolisce utilizzando
  la rotellina del mouse.
* Control+Windows+M: apre le impostazioni dell'ingranditore.
* Control+Alt+R: ridimensiona la lente con il mouse.
* Control+Alt+Spazio: mostra rapidamente l'intero desktop quando si usa la
  visualizzazione a tutto schermo.

Nessuno dei comandi nativi dell'ingranditore può essere modificato.


## Note

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
  
    * Premete Windows+Escape per chiudere l'ingranditore.
    * Premete Alt+Shift+freccia destra per diminuire il livello del titolo
      selezionato.
    * Premete Windows++ per riaprire l'ingranditore.

* Per ulteriori informazioni sui comandi e le funzionalità dell'ingranditore
  di Windows, consultate le seguenti pagine:

    * [Use Magnifier to make things on the screen easier to
      see](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows keyboard shortcuts for accessibility][4]


## Elenco delle modifiche

### Novità nella versione 1.0

* Versione iniziale.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

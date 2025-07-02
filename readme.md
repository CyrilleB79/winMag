# Windows Magnifier

* Author: Cyrille Bougot
* NVDA compatibility: 2019.2.1 and beyond

This add-on improves the use of Windows Magnifier with NVDA.


## Features

* Allows to report the result of some native Magnifier and color filtering keyboard commands.
* Allows to reduce the cases where table navigation commands conflict with Magnifier's commands.
* Adds some keyboard shortcuts to toggle various native options of the Magnifier.
* Allow to save and restore the configuration parameters of the Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse to view, Magnifier window not on top)

## Settings

The setting panel of Windows Magnifier add-on allows to configure how NVDA reacts to native Windows Magnifier commands.
You may want to have more or less commands reported according to what you are able to see.
The panel also contains an option to modify the behaviour of Windows Magnifier control window.

This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

The panel contains the following options:

* Report view moves: controls what is reported when you move the view with Control+Alt+Arrows commands. The three options are:
  
    * Off: Nothing is reported.
    * With speech: a speech message indicates the position of the zoomed view on the dimension the view is being moved.
    * With tones: a tone is played and its pitch indicates the position of the zoomed view on the dimension the view is being moved.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of the screen while moving the view with Control+Alt+Arrows commands.
  The three options are: Off, With speech and With tones.
  This option does not affect docked view mode.
* Volume of the tones reporting the position of the view: allows to define the volume of the tones if you have selected to report view moves or screen edges with tones.
* Report turn on or off:
  If checked, the Magnifier's state is reported when you use Windows++ or Windows+Escape commands to turn it on or off.
* Report zoom:
  If checked, the Magnifier's zoom level is reported when you use Windows++ or Windows+- zoom commands.
* Report color inversion:
  If checked, the color inversion state is reported when you use the control+Alt+I toggle command.
* Report view change:
  If checked, the view type is reported when you use a command that changes the view type (Control+Alt+M, Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Report lens or docked window resizing:
  If checked, a message is reported when you use the resizing commands (Alt+Shift+Arrows).
  In docked window mode, the height or the width is reported.
  In lens mode, the new dimension cannot be reported for now.
  These resizing command do not seem to be available on all versions of Windows; if your Windows version does not support them, you should keep this option unchecked.
* In documents and list views, pass control+alt+arrows shortcuts to Windows Magnifier:
  There are three possible choices:  
  
    * Never: The command is not passed to Windows Magnifier and standard NVDA table navigation can operate.
      When used in documents out of a table, the Control+Alt+Arrow command reports a "Not in a table" error message.
      This is the standard behaviour of NVDA without this add-on.
      You can still use NVDA+Windows+O then arrows to move the magnified view.
    * Only when not in table: In table or in list views, Control+Alt+Arrow commands perform standard table navigation.
      When used in documents out of a table, Control+Alt+Arrow commands perform standard Magnifier view move commands.
      If you still want to move Windows Magnifier view while in table or in list view, you will need to press NVDA+F2 before using Control+Alt+Arrow commands or alternately use NVDA+Windows+O then arrows.
      This option is the best compromise if you want to use Control+Alt+Arrow for both Magnifier and table navigation.
    * Always: Control+Alt+Arrow commands moves the Magnifier's view in any case.
      This option may be useful if you do not use Control+Alt+Arrow to navigate in table, e.g. because you have changed table navigation shortcuts in NVDA or because you exclusively use [Easy table navigator][5] add-on for table navigation.

* Keep Windows Magnifier command window always on top:
  If unchecked, the Magnifier's control window will not be kept always on top of other windows.
* Report color filter
  If checked, the used color filter is reported when you use the `Windows+Control+C` toggle command.

## Commands added by this add-on

In addition to native Magnifier commands, this add-on provide additional commands:

* Commands that allow to control Magnifier's options without opening its configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer command NVDA+Windows+O:

* NVDA+Windows+O then C: Toggles on or off caret tracking.
* NVDA+Windows+O then F: Toggles on or off focus tracking.
* NVDA+Windows+O then M: Toggles on or off mouse tracking.
* NVDA+Windows+O then T: Toggles on or off tracking globally.
  When tracking is toggled on again, it is set to the last active tracking configuration before tracking was toggled off.
* NVDA+Windows+O then S: Toggles on or off smoothing.
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes (within the edge of the screen or centered on the screen); this feature is only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O then X: Switches between text cursor tracking modes (within the edge of the screen or centered on the screen); this feature is only available on Windows 10 build 18894 or higher.
* NVDA+Windows+O then shift+P: Saves the current configuration parameters of the magnifier to NVDA's configuration.
* NVDA+Windows+O then P: Restores the current configuration parameters of the magnifier from NVDA's configuration.
  If no configuration parameters has been previously saved to NVDA's configuration, the default configuration parameters of Windows Magnifier are restored instead.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode allowing to keep Windows Magnifier's control window always on top of the other ones.
  This feature is only available for installed versions of NVDA.
* NVDA+Windows+O then O: Opens Windows Magnifier add-on settings.
* NVDA+Windows+O then H: Displays help on Magnifier layer commands.

There is no default direct gesture for each command, but you can attribute one normally in the input gesture dialog if you wish.
The same way, You can also modify or delete the Magnifier layer access gesture (NVDA+Windows+O).
Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.


## Magnifier's native commands

The result of the following Magnifier native commands, or other Accessibility commands, may be reported by this add-on, according to its configuration:

* Start Magnifier: Windows++ (on alpha-numeric keyboard or on numpad)
* Quit Magnifier: Windows+Escape
* Zoom in: Windows++ (on alpha-numeric keyboard or on numpad)
* Zoom out: Windows+- (on alpha-numeric keyboard or on numpad)
* Toggle color inversion: Control+Alt+I
* Select the docked view: Control+Alt+D
* Select the full screen view: Control+Alt+F
* Select the lens view: Control+Alt+L
* Cycle through the three view types: Control+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow
  Note: although this does not seem to be documented, this shortcut seems to have been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows
* Toggle color filters: `Windows+Control+C` (provided you have enabled this shortcut in [Windows Accessibility settings, Color Filters][9])

Here is also a list of other Magnifier native commands, just for information:

* Control+Alt+mouseScrollWheel: Zooms in and out using the mouse scroll wheel.
* Control+Windows+M: Opens the Magnifier's settings window.
* Control+Alt+R: Resizes the lens with the mouse.
* Control+Alt+Space: Quickly shows the entire desktop when using full screen view.

None of the Magnifier native commands can be modified.


## Notes

* For computers equipped with an Intel graphic card, control+alt+arrow (left/right/up/down) are also shortcuts to modify the orientation of the screen.
  These shortcut are enabled by default and conflict with Windows Magnifiers shortcuts to move the view.
  You will need to disable them to be able to use them for the Magnifier.
  They can be disabled in the Intel control panel or in the Intel menu present in the system tray.
* Depending on your Windows version, Alt+Shift+Arrow are Windows Magnifier shortcuts to resize the magnified view (lens or docked).
  When Magnifier is active (even in full screen mode), these shortcuts are captured by Magnifier and cannot be passed to the application, even if you press NVDA+F2 before.
  To use these shortcuts in the current application, you need to quit the Magnifier (Windows+Escape) and re-open it after (Windows++).
  For example in MS word, to decrease title level:
  
    * Press Windows+Escape to quit Magnifier.
    * Press Alt+Shift+RightArrow to decrease current title level.
    * Press Windows++ to re-open the Magnifier.

* For more information about Windows Magnifier's features and shortcuts, you may want to consult the following pages:

    * [Use Magnifier to make things on the screen easier to see](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows keyboard shortcuts for accessibility][4]

* This add-on has not been tested in multi-screen environment and there are chances that some feature are not working in this environment.
  If you are using multi-screen environment and want it to be supported, please contact me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of this add-on or directly by e-mail.


## Change log

### Version 4.2

* Magnifier or Color filtering commands will no longer fail if used for the first time with this add-on running.

### Version 4.0

* The filter enabled by the toggle color filter command (`Windows+Control+C`) can now be reported; this toggle command should have been previously enabled in Windows Accessibility settings.
* Compatibility with NVDA 2025.1.

### Version 3.7

* Compatibility with NVDA 2024.1.

### Version 3.6

* Fixed erroneous compatibility range.

### Version 3.5

* Prepares compatibility with NVDA 2024.1.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][8] when using the add-on with older versions of NVDA. However, it is recommended to use NVDA 2023.3.3 or higher.
* Note: From now on, translation updates will not appear anymore in the change log.

### Version 3.4

* The "move mouse to view" command works again
* Updated localizations.

### Version 3.3

* Compatibility reduced to NVDA 2019.2.1 and beyond.
  The last compatible versions with NVDA 2018.3 are the [3.2][7] (partially compatible) and [1.1][6] (fully compatible)
* Fixed a bug in the settings panel with NVDA 2019.2.1.

### Version 3.2

* Removed the dev channel.
* Updated localizations.

### Version 3.1

* Fixed an issue preventing the Magnifier's command window from being restored on top.
* Fixed an issue preventing the add-on to run on NVDA 2019.2.1.
* Updated localizations.

### Version 3.0

* Pressing the zoom buttons in the Magnifier window (with the keyboard) now reports the new zoom level.
* The parameter controlling if Magnifier control window remains always on top is now stored in configuration;
  this means that this parameter is remembered when restarting NVDA and can be enabled or not depending on the active profile.
* Fixed a bug causing unexpected screen curtain de-activation when using move to view or move view commands.
* Option alwaysOnTop setting will now be honoured also when changing magnification mode.
* Added ability to save and restore Windows Magnifier's config in NVDA's config.
* Compatibility with NVDA 2023.1.
* Clarify which type of tracking is re-enabled when tracking is toggled on again.
* Updated localizations.

### Version 2.0

* The view can be moved with arrows while in Windows Magnifier layer.
* Capability to keep the Magnifier commands Window always on top or not.
* Added "Report screen edges" feature.
* Volume setting of tones when using move view commands.
* Reporting view moves and mouse to view commands are now supported in Lens mode.
* Compatibility with NVDA 2022.1.
* Fixed a bug that sometimes incorrectly reported that the Magnifier was not working upon script call.
* The release is now performed thanks to a GitHub action instead of appVeyor.
* Updated localizations.

### Version 1.1

* Added localizations.

### Version 1.0

* Initial release.

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

[6]: https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]: https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]: https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

[9]: https://support.microsoft.com/en-us/windows/make-windows-easier-to-see-c97c2b0d-cadb-93f0-5fd1-59ccfe19345d

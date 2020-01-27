# Windows Magnifier

* Author: Cyrille Bougot
* NVDA compatibility: 2018.3 to 2019.3
* Download [development version][2]

This addon improves the use of the Windows Magnifier with NVDA.


## Features

* Adds some keyboard shortcuts to toggle various Magnifier options.
* Reports the result of some native Magnifier keyboard commands.
* Reduces the cases where table navigation command conflict with Magnifier's commands


## Commands added by this add-on

All the commands added to control Magnifier options are accessible through the Magnifier layer command NVDA+Windows+M:

* NVDA+Windows+M then C: Toggles on or off caret tracking
* NVDA+Windows+M then F: Toggles on or off focus tracking
* NVDA+Windows+M then M: Toggles on or off mouse tracking
* NVDA+Windows+M then T: Toggles on or off tracking globally
* NVDA+Windows+M then S: Toggles on or off smoothing
* NVDA+Windows+M then R: Switch between mouse tracking modes (within the edge of the screen or centered on the screen); this feature is only available on Windows 10 build 17643 or higher.
* NVDA+Windows+M then H: Displays help on Magnifier layer commands

There is no default gesture for each command, but you can attribute one normally in the input gesture dialog if you wish. The same way, You can also modify or delete the Magnifier layer access gesture (NVDA+Windows+M). Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.


## Magnifier's native commands

The result of the following Magnifier native commands is vocalized by this add-on:

* Start Magnifier: Windows++ (on alpha-numeric keyboard or on numpad)
* Quit Magnifier: Windows+Escape
* Zoom in: Windows++ (on alpha-numeric keyboard or on numpad)
* Zoom out: Windows+- (on alpha-numeric keyboard or on numpad)
* Toggle color inversion: Control+Alt+I
* Select the docked view: Control+Alt+D
* Select the full screen view: Control+Alt+F
* Select the lens view: Control+Alt+L
* Cycle through the three view types: Control+Alt+M

The following keyboard shortcuts are also native Magnifier commands: Control+Alt+LeftArrow, Control+Alt+RightArrow, Control+Alt+UpArrow, Control+Alt+DownArrow. They are used to move the magnified view respectively to the left, the right, up or down. Since they are also table navigation commands in NVDA, they are managed as follow by this add-on:

* If the focus or the virtual cursor is not located in a table or a list view, the Magnifier command is executed.
* If the focus or the virtual cursor is located in a table or a list view, the NVDA table navigation command is executed
* If you still want to move the Magnifier's view while being in a table or a list view, you will need to press NVDA+F2 before pressing control+alt+arrowKey.


At last, here is a list of other Magnifier native commands, just for information:

* Control+Windows+M: Open the Magnifier's settings window.
* Control+Alt+R: Resize the lens with the mouse
* Shift+Alt+Left/Right/Up/DownArrow: Resize the lens with the keyboard
* Control+Alt+Space: Quickly see the entire desktop when using full screen view

None of the Magnifier native commands can be modified.


## Change log

### Version 1.0

* Initial release.

[2]: https://github.com/CyrilleB79/winMag/releases/download/V1.0-dev-20200127/winMag-1.0-dev-20200127.nvda-addon

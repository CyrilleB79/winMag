# Windows Magnifier

* Author: Cyrille Bougot
* NVDA compatibility: 2018.3 to 2019.3
* Download [development version][2]

This add-on improves the use of the Windows Magnifier with NVDA.


## Features

* Adds some keyboard shortcuts to toggle various Magnifier options.
* Reports the result of some native Magnifier keyboard commands.
* Reduces the cases where table navigation command conflict with Magnifier's commands.


## Commands added by this add-on

All the commands added to control Magnifier options are accessible through the Magnifier layer command NVDA+Windows+O:

* NVDA+Windows+O then C: Toggles on or off caret tracking.
* NVDA+Windows+O then F: Toggles on or off focus tracking.
* NVDA+Windows+O then M: Toggles on or off mouse tracking.
* NVDA+Windows+O then T: Toggles on or off tracking globally.
* NVDA+Windows+O then S: Toggles on or off smoothing.
* NVDA+Windows+O then R: Switches between mouse tracking modes (within the edge of the screen or centered on the screen); this feature is only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O then H: Displays help on Magnifier layer commands.

There is no default gesture for each command, but you can attribute one normally in the input gesture dialog if you wish. The same way, You can also modify or delete the Magnifier layer access gesture (NVDA+Windows+O). Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.


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
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow

The following keyboard shortcuts are also native Magnifier commands: Control+Alt+LeftArrow, Control+Alt+RightArrow, Control+Alt+UpArrow, Control+Alt+DownArrow. They are used to move the magnified view respectively to the left, the right, up or down. Since they are also table navigation commands in NVDA, they are managed as follows by this add-on:

* If the focus or the virtual cursor is not located in a table or a list view, the Magnifier command is executed.
* If the focus or the virtual cursor is located in a table or a list view, the NVDA table navigation command is executed.
* If you still want to move the Magnifier's view while being in a table or a list view, you will need to press NVDA+F2 before pressing control+alt+arrowKey.


At last, here is a list of other Magnifier native commands, just for information:

* Control+Alt+mouseScrollWheel: Zooms in and out using the mouse scroll wheel.
* Control+Windows+M: Opens the Magnifier's settings window.
* Control+Alt+R: Resizes the lens with the mouse.
* Control+Alt+Space: Quickly shows the entire desktop when using full screen view.

None of the Magnifier native commands can be modified.


## Notes

* For computers equipped with an Intel graphic card, control+alt+arrow (left/right/up/down) are also shortcut to modify the orientation of the screen. These shortcut are enabled by default and conflict with Windows Magnifiers shortcuts to move the view. You will need to disable them to be able to use them for the Magnifier. They can be disabled in the Intel control panel or in the Intel menu present in the system tray.
* Alt+Shift+Arrow are Windows Magnifier shortcuts to resize the magnified view (lens or docked). When Magnifier is active (even in full screen mode), these shortcuts are captured by Magnifier and cannot be passed to the application, even if you press NVDA+F2 before. To use these shortcuts in the current application, you need to quit the Magnifier (Windows+Escape) and re-open it after (Windows++). For example in MS word, to decrease title level:

    * Press Windows+Escape to quit Magnifier.
    * Press Alt+Shift+RightArrow to decrease current title level.
    * Press Windows++ to re-open the Magnifier.

* For more information about Windows Magnifier's features and shortcuts, you may want to consult the following pages:

    * [Use Magnifier to make things on the screen easier to see](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows keyboard shortcuts for accessibility](https://support.microsoft.com/en-us/help/13810)


## Change log

### Version 1.0

* Initial release.

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

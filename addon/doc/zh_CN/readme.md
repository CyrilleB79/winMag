# Windows 放大镜增强插件（插件为英语） #

* 作者: Cyrille Bougot
* NVDA compatibility: 2018.3 and beyond
* Download [stable version][1]
* 下载 [开发版][2]

This add-on improves the use of Windows Magnifier with NVDA.


## 功能

* Allows to report the result of some native Magnifier keyboard commands.
* Allows to reduce the cases where table navigation commands conflict with
  Magnifier's commands.
* 添加一些键盘快捷键来切换各种放大镜选项。


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


## 此插件添加的命令

In addition to native Magnifier commands, this add-on provide additional
commands that allow to control Magnifier's options without opening its
configuration page.  All the commands added to control Magnifier options are
accessible through the Magnifier layer command NVDA+Windows+O:

* NVDA+Windows+O,C:打开或关闭跟随文本光标。
* NVDA+Windows+O,F：打开或关闭跟随键盘焦点。
* NVDA+Windows+O,M：打开或关闭跟随鼠标指针。
* NVDA+Windows+O,T：打开或关闭全局跟随。
* NVDA+Windows+O,S：打开或关闭图像和文本的平滑边缘。
* NVDA+Windows+O,R：在保留鼠标指针模式之间切换，包括屏幕边缘内和在屏幕上居中（此功能仅适用于 Windows 10
  Build17643及以上版本）。
* NVDA+Windows+O then X: Switches between text cursor tracking modes (within
  the edge of the screen or centered on the screen); this feature is only
  available on Windows 10 build 18894 or higher.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command available in full screen view only).
* NVDA+Windows+O then O: Opens Windows Magnifier add-on settings.
* NVDA+Windows+O,H：显示放大镜命令的帮助。

There is no default direct gesture for each command, but you can attribute
one normally in the input gesture dialog if you wish.  The same way, You can
also modify or delete the Magnifier layer access gesture (NVDA+Windows+O).
Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.


## 放大镜的原有快捷键

The result of the following Magnifier native commands may be reported by
this add-on, according to its configuration:

* Windows 徽标键  + 加号 (+)：打开放大镜
* Windows 徽标键  + Esc：关闭放大镜
* Windows 徽标键  + 加号 (+)：当放大镜打开时，进行放大
* Windows 徽标键  + 减号 (-)：当放大镜打开时，进行缩小
* Ctrl + Alt + I：打开或关闭反色
* Ctrl + Alt + D：切换到停靠视图
* Ctrl + Alt + F：切换到全屏视图
* Ctrl + Alt + L：切换到镜头视图
* Ctrl + Alt + M：循环浏览视图
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow.
  Note: although this does not seem to be documented, this shortcut seems to
  have been withdrawn in recent Windows versions such as Windows 2004.
* Move the magnified view: Control+Alt+Arrows (reporting only affects full
  screen mode)

Here is also a list of other Magnifier native commands, just for
information:

* Ctrl + Alt + 鼠标滚轮：使用鼠标滚轮放大和缩小。
* Windows 徽标键  + Ctrl + M：打开“放大镜”设置。
* Ctrl + Alt + R：使用鼠标调整镜头大小。
* Ctrl + Alt + 空格键：使用全屏视图时快速查看整个桌面。

您不能修改放大镜的原有快捷键。


## 注意

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
  
    * 按 Windows 徽标键  +Esc退出放大镜。
    * 按Alt+Shift+右光标键可降低当前标题级别。
    * 按 Windows 徽标键  + 加号 (+)重新打开放大镜。

* 有关Windows放大镜功能和快捷方式的详细信息，请参阅以下页面：

    * [Use Magnifier to make things on the screen easier to
      see](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows keyboard shortcuts for accessibility][4]


## 更新日志

### 版本 1.0

* 发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

# Windows 放大镜增强插件 #

* 作者: Cyrille Bougot
* NVDA compatibility: 2019.2.1 and beyond
* 下载 [稳定版][1]

此插件增强了 NVDA 使用 Windows 放大镜时的体验。


## 功能

* 允许读出某些放大镜原有快捷键的结果。
* 允许减少表格导航快捷键与放大镜快捷键的冲突。
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Allow to save and restore the configuration parameters of the Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

## 设置

The setting panel of Windows Magnifier add-on allows to configure how NVDA
reacts to native Windows Magnifier commands.  You may want to have more or
less commands reported according to what you are able to see.  The panel
also contains an option to modify the behaviour of Windows Magnifier control
window.

This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

该面板包含以下选项：

* 读出试图移动：控制使用 Ctrl+Alt+光标命令移动视图时读出的内容。这三个选项是：
  
    * 关闭：不读出任何内容。
    * 语音：用语音在视图移动时提示视图缩放范围的位置。
    * 提示音：在视图移动时播放，且用音高提示视图缩放范围的位置。
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the position of the view: allows to define
  the volume of the tones if you have selected to report view moves or
  screen edges with tones.
* 读出打开或关闭：如果选中，当您使用 Windows++ 或 Windows+ESC 命令打开或关闭放大镜时，将读出放大镜的状态。
* 读出缩放：如果选中，当您使用 Windows++ 或 Windows+- 缩放命令时会读出放大镜的缩放级别。
* 读出反色：如果选中，则在使用 Ctrl+Alt+I 切换命令时读出反色状态。
* 读出视图更改：如果选中，则在使用更改视图类型的命令（Ctrl+Alt+M、Ctrl+Alt+F、Ctrl+Alt+D、Ctrl+Alt+L）时读出视图类型
* 读出镜头或停靠窗口调整大小：如果选中，则在您使用调整大小命令（Alt+Shift+光标）时会读出一条消息。在停靠窗口模式下，读出高度或宽度。在镜头模式下，目前无法读出新维度。这些调整大小命令并非在所有版本的
  Windows 上都可用；如果您的 Windows 版本不支持，您不应选中此选项。
* 在文档和列表视图中，将Ctrl+alt+光标快捷键传递给 Windows 放大镜： 有三种选择：
  
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
    * 始终：Ctrl+Alt+光标命令在任何情况下都会移动放大镜的视图。如果您不使用
      Ctrl+Alt+光标在表格中导航，则此选项可能很有用，例如您在 NVDA 中更改了表格导航快捷键，或者您专门使用 [简单表格导航][5]
      插件进行表格导航。

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## 此插件添加的命令

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O,C:打开或关闭跟随文本光标。
* NVDA+Windows+O,F：打开或关闭跟随键盘焦点。
* NVDA+Windows+O,M：打开或关闭跟随鼠标指针。
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+Windows+O,S：打开或关闭图像和文本的平滑边缘。
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes
  (within the edge of the screen or centered on the screen); this feature is
  only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O,X：在保留文本光标模式之间切换，包括屏幕边缘内和在屏幕上居中（此功能仅适用于 Windows 10 build
  18894 及以上版本）。
* NVDA+Windows+O then shift+P: Saves the current configuration parameters of
  the magnifier to NVDA's configuration.
* NVDA+Windows+O then P: Restores the current configuration parameters of
  the magnifier from NVDA's configuration.  If no configuration parameters
  has been previously saved to NVDA's configuration, the default
  configuration parameters of Windows Magnifier are restored instead.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode allowing to keep
  Windows Magnifier's control window always on top of the other ones.  This
  feature is only available for installed versions of NVDA.
* NVDA+Windows+O,O：打开Windows 放大镜插件设置。
* NVDA+Windows+O,H：显示放大镜命令的帮助。

每个命令没有默认手势和快捷键，但如果需要，可以在“按键与首饰”对话框中正常设置一个。同样，您也可以修改或删除放大镜层访问快捷键（NVDA+Windows+O）。但是，不能修改放大镜图层子命令的快捷键。


## 放大镜的原有快捷键

根据您的设置，此插件会朗读以下放大镜原有快捷键按下时的状态信息：

* Windows 徽标键  + 加号 (+)：打开放大镜
* Windows 徽标键  + Esc：关闭放大镜
* Windows 徽标键  + 加号 (+)：当放大镜打开时，进行放大
* Windows 徽标键  + 减号 (-)：当放大镜打开时，进行缩小
* Ctrl + Alt + I：打开或关闭反色
* Ctrl + Alt + D：切换到停靠视图
* Ctrl + Alt + F：切换到全屏视图
* Ctrl + Alt + L：切换到镜头视图
* Ctrl + Alt + M：循环浏览视图
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

下面是其他放大镜原有快捷键的列表，仅供参考：

* Ctrl + Alt + 鼠标滚轮：使用鼠标滚轮放大和缩小。
* Windows 徽标键  + Ctrl + M：打开“放大镜”设置。
* Ctrl + Alt + R：使用鼠标调整镜头大小。
* Ctrl + Alt + 空格键：使用全屏视图时快速查看整个桌面。

您不能修改放大镜的原有快捷键。


## 注意

* 对于配备 Intel 显卡的计算机，Ctrl+Alt+光标键也是修改屏幕方向的快捷键。这些快捷键在默认情况下是启用的，并且与移动放大镜视图的
  Windows 快捷键冲突。您需要禁用它们才能将其用于放大镜。它们可以在 Intel 图形控制面板或系统托盘中的 Intel菜单中禁用。
* 在某些 Windows 版本，Alt+Shift+光标键是 Windows
  放大镜的快捷键，用于调整放大视图的大小（镜头或停靠）。当放大镜处于活动状态时，即使在全屏试图下，这些快捷键也将被放大镜捕获，并且不能传递给应用程序，即使您之前按了
  NVDA+F2。要在当前应用程序中使用这些快捷键，您需要退出放大镜（Windows+Esc），然后再重新打开它（Windows++）。例如在
  Word 中降低标题级别：
  
    * 按 Windows 徽标键  +Esc退出放大镜。
    * 按Alt+Shift+右光标键可降低当前标题级别。
    * 按 Windows 徽标键  + 加号 (+)重新打开放大镜。

* 有关Windows放大镜功能和快捷方式的详细信息，请参阅以下页面：

    * [使用“放大镜”可使屏幕上的内容更易于查看](https://support.microsoft.com/zh-cn/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [用于辅助功能的 Windows 键盘快捷方式][4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## 更新日志

### Version 3.5

* Prepares compatibility with NVDA 2024.1.
* Addresses potential security issues related to [GHSA-xg6w-23rw-39r8][8]
  when using the add-on with older versions of NVDA. However, it is
  recommended to use NVDA 2023.3.3 or higher.
* Note: From now on, translation updates will not appear anymore in the
  change log.

### Version 3.4

* The "move mouse to view" command works again
* Updated localizations.

### Version 3.3

* Compatibility reduced to NVDA 2019.2.1 and beyond.  The last compatible
  versions with NVDA 2018.3 are the [3.2][7] (partially compatible) and
  [1.1][6] (fully compatible)
* Fixed a bug in the settings panel with NVDA 2019.2.1.

### Version 3.2

* Removed the dev channel.
* Updated localizations.

### Version 3.1

* Fixed an issue preventing the Magnifier's command window from being
  restored on top.
* Fixed an issue preventing the add-on to run on NVDA 2019.2.1.
* Updated localizations.

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
* Updated localizations.

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

### 版本 1.0

* 发布初始版本。

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/zh-cn/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.zh_CN.html

[6]:
https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]:
https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

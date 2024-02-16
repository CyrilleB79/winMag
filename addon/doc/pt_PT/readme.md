# Lupa do Windows #

* Autor: Cyrille Bougot
* NVDA compatibility: 2019.2.1 and beyond
* Descarregar a [Versão estável][1]

Este extra melhora a utilização da Lupa do Windows com NVDA.


## Funcionalidades

* Permite anunciar o resultado de alguns comandos de teclado nativos da
  Lupa.
* Permite reduzir os casos em que os comandos de navegação em tabelas entram
  em conflito com os comandos da Lupa...
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Allow to save and restore the configuration parameters of the Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

## Configurações

The setting panel of Windows Magnifier add-on allows to configure how NVDA
reacts to native Windows Magnifier commands.  You may want to have more or
less commands reported according to what you are able to see.  The panel
also contains an option to modify the behaviour of Windows Magnifier control
window.

This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

O painel contém as seguintes opções:

* Anúncio de movimentos da vista: controla o que é anunciado quando se move
  a vista com os comandos Control+Alt+Setas. As três opções são:
  
    * Desligado: Nada é anunciado.
    * Com voz: uma mensagem anuncia a posição relativa à direcção em que a
      vista ampliada está a ser movida.
    * Com bips: São reproduzidos bips e o seu tom indica a posição relativa
      à direcção em que a vista ampliada está a ser movida.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the position of the view: allows to define
  the volume of the tones if you have selected to report view moves or
  screen edges with tones.
* Anunciar ligar ou desligar: Se marcado, o estado da Lupa é anunciado
  quando se usa os comandos Windows++ ou Windows+Escape para ligar ou
  desligar a Lupa.
* Anunciar ampliação: Se marcado, o nível de ampliação da lupa é anunciado
  quando se usam os comandos Windows++ ou Windows+-.
* Anunciar inversão de cores: Se marcado, o estado de inversão de cores é
  anunciado quando se usa o comando control+Alt+I.
* Anunciar mudanças de vista: Se marcado, o tipo de vista é anunciado quando
  se utiliza um comando que altera o tipo de vista (Control+Alt+M,
  Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Anunciar o redimensionamento da lente ou da vista ancorada: Se marcado, é
  anunciado quando se utilizam os comandos de redimensionamento
  (Alt+Shift+setas). No modo de vista ancorada, a altura ou a largura é
  anunciada.  Na vista Lente, a nova dimensão não pode ser anunciada por
  agora.  Estes comandos de redimensionamento não parecem estar disponíveis
  em todas as versões do Windows; se a sua versão do Windows não os
  suportar, deve manter esta opção desmarcada.
* Em documentos e listas, passar os comandos controlo+alt+setas para a
  lupa. Existem três opções:
  
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
    * Sempre: Os comandos Control+Alt+setas movem a vista da Lupa em
      qualquer caso.  Esta opção pode ser útil se não usar Control+Alt+setas
      para navegar em tabelas, por exemplo, porque mudou os atalhos de
      navegação em tabela do NVDA ou porque usa exclusivamente o extra
      [Navigação fácil em tabelas][5] para navegação em tabelas.

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## Comandos adicionados por este extra:

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O e depois C: Liga ou desliga o seguimento do cursor de
  texto.
* NVDA+Windows+O e depois F: Liga ou desliga o seguimento do foco de teclado
* NVDA+Windows+O depois M: Liga ou desliga o seguimento do rato.
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+Windows+O depois S: Liga ou desliga a suavização.
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes
  (within the edge of the screen or centered on the screen); this feature is
  only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O e depois R: Alterna entre modos de seguimento do rato
  (dentro das extremidades do ecrã ou centrado no ecrã); esta característica
  só está disponível em Windows 10 build 17643 ou superiores.
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
* NVDA+Windows+O depois O: Abre a janela de configurações da Lupa.
* NVDA+Windows+O depois H: Mostra a ajuda dos comandos em camada da lupa.

Não há nenhum comando padrão para os vários comandos, mas pode atribui-los,
normalmente, no diálogo definir comandos, se o desejar. Da mesma forma,
também é possível modificar ou apagar o comando para iniciar os comandos em
camada da Lupa (NVDA+Windows+O). No entanto, não pode modificar a tecla de
atalho dos sub-comandos da camada da Lupa.


## Comandos nativos da Lupa do Windows

O resultado dos seguintes comandos nativos da Lupa pode ser anunciado por
este extra, dependendo das suas configurações:

* Início da Lupa: Windows++ (no teclado alfanumérico ou no numérico)
* Sair da lupa: Windows+Escape
* Aumentar a ampliação: Windows++ (no teclado alfanumérico ou no numérico)
* Diminuir a ampliação: Windows+- (no teclado alfanumérico ou no numérico)
* Alternar a inversão de cores: Controlo+Alt+I
* Seleccionar a vista ancorada: Controlo+Alt+D
* Seleccionar a visualização em ecrã inteiro: Controlo+Alt+F
* Seleccionar a vista Lente: Controlo+Alt+L
* Alterna entre os três tipos de vista: Controlo+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Eis uma lista de outros comandos nativos da Lupa, apenas para informação:

* Control+Alt+RodaDoRato: Aumenta e diminui a ampliação usando a roda de
  rolagem do rato.
* Control+Windows+M: Abre a janela de configurações da Lupa.
* Control+Alt+R: Redimensiona a lente com o rato.
* Control+Alt+espaço: Mostra rapidamente todo o ambiente de trabalho quando
  se utiliza a vista de ecrã inteiro.

Nenhum dos comandos nativos da Lupa pode ser modificado.


## Notas

* Para computadores equipados com uma placa gráfica Intel, control+alt+seta
  (esquerda/direita/cima/baixo) são comandos para modificar a orientação do
  ecrã. Estes comandos são activados por defeito e entram em conflito com os
  comandos da Lupa, para mover a vista. Terá de os desactivar para poder
  utilizá-los para o aumento pela Lupa. Podem ser desactivados no painel de
  controlo Intel ou no menu Intel presente no tabuleiro do sistema.
* Dependendo da sua versão do Windows, Alt+Shift+setas são comandos da Lupa
  do Windows para redimensionar a vista ampliada (lente ou ancorada). Quando
  a Lupa está activa (mesmo em modo ecrã inteiro), estes comandos são
  capturados pela lupa e não podem ser passados para a aplicação, mesmo que
  se prima NVDA+F2 antes. Para utilizar estes comandos na aplicação actual,
  é necessário abandonar a Lupa (Windows+Escape) e reabri-la depois
  (Windows++). Por exemplo, no MS Word, para diminuir o nível de título:
  
    * Pressione Windows+Escape para sair da lupa.
    * Pressione Alt+Shift+RightArrow para diminuir o nível de título actual.
    * Pressione Windows++ para reabrir a lupa.

* Para mais informações sobre as funcionalidades e atalhos da lupa, poderá
  consultar as seguintes páginas:

    * [Use a Lupa para tornar as coisas mais fáceis de ver no
      ecrã](https://support.microsoft.com/pt-pt/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * Atalhos de teclado do Windows para acessibilidade[4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Registro de Alterações

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

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/pt-pt/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

[6]:
https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]:
https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

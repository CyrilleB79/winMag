# Lupa do Windows (Windows Magnifier) #

* Autor: Cyrille Bougot
* Compatibilidade com NVDA: 2018.3 e além
* Baixe a [versão estável][1]

Este complemento melhora o uso da Lupa do Windows com NVDA.


## Recursos

* Permite informar o resultado de alguns comandos de teclado nativo da Lupa.
* Permite reduzir os casos em que os comandos de navegação em tabelas entram
  em conflito com os comandos da Lupa.
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

* Relatar movimentos da visualização: controla o que é informado quando você
  move a visualização com os comandos Control+Alt+Setas. As três opções são:
  
    * Desativado: Nada é relatado.
    * Com voz: uma mensagem de voz indica a posição da visualização ampliada
      na dimensão em que a visualização está sendo movida.
    * Com tons: um tom é reproduzido e sua altura indica a posição da
      visualização ampliada na dimensão em que a visualização está sendo
      movida.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the position of the view: allows to define
  the volume of the tones if you have selected to report view moves or
  screen edges with tones.
* Relatar ativação ou desativação: Se marcada, o estado da lupa é informado
  quando você usa os comandos Windows++ ou Windows+Esc para ativá-la ou
  desativá-la.
* Relatar ampliação: Se marcada, o nível de ampliação da Lupa é informado
  quando você usa os comandos de zoom Windows++ ou Windows+-.
* Relatar inversão de cores: Se marcada, o estado de inversão de cores é
  rinformado quando você usa o comando de alternância control+Alt+I.
* Relatar mudança da visualização: Se marcada, o tipo de visualização é
  informado quando você usa um comando que altera o tipo da visualização
  (Control+Alt+M, Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Relatar redimensionamento de lente ou janela acoplada: Se marcada, uma
  mensagem é relatada quando você usa os comandos de redimensionamento
  (Alt+Shift+Setas). No modo de janela acoplada, a altura ou largura é
  informada. No modo de lente, a nova dimensão não pode ser informada por
  enquanto. Estes comandos de redimensionamento não parecem estar
  disponíveis em todas as versões do Windows; se a sua versão do Windows não
  os suportar, você deve manter esta opção desmarcada.
* Em documentos e visualizações de listas, passar atalhos control+alt+setas
  para a Lupa do Windows: Há três opções possíveis:
  
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
    * Sempre: Os comandos Control+Alt+Seta movem a visualização da Lupa em
      qualquer caso. Esta opção pode ser útil se você não usar
      Control+Alt+Seta para navegar em tabela, por exemplo, porque alterou
      os atalhos de navegação em tabelas no NVDA ou porque utiliza
      exclusivamente o complemento [Navegação fácil em tabelas (Easy table
      navigator)][5] para navegação nas tabelas.

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## Comandos adicionados por este complemento

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O depois C: Ativa ou desativa o rastreamento do cursor.
* NVDA+Windows+O depois F: Ativa ou desativa o rastreamento do foco.
* NVDA+Windows+O depois M: Ativa ou desativa o rastreamento do mouse.
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+Windows+O depois S: Ativa ou desativa a suavização.
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes
  (within the edge of the screen or centered on the screen); this feature is
  only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O depois X: Alterna entre os modos de rastreamento do cursor
  de texto (no limite da tela ou centralizado na tela); esse recurso está
  disponível apenas no Windows 10 compilação 18894 ou superior.
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
* NVDA+Windows+O depois O: Abre as configurações do complemento Lupa do
  Windows.
* NVDA+Windows+O depois H: Exibe a ajuda sobre os comandos de camada Lupa.

Não há comando (gesto) direto padrão para cada comando, mas você pode
atribuir um normalmente no diálogo definir comandos (gesto de entrada), se
desejar. Da mesma forma, você também pode modificar ou excluir o gesto de
acesso à camada Lupa (NVDA+Windows+O). Ainda assim, você não pode modificar
a tecla de atalho dos subcomandos da camada Lupa.


## Comandos nativos da Lupa

O resultado dos seguintes comandos nativos da Lupa pode ser relatado por
este complemento, de acordo com sua configuração:

* Iniciar Lupa: Windows++ (no teclado alfanumérico ou no teclado numérico)
* Sair da Lupa: Windows+Esc
* Ampliar: Windows++ (no teclado alfanumérico ou no teclado numérico)
* Diminuir ampliação: Windows+- (no teclado alfanumérico ou no teclado
  numérico)
* Alternar inversão de cores: Control+Alt+I
* Selecionar visualização acoplada: Control+Alt+D
* Selecionar visualização em tela cheia: Control+Alt+F
* Selecionar visualização de lente: Control+Alt+L
* Circuitar através dos três tipos de visualização: Control+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Aqui está também uma lista de outros comandos nativos da Lupa, apenas para
informação:

* Control+Alt+rodinhaDeRolagemDoMouse: Aumenta e diminui a ampliação usando
  a rodinha de rolagem do mouse.
* Control+Windows+M: Abre a janela de configurações da Lupa.
* Control+Alt+R: Redimensiona a lente com o mouse.
* Control+Alt+Espaço: Mostra rapidamente toda a área de trabalho ao usar a
  visualização em tela cheia.

Nenhum dos comandos nativos da Lupa podem ser modificados.


## Notas

* Para computadores equipados com uma placa de vídeo Intel, control+alt+seta
  (esquerda/direita/cima/baixo) também são atalhos para modificar a
  orientação da tela. Esses atalhos são habilitados por padrão e entram em
  conflito com os atalhos da Lupa do Windows para mover a visualização. Você
  precisará desabilitá-los para poder usá-los na Lupa. Eles podem ser
  desabilitados no painel de controle Intel ou no menu Intel presente na
  bandeja do sistema (área de notificação).
* Dependendo da sua versão do Windows, Alt+Shift+Seta são atalhos da Lupa do
  Windows para redimensionar a visualização ampliada (lente ou
  acoplada). Quando a Lupa está ativa (mesmo no modo de tela cheia), esses
  atalhos são capturados pela Lupa e não podem ser passados para o
  aplicativo, mesmo se antes você pressionar NVDA+F2. Para usar esses
  atalhos no aplicativo atual, você precisa sair da Lupa (Windows+Esc) e
  reabri-la depois (Windows++). Por exemplo, no Ms Word, para diminuir o
  nível do título:
  
    * Pressione Windows+Esc para sair da Lupa.
    * Pressione Alt+Shift+SetaParaDireita para diminuir o nível do título
      atual.
    * Pressione Windows++ para reabrir a Lupa.

* Para mais informações sobre os recursos e atalhos da Lupa do Windows, pode
  consultar as seguintes páginas:

    * [Usar a Lupa para facilitar a visualização dos itens na
      tela](https://support.microsoft.com/pt-br/windows/usar-a-lupa-para-facilitar-a-visualiza%C3%A7%C3%A3o-dos-itens-na-tela-414948ba-8b1c-d3bd-8615-0e5e32204198)
    * [Atalhos de teclado de acessibilidade do Windows][4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Registro de alterações (Change log)

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

[4]: https://support.microsoft.com/pt-br/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.pt_BR.html

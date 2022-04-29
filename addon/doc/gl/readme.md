# Windows Magnifier #

* Autor: Cyrille Bougot
* Compatibilidade con NVDA: 2018.3 en diante
* Descargar  [versión estable][1]
* Descargar [versión de desenvolvemento][2]

Este complemento mellora o uso da Lupa de Windows (Windows Magnifier) con
NVDA.


## Características

* Permite anunciar o resultado de certos atallos nativos da lupa.
* Permite reducir os casos nos que as ordes de navegación por táboas fan
  conflicto con atallos da Lupa.
* Adds some keyboard shortcuts to toggle various native options of the
  Magnifier.
* Adds some extra features that are not provided by Windows Magnifier (mouse
  to view, Magnifier window not on top)

## Opcións

O panel de opcións do complemento Windows Magnifier permite configurar como NVDA reacciona ás ordes da Lupa nativa de Windows.
Poderías querer que se anuncien máis ou menos ordes segundo o que sexas capaz de ver.
Este panel pódese abrir escollendo Preferencias > Opcións no menú de NVDA e seleccionando despois a categoría Windows Magnifier na ventá de Opcións.
O atallo NVDA+Windows+O logo O tamén permite abrir este panel de opcións directamente.

O panel contén as seguintes opcións:

* Anunciar movementos da vista: controla o que se anuncia cando moves a
  vista coas ordes Control+Alt+Frechas. As tres opcións son:
  
    * Desactivado: Non se anuncia nada.
    * Con voz: unha mensaxe de voz indica a posición da vista ampliada na
      dimensión na que se está a mover a vista.
    * Con tons: reprodúcese un ton e a súa altura indica a posición da vista
      ampliada na dimensión na que se está a mover a vista.
  
  This option does not affect docked view mode.

* Report screen edges: controls what is reported when you reach the edges of
  the screen while moving the view with Control+Alt+Arrows commands.  The
  three options are: Off, With speech and With tones.  This option does not
  affect docked view mode.
* Volume of the tones reporting the view position: allows to define the
  volume of the tones if you have selected to report view moves or screen
  edges with tones.
* Anunciar activación e desactivación: Se está marcado, o estado da Lupa
  anúnciase cando utilizas as ordes Windows++ ou Windows+Escape para
  activala ou desactivala.
* Anunciar zoom: Se está marcada, o nivel de zoom da Lupa anúnciase cando
  utilizas as ordes de zoom Windows++ e windows+-.
* Anunciar inversión de cores: Se está marcada, o estado da inversión de
  cores anúnciase cando utilizas a orde alternadora control+Alt+I.
* Anunciar cambio de vista: Se está marcada, o tipo de vista anúnciase cando
  utilizas unha orde que cambia o tipo de vista (control+Alt+M,
  Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Anunciar redimensionamento de ventá de lupa ou acoplado: Se está marcada,
  anúnciase unha mensaxe cando utilizas as ordes de redimensionamento
  (Alt+Shift+Frechas).  No modo de ventá acoplado, repórtase o alto ou o
  ancho.  No modo lente, non se pode anunciar a nova dimensión por agora.
  Estas ordes de redimensionamento non parecen estar dispoñibles en tódalas
  versións de Windows; se a túa versión de Windows non as soporta, deberías
  deixar esta opción desmarcada.
* En vistas de &documentos e lista, pasar as ordes control+alt+frechas á
  Lupa de Windows: Hai tres posibles escollas:
  
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
    * Sempre: Os atallos de control+Alt+Frecha moven a vista da Lupa en
      calquera caso.  Esta opción podería ser útil se non utilizas
      Control+Alt+Frecha para navegar en táboa, p.ex. porque cambiaches as
      ordes de navegación por táboas en NVDA ou porque utilizas
      exclusivamente [Easy table navigator][5] para navegación por táboas.


## Ordes engadidas por este complemento

In addition to native Magnifier commands, this add-on provide additional
commands:

* Commands that allow to control Magnifier's options without opening its
  configuration page.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O logo C: Activa ou desactiva seguemento do cursor.
* NVDA+Windows+O logo F: Activa ou desactiva seguemento do foco.
* NVDA+Windows+O logo M: Activa ou desactiva seguemento do rato.
* NVDA+Windows+O logo T: Activa ou desactiva o seguemento a nivel global.
* NVDA+Windows+O logo S: Activa ou desactiva o suavizado.
* NVDA+Windows+O logo R: Alterna entre os modos de seguemento do rato
  (dentro do borde da pantalla ou centrado na pantalla); esta característica
  só está dispñible en Windows 10 compilación 17643 ou superior.
* NVDA+Windows+O logo X: Alterna entre os modos de seguemento do cursor de
  texto (dentro do borde da pantalla ou centrado na pantalla); esta
  característica só está dispñible en Windows 10 compilación 18894 ou
  superior.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O then W: Switches on or off the mode keeping Windows
  Magnifier's control window always on top of the other ones.  This feature
  is only available for installed versions of NVDA.
* NVDA+Windows+O logo O: Abre as opcións do complemento Windows Magnifier.
* NVDA*Windows+O logo H: Amosa axuda sobre as ordes da capa da Lupa.

Non hai un xesto directo predeterminado para cada orde, pero podes
atribuírlles un normalmente no diálogo de xestos de entrada se o desexas.
Da mesma maneira, podes modificar ou eliminar o xesto de acceso á capa da
Lupa (NVDA+Windows+O).  Porén, non podes modificar as teclas de atallo dos
subordes da capa da Lupa.


## Ordes nativas da Lupa

O resultado das seguintes ordes nativas da Lupa pódeo anunciar este
complemento, de acordo coa súa configuración:

* Iniciar Lupa: windows++ (no teclado alfanumérico ou numérico)
* Saír da Lupa: windows+Escape
* Achegar (zoom-in): Windows++ (no teclado alfanumérico ou numérico)
* Afastar (zoom-out): Windows+- (no teclado alfanumérico ou numérico)
* Activar ou desactivar inversión de cor: Control+Alt+I
* Seleccionar vista acoplada: Control+Alt+D
* Seleccionar vista en pantalla completa: Control+Alt+F
* Seleccionar vista lente: Control+Alt+L
* Recorrer os tres tipos de vista: Control+Alft+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Aquí está tamén unha lista de outras ordes nativas da Lupa, só para
información:

* Control+Alt+Roda de desprazamento do rato: Achega e afasta utilizando a
  roda de desprazamento do rato.
* Control+Windows+M: Abre a ventá de configuración da Lupa.
* Control+Alt+R: Redimensiona a lente co rato.
* Control+Alt+Espazo: Amosa rapidamente todo o escritorio cando se utilice a
  vista de pantalla completa.

Ningunha das ordes nativas da Lupa se poden modificar.


## Notas

* Para ordenadores equipados cunha tarxeta gráfica Intel, Control+Alt+frecha
  (esquerda/dereita/arriba/abaixo) tamén son atallos para modificar a
  orientación da pantalla.  Estas ordes están habilitadas por defecto e fan
  conflicto coas da Lupa de Windows para mover a vista.  Necesitarás
  deshabilitalas para poder utilizalas para a Lupa.  Pódense deshabilitar no
  Panel de Control Intel ou no Menú Intel presente na bandexa sistema.
* Dependendo da túa versión de windows, Alt+Shift+Frecha son ordes da Lupa
  de windows para redimensionar a vista da Lupa (lente ou acoplada).  Cando
  a Lupa está activa (mesmo en modo de pantalla completa), estas ordes
  captúraas a Lupa e non se poden pasar á aplicación, aínda que premas
  NVDA+F2 antes.  Para usar estes atallos na aplicación actual, necesitas
  saír da Lupa (Windows+Escape) e reabrila despois (windows++).  Por
  exemplo, en Microsoft Word, para reducir o nivel de título:
  
    * Preme Windows+Escape para saír da Lupa.
    * Preme Alt+Shift+Frecha Dereita para reducir o nivel do título actual.
    * Preme windows++ para reabrir a Lupa.

* Para máis información sobre as características e as ordes da Lupa de
  Windows, poderías querer consultar as seguintes páxinas:

    * [Use Magnifier to make things on the screen easier to see (Utilizando
      a Lupa para facer que as cousas en pantalla sexan máis fáciles de
      ver)](https://support.microsoft.com/en-us/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Windows keyboard shortcuts for accessibility (Atallos de teclas de
      Windows para a accesibilidade)][4]

* This add-on has not been tested in multi-screen environment and there are
  chances that some feature are not working in this environment.  If you are
  using multi-screen environment and want it to be supported, please contact
  me to have it implemented.
* More generally, do not hesitate to contact me on the [GitHub page][3] of
  this add-on or directly by e-mail.


## Rexistro de trocos

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

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

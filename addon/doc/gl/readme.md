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
* Engade algúns atallos de teclado para alternar certas opcións nativas da
  Lupa.
* Allow to save and restore the configuration parameters of the Magnifier.
* Engade algunhas características extra que non proporciona a Lupa de
  Windows (rato á vista, xanela da Lupa non en primeiro plano)

## Opcións

The setting panel of Windows Magnifier add-on allows to configure how NVDA
reacts to native Windows Magnifier commands.  You may want to have more or
less commands reported according to what you are able to see.  The panel
also contains an option to modify the behaviour of Windows Magnifier control
window.

This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window.
The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.

O panel contén as seguintes opcións:

* Anunciar movementos da vista: controla o que se anuncia cando moves a
  vista coas ordes Control+Alt+Frechas. As tres opcións son:
  
    * Desactivado: Non se anuncia nada.
    * Con voz: unha mensaxe de voz indica a posición da vista ampliada na
      dimensión na que se está a mover a vista.
    * Con tons: reprodúcese un ton e a súa altura indica a posición da vista
      ampliada na dimensión na que se está a mover a vista.
  
  Esta opción non afecta ó modo de vista acoplada.

* Anunciar bordes da pantalla: controla que se anuncia cando chegas ós
  bordes da pantalla mentres moves a vista coas ordes Control+Alt+Frechas.
  As tres opcións son: desactivado, con voz ou con tons.  Esta opción non
  afecta ó modo de vista acoplada.
* Volume of the tones reporting the position of the view: allows to define
  the volume of the tones if you have selected to report view moves or
  screen edges with tones.
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
  
    * Nunca: A orde non se pasa á Lupa de Windows e pode operar a navegación
      de táboa estándar de NVDA.  Cando se use en documentos fóra dunha
      táboa, o atallo Control+Alt+Frecha anuncia unha mensaxe de erro de
      "non estás nunha celda da táboa".  Éste é o comportamento estándar de
      NVDA sen este complemento.
    * Só cando non estea nunha táboa: en vistas de táboa ou lista, os
      atallos de Control+Alt+Frecha realizan navegación por táboa estándar.
      Cando se utilicen en documento fóra dunha táboa, os atallos de
      Control+Alt+Frecha realizan ordes estándar de mover vista da Lupa.  Se
      aínda desexas mover a vista da Lupa de windows mentres estás en vista
      de táboa ou lista, terás que premer NVDA+F2 antes de utilizar os
      atallos de Control+Alt+Frecha.  Esta opción é a mellor ponderación se
      queres utilizar Control+Alt+Frecha tanto para a Lupa como para
      navegación por táboas.
    * Sempre: Os atallos de control+Alt+Frecha moven a vista da Lupa en
      calquera caso.  Esta opción podería ser útil se non utilizas
      Control+Alt+Frecha para navegar en táboa, p.ex. porque cambiaches as
      ordes de navegación por táboas en NVDA ou porque utilizas
      exclusivamente [Easy table navigator][5] para navegación por táboas.

* Keep Windows Magnifier command window always on top: If unchecked, the
  Magnifier's control window will not be kept always on top of other
  windows.

## Ordes engadidas por este complemento

Ademais dos atallos da Lupa nativa, este complemento fornece ordes
adicionais:

* Ordes que permiten controlar as opcións da Lupa sen abrir a súa páxina de
  configuración.
* Ordes adicionais específicas deste complemento.

Todas estas ordes adicionais son accesibles a través da orde de capa da Lupa
NVDA+Windows+O:

* NVDA+Windows+O logo C: Activa ou desactiva seguemento do cursor.
* NVDA+Windows+O logo F: Activa ou desactiva seguemento do foco.
* NVDA+Windows+O logo M: Activa ou desactiva seguemento do rato.
* NVDA+Windows+O then T: Toggles on or off tracking globally.  When tracking
  is toggled on again, it is set to the last active tracking configuration
  before tracking was toggled off.
* NVDA+Windows+O logo S: Activa ou desactiva o suavizado.
* NVDA+Windows+O then R: Switches between mouse pointer tracking modes
  (within the edge of the screen or centered on the screen); this feature is
  only available on Windows 10 build 17643 or higher.
* NVDA+Windows+O logo X: Alterna entre os modos de seguemento do cursor de
  texto (dentro do borde da pantalla ou centrado na pantalla); esta
  característica só está dispñible en Windows 10 compilación 18894 ou
  superior.
* NVDA+Windows+O then shift+P: Saves the current configuration parameters of
  the magnifier to NVDA's configuration.
* NVDA+Windows+O then P: Restores the current configuration parameters of
  the magnifier from NVDA's configuration.  If no configuration parameters
  has been previously saved to NVDA's configuration, the default
  configuration parameters of Windows Magnifier are restored instead.
* NVDA+Windows+O logo frechas: Mover a vista da Lupa.
* NVDA+Windows+O LOGO V: Move o cursor do rato ó centro da vista da Lupa
  (orde non dispoñible en vista acoplada).
* NVDA+Windows+O then W: Switches on or off the mode allowing to keep
  Windows Magnifier's control window always on top of the other ones.  This
  feature is only available for installed versions of NVDA.
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
* Redimensionar a lente co teclado:
  Shift+Alt+FrechaEsquerda/Dereita/Arriba/Abaixo Nota: Aínda que isto non
  parece estar documentado, este atallo parece que foi retirado en versións
  de Windows recentes como Windows 10 2004.
* Mover a vista da Lupa: Control+Alt+Frechas

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

* Este complemento non se probou nun entorno multipantalla e podería ser que
  algunhas características non funcionasen neste entorno.  Se estás
  utilizando un entorno multipantalla e queres que se soporte, por favor
  contáctame para implementalo.
* Máis en xeral, non dubides en contactarme na [páxina de gitHub][3] deste
  complemento ou directamente por correo electrónico.


## Rexistro de trocos

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
* Traducións actualizadas.

### Versión 2.0

* A vista pódese mover coas frechas dende a capa de windows Magnifier.
* Capacidade para manter a xanela de ordes da Lupa sempre enriba ou non.
* Engadida a aracterística "Anunciar bordes da pantalla".
* Axuste do volume dos tons ó utilizar ordes de movemento da vistsa.
* As ordes para anunciar cambios de vista e rato á vista agora sopórtanse en
  modo Lente.
* Compatibilidade con NVDA 2022.1.
* Arranxado un erro polo que en ocasións se anunciaba que a lupa non estaba
  funcionando ó chamar ó script.
* A publicación agora faise grazas a unha acción de GitHub no canto de
  appVeyor.
* Traducións actualizadas.

### Versión 1.1

* Traducións engadidas.

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/en-us/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html

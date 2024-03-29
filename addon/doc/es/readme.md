# Lupa de Windows #

* Autor: Cyrille Bougot
* Compatibilidad con NVDA: de 2019.2.1 en adelante
* Descargar [versión estable][1]

Este complemento mejora el uso de la lupa de Windows con NVDA.


## Características

* Permite indicar el resultado de algunas órdenes de teclado nativas de la
  lupa.
* Permite reducir los casos en los que las órdenes de navegación por tablas
  interfieren con las órdenes de la lupa.
* Añade varios atajos de teclado para conmutar ciertas opciones nativas de
  la lupa.
* Se permite guardar y restaurar los parámetros de configuración de la lupa.
* Añade algunas funciones extra que la lupa de Windows no proporciona (ratón
  a la vista, ventana de lupa no siempre visible)

## Opciones

El panel de opciones de la extensión de la lupa de Windows permite
configurar cómo reacciona NVDA ante órdenes nativas de la lupa de
Windows. Puedes querer tener más o menos órdenes indicadas en función de
cuánto seas capaz de ver. El panel también contiene una opción para
modificar el comportamiento de la ventana de control de la lupa de Windows.

Se puede abrir este panel eligiendo Preferencias -> Opciones en el menú de NVDA y seleccionando la categoría Lupa de Windows en la ventana de opciones.
El atajo de teclado NVDA+windows+O seguido de O también permite abrir este panel de opciones directamente.

El panel contiene las siguientes opciones:

* Anunciar movimientos de la vista: controla qué se anuncia al mover la
  vista con las órdenes control+alt+flechas. Las tres opciones son:
  
    * Desactivado: no se anuncia nada.
    * Con voz: un mensaje de voz que indica la posición de la vista
      aumentada en la dimensión en la que se mueve la vista.
    * Con tonos: se reproduce un sonido y su tono indica la posición de la
      vista aumentada en la dimensión en la que se mueve la vista.
  
  Esta opción no afecta al modo de vista acoplada.

* Indicar bordes de la pantalla: controla qué se indica al alcanzar los
  bordes de la pantalla al mover la vista con las órdenes
  control+alt+flechas. Las tres opciones son: desactivado, con voz y con
  pitidos. Esta opción no afecta al modo de vista acoplada.
* Volumen de los pitidos que indican la posición de la vista: permite
  definir el volumen de los pitidos si has elegido indicar los movimientos
  de la vista o bordes de la pantalla con pitidos.
* Anunciar activada o desactivada: si se marca, se anuncia el estado de la
  lupa al utilizar las órdenes Windows++ y Windows+escape para encenderla o
  apagarla.
* Anunciar zoom: si se marca, el nivel de zoom de la lupa se indica al usar
  las órdenes del zoom Windows++ y Windows+-.
* Anunciar inversión de color: si se marca, se anuncia el estado de la
  inversión de color al usar la orden de conmutación control+alt+i.
* Anunciar cambio de vista: si se marca, se anuncia el tipo de vista al usar
  una orden que cambia el tipo de vista (Control+Alt+M, Control+Alt+F,
  Control+Alt+D, Control+Alt+L)
* Anunciar redimensión de la lente o de la ventana acoplada: si se marca,
  aparecerá un mensaje al usar las órdenes de redimensión
  (alt+shift+flechas). En el modo ventana acoplada, se anuncian la altura o
  la anchura. En el modo lente, no se puede anunciar por el momento la nueva
  medida. Estas órdenes de redimensión parecen no estar disponibles en todas
  las versiones de Windows; si tu versión de Windows no las soporta,
  deberías dejar esta opción desmarcada.
* En documentos y vistas de lista, pasar a la lupa los atajos
  control+alt+flechas: hay tres posibles opciones:
  
    * Nunca: la orden nunca se pasa a la lupa de Windows y la navegación
      normal por tablas funciona. Al usarse en documentos fuera de una
      tabla, las órdenes control+alt+flechas indican un mensaje de error "no
      estás en una tabla". Este es el comportamiento estándar de NVDA sin
      este complemento. Todavía puedes usar NVDA+windows+o seguido de
      flechas para mover la vista ampliada.
    * Sólo si no es una tabla: en las tablas y en las listas, las órdenes
      control+alt+flechas realizan una navegación estándar por tablas. Al
      usarse en documentos fuera de una tabla, las órdenes
      control+alt+flechas realizan órdenes estándar de la lupa para mover la
      vista. Si quieres mover la vista de la lupa de Windows mientras estés
      en una lista o tabla, tendrás que pulsar NVDA+f2 antes de usar las
      órdenes control+alt+flechas, o alternativamente usar NVDA+windows+o y
      las flechas. Esta opción es la más equilibrada si quieres usar
      control+alt+flechas tanto en el movimiento de la lupa como en la
      navegación por tablas.
    * Siempre: las órdenes control+alt+flechas mueven la vista de la lupa en
      cualquier caso. Esta opción puede ser útil si no usas
      control+alt+flechas para navegar por tablas, por ejemplo porque has
      modificado los atajos de navegación por tablas en NVDA o porque
      utilizas exclusivamente el complemento [Easy Table Navigator][5] para
      navegar por tablas.

* Mantener ventana de control de la lupa siempre visible: si se desmarca, la
  ventana de control de la lupa no permanecerá siempre por encima de otras
  ventanas.

## Órdenes que añade este complemento

Además de las órdenes nativas de la lupa, este complemento proporciona
órdenes adicionales:

* Órdenes que permiten controlar opciones de la lupa sin abrir su página de
  configuración.
* Órdenes extra específicas de este complemento.

Todas estas órdenes adicionales se encuentran accesibles a través de la
orden de capa de la lupa NVDA+windows+O:

* NVDA+windows+o, c: activa o desactiva el seguimiento del cursor.
* NVDA+windows+o, f: activa o desactiva el seguimiento del foco.
* NVDA+windows+o, m: activa o desactiva el seguimiento del ratón.
* NVDA+windows+o, t: activa o desactiva el seguimiento global. Cuando se
  reactive el seguimiento, se establecerá según la última configuración de
  seguimiento activa antes de apagarlo.
* NVDA+windows+o, s: activa o desactiva el suavizado.
* NVDA+windows+o, r: cambia entre los distintos modos de seguimiento del
  puntero del ratón (dentro de los bordes de la pantalla o centrado en la
  pantalla); esta función sólo está disponible en Windows 10, compilación
  17643 o posterior.
* NVDA+windows+o seguido de x: cambia entre los distintos modos de
  seguimiento del cursor de texto (dentro de los bordes de la pantalla o
  centrado en la pantalla); esta función sólo está disponible en Windows 10,
  compilación 18894 o posterior.
* NVDA+windows+o, shift+p: guarda las opciones de configuración actuales de
  la lupa en la configuración de NVDA.
* NVDA+windows+o, p: restaura las opciones de configuración actuales de la
  lupa desde la configuración de NVDA. Si no se han guardado previamente
  ajustes en la configuración de NVDA, se restauran en su lugar los valores
  por defecto de la lupa.
* NVDA+windows+o seguido de flechas: mueve la vista ampliada.
* NVDA+windows+o seguido de v: mueve el cursor del ratón al centro de la
  vista ampliada (orden no disponible en la vista acoplada).
* NVDA+windows+o seguido de w: activa o desactiva el modo siempre visible de
  la ventana de la lupa sobre otras ventanas. Esta función sólo está
  disponible en versiones instaladas de NVDA.
* NVDA+windows+o seguido de o: abre las opciones del complemento Lupa de
  Windows.
* NVDA+windows+o, h: muestra ayuda sobre las órdenes de capa de la lupa.

No hay un gesto directo por defecto para cada orden, pero se pueden asignar
desde el diálogo Gestos de entrada si lo deseas. Del mismo modo, se puede
editar o eliminar la orden de la capa de la lupa (NVDA+windows+o). Todavía
no se pueden modificar las subórdenes de esta capa.


## Órdenes nativas de la lupa

Este complemento puede verbalizar el resultado de las siguientes órdenes
nativas de la lupa, en función de su configuración:

* Iniciar lupa: windows+más (alfanumérico o del teclado numérico).
* Salir de la lupa: windows+escape
* Acercar: windows+más (de los teclados alfanumérico y numérico).
* Alejar: windows+- (teclados alfanumérico y numérico).
* Conmutar inversión de colores: control+alt+i
* Seleccionar la vista acoplada: control+alt+d
* Seleccionar la vista a pantalla completa: control+alt+f
* Seleccionar la vista lente: control+alt+l
* Pasar cíclicamente por los tres tipos de vista: control+alt+m
* Redimensionar la lente con el teclado: shift+alt+flechas izquierda,
  derecha, arriba o abajo. Nota: aunque no parece estar documentado, parece
  que se ha retirado este atajo en versiones recientes de Windows, como
  Windows 10 2004.
* Mover la vista ampliada: control+alt+flechas

Aquí se encuentra una lista con más órdenes nativas de la lupa, para más
información:

* Control+alt+rueda del ratón: acerca o aleja la lupa usando la rueda del
  ratón.
* Control+windows+m: abre la ventana de configuración de la lupa.
* Control+alt+r: redimensiona la lente con el ratón.
* Control+alt+barra espaciadora: muestra rápidamente el escritorio entero al
  usar la vista de pantalla completa.

Ninguna de las órdenes nativas de la lupa se puede modificar.


## Notas

* En ordenadores equipados con una tarjeta gráfica Intel,
  control+alt+flechas (izquierda, derecha, arriba o abajo) también se
  utilizan como atajos para cambiar la orientación de la pantalla. Estos
  atajos están activados por defecto y hacen conflicto con los atajos de la
  lupa de Windows para mover la vista. Deberás desactivarlos para poder
  usarlos con la lupa. Se pueden deshabilitar en el panel de control de
  Intel o desde el menú de Intel presente en la bandeja del sistema.
* Dependiendo de tu versión de Windows, alt+shift+flechas son atajos de la
  lupa para redimensionar la vista ampliada (lente o acoplada). Cuando la
  lupa está activa (incluso en el modo a pantalla completa), la lupa captura
  estos atajos e impide que pasen a la aplicación, incluso pulsando NVDA+f2
  antes. Para usar estos atajos en la aplicación actual, debes salir de la
  lupa (windows+escape) y reabrirla después (windows+más). Por ejemplo, en
  Microsoft Word, para reducir el nivel de un título:
  
    * Pulsa windows+escape para salir de la lupa.
    * Pulsa alt+shift+flecha derecha para reducir el nivel del título
      actual.
    * Pulsa windows+más para reabrir la lupa.

* Para más información sobre los atajos y características de la lupa de
  Windows, puedes consultar las siguientes páginas:

    * [Utilizar la lupa para facilitar la visualización en la
      pantalla](https://support.microsoft.com/es-es/windows/utilizar-la-lupa-para-facilitar-la-visualizaci%C3%B3n-en-la-pantalla-414948ba-8b1c-d3bd-8615-0e5e32204198)
    * [Accesos directos de teclado de Windows para accesibilidad][4]

* Este complemento no se ha probado en entornos de varias pantallas, por lo
  que hay posibilidades de que algunas características no funcionen. Si usas
  un entorno de varias pantallas y quieres que se soporte, contacta conmigo
  para que lo implemente.
* De manera más general, no dudes en contactar conmigo en la [página de
  GitHub][3] de este complemento, o directamente por correo.


## Registro de cambios

### Versión 3.5

* Prepara la compatibilidad con NVDA 2024.1.
* Resuelve posibles problemas de seguridad relacionados con
  [GHSA-xg6w-23rw-39r8][8] al usar el complemento con versiones antiguas de
  NVDA. Sin embargo, se recomienda usar NVDA 2023.3.3 o posterior.
* Nota: de ahora en adelante, las actualizaciones de traducciones ya no
  aparecerán en el registro de cambios.

### Versión 3.4

* La orden "Mover ratón a la vista" vuelve a funcionar
* Traducciones actualizadas.

### Versión 3.3

* Compatibilidad reducida a NVDA 2019.2.1 y posterior. Las últimas versiones
  compatibles con NVDA 2018.3 son la [3.2][7] (parcialmente compatible) y la
  [1.1][6] (totalmente compatible)
* Corregido un problema con el panel de opciones en NVDA 2019.2.1.

### Versión 3.2

* Se ha eliminado el canal de desarrollo.
* Traducciones actualizadas.

### Versión 3.1

* Corregido un problema que impedía que la ventana de control de la lupa se
  restaurara en la parte superior.
* Corregido un problema que impedía ejecutar el complemento en NVDA
  2019.2.1.
* Traducciones actualizadas.

### Versión 3.0

* Ahora se anuncia el nuevo nivel de ampliación al pulsar los botones de
  zoom en la ventana de la lupa (con el teclado).
* El parámetro que controla si la ventana de control de la lupa permanece
  siempre visible ahora se guarda en la configuración. Esto significa que
  este parámetro se recuerda cuando se reinicia NVDA y puede habilitarse o
  no dependiendo del perfil activo.
* Se ha corregido un fallo que causaba una desactivación inesperada de la
  cortina de pantalla al usar las órdenes mover a la vista o mover vista.
* Ahora, se respetará la opción Siempre visible al cambiar el modo de
  ampliación.
* Se ha añadido la posibilidad de guardar y restaurar la configuración de la
  lupa de Windows en la configuración de NVDA.
* Compatibilidad con NVDA 2023.1.
* Se aclara qué tipo de seguimiento se reactiva cuando se vuelve a activar
  el seguimiento.
* Traducciones actualizadas.

### Versión 2.0

* Se puede mover la vista con las flechas mientras estés en la capa de la
  lupa de Windows.
* Posibilidad de mantener la ventana de órdenes de la lupa siempre visible o
  no.
* Añadida función "Indicar bordes de la pantalla".
* Ajuste del volumen de los pitidos al usar las órdenes para mover la vista.
* Las órdenes para indicar los movimientos de la vista y ratón a vista se
  soportan en el modo lente.
* Compatibilidad con NVDA 2022.1.
* Corregido un problema por el que se anunciaba incorrectamente que la lupa
  no funcionaba al llamar a un script.
* La liberación ahora se realiza mediante una acción de GitHub en lugar de
  AppVeyor.
* Traducciones actualizadas.

### Versión 1.1

* Nuevos idiomas añadidos.

### Versión 1.0

* Versión inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/es-es/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.es.html

[6]:
https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]:
https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994

# Loupe Windows #

* Auteur: Cyrille Bougot
* Compatibilité NVDA: 2018.3 et ultérieure
* Télécharger [version stable][1]
* Télécharger [version de développement][2]

Cette extension améliore l'utilisation de la loupe Windows avec NVDA.


## Fonctionnalités

* Permet d'annoncer le résultat de certaines commandes clavier natives de la
  Loupe.
* Permet de réduire les cas où les commandes de navigation dans les tableaux
  entre en conflit avec les commandes de la loupe.
* Ajout de raccourcis clavier pour basculer entre diverses options natives
  de la loupe.
* Ajoute quelques fonctionnalités supplémentaires qui ne sont pas fournies
  par la loupe Windows (souris pour afficher, fenêtre de la loupe pas en
  haut)

## Paramètres

Le panneau des paramètres de l'extension Loupe Windows permet de configurer la façon dont NVDA réagit aux commandes natives de la Loupe Windows.
Vous voudrez peut-être avoir plus ou moins de commandes annoncées en fonction de ce que vous pouvez voir.
On ouvre ce panneau en choisissant Préférences -> Paramètres dans le menu NVDA, puis en sélectionnant la catégorie Loupe Windows dans la fenêtre Paramètres.
Le raccourci clavier NVDA+Windows+O puis O permet également d'ouvrir directement ce panneau de paramètres.

Le panneau contient les options suivantes :

* Annoncer les déplacements de la vue : contrôle ce qui est annoncée lorsque
  vous déplacez la vue avec les commandes Ctrl+Alt+Flèches. Les trois
  options sont :
  
    * Désactivé : rien n'est annoncé.
    * Avec la parole : un message parlé indique la position de la vue
      agrandie le long de la dimension dans laquelle la vue est déplacée.
    * Avec des sons : des sons sont émis et leur hauteur indique la position
      de la vue agrandie sur la dimension le long de laquelle la vue est
      déplacée.
  
  This option does not affect docked view mode.

* Annoncer les bords de l'écran : contrôle ce qui est signalé lorsque vous
  atteignez les bords de l'écran tout en déplaçant la vue avec les commandes
  Contrôle+Alt+Flèches. Les trois options sont : Désactivé, Avec parole et
  Avec tonalités. Cette option n'affecte pas le mode d'affichage ancré.
* Volume des tonalités signalant la position de la vue : permet de définir
  le volume des tonalités si vous avez choisi de signaler les mouvements de
  vue ou les bords d'écran avec des tonalités.
* Annoncer l'activation ou la désactivation : si cette option est cochée,
  l'état de la Loupe est signalé lorsque vous utilisez les commandes
  Windows++ ou Windows+Échap pour l'activer ou la désactiver.
* Annoncer le grossissement : si cette option est cochée, le niveau de
  grossissement de la Loupe est annoncé lorsque vous utilisez les commandes
  de grossissement Windows++ ou Windows+-.
* Annoncer l'inversion des couleurs : si cette option est cochée, l'état
  d'inversion des couleurs est annoncé lorsque vous utilisez la commande de
  modification Ctrl+Alt+I.
* Annoncer le changement d'affichage : si cette option est coché, le type
  d'affichage est annoncé lorsque vous utilisez une commande qui modifie le
  type d'affichage (Contrôle+Alt+M, Contrôle+Alt+F, Contrôle+Alt+D,
  Contrôle+Alt+L)
* Annoncer le redimensionnement de l'objectif ou de la fenêtre ancrée : Si
  cette option est cochée, un message est annoncé lorsque vous utilisez les
  commandes de redimensionnement (Alt+Maj+Flèches). En mode fenêtre ancrée,
  la hauteur ou la largeur est annoncée. En mode objectif, la nouvelle
  dimension ne peut pas être annoncée pour l'instant. Ces commandes de
  redimensionnement ne semblent pas être disponibles sur toutes les versions
  de Windows ; si votre version de Windows ne les prend pas en charge, vous
  devez laisser cette option décochée.
* Dans les documents et les vues de liste, passer les raccourcis
  Ctrl+alt+flèches à la Loupe Windows : Il y a trois choix possibles :
  
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
    * Toujours : les commandes Ctrl+Alt+Flèche déplacent la vue de la Loupe
      dans tous les cas. Cette option peut être utile si vous n'utilisez pas
      Ctrl+Alt+Flèche pour naviguer dans les tableaux, par exemple parce que
      vous avez modifié les raccourcis de navigation dans les tableaux dans
      NVDA ou parce que vous utilisez exclusivement l'extension [Easy table
      navigator][5] pour la navigation dans les tableaux.


## Commandes ajoutées par cette extension

En plus des commandes natives de la loupe, cette extension fournit des
commandes supplémentaires :

* Commandes permettant de contrôler les options de la Loupe sans ouvrir sa
  page de configuration.
* Extra commands specific to this add-on.

All these additional commands are accessible through the Magnifier layer
command NVDA+Windows+O:

* NVDA+Windows+O puis C: active ou désactive le suivi du curseur.
* NVDA+Windows+O puis F: active ou désactive le suivi du focus.
* NVDA+Windows+O puis M: active ou désactive le suivi de la souris.
* NVDA+Windows+O puis T: active ou désactive le suivi de manière générale.
* NVDA+Windows+O puis S: active ou désactive le lissage.
* NVDA+Windows+O puis R: Bascule entre les modes de suivi de la souris
  (entre les bords de l'écran ou centré sur l'écran); cette fonctionnalité
  n'est disponible que sous Windows 10 build 17643 ou supérieur.
* NVDA+Windows+O puis X: Bascule entre les modes de suivi du curseur de
  texte (entre les bords de l'écran ou centré sur l'écran); cette
  fonctionnalité n'est disponible que sous Windows 10 build 18894 ou
  supérieur.
* NVDA+Windows+O then Arrows: Move the magnified view.
* NVDA+Windows+O then V: Moves the mouse cursor in the center of the
  magnified view (command not available in docked view mode).
* NVDA+Windows+O puis W : active ou désactive le mode en gardant la fenêtre
  de contrôle de la loupe Windows toujours au-dessus des autres. Cette
  fonctionnalité n'est disponible que pour les versions installées de NVDA.
* NVDA+Windows+O puis O : Ouvre les paramètres de l'extension Loupe Windows.
* NVDA+Windows+O puis H: affiche l'aide sur les commandes séquentielles de
  la Loupe.

Il n'y a pas de geste direct par défaut pour chacune des commande, mais vous
pouvez en attribuer un normalement dans la boîte de dialogue des gestes de
commande si vous le souhaitez. De la même manière, vous pouvez également
modifier ou supprimer le raccourci clavier d'accès aux commandes
séquentielles de la Loupe (NVDA+Windows+O). Cependant, vous ne pouvez pas
modifier les touches de raccourci des sous-commandes de la Loupe.


## Commandes natives de la Loupe

Le résultat des commandes suivantes de la Loupe peut être annoncé par cette
extension, selon sa configuration :

* Démarrer la loupe: Windows++ (sur un clavier alphanumérique ou sur un pavé
  numérique)
* Quitter la loupe: Windows+Échap
* Zoom avant: Windows++ (sur clavier alphanumérique ou pavé numérique)
* Zoom arrière: Windows+- (sur clavier alphanumérique ou sur pavé numérique)
* Activer ou désactiver l'inversion des couleurs: Ctrl+Alt+I
* Sélectionnez l'affichage ancré: Ctrl+Alt+D
* Sélectionnez l'affichage plein écran: Ctrl+Alt+F
* Sélectionnez l'affichage objectif (anciennement affichage loupe):
  Ctrl+Alt+L
* Parcourir les trois types d'affichage: Ctrl+Alt+M
* Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow Note:
  although this does not seem to be documented, this shortcut seems to have
  been withdrawn in recent Windows versions such as Windows 10 2004.
* Move the magnified view: Control+Alt+Arrows

Voici également une liste d'autres commandes natives de la Loupe, juste à
titre informatif:

* Ctrl+Alt+rouletteDeDéfilementSouris: Zoom avant et arrière à l'aide de la
  roulette de défilement de la souris.
* Contrôle+Windows+M: Ouvre la fenêtre des paramètres de la Loupe.
* Ctrl+Alt+R: redimensionner l'objectif à l'aide de la souris.
* Contrôle+Alt+Espace: affiche rapidement l'ensemble du bureau en affichage
  plein écran.

Aucune des commandes natives de la Loupe ne peut être modifiée.


## Remarques

* Pour les ordinateurs équipés d'une carte graphique Intel,
  contrôle+alt+Flèche (gauche / droite / haut / bas) sont également des
  raccourcis pour modifier l'orientation de l'écran. Ces raccourcis sont
  activés par défaut et entrent en conflit avec les raccourcis de la loupe
  Windows pour déplacer la vue. Vous devrez les désactiver pour pouvoir les
  utiliser pour la Loupe. Ils peuvent être désactivés dans le panneau de
  configuration Intel ou dans le menu Intel présent dans la zone de
  notification.
* Selon votre version de Windows, Alt+Maj+Flèche sont des raccourcis de la
  Loupe Windows pour redimensionner la loupe (affichage objectif ou
  ancré). Lorsque la Loupe est active (même en mode plein écran), ces
  raccourcis sont capturés par la Loupe et ne peuvent pas être transmis à
  l'application, même si vous appuyez sur NVDA+F2 auparavant. Pour utiliser
  ces raccourcis dans l'application courante , vous devez quitter la Loupe
  (Windows+Échap) et la rouvrir après (Windows++). Par exemple dans MS Word,
  pour diminuer le niveau du titre:
  
    * Appuyez sur Windows+Échap pour quitter la Loupe.
    * Appuyez sur Alt+Maj+FlècheDroite pour diminuer le niveau de titre
      courant.
    * Appuyez sur Windows++ pour rouvrir la loupe.

* Pour plus d'informations sur les fonctionnalités et les raccourcis de la
  Loupe Windows, vous pouvez consulter les pages suivantes:

    * [Utiliser la Loupe pour mieux voir les éléments à
      l'écran](https://support.microsoft.com/fr-fr/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * [Raccourcis clavier d'accessibilité dans Windows][4]

* Cette extension n'a pas été testée dans un environnement multi-écran et il
  est possible que certaines fonctionnalités ne fonctionnent pas dans cet
  environnement. Si vous utilisez un environnement multi-écran et que vous
  souhaitez qu'il soit pris en charge, veuillez me contacter pour
  l'implémenter.
* Plus généralement, n'hésitez pas à me contacter sur la [page GitHub][3] de
  cet add-on ou directement par e-mail.


## Journal des modifications

### Version 2.0

* La vue peut être déplacée avec les flèches dans la couche de la loupe
  Windows.
* Possibilité de garder la fenêtre des commandes de la loupe toujours en
  haut ou non.
* Ajout de la fonctionnalité "Signaler les bords de l'écran".
* Réglage du volume des tonalités lors de l'utilisation des commandes de
  déplacement de vue.
* Les déplacements de vue de rapport et les commandes de souris pour
  afficher sont désormais pris en charge en mode Objectif.
* Compatibilité avec NVDA 2022.1.
* Correction d'un bogue qui signalait parfois à tort que la loupe ne
  fonctionnait pas lors d'un appel de script.
* La release est maintenant effectuée grâce à une action GitHub au lieu
  d'appVeyor.
* Localisations mises à jour.

### Version 1.1

* Localisations ajoutées.

### Version 1.0

* Première version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[3]: https://github.com/CyrilleB79/winMag

[4]: Raccourcis clavier d'accessibilité dans Windows

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.fr.html

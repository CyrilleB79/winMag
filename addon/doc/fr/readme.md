# Loupe Windows #

* Auteur: Cyrille Bougot
* Compatibilité NVDA: 2018.3 et ultérieure
* Télécharger [version stable][1]

Cette extension améliore l'utilisation de la loupe Windows avec NVDA.


## Fonctionnalités

* Permet d'annoncer le résultat de certaines commandes clavier natives de la
  Loupe.
* Permet de réduire les cas où les commandes de navigation dans les tableaux
  entre en conflit avec les commandes de la loupe.
* Ajout de raccourcis clavier pour basculer entre diverses options natives
  de la loupe.
* Permet de sauvegarder et de restaurer les paramètres de configuration de
  la Loupe.
* Ajoute quelques fonctionnalités supplémentaires qui ne sont pas fournies
  par la loupe Windows (souris au centre de la vue, fenêtre de la loupe pas
  au dessus)

## Paramètres

Le panneau des paramètres de l'extension Loupe Windows permet de configurer
la façon dont NVDA réagit aux commandes natives de la Loupe Windows. Vous
voudrez peut-être avoir plus ou moins de commandes annoncées en fonction de
ce que vous pouvez voir.  Le panneau contient également une option pour
modifier le comportement de la fenêtre de contrôle de la loupe Windows.

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
  
  Cette option n'affecte pas le mode d'affichage ancré.

* Annoncer les bords de l'écran : contrôle ce qui est signalé lorsque vous
  atteignez les bords de l'écran tout en déplaçant la vue avec les commandes
  Contrôle+Alt+Flèches. Les trois options sont : Désactivé, Avec parole et
  Avec des sons. Cette option n'affecte pas le mode d'affichage ancré.
* Volume des sons indiquant la position de la vue : permet de définir le
  volume des sons si vous avez choisi de signaler les mouvements de la vue
  ou les bords de l'écran avec des sons.
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
  
    * Jamais : la commande n'est pas transmise à la Loupe Windows et la
      navigation standard de NVDA dans les tableaux peut fonctionner.
      Utilisée dans les documents hors des tableaux, la commande
      Ctrl+Alt+Flèche annoncent un message d'erreur « Pas dans un
      tableau ».  C'est le comportement habituel de NVDA sans cette
      extension.  Vous pouvez toujours utiliser NVDA+Windows+O puis les
      flèches pour déplacer la vue agrandie.
    * Seulement en dehors des tableaux : Dans les tableaux ou les vues de
      liste, les commandes Ctrl+Alt+Flèche effectuent la navigation
      habituelle dans les tableaux.  Utilisées dans les documents en dehors
      des tableaux, les commandes Ctrl+Alt+Flèche exécutent les commandes
      habituelles de déplacement de la vue de la Loupe.  Si vous souhaitez
      malgré tout déplacer la vue de la Loupe Windows alors que vous êtes
      dans un tableau ou une vue de liste, vous devrez appuyer sur NVDA+F2
      avant d'utiliser les commandes Ctrl+Alt+Flèche ou alors utiliser
      NVDA+Windows+O puis les flèches.  Cette option est le meilleur
      compromis si vous souhaitez utiliser Ctrl+Alt+Flèche à la fois pour la
      Loupe et la navigation dans les tableaux.
    * Toujours : les commandes Ctrl+Alt+Flèche déplacent la vue de la Loupe
      dans tous les cas. Cette option peut être utile si vous n'utilisez pas
      Ctrl+Alt+Flèche pour naviguer dans les tableaux, par exemple parce que
      vous avez modifié les raccourcis de navigation dans les tableaux dans
      NVDA ou parce que vous utilisez exclusivement l'extension [Easy table
      navigator][5] pour la navigation dans les tableaux.

* Conserver la fenêtre de commande de la loupe Windows toujours au dessus :
  si cette case n'est pas cochée, la fenêtre de commande de la loupe ne sera
  pas toujours gardée au-dessus des autres fenêtres.

## Commandes ajoutées par cette extension

En plus des commandes natives de la loupe, cette extension fournit des
commandes supplémentaires :

* Commandes permettant de contrôler les options de la Loupe sans ouvrir sa
  page de configuration.
* Commandes supplémentaires spécifiques à cette extension.

Toutes ces commandes supplémentaires sont accessibles via l'accès aux
commandes séquentielles de la Loupe NVDA+Windows+O :

* NVDA+Windows+O puis C: active ou désactive le suivi du curseur.
* NVDA+Windows+O puis F: active ou désactive le suivi du focus.
* NVDA+Windows+O puis M: active ou désactive le suivi de la souris.
* NVDA+Windows+O puis T : Active ou désactive le suivi global. Lorsque le
  suivi est réactivé, il est défini sur la dernière configuration de suivi
  active avant la désactivation du suivi.
* NVDA+Windows+O puis S: active ou désactive le lissage.
* NVDA+Windows+O puis R: Bascule entre les modes de suivi du pointeur de la
  souris (entre les bords de l'écran ou centré sur l'écran); cette
  fonctionnalité n'est disponible que sous Windows 10 build 17643 ou
  supérieur.
* NVDA+Windows+O puis X: Bascule entre les modes de suivi du curseur de
  texte (entre les bords de l'écran ou centré sur l'écran); cette
  fonctionnalité n'est disponible que sous Windows 10 build 18894 ou
  supérieur.
* NVDA+Windows+O puis maj+P : Enregistre les paramètres de configuration
  actuels de la loupe dans la configuration de NVDA.
* NVDA+Windows+O puis P : Restaure les paramètres de configuration actuels
  de la loupe à partir de la configuration de NVDA. Si aucun paramètre de
  configuration n'a été précédemment enregistré dans la configuration de
  NVDA, les paramètres de configuration par défaut de la Loupe Windows sont
  restaurés à la place.
* NVDA+Windows+O puis Flèches : Déplacer la vue agrandie.
* NVDA+Windows+O puis V : Déplace le curseur de la souris au centre de la
  vue agrandie (commande non disponible en mode d'affichage ancré).
* NVDA+Windows+O puis W : active ou désactive le mode permettant de garder
  la fenêtre de commande de la loupe Windows toujours au-dessus des
  autres. Cette fonctionnalité n'est disponible que pour les versions
  installées de NVDA.
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

* Démarrer la loupe: Windows++ (sur le clavier alphanumérique ou sur le pavé
  numérique)
* Quitter la loupe: Windows+Échap
* Zoom avant: Windows++ (sur le clavier alphanumérique ou le pavé numérique)
* Zoom arrière: Windows+- (sur le clavier alphanumérique ou sur le pavé
  numérique)
* Activer ou désactiver l'inversion des couleurs: Ctrl+Alt+I
* Sélectionnez l'affichage ancré: Ctrl+Alt+D
* Sélectionnez l'affichage plein écran: Ctrl+Alt+F
* Sélectionnez l'affichage objectif (anciennement affichage loupe):
  Ctrl+Alt+L
* Parcourir les trois types d'affichage: Ctrl+Alt+M
* Redimensionnez la loupe avec le clavier : Maj+Alt+Gauche/Droite/Haut/Bas
  Remarque : bien que cela ne semble pas documenté, ce raccourci semble
  avoir été supprimé dans les versions récentes de Windows telles que
  Windows 10 2004.
* Déplacer la vue agrandie : Ctrl+Alt+Flèches

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
  cette extension ou directement par e-mail.


## Journal des modifications

### Version 3.2

* Suppression du canal de développement.
* Localisations mises à jour.

### Version 3.1

* Correction d'un problème empêchant la fenêtre de commande de la loupe
  d'être restaurée au dessus des autres.
* Correction d'un problème empêchant l'extension de s'exécuter sur NVDA
  2019.2.1.
* Localisations mises à jour.

### Version 3.0

* L'appui sur les boutons de zoom dans la fenêtre de la Loupe (avec le
  clavier) signale maintenant le nouveau niveau de zoom.
* Le paramètre définissant si la fenêtre de contrôle de la loupe reste
  toujours visible est maintenant stocké dans la configuration ; cela
  signifie que ce paramètre est mémorisé lors du redémarrage de NVDA et peut
  être activé ou non selon le profil actif.
* Correction d'un bogue provoquant la désactivation inattendue du rideau
  d'écran lors de l'utilisation des commandes de déplacement vers la vue ou
  de déplacement de la vue.
* Le réglage de l'option toujoursAuDessus sera maintenant honoré également
  lors du changement d'affichage.
* Ajout de la possibilité de sauvegarder et de restaurer la configuration de
  la Loupe Windows dans la configuration de NVDA.
* Compatibilité avec NVDA 2023.1.
* Précision du type de suivi réactivé lorsque le suivi est réactivé.
* Localisations mises à jour.

### Version 2.0

* La vue peut être déplacée avec les flèches dans les commandes
  séquentielles de la loupe Windows.
* Possibilité de garder la fenêtre des commandes de la loupe toujours au
  dessus ou pas.
* Ajout de la fonctionnalité "Signaler les bords de l'écran".
* Réglage du volume des sons lors de l'utilisation des commandes de
  déplacement de vue.
* L'annonce des déplacements de la vue et la commande de déplacement de la
  souris vers la vue pour afficher sont désormais pris en charge en mode
  Objectif.
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

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: Raccourcis clavier d'accessibilité dans Windows

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.fr.html

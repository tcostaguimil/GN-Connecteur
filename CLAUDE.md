# GN-Connecteur — Contexte projet

Node group Geometry Nodes **partagé** (`GN-CONNECTEUR-TEXTE-02`) qui produit
un connecteur d'annotation (callout / info-bulle / pointeur) : une bulle de
texte avec cartouche, reliée par une ligne à un point d'intérêt.

Ce repo n'est pas un addon. C'est la **source de vérité d'un composant
réutilisé par deux addons Blender distincts** :

- **GeoData to Geometry Nodes** (`tcostaguimil/Blender-geodata`) — import
  GeoJSON, met en exergue des communes.
- **Geomapper** (`tcostaguimil/Blender-GeoMapper`) — globe terrestre,
  tracés, marqueurs géographiques.

Chacun appelle ce connecteur pour ses propres besoins. **Les deux addons ne
doivent connaître que le contrat de sockets, jamais l'intérieur du node
group.**

## Contexte de l'utilisateur

- Lixo (Thiago), motion designer / graphic designer senior, 20 ans
  d'expérience, travaille à RTS (broadcast graphics).
- Expert Blender, After Effects, Unreal Engine. Débutant en Python.
- Raisonne volontiers par analogie avec UE5 (widget 2D construit d'abord,
  puis géré en 3D pour le suivi caméra) — analogie utile et pertinente
  pour ce projet.
- **Réponses directes, pas de blabla. Commentaires et labels en français.**

## Contrainte de compatibilité : Blender 4.2 LTS

- **4.2 LTS sur la machine de travail** (contrainte réelle, pas de choix).
- 5.2 LTS sur machine personnelle.
- **Le connecteur doit rester compatible 4.2 LTS.** Avant d'ajouter un
  nœud sorti récemment, vérifier sa version d'introduction dans la doc
  officielle. Vérifié : `Active Camera` est arrivé en 4.1, donc OK.

## Décisions d'architecture verrouillées

1. **Construction à la main dans l'éditeur de nœuds.** Pas de génération
   procédurale par script (`bpy.data.node_groups.new()` nœud par nœud).
   Même raison que la décision n°4 de Blender-geodata : le code de
   génération est fragile, sans retour visuel, et casse le plaisir de
   designer. Les échanges se font via des exports "Copy as Python" servant
   de **matière à analyse**, jamais de source à exécuter.

2. **Séparation stricte LOCAL / MONDE** — le principe directeur du graphe.
   - **LOCAL ("widget 2D")** : tout ce qui construit le visuel (texte,
     cartouche, ligne de connecteur, alignement, marges). Rien ici ne doit
     lire `Object Info` ni `Active Camera`.
   - **MONDE ("placement 3D")** : une seule étape finale qui positionne le
     widget à l'ancrage, applique la rotation caméra (calculée en
     **relatif** : `position_caméra − position_ancrage`, jamais la position
     absolue de la caméra) et le scale global.
   - **Garantie que ça achète** : tout le bloc local subit ensuite *une
     seule transformation rigide*. Une transformation rigide préserve les
     relations entre les éléments qu'elle déplace ensemble — donc un calcul
     correct en local reste correct dans n'importe quelle position/rotation
     du monde. C'est gratuit, à condition de ne jamais mélanger les deux
     espaces.

3. **`Menu-Align` — sous-node-group réutilisable pour tout ce qui dépend de
   l'alignement.** Sockets : `Menu` (enum Gauche/Droite/Centre) + 3 entrées
   Geometry, 1 sortie. Instancié une fois par endroit où une géométrie doit
   changer selon l'alignement (texte, segments de la ligne de connecteur…).
   Préféré à un recalcul géométrique automatique (type `Compare` sur
   `abs(Min.x)`/`abs(Max.x)`) : une seule logique à maintenir, et le cas
   Centre est fourni explicitement au lieu d'être déduit — donc pas
   d'ambiguïté ni de sensibilité aux arrondis.

4. **`CompensationYX` — sous-node-group réutilisable pour les compensations
   de centrage.** Entrées : Geometry + Value. Calcule
   `(Value/2, hauteur_bbox/2 + Value/2, 0)`. Utilisé en deux étages :
   d'abord sur le texte, puis sur la cartouche construite à partir de ce
   texte déjà compensé.
   **Point clé pour que ça fonctionne** : la compensation doit être insérée
   sur le **fil réellement partagé** par tous les consommateurs en aval
   (ex. `Reroute.035`), pas sur une branche parallèle qui forke plus tôt.

5. **Positions dérivées de la Bounding Box, jamais d'indices de sommets
   codés en dur.** Un indice de sommet/arête est topologiquement fixe mais
   géométriquement mobile : il suit la bbox et casse dès que l'alignement
   ou la topologie change. Toujours passer par `Min`/`Max`.

6. **Distribution : un petit objet par marqueur**, portant sa propre
   instance du modifier connecteur. Décision prise parce que le node group
   n'était pas stable et que le nombre de marqueurs reste faible. Évolution
   possible plus tard (un seul objet "points" + attribut texte par point)
   sans remettre en cause le contrat de sockets.

## Pièges connus — à ne PAS "simplifier"

Ces comportements ressemblent à des bugs mais sont **volontaires**. Deux
corrections proposées à tort par le passé, testées et rejetées :

- **`MargesBox` dans la translation** (pas seulement dans la taille) :
  c'est une marge voulue et assumée. Ne pas la retirer.
- **Mécanismes de compensation par annulation** : certains points sont
  délibérément pré-décalés en sens inverse (ex. `Start = -distance`) pour
  s'annuler avec un décalage appliqué plus loin au bloc entier
  (`-distance + distance = 0`). Figer un tel point à `(0,0,0)` casse
  l'annulation — la ligne se réduit à un point. **Avant de proposer de
  couper une dépendance qui "n'a pas l'air d'avoir de sens", vérifier
  qu'elle ne fait pas partie d'une paire qui s'annule.**

## Retrouver un nœud dans l'éditeur

Le graphe est très étalé et les nœuds portent des noms auto-générés
(`Math.017`, `Reroute.011`…) difficiles à localiser à l'œil.

- **`Select ▸ Find Node` (Ctrl+F)** dans l'éditeur de nœuds : ouvre une
  recherche, sélectionne le nœud trouvé et **recentre la vue dessus**.
  Cherche par nom, label de socket, avertissement, ou certaines valeurs
  de sockets. C'est le moyen fiable de suivre les instructions de la
  roadmap, qui désignent les nœuds par leur nom interne.
- Dans l'autre sens (identifier un nœud visible) : le sélectionner puis
  sidebar `N` → onglet **Item**, qui affiche son nom.

## Méthode de travail — vérifications obligatoires

Le graphe a grandi de façon organique et contient beaucoup de pièges de
lecture. Discipline à respecter :

- **Toujours tracer les liens réels** dans la section `links.new(...)` de
  l'export Python. Ne jamais déduire le comportement du nom d'un nœud, de
  son label, ni d'une description verbale.
- **Les noms internes sont réutilisés.** Blender réattribue un nom libéré
  par un renommage manuel : un `Frame.006` peut désigner un cadre
  totalement différent d'une version à l'autre. **Se fier au label
  visible**, pas au nom interne.
- **Les nœuds orphelins sont fréquents** : branchés en entrée mais dont la
  sortie ne va nulle part (culs-de-sac inertes). Vérifier qu'un nœud est
  réellement consommé avant de bâtir un diagnostic dessus.
- **Les variables Python homonymes** entre sous-groupes ne désignent pas
  les mêmes nœuds : chaque fonction de l'export renumérote depuis zéro
  (`Math.017` du sous-groupe ≠ `Math.017` du graphe principal).
- **L'algèbre vectorielle à plusieurs variables est la zone à risque.**
  Sur ces sujets (annulations, miroirs de signe, compensations), donner
  l'hypothèse *et* un test minimal à valider dans Blender avant d'enchaîner
  d'autres recommandations dessus.

## Feuille de route

L'état d'avancement détaillé, les phases et les bugs en cours vivent dans
**`docs/ROADMAP.md`** — avec, pour chaque étape, le cadre (label visible)
où se trouvent les nœuds concernés et un critère de validation.

## Contrat de sockets (à figer une fois le node group stabilisé)

Interface actuelle : `Geometry` (in/out), `String`, `Menu` (alignement),
`Radius`, `MargesBox`, `connector line offset x`, `connector line offset
down`, `Suivi Camera`, `Scale global`, `distance`, `Rotation Manuel`,
`Cartouche ronde`, `Cartouche Radius`, `Cartouche Res`,
`Souligne Vert-Horiz`.

Cette liste bougera encore. Une fois les phases de la roadmap terminées et
testées, la figer ici comme référence stable pour GeoData et Geomapper.

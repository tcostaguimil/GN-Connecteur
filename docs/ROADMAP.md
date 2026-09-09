# Feuille de route — refonte du node group GN-CONNECTEUR-TEXTE-02

Ce document sert de checklist pour appliquer, dans l'éditeur Geometry Nodes
de Blender, les corrections identifiées en analysant le graphe actuel
(`GN-Connecteur-Texte-02.py`, export "Copy as Python"). Construction à la
main dans l'éditeur, pas de génération procédurale par script — cohérent
avec la doctrine retenue côté addons consommateurs (GeoData to Geometry
Nodes, Geomapper).

## Contrainte de compatibilité : Blender 4.2 LTS

Le connecteur doit rester utilisable dans des extensions packagées pour
Blender 4.2 LTS (système d'Extensions 4.2+). Vérifié : le nœud **Active
Camera**, déjà utilisé dans le graphe actuel, est arrivé en **Blender 4.1**
— donc disponible en 4.2 LTS. Tous les nœuds utilisés dans les phases
ci-dessous (Vector Math, Switch, Bounding Box, Sample Index, Fillet Curve,
Separate/Combine XYZ) existent depuis bien plus longtemps. **Réflexe à
garder pour la suite** : avant d'ajouter un nœud tout juste sorti dans une
version récente de Blender, vérifier sa version d'introduction sur la
documentation officielle.

## Repères dans l'éditeur — quel nœud est où

Le graphe n'utilise pas les cadres (Frames) de façon homogène : certaines
zones sont proprement étiquetées, d'autres sont des nœuds qui flottent
librement sans aucun cadre autour. **Chaque étape ci-dessous précise
maintenant une ligne "Cadre :"** — soit le label visible d'un cadre existant,
soit "aucun (nœuds flottants)" avec un repère relatif à un cadre visible.

### Cadres existants (nom interne → label visible → contenu)

| Nom interne | Label visible dans l'éditeur | Contenu |
|---|---|---|
| `Frame` | **Cartouche** | Fond de la bulle (Grid), bbox du texte, calcul de taille, cartouche ronde/switch |
| `Frame.001` | **TEXTE** | `String to Curves`, `Fill Curve`, réalisation des instances de caractères |
| `Frame.002` | **CONNECTOR LINE** | Les deux segments de ligne (`Curve Line`, `Curve Line.002`), leur profil circulaire |
| `Frame.006` | **trouve centre pour revenir en arrière** | Bbox globale du widget + calcul du centre (`Vector Math.004/.007/.008/.009`) |
| `Frame.007` | **1. decentre par la moitier 2.Scale 3.repositionne + la scale** | Les 3 `Transform Geometry` du pivot/scale final, tout à l'extrême droite du graphe, juste avant `Group Output` |

**Deux cadres sont vides — ignore-les** : `Frame.004` (pas de label,
aucun nœud) et `Frame.005` (label "deplacement du tout au pivot", aucun
nœud non plus). Ce sont des cadres fantômes, comme les nœuds orphelins de
la Phase 0 — tu peux les supprimer sans risque à l'occasion.

### Nœuds flottants (aucun cadre) — les 3 zones à connaître

- **Zone "Suivi caméra"** (Phase 1) : `Object Info`, `Active Camera`,
  `Align Rotation to Vector`, `Switch`, `Compare`, `Group Input.003`.
  Repère : juste en dessous et à gauche du cadre **Cartouche**.
- **Zone "Ancrage"** (Phase 2 — celle qui bloque) : `Sample Index.002`,
  `Position.002`. Repère : **nettement en dessous du cadre CONNECTOR
  LINE**, isolés, sans cadre autour — c'est le duo de nœuds tout seul
  dans le vide sous cette zone. (`Points`, juste à côté, est l'orphelin
  déjà supprimé en Phase 0.)
- **Zone "Sortie finale"** : `Realize Instances.002`, `Transform
  Geometry.006`, `Group Output.001`. Repère : dans l'espace entre le
  cadre **trouve centre pour revenir en arrière** et le cadre **1.
  decentre...** — `Group Output.001` est le nœud le plus à droite de
  tout le graphe, impossible à rater une fois dézoomé en entier (touche
  `Home` dans l'éditeur pour tout voir d'un coup).

## Diagnostic (rappel — pourquoi ces changements)

En traçant les connexions réelles du graphe (pas seulement les noms de
nœuds), 5 constats :

1. **Bug racine — absolu vs relatif** : la rotation "Suivi Caméra" est
   calculée à partir de la position *absolue* de la caméra (`Object
   Info.Location`, espace `ORIGINAL`), envoyée telle quelle dans `Align
   Rotation to Vector`. Ce nœud attend une *direction*, pas une position —
   ça ne fonctionne "par hasard" que si le connecteur est à l'origine du
   monde (0,0,0).
2. **L'ancrage (position du marqueur) n'est jamais utilisé** : `Sample
   Index.002` calcule la position du point d'ancrage (input `Geometry`)
   mais sa sortie n'est branchée nulle part. Le connecteur se positionne
   aujourd'hui uniquement via la transform de l'objet Blender qui porte le
   modifier.
3. **Deux nœuds orphelins** : `Object Info.001` (référence codée en dur à
   un objet nommé `"Empty"`, jamais branché) et `Points` (position codée en
   dur `(0, -1.4, 0)`, jamais branché) — traces d'essais abandonnés.
4. **Le bloc pivot/scale est correct** : `Frame.005/.006/.007`
   ("déplacement au pivot" → scale → repositionne) recentre le widget sur
   son propre bbox avant de scaler — raisonnement local/relatif correct, à
   garder et à généraliser plutôt qu'à toucher.
5. **Points d'accroche du connecteur codés en dur** : `Sample Index` /
   `Sample Index.001` lisent des indices de sommets fixes (6 et 8) sur la
   géométrie de la cartouche — fragile si la topologie change.
   *(Résolu en Phase 4 — remplacé par un calcul Bounding Box.)*

## Phase 0 — Nettoyage (rapide, sans risque) ✅ fait

- [x] Supprimer `Object Info.001` (référence à `"Empty"`, jamais branché).
- [x] Supprimer `Points` (position `(0, -1.4, 0)`, jamais branché).
- [ ] *Ajout après coup* : supprimer aussi les deux cadres vides
      `Frame.004` et `Frame.005` (voir "Repères" ci-dessus) — décoratifs,
      sans nœud dedans, ils n'ont plus de raison d'être une fois les
      orphelins supprimés.

**Cadre** : aucun (les nœuds supprimés étaient flottants).

**Validation** : le graphe évalue toujours sans erreur, rendu visuel
identique à avant (ces nœuds ne produisaient aucun effet).

## Phase 1 — Corriger le suivi caméra (bug absolu/relatif) ✅ fait

**Cadre** : aucun — zone "Suivi caméra" flottante, sous le cadre Cartouche
(voir "Repères" ci-dessus).

- [x] Ajouter un `Vector Math` (Subtract) :
      `Object Info.Location (caméra)` − `Sample Index.002 (ancrage)`.
- [x] Brancher la sortie de cette soustraction sur
      `Align Rotation to Vector.Vector`, à la place de la sortie directe de
      `Object Info.Location`.

**Validation** : déplacer l'objet portant le modifier loin de l'origine du
monde, activer "Suivi Camera", vérifier que le texte s'oriente
correctement vers la caméra quelle que soit la position de l'objet (pas
seulement à l'origine).

*Lien avec la Phase 2* : tu as déjà branché `Sample Index.002` comme
**entrée** de la soustraction ci-dessus. La Phase 2 réutilise cette même
sortie pour un second usage (voir juste en dessous) — normal qu'un même
nœud alimente deux endroits différents du graphe.

## Phase 2 — Brancher réellement l'ancrage (position du marqueur)

**Cadre** : aucun. Le nœud clé, `Sample Index.002`, est dans la zone
"Ancrage" flottante — **nettement en dessous du cadre CONNECTOR LINE**,
isolé (voir "Repères" ci-dessus). La destination du branchement,
`Transform Geometry.003`, est à l'opposé du graphe : tout à l'extrême
droite, à l'intérieur du cadre **1. decentre par la moitier 2.Scale
3.repositionne + la scale**, juste avant `Group Output.001`.

**Pourquoi cette phase** : `Sample Index.002` calcule bien la position du
point d'ancrage reçu sur l'input `Geometry` du node group — mais
aujourd'hui, cette valeur ne sert (depuis la Phase 1) qu'au calcul de
rotation caméra. Elle n'est **jamais utilisée pour positionner le
widget**. Résultat concret : quel que soit le point que tu branches sur
l'input `Geometry`, le connecteur reste toujours affiché à l'origine de
l'objet Blender qui porte le modifier — il ignore complètement où se
trouve le point reçu. C'est bloquant pour l'usage prévu (un objet
"points de marqueurs" avec plusieurs positions, une par commune) : sans
cette phase, tous les marqueurs s'afficheraient au même endroit.

- [ ] Ouvre le cadre **1. decentre...** (`Frame.007`, extrême droite) et
      repère `Transform Geometry.003` — c'est celui dont la sortie
      `Geometry` part directement vers `Group Output.001`. Regarde ce qui
      alimente actuellement son entrée `Translation` : c'est la sortie de
      `Vector Math.009` (le calcul du pivot compensé par l'échelle).
- [ ] Ajoute un nouveau `Vector Math` (opération **Add**) à côté.
- [ ] Branche dedans : entrée A = sortie actuelle de `Vector Math.009`
      (le lien existant vers `Transform Geometry.003.Translation`),
      entrée B = sortie de `Sample Index.002` (zone "Ancrage", à
      récupérer tout en bas à gauche du graphe — le lien va être long,
      c'est normal vu la dispersion du graphe).
- [ ] Branche la sortie de ce nouveau `Vector Math (Add)` sur
      `Transform Geometry.003.Translation`, à la place du lien direct
      depuis `Vector Math.009`.

**Résultat logique** : `Translation finale = pivot compensé par l'échelle
+ position réelle de l'ancrage`. Le pivot/scale continue de fonctionner
comme avant (Phase inchangée), et le widget se positionne EN PLUS à
l'endroit reçu sur l'input `Geometry`.

**Validation** : brancher un objet ou un point différent sur l'input
`Geometry` du node group, vérifier que le connecteur suit bien cette
nouvelle position (déplace l'objet test loin de l'origine pour bien voir
la différence avec le comportement actuel).

## Phase 3 — Alignement du texte gauche/droite/centre ✅ largement fait

**Mise à jour (version 2 du fichier)** : implémenté en mieux que prévu —
3 branches (`Frame.001` **TEXTE Gauche**, `Frame.003` **TEXTE Droite**,
`Frame.004` **TEXTE Centre**) plutôt que 2, sélectionnées par un
**Menu Switch** (socket `Menu` à 3 entrées Gauche/Droite/Centre) plutôt
qu'un simple bool `Switch` — plus extensible si un 4e alignement arrive un
jour.

- [x] Dupliquer `String to Curves` + `Fill Curve`/`Realize Instances` :
      une branche par alignement.
- [x] `Menu Switch` juste après ces branches, avant le calcul de
      bbox/cartouche/pivot.
- [x] Socket `Menu` exposé sur l'interface du node group.

**🐛 Bug à vérifier avant tout le reste** : `String to Curves.002`
(branche **Centre**, dans `Frame.004`) a `align_x = 'RIGHT'` — identique à
`String to Curves.001` (branche **Droite**, `Frame.003`). Vérifie dans
Blender si c'est voulu ou un copier-coller de "Droite" jamais corrigé en
`'CENTER'`.

**Validation** : basculer le `Menu` doit produire un texte qui grandit
dans le sens attendu pour chacune des 3 options.

## Phase 3bis — Faire suivre la cartouche à l'alignement

**Cadre** : **Cartouche** (`Frame`) — `Bounding Box`, `Separate XYZ` /
`Separate XYZ.001` (Min/Max), `Math.007/.008/.009`, `Combine XYZ.003`
(sortie vers la Translation du `Transform Geometry` qui positionne la
cartouche), `Mesh to Points`, `Instance on Points.002`/`.003`.

### Partie A — centre de bbox dynamique ✅ fait (v3 du fichier)

**Pourquoi la cartouche ne suivait pas** : la translation de la cartouche
(`Math.007` → `.008` → `.009` → `Combine XYZ.003.X`) était une formule qui
*supposait* que le texte commence à `x=0` et grandit vers la droite (vrai
seulement pour la branche Gauche). Remplacée par un vrai centre de bbox
dynamique, `centre.x = (Min.x + Max.x) / 2` — appliqué et confirmé présent
dans le fichier v3.

### Partie B — une deuxième translation cachée annulait le fix ✅ fait (v4 du fichier)

**Pourquoi c'était toujours cassé après la Partie A** : `Instance on
Points.002` (cartouche rectangulaire) et `.003` (cartouche ronde) ne
servent pas qu'à appliquer la rotation "Suivi Caméra" (`Reroute.012` →
leur input `Rotation`) — ils instanciaient aussi le bloc `Transform
Geometry` (déjà bien centré par la Partie A) sur un **point** venant de
`Mesh to Points` (mode EDGES, filtré à l'arête d'index 2 via
`Compare.001`), un point topologiquement fixe mais **géométriquement
mobile** qui suivait la bbox réelle — les deux translations
s'additionnaient au lieu que la bonne remplace l'ancienne.

- [x] Nœud `Points` (Count=1, Position=`(0,0,0)`) ajouté, branché sur
      `Instance on Points.002.Points` **et** `Instance on
      Points.003.Points`, à la place de `Mesh to Points.Points`.
- [ ] Nettoyage restant : `Mesh to Points`, `Compare.001`, `Index.002`
      (devenus inutiles) et `Mesh to Points.002` (alimente `Join
      Geometry.003`, dont la sortie n'est branchée nulle part — reste de
      débogage mort) peuvent être supprimés.

### Partie C — ❌ diagnostic écarté par l'utilisateur (décision produit)

**Correction** : `Math.009` (= `-MargesBox/2` dans la translation) n'est
**pas** un bug — c'est une marge voulue et assumée. Décision de garder
`MargesBox` dans la translation en plus de la taille. Ne pas y retoucher.

### Partie D — cause réelle en cours de vérification

L'utilisateur a identifié une cause différente : un ancien setup autour de
`Transform Geometry.004` (`Instance on Points` / `Mesh to Points.001` /
`Compare.002` / `Index.003`) dont il ne se souvient plus de la raison
d'être, source d'un couplage texte↔cartouche non désiré. Décrit comme
supprimé ("le texte suit la cartouche et vice versa" une fois retiré) mais
**toujours présent et branché dans le fichier v5 fourni** — à vérifier :
soit cet export précède la suppression, soit elle a été faite dans un
autre état de la scène. Reprendre le diagnostic sur un export qui reflète
l'état réellement testé.

**Validation** : basculer le `Menu` (Gauche/Droite/Centre) — la cartouche
doit rester visuellement centrée sur le texte (à la marge `MargesBox`
près, désormais assumée) dans les 3 cas, sans réajustement manuel, y
compris avec "Suivi Camera" activé.

## Phase 4 — Connecteur en mode "soulignement" ✅ largement fait

**Mise à jour (version 2 du fichier)** : déjà implémenté avec l'approche
Bounding Box recommandée (pas les indices fixes de l'ancienne version) —
`Bounding Box.002`/`.003` + `Separate XYZ.002/.003/.004` +
`Combine XYZ.006/.007/.008` calculent les deux points candidats, un
`Switch.003` (type Vector, socket `Souligne Vert-Horiz`) choisit entre
les deux. Tout ça dans **CONNECTOR LINE** (`Frame.002`).

- [x] Point d'accroche dérivé de la Bounding Box plutôt que d'un indice
      fixe.
- [x] Point "soulignement" calculé de la même façon.
- [x] `Switch` (Vector) entre les deux, piloté par `Souligne Vert-Horiz`.

**Validation** : basculer `Souligne Vert-Horiz` change le point d'accroche
de la ligne sans casser le style "côté" existant.

## Phase 4bis — Arrondir le coin entre la ligne d'origine et le soulignement

**Cadre** : **CONNECTOR LINE** (`Frame.002`) — `Curve Line`, `Curve
Line.002`, jointes ensuite par `Join Geometry.001`.

**Pourquoi c'est anguleux actuellement** : `Curve Line` et `Curve
Line.002` sont deux courbes indépendantes, chacune convertie en tube
séparément (`Curve to Mesh`) puis jointes après coup. Une jonction entre
deux tubes indépendants ne peut pas être arrondie — chaque segment reste
géométriquement isolé, `Join Geometry` ne fusionne pas les splines entre
eux.

**Solution recommandée — tu utilises déjà cette technique pour les coins
de la cartouche** (`Quadrilateral → Fillet Curve → Fill Curve.001`) :

- [ ] Remplace les deux `Curve Line` par un **seul spline à 3 points**
      (origine → coude → point de soulignement/côté) construit via
      `Points` (3 points, même `Curve Group ID`) → `Points to Curves`
      (relie les points dans l'ordre en un seul poly spline).
- [ ] Branche ce spline dans un `Fillet Curve` (mode POLY — identique à
      celui déjà présent pour la cartouche), avec un nouveau socket
      `Rayon coin connecteur` si tu veux le piloter depuis l'UI.
- [ ] `Curve to Mesh` avec le même profil circulaire (`Curve Circle`)
      qu'actuellement, en aval du fillet plutôt que sur chaque segment
      séparément.

**Options moins bonnes, pour référence** :
- `Merge by Distance` sur les deux courbes jointes : ne recrée pas un
  spline continu, `Fillet Curve` n'aurait rien à arrondir — à éviter.
- Une sphère au coin pour masquer la jonction : dépannage visuel rapide,
  mais pas un vrai rayon réglable.

**Validation** : le coin entre les deux segments doit apparaître comme un
arc continu, dont le rayon suit le socket exposé, dans les deux modes
(côté et soulignement).

## Phase 4ter — Faire suivre le point d'accroche du connecteur à l'alignement ✅ solution adoptée (v5)

**Constat initial** : le même problème que la Phase 3bis se reproduit sur
la ligne de connecteur — quand le texte change d'alignement, le point
d'accroche doit changer de côté lui aussi.

**Garantie de robustesse dans le monde global** (reste valable quelle que
soit la technique utilisée) : ce calcul se fait dans **CONNECTOR LINE**
(`Frame.002`), donc en espace **local**, avant l'étape finale de placement
monde (`Frame.007` + Phase 2). Tout ce qui est construit en local — texte,
cartouche, ligne — subit ensuite **une seule transformation rigide**
(rotation caméra + position de l'ancrage), qui préserve les relations
entre les éléments qu'elle déplace ensemble. Un point correct en local
reste correct après rotation/translation, quelle que soit la position
finale dans le monde.

**Solution réellement adoptée — meilleure que ma suggestion initiale** :
plutôt qu'un `Compare`/`abs(Min/Max)` (ma proposition d'origine), le
`Menu Switch` a été extrait dans un **sous-node-group réutilisable**,
`Menu-Align` (sockets `Menu` + `Gauche`/`Droite`/`Centre` en Geometry,
1 sortie), instancié plusieurs fois (`Group`, `Group.001`, `Group.002` —
un par endroit où une géométrie doit changer selon l'alignement, dont la
ligne de connecteur). Avantage : une seule logique de sélection à
maintenir, réutilisée partout, chaque instance recevant juste les 3
géométries candidates spécifiques à son contexte — plus lisible qu'un
recalcul géométrique par `Compare`, et pas d'ambiguïté sur le cas Centre
puisque sa valeur est fournie explicitement comme les deux autres, pas
déduite.

**Validation** : basculer le `Menu` (Gauche/Droite/Centre) — le point
d'accroche du connecteur doit suivre le bon côté du texte dans les 3 cas,
et rester correct après avoir changé la position/rotation de l'objet
porteur dans la scène (test de non-régression de la garantie ci-dessus).

## Note — attribut `CompY` (compensation de position, en cours)

Approche en cours pour compenser le centrage automatique de la page en X/Y
(le bord du cadre doit tomber à 0, gauche ou droite) : un
`Store Named Attribute` (`CompY`, `FLOAT_VECTOR`, domaine POINT) calculé
depuis une Bounding Box, à relire plus loin dans le graphe via
`Named Attribute` plutôt que de tirer un fil sur toute la largeur de
l'éditeur. Technique saine, cohérente avec un graphe aussi étalé —
équivalent d'une variable nommée plutôt qu'un branchement longue distance.

- Le socket est déjà en `FLOAT_VECTOR` : pas besoin d'un `CompX` séparé,
  les deux composantes (X et Y) peuvent cohabiter dans le même attribut
  une fois la partie X ajoutée (renommer en `CompXY` si `CompY` prête à
  confusion).
- À vérifier une fois câblé bout en bout : qu'aucun `Join Geometry` /
  `Realize Instances` entre le `Store` et le `Named Attribute` de lecture
  ne casse le contexte par-point attendu.

## Phase 5 — Organisation visuelle (lisibilité, pas de logique nouvelle)

Maintenant qu'on sait précisément ce qui flotte (voir "Repères" en haut de
ce document), cette phase consiste à donner un cadre à chaque zone
flottante identifiée, pour que plus aucune instruction future n'ait besoin
de "repères relatifs" comme dans ce document.

- [ ] Sélectionner les nœuds de la zone "Suivi caméra" (`Object Info`,
      `Active Camera`, `Align Rotation to Vector`, `Switch`, `Compare`,
      `Group Input.003`, plus le `Vector Math (Subtract)` ajouté en Phase
      1) et les grouper en un nouveau cadre (sélection + `Ctrl+J`),
      labellisé ex. **MONDE — Rotation caméra**.
- [ ] Faire de même pour la zone "Ancrage" (`Sample Index.002`,
      `Position.002`, plus le `Vector Math (Add)` ajouté en Phase 2) →
      cadre **MONDE — Ancrage**.
- [ ] Faire de même pour la zone "Sortie finale" (`Realize Instances.002`,
      `Transform Geometry.006`, `Group Output.001`, reroutes associées)
      → cadre **MONDE — Sortie**.
- [ ] Supprimer `Frame.004` et `Frame.005` si pas déjà fait en Phase 0.

**Validation** : purement visuelle — aucun changement de comportement
attendu.

## Phase 6 — Figer le contrat de sockets (une fois 1 à 5 testées)

Une fois les phases précédentes appliquées et testées dans Blender :

- [ ] Lister la version stabilisée des sockets d'entrée/sortie du node
      group (inclut les nouveaux : alignement, soulignement).
- [ ] Documenter ce contrat comme référence stable pour les deux addons
      consommateurs (GeoData to Geometry Nodes, Geomapper) — eux ne
      doivent connaître que ces sockets, jamais l'intérieur du node group.
- [ ] Rappel de décision déjà actée : chaque marqueur reste un petit objet
      séparé portant sa propre instance du modifier (pas de distribution
      via un seul objet "points" + attribut par point pour l'instant —
      cette évolution reste possible plus tard sans remettre en cause ce
      contrat).

## Notes complémentaires

- Toutes les phases sont indépendantes sauf 1↔2 (voir dépendance notée en
  Phase 1). L'ordre 0 → 1/2 → 3/3bis → 4/4bis → 5 → 6 est recommandé mais
  le bloc 3/3bis et le bloc 4/4bis peuvent être inversés entre eux sans
  risque.
- Renommage à surveiller : dans la v2 du fichier, une nouvelle frame a
  été créée avec le nom interne `Frame.006` (label **Calcul Marge**) —
  différent de `Frame.006 nom de la frame` (label **trouve centre pour
  revenir en arrière**, celle référencée dans ce document). Blender
  réutilise les noms internes libérés par un renommage manuel — vérifie
  toujours le **label visible**, pas seulement le nom interne, si tu
  compares avec une version antérieure du fichier.
- Aucune de ces corrections ne nécessite de génération procédurale par
  script Python — tout se fait à la main dans l'éditeur Geometry Nodes.

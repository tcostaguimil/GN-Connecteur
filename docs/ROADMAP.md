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

**Pour retrouver un nœud par son nom** : `Ctrl+F` (`Select ▸ Find Node`)
dans l'éditeur — sélectionne le nœud et recentre la vue dessus. C'est le
moyen fiable de suivre les instructions ci-dessous, qui désignent les
nœuds par leur nom interne.

### Cadres existants — **resynchronisé sur le fichier v7**

| Nom interne | Label visible | Nb nœuds | Contenu |
|---|---|---|---|
| `Frame` | **Cartouche** | 45 | Fond de la bulle (Grid), bbox du texte, taille, cartouche ronde/switch |
| `Frame.001` | **TEXTE Gauche** | 3 | `String to Curves` + Transform + Realize de la branche Gauche |
| `Frame.003` | **TEXTE Droite** | 3 | Idem branche Droite |
| `Frame.004` | **TEXTE Centre** | 3 | Idem branche Centre |
| `Frame.002` | **CONNECTOR LINE** | 56 | Les 3 chaînes du connecteur (Points / Points to Curves / Fillet), points d'accroche bbox, switch soulignement |
| `Frame.005` | **MARGES** | 1 | — |
| `Frame.006` | **Calcul Marge** | 4 | Calcul de la marge |
| `Frame.006 nom de la frame` | **trouve centre pour revenir en arrière** | 5 | Bbox globale du widget + calcul du centre |
| `Frame.007` | **1. decentre par la moitier 2.Scale 3.repositionne + la scale** | 3 | Les 3 `Transform Geometry` du pivot/scale final, juste avant `Group Output` |
| `Frame.008` | **Pivot compensé par l'échelle - Selectionne le Vectex du Mesh** | 3 | Ancrage (`Sample Index.002`, `Position.002`) |
| `Frame.009` | **Distance Origine** | 13 | Pré-décalage et miroir de `distance` (voir Phase 4quater) |
| `Suivi caméra` | *(le nom sert de label)* | 7 | `Object Info`, `Active Camera`, `Align Rotation to Vector`, `Switch` |

⚠️ **Attention aux deux `Frame.006`** : `Frame.006` (label *Calcul Marge*)
et `Frame.006 nom de la frame` (label *trouve centre pour revenir en
arrière*) sont deux cadres différents. Toujours se fier au **label
visible**, jamais au nom interne.

L'ancienne note « `Frame.004` et `Frame.005` sont vides » est **obsolète**
— ils portent maintenant du contenu. De même, les zones de nœuds
flottants décrites dans les versions précédentes ont été encadrées :
l'ancrage est dans `Frame.008`, le suivi caméra dans `Suivi caméra`.

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
- [x] Nettoyage effectué : `Mesh to Points`, `Mesh to Points.002` et
      `Join Geometry.003` ont bien disparu du graphe — vérifié, ils
      n'existent plus dans le fichier v7.

### Partie C — ❌ diagnostic écarté par l'utilisateur (décision produit)

**Correction** : `Math.009` (= `-MargesBox/2` dans la translation) n'est
**pas** un bug — c'est une marge voulue et assumée. Décision de garder
`MargesBox` dans la translation en plus de la taille. Ne pas y retoucher.

### Partie D — ✅ supprimés (vérifié v7)

`Instance on Points` / `Mesh to Points.001` / `Compare.002` / `Index.003`
(autour de `Transform Geometry.004`) étaient branchés mais ne menaient
nulle part — culs-de-sac inertes. Ils n'existent plus dans le fichier v7.

### Partie E — ✅ résolu (v6) : sous-node-group `CompensationYX`

Solution retenue, différente de `Store Named Attribute` : un vrai
sous-node-group réutilisable `CompensationYX` (Geometry + Value en entrée,
calcule `(Value/2, hauteur_bbox/2 + Value/2, 0)` en sortie), instancié deux
fois :
- **`Group.003`** : appliqué au texte (sortie de `Group`, le sélecteur
  d'alignement `Menu-Align`) via `Transform Geometry.010`, **directement
  sur `Reroute.035`** — le fil partagé que tout le reste (bbox de la
  Cartouche, etc.) lit ensuite. C'est la raison pour laquelle ça
  fonctionne : contrairement à la tentative précédente, la compensation
  est insérée sur le tuyau réellement partagé par tous les consommateurs,
  pas sur une branche parallèle qui ferait un fork trop tôt.
- **`Group.004`** : appliqué à la Bounding Box de la Cartouche elle-même,
  branché sur `Combine XYZ.003.Y` (anciennement figé à `0.0` en dur).

Architecture en deux étages (texte compensé, puis cartouche construite
sur ce texte déjà compensé) — validée, rien à changer ici.

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

## Phase 4bis — Arrondir le coin du connecteur ✅ structure en place (v7)

**Cadre** : **CONNECTOR LINE** (`Frame.002`).

Les `Curve Line` ont été remplacées par trois chaînes complètes, une par
alignement, toutes construites sur le bon pattern :

`Points` (Count = 3, Position pilotée par un `Index Switch` alimenté par
`Index`) → `Points to Curves` (Curve Group ID laissé à 0 = une seule
courbe) → `Fillet Curve` → sélection par `Group.002` (Menu-Align).

| Chaîne | Index Switch | Points | Points to Curves | Fillet Curve |
|---|---|---|---|---|
| Gauche | `Index Switch` | `Points.002` | `Points to Curves` | `Fillet Curve.001` |
| Droite | `Index Switch.001` | `Points.003` | `Points to Curves.001` | `Fillet Curve.002` |
| Centre | `Index Switch.002` | `Points.004` | `Points to Curves.002` | `Fillet Curve.003` |

**Règle à garder en tête** : `Fillet Curve` n'arrondit que les points
*intérieurs* d'une spline, jamais les extrémités. Sur un spline à 3
points, seul le point **d'index 1** est arrondi — il doit donc toujours
être le **coude**.

### L'ordre des points = le choix du coin d'accroche (mécanisme voulu)

Contenu réel des `Index Switch` :

| Chaîne | point 0 | point 1 (celui qui est arrondi) | point 2 |
|---|---|---|---|
| Gauche | `Reroute.011` (ancrage) | `Vector Math.001` (coude) | `Switch.003` (accroche) |
| Droite | `Reroute.011` (ancrage) | `Switch.003` | `Vector Math.001` |
| Centre | `Reroute.011` (ancrage) | `Combine XYZ.002` | `Combine XYZ.002` |

**L'inversion des points 1 et 2 entre Gauche et Droite n'est pas une
erreur — c'est le mécanisme qui fait changer le connecteur de coin de la
cartouche.** Logique de conception : la cartouche a 4 côtés (haut, bas,
gauche, droite). Si le texte est ferré à gauche, il se développe vers la
droite, donc le coude doit se trouver du côté **gauche** ; si le texte est
ferré à droite, il part vers la gauche, donc le coude passe du côté
**droit**. Inverser les deux points est précisément ce qui produit ce
basculement.

*(Cette entrée corrige une analyse antérieure qui qualifiait à tort cette
inversion de bug — même famille d'erreur que pour `MargesBox` et les
pré-décalages qui s'annulent : voir la section « Pièges connus » du
`CLAUDE.md`.)*

### Centre — refonte prévue (décision utilisateur)

Le montage actuel (même `Combine XYZ.002` sur les points 1 et 2, donc deux
points confondus) est reconnu comme peu élégant et **sera remplacé**, pas
rafistolé :

- [ ] Construire une courbe à **2 points seulement** (du centre jusqu'à la
      cartouche) pour le mode Centre.
- [ ] Ajouter une **seconde courbe séparée** pour le surlignement.

Un spline à 2 points n'a pas de point intérieur, donc pas de fillet à
prévoir sur cette branche — la question du coude ne se pose plus pour
Centre.

- [ ] Optionnel : exposer un socket `Rayon coin connecteur` pour piloter
      le rayon des `Fillet Curve` de Gauche et Droite depuis l'UI.

- [ ] Optionnel : exposer un socket `Rayon coin connecteur` pour piloter
      le rayon des trois `Fillet Curve` depuis l'UI du modifier.

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

## Phase 4quater — l'ancrage ne s'annule pas côté Droite (🐛 à faire) — *resynchronisé v7*

**Cadre** : **Distance Origine** (`Frame.009`), plus `Reroute.011` dans
**CONNECTOR LINE** (`Frame.002`).

**Symptôme** : l'ancrage (point 0 des trois chaînes) part à `x = -4` au
lieu de rester à `0` quand l'alignement est à Droite. Gauche est correct.

**Le mécanisme (compensation par annulation — volontaire)** : l'ancrage
est délibérément pré-décalé de `-distance`, pour s'annuler avec le
décalage `+distance` appliqué plus loin au bloc entier. Ne **pas** essayer
de figer l'ancrage à `(0,0,0)` : testé, ça réduit la ligne à un point.

Câblage réel en v7 :

| Élément | Valeur |
|---|---|
| Pré-décalage (les 3 chaînes) | `Reroute.011` ← `Vector Math.012` = `distance × (-1,-1,-1)` = **`-distance`** |
| Décalage du bloc, Gauche | `Transform Geometry.006.Translation` = `distance` (tel quel) |
| Décalage du bloc, Droite | `Transform Geometry.011.Translation` ← `Vector Math.011` ← `Combine XYZ.010` = **`(-distance.x, distance.y, distance.z)`** |

Addition des deux :
- Gauche : `(-dx,-dy,-dz) + (dx,dy,dz)` = `(0,0,0)` ✅
- Droite : `(-dx,-dy,-dz) + (-dx,dy,dz)` = **`(-2·dx, 0, 0)`** ❌ → avec
  `distance.x = 2`, ça donne bien le `-4` observé.

**Cause** : le bloc est mirroré en X côté Droite, mais le pré-décalage de
l'ancrage ne l'est pas — les deux poussent dans le même sens au lieu de
s'opposer. Il faut que le pré-décalage Droite devienne
`(+distance.x, -distance.y, -distance.z)`.

**Le nœud nécessaire existe déjà** : `Vector Math.003` (dans `Frame.009`)
est réglé sur MULTIPLY par `(-1, 1, 1)` — le bon multiplicateur — mais
n'est branché à rien, ses entrées sont sur leurs valeurs par défaut.

- [ ] Brancher `Vector Math.012` (= `-distance`) → `Vector Math.003`
      (×`(-1,1,1)`) → **`Index Switch.001`, entrée du point 0** (chaîne
      Droite uniquement).
- [ ] ⚠️ Ne **pas** insérer ce miroir sur `Reroute.011` lui-même : ce
      reroute alimente les trois chaînes (Gauche, Droite et Centre) — le
      mirorer là casserait Gauche, qui fonctionne. Il faut une dérivation
      dédiée à Droite.

Vérification : `(-dx,-dy,-dz) × (-1,1,1)` = `(+dx,-dy,-dz)`, puis
`+ (-dx,dy,dz)` = `(0,0,0)` ✅

**Obsolète depuis v7** : le facteur `×2.0` de `Math.018` n'est plus en
cause — `Math.017` et `Math.018` lisent maintenant `distance.x` en
parallèle au lieu d'être chaînés, donc `Combine XYZ.010.X` reçoit un
`-1×distance.x` propre. `Math.018` est devenu orphelin (sa sortie ne va
nulle part) et peut être supprimé. `Vector Math.011` (ADD avec `(0,0,0)`)
est un simple passe-plat, supprimable aussi si tu veux alléger.

**Validation** : quel que soit `distance` et quel que soit l'alignement,
l'ancrage (point 0) reste à `(0,0,0)` en local — seul l'autre bout de la
ligne suit `distance`, dans le bon sens selon le côté.

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

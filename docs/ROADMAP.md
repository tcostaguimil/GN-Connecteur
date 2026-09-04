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

## Phase 3 — Alignement du texte gauche/droite

**Cadre** : `String to Curves` et `Fill Curve` sont dans **TEXTE**
(`Frame.001`). Le `Switch` à ajouter doit rester dans ce même cadre
(agrandis-le si besoin) puisqu'il se situe juste après ces deux nœuds et
avant que la géométrie ne sorte vers **Cartouche** (`Frame`).

- [ ] Dupliquer `String to Curves` + `Fill Curve` : une branche par
      alignement (`align_x` = LEFT / RIGHT, `pivot_mode` adapté en
      conséquence).
- [ ] Ajouter un `Switch` (type **Geometry**) juste après ces deux
      branches, **avant** le calcul de bbox/cartouche/pivot (`Frame` /
      `Frame.007`) — pour que cette logique reste commune aux deux
      alignements, pas dupliquée.
- [ ] Ajouter un nouveau socket bool sur l'interface du node group, ex.
      `Aligner à droite`, branché sur ce `Switch`.

**Validation** : basculer le socket produit un texte qui grandit dans
l'autre sens ; la cartouche/bbox s'adapte correctement dans les deux cas.

## Phase 4 — Connecteur en mode "soulignement"

Décision : même ligne point-à-point vers le marqueur, mais avec un point
d'accroche différent (pas un second segment indépendant).

**Cadre** : `Sample Index` (l'indice 6 à remplacer) est dans **CONNECTOR
LINE** (`Frame.002`). `Bounding Box.001`, dont tu vas dériver les deux
points, est dans **trouve centre pour revenir en arrière** (`Frame.006`)
— un lien devra donc traverser d'un cadre à l'autre, c'est normal.

- [ ] Remplacer le point d'accroche actuel (aujourd'hui : `Sample Index`
      sur l'indice fixe 6) par un calcul dérivé de `Bounding Box.001`
      (Min/Max) : ex. `(Max.X, Min.Y, Z)` via `Separate XYZ` (déjà présent
      dans le graphe) + `Combine XYZ`. Corrige au passage la fragilité de
      l'indice codé en dur.
- [ ] Calculer le point "soulignement" (milieu du bord bas) de la même
      façon : `((Min.X + Max.X) / 2, Min.Y, Z)` via `Math (Add)` +
      `Math (Multiply 0.5)` sur les X du Min/Max, `Combine XYZ` avec le Y
      du Min.
- [ ] `Switch` (type **Vector**) entre les deux points, piloté par un
      nouveau socket bool, ex. `Connecteur en soulignement`.
- [ ] Brancher la sortie de ce `Switch` là où `Sample Index` alimentait
      `Vector Math` → `Curve Line.Start` (répéter le même principe pour le
      second point si besoin, `Sample Index.001` / indice 8).

**Validation** : basculer le socket change le point d'accroche de la
ligne sans casser le style "côté" existant quand le socket est désactivé.

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
  Phase 1). L'ordre 0 → 1/2 → 3 → 4 → 5 → 6 est recommandé mais 3 et 4
  peuvent être inversées entre elles sans risque.
- Aucune de ces corrections ne nécessite de génération procédurale par
  script Python — tout se fait à la main dans l'éditeur Geometry Nodes.

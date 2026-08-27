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

## Phase 0 — Nettoyage (rapide, sans risque)

- [ ] Supprimer `Object Info.001` (référence à `"Empty"`, jamais branché).
- [ ] Supprimer `Points` (position `(0, -1.4, 0)`, jamais branché).

**Validation** : le graphe évalue toujours sans erreur, rendu visuel
identique à avant (ces nœuds ne produisaient aucun effet).

## Phase 1 — Corriger le suivi caméra (bug absolu/relatif)

- [ ] Ajouter un `Vector Math` (Subtract) :
      `Object Info.Location (caméra)` − `Sample Index.002 (ancrage)`.
- [ ] Brancher la sortie de cette soustraction sur
      `Align Rotation to Vector.Vector`, à la place de la sortie directe de
      `Object Info.Location`.

**Validation** : déplacer l'objet portant le modifier loin de l'origine du
monde, activer "Suivi Camera", vérifier que le texte s'oriente
correctement vers la caméra quelle que soit la position de l'objet (pas
seulement à l'origine).

*Dépend de : Phase 2 doit fournir une valeur valide dans `Sample Index.002`
— à faire en même temps ou juste avant.*

## Phase 2 — Brancher réellement l'ancrage (position du marqueur)

- [ ] Brancher la sortie de `Sample Index.002` (déjà câblée en entrée,
      inutilisée en sortie) sur la `Translation` du dernier
      `Transform Geometry` avant `Group Output` (aujourd'hui seul le
      pivot/scale y contribue).

**Validation** : brancher un objet ou un point différent sur l'input
`Geometry` du node group, vérifier que le connecteur suit bien cette
nouvelle position.

## Phase 3 — Alignement du texte gauche/droite

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

- [ ] Regrouper visuellement les Frames existantes en deux zones
      clairement nommées : **LOCAL — Widget** (Cartouche / TEXTE /
      CONNECTOR LINE / pivot-scale — rien ici ne doit lire `Object Info`
      ni `Active Camera`) et **MONDE — Placement caméra** (ancrage,
      rotation caméra relative, scale global appliqué en dernier).
- [ ] Documenter cette frontière dans le label des Frames ou une note
      texte à côté, pour que la séparation reste visible en rouvrant le
      fichier plus tard.

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

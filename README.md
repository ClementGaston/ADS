# 📊 Étude sur l'impact des optimisations Web

Ce projet s’inscrit dans une démarche de recherche scientifique. Il a pour objectif de **comprendre l’utilité réelle du temps de chargement d’une page internet** en évaluant différentes **optimisations Web** couramment utilisées.

---

## 🧪 Description du projet

Nous nous intéressons à un ensemble d’optimisations Web connues, que nous testons **une à une** à travers des expériences simples et reproductibles. Le but est de mesurer le **gain réel** apporté par chaque technique d’optimisation et d’en tirer, si possible, des **règles générales**.

Chaque test est réalisé à travers un **fichier `.html`** dédié, **ouvrable localement**, sans besoin de serveur ou d’installation.

---

## 🎯 Objectifs

L’objectif principal est de déterminer **si une optimisation impacte ou non le temps de chargement** d’un site internet.

Plus précisément, nous cherchons à :

-   Identifier les optimisations efficaces
-   Mesurer leur impact réel en pourcentage (temps ou taille)
-   Établir, si possible, une **règle générale d’optimisation**

Par exemple :

> En moyenne, l’optimisation X permet de réduire de Y% le temps de chargement ou de Z% la taille d’un fichier.

---

## 🔬 Déroulement de l’étude

Pour chaque optimisation testée :

-   Une **expérience spécifique** est mise en place dans un fichier `.html`
-   Les **optimisations de taille de fichier** sont mesurées via comparaison directe des tailles
-   Les **optimisations d’affichage rapide** sont évaluées via les temps de rendu visuel
-   Les **optimisations de chargement** sont analysées via les temps moyens enregistrés

Chaque test est **reproductible** et répété plusieurs fois pour garantir la **précision des résultats**.

👉 **Tous les tests sont disponibles dans ce dépôt** sous forme de fichiers `.html` à ouvrir localement.

---

## 📄 Résultats et conclusion

L’étude est considérée comme **réussie** :  
Parmi les 8 optimisations testées, **5 d’entre elles ont démontré une amélioration notable du temps de chargement**.

Il a donc été possible d’en **tirer des règles d’optimisation générales**, réutilisables dans des projets web réels.

---

## 📂 Structure du dépôt

-   `etude.pdf` → Document complet de l’étude avec méthodologie, résultats et analyses
-   `*.html` → Fichiers de test pour chaque optimisation (ouvrables localement)
-   Aucune installation nécessaire

---

## ✅ Lancer les tests

Il vous suffit d’**ouvrir les fichiers `.html` dans votre navigateur**.  
Chaque fichier correspond à un test indépendant d’une optimisation particulière.

Aucun backend, aucune installation, juste du HTML.

---

## 📚 Référence

L’ensemble de l’étude, les hypothèses, les mesures et les conclusions sont disponibles dans le fichier [`etude.pdf`](./etude.pdf).

---

_Dernière mise à jour : 01/09/2021_

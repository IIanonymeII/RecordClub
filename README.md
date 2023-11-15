# RecordClub

## Sommaire
I. [English Version](#i-english-version)
   1. [Single Result](#a-single-result)
   1. [Relays Result](#b-relays-result)
   1. [Warning](#c-warning)
   1. [Improvement](#d-areas-for-improvement)

II. [Version Française](#ii-version-française)
   1. [Résultat Individuel](#a-résultat-individuel)
   1. [Résultats des Relais](#b-résultats-des-relais)
   1. [Avertissement](#c-avertissement)
   1. [Axes d'Amélioration](#d-axes-damélioration)

---

## I. English Version

### A. Single Result

To begin, run the following command to obtain the dataset from 1996 to the present:
```bash
python save_data.py
```
The outcome will be stored as `final.csv`.

Following this, for result analysis, utilize the Jupyter Notebook `single_compet.ipynb`.

### B. Relays Result

For relay data, make sure you have the `final.csv` dataset, then run:
```bash
python save_data_relais.py
```
It will produce a dataset named `final_relai.csv`. Afterward, you can view the results using `relai_compet.ipynb`.

### C. Warning

Please note that both programs involve web scraping, which may take some time. But don't worry, progress bars are there to show you the advancement (technology is amazing).


### D. Areas for Improvement
Not everything is perfect; potential improvements include:

* Extending the program to other clubs
* Getting results directly in an Excel spreadsheet
* Enhancing comments in the code (mixing French and English)
* Further refining certain functions

---

## II. Version Française

### A. Résultat Individuel

Pour commencer, exécutez la commande suivante pour obtenir le jeu de données de 1996 à aujourd'hui :
```bash
python save_data.py
```

Le résultat sera enregistré sous le nom `final.csv`.
Ensuite, pour analyser les résultats, utilisez le calepin Jupyter `single_compet.ipynb`.

### B. Résultats des Relais
Pour les données de relais, assurez-vous d'avoir le jeu de données final.csv, puis exécutez :

```bash
python save_data_relais.py
```

Cela produira un jeu de données appelé final_relai.csv. Ensuite, vous pouvez voir les résultats avec `relai_compet.ipynb`.

### C. Avertissement

Veuillez noter que les deux programmes impliquent du web scraping, ce qui peut prendre du temps. Mais ne vous inquiétez pas, des barres de progression sont là pour vous montrer l'avancement (la technologie est incroyable). 



### D. Axes d'Amélioration
Tout n'est pas parfait, des améliorations possibles comprennent :

* Étendre le programme à d'autres clubs
* Obtenir des résultats directement dans une feuille de calcul Excel
* Améliorer les commentaires dans le code (mélange de français et d'anglais)
* Affiner davantage certaines fonctions
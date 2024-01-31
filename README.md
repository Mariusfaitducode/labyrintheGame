# labyrintheGame

Ce projet permet générer un labyrinthe de manière aléatoire puis de le résoudre. 

Je me suis inspiré d'une vidéo de <a href="https://www.youtube.com/watch?v=K7vaT8bZRuk">Dimension Code</a> et renseigné plus en précision sur 
<a href="https://fr.wikipedia.org/wiki/Mod%C3%A9lisation_math%C3%A9matique_d%27un_labyrinthe" target="_blank">Wikipédia</a>. 

J'ai implémenté 2 algorithmes différents permettant de générer le labyrinthe.
Ces 2 méthodes partent d'un labyrinthe où tous les murs sont fermés puis construisent les chemins en cassant les murs,
résultant ainsi à un vrai labyrinthe :

## Fusion aléatoire de chemins : 
Le programme choisit un mur au hasard, 
qu'il casse si les couleurs des 2 cases à côté sont différentes, 
une fois le mur cassé, la couleur des cases et de l'ancien mur sont uniformisés.
A la fin du programme il ne reste ainsi plus qu'une seule couleur et le labyrinthe est formé.

## Exploration exhaustive :
L'algorithme part d'une case puis casse un des murs autour de la case de manière aléatoire.
Il se déplace ensuite à la nouvelle case dévoilée et la marque comme visitée.
Lorsque une case n'a plus de mur a casser menant à une case non visitée, l'algorithme retourne à la case précédente.

## Résolution algorithme A*
Pour la résolution, il s'agit de l'algorithme A* qui permet de déterminer le chemin le plus court entre 2 points :
Cet algorithme donne une évaluation à chaque case pour définir laquelle il doit visiter en priorité.
Dans notre cas, cette évaluation est réalisée en fonction de la distance qu'il reste à parcourir et du nombre de cases parcourues jusqu'à la case évaluée.

<br><br>
J'ai réutilisé ce projet pour construire le labyrinthe du jeu <a href="https://github.com/Mariusfaitducode/SquaryGame">Squary</a> lors d'une Scientifique Game Jam.

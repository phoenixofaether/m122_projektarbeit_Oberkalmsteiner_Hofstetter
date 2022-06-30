Skript 1

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem input file aufgerufen werden, in welchem nur verfügbare Git-URLs sind. Diese sollen in ein noch nicht existierendes Verzeichnis geklont werden:<pre>git_clone_update_repos.bash repolist.txt /tmp/myrepos</pre> | repolist.txt mit folgendem Inhalt:<pre>https://gitlab.com/armindoerzbachtbz/m122_praxisarbeit Armin_Doerzbach<br>https://gitlab.com/wapdc/InfoSearch/Project-2017 Hans_Meier_Peter_Mueller</pre> | Verzeichnis wird erstellt und alle Repos werden darin geklont | | | |


Skript 2

| Testfall | Testbeschreibung | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - | - |
| Erstmaliger Aufruf | Das Skript soll mit einem Verzeichnis als parameter augerufen werden in welchem 2 Repos sind:<pre> git_extract_commits.bash /tmp/myrepos /tmp/commits.csv</pre> | Verzeichnis mit den GIT-Repos die mit dem Skript 1 geklont wurden:<pre>/tmp/myrepos</pre> | Alle Repos aus /tmp/myrepos werden gelesen und ein File /tmp/commits.csv erstellt mit allen Commits beider Repos | | | |

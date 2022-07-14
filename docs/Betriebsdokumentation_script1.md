# Betriebsdokumentation

[[_TOC_]]

## Einführungstext

Das Skript git_clone_update_repos_input_file kann grundsaetzlich Git Repositories Clonen und Pullen. Dies geschieht basierend auf einem Input File welches der User als Parameter mitgibt.
Ausserdem werden alte Ordner welche nicht im Input File enthalten sind gelöst.

## Installationsanleitung für Administratoren

### Installation

- Repository clonen mit: "git clone https://github.com/phoenixofaether/m122_projektarbeit_Oberkalmsteiner_Hofstetter.git"
- Stelle sicher das python installiert wurde. Dies kannst du tun indem du "py" oder "python" in der Konsole eingibst.
- Stelle sicher das Git isntalliert wurde. Dies kannst du tun indem du "git -v" in der Konsole eingibst.
- Danach muss das Modul GitPython mit "pip isntall GitPython" heruntergeladen werden. (möglicherweise musst du dasselbe bei "argparse", "shutil" und "configparser" wiederholen)

#### Mögliche Fehler

Falls es einen ImportModulError bei dem Modul GitPython auftritt, musst du die Environmentvariable "GIT_PYTHON_REFRESH" auf "quiet" stellen.

### Konfiguration

Dateiname: config.\*

```
[Config]
log_path=<path_to_logging_script>
```

Dateiname: input_file.\*

```
<github/gitlab> <folder_name>
```

....

## Bediensanleitung Benutzer

Verschiebe in den Ordner "...\m122_projektarbeit_Oberkalmsteiner_Hofstetter\bin" in diesem befinden sich die beiden Skripts und Beispiele der Konfigurationsdateien.

Als erstes Editiere das File "git_clone_update_repos_input_file.txt" und gib dort die Githublinks mit den Zugehörigen Ordnernamen ein.
Falls du nicht willst, dass das Logfile im gleichen Ordner als log.log abgespeichert wird, musst du die Datei git_clone_update_repos_config.txt bearbeiten und den Pfad abändern.
Um das Skript dann auszuführen musst du ein Konsolenfenster im Ordner "...\m122_projektarbeit_Oberkalmsteiner_Hofstetter\bin" öffnen.
Danach kannst du mit folgendem Befehl das Skript aufrufen:

```
python .\git_clone_update_repos.py -c .\git_clone_update_repos_config.txt -i .\git_clone_update_repos_input_file.txt -b <Ordner wo die Repos hingecloned werden sollten>
```

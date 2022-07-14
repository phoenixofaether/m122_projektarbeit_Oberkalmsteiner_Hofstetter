# Betriebsdokumentation
[[_TOC_]]
## Einführungstext
Dieses Script liest alle Commits von allen Repositories aus und speichert diese in ein Text-file.

## Installationsanleitung für Administratoren

### Installation
- Klone das repository: "git clone https://github.com/phoenixofaether/m122_projektarbeit_Oberkalmsteiner_Hofstetter.git"
- Du musst sicherstellen, dass Python auf deinem Computer installiert ist. Du kannst Python mit "python" in der Konsole heruntergeladen.
- Du musst sicherstellen, dass Git auf deinem Computer installiert ist. Du kannst git mit "git -v" in der Konsole heruntergeladen.
- Danach muss das Modul GitPython mit "pip install GitPython" heruntergeladen werden. (möglicherweise musst du dasselbe bei "argparse", "shutil" und "configparser" wiederholen)

### Konfiguration
Für die Benutzung dieses Scripts wird keine Konfiguration benötigt.

## Bediensanleitung Benutzer
Verschiebe das Projekt in den Ordner "...\m122_projektarbeit_Oberkalmsteiner_Hofstetter\bin" in diesem befinden sich die beiden Skripts und Beispiele der Konfigurationsdateien.

Als erstes Editiere das File "git_clone_update_repos_input_file.txt" und gib dort die Githublinks mit den Zugehörigen Ordnernamen ein.
Falls du nicht willst, dass das Logfile im gleichen Ordner als example.log abgespeichert wird, musst du die Datei git_clone_update_repos_config.txt bearbeiten und den Pfad abändern.
Um das Skript dann auszuführen musst du ein Konsolenfenster im Ordner "...\m122_projektarbeit_Oberkalmsteiner_Hofstetter\bin" öffnen.
Danach kannst du mit folgendem Befehl das Skript aufrufen:

### Scriptaufruf
python git_extract_commits.py --base_dir_path <path_to_git_directory>

### Erzeugte Files
- example.log: Alle Logs des git_extract_commits.py Scripts werden darin festgehalten
- commits.txt: Liste aller github-commits

### Lokation von logfiles
Logfile wird erstellt, wo du es definiert hast.

# Projekt Dokumentation

[[_TOC_]]

## Lösungsdesign

Anhand der Analyse wurde folgendes Lösungsdesign entworfen.

### Aufruf der Skripte

| Parametername   | Erklärung                                                   | Typ    | Standart |
| --------------- | ----------------------------------------------------------- | ------ | -------- |
| config_path     | Pfad zu deinem Konfigurationsfile                           | string |          |
| input_file_path | Pfad zu deinem File, in dem du die GitRepos definiert hast  | string |          |
| base_dir_path   | Pfad zu deinem Base-Verzeichnis, wo die GitRepos hingehören | string |          |

### Ablauf der Automation

Siehe doc/script1.pdf

### Konfigurationsdateien

Dateiname: config.\*

```
[Config]
log_path=<path_to_logging_script>
```

Dateiname: input_file.\*

```
<github/gitlab> <folder_name>
```

## Abgrenzungen zum Lösungsdesign

TODO: Nachdem das Programm verwirklicht wurde hier die unterschiede von der Implemenatino zum Lösungsdesign beschreiben (was wurde anders gemacht, was wurde nicht gemacht, was wurde zusaetzlich gemacht)

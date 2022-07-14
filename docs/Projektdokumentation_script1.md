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

<object data="../doc/script1.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="./doc/script1.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="./doc/script1.pdf">Download PDF</a>.</p>
    </embed>
</object>

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

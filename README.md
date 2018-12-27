# Promotions

Statische Webseiten um einzelne KRONOS Grades zu promoten

Derzeit sind folgende Seiten enthalten:

| KRONOS Produkt    | Domäne                |
| ------------------|-----------------------|
| KRONOS2066        | kronos2066.com        | 
| KRONOS2360        | kronos2360.com        | 
| KRONOS Ink Grades | kronos-ink-grades.com |
| KRONOBAG          | kronobag.com          | 

Um die Seiten auf S3 hoch laden zu können, wird das CLI von AWS benötigt. Da es
sich hierbei um ein Python Paket handelt, sollte eine virtuelle Umgebung mit
pipenv erstellt und die im Pipfile angegebene Software installiert werden.

Die Batch-Datei sync.sh synchronisiert dann alle oben angegebenen Ordner mit
den entsprechenden S3 Buckets.

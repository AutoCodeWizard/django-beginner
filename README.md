# django-beginner
Ein Repository für Anfänger, um das Django-Framework zu erlernen und zu üben.


### Klonen des Rrepositorys
1. Öffne ein Terminal, gehe in das Verzeichnis, in dem du das Projekt speichern möchtest. (gerne erstmal auf den Desktop)
2. Führe die folgenden Befehle einzeln hintereinander aus, um das Repository zu klonen und in das Verzeichnis des Projekts zu wechseln.
```bash
git clone https://github.com/AutoCodeWizard/django-beginner.git
```
```bash
cd django-beginner
```
```bash
# um die git Verfolgung erstmal auszuschalten
rd /S /Q .git
```

## Virtuelle Umgebung erstellen und verwalten

### Mit conda (Anaconda)
Wenn du nun das integrierte Terminal in VSCode öffnest, solltest du zum einen sehen dass deine Anaconda (base) Umgebung aktiviert ist und dass du dich im richtigen Verzeichnis befindest. z.B. `(base) C:\Users\Benutzer\Desktop\django-beginner>`

Virtuelle Umgebung erstellen:
```bash
conda create --name djangovenv
```
Virtuelle Umgebung aktivieren:
```bash
conda activate djangovenv
```
Danach sollte der Pfad in deinem Terminal so aussehen: `(djangovenv) C:\Users\Benutzer\Desktop\django-beginner>`

```bash
cd final_app
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py runserver
```
Nun sollte die Webseite unter `http://localhost:8000/` erreichbar sein.




```bash
python manage.py createsuperuser
```

http://localhost:8000/admin besuchen


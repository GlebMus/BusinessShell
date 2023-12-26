# Business shell 

### Настройка и запуск проекта:
  - Провести миграции командами  
```bash
python manage.py makemigrations
python manage.py migrate
```
  - Загрузить данные фикстур в папке post командой 
```bash
python manage.py dumpdata > post/fixtures/data.json
```

  - Установить зависимости проекта из файла 
```bash
pip install -r requirements.txt
```
  - Запустить сервер командой 
```bash
python manage.py runserver
```

### Используемый стек 
  - Python 3.10
  - Django
  - Django Rest Framework
### Используемые библиотеки 
  - Django allauth
  - corsheaders
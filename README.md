### Запуск сервера FLASK
```
Linux и Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run

Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
```

### Запуск postgres и adminer контейнеров
```
docker-compose up
```
### Создаем таблицы из метаданных Base.metadata.create_all(engine)
Вызывается только один раз при пустой базе
```
python3 models.py
```
### Flask main app
```
python __init__.py
```


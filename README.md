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
python main.py
```


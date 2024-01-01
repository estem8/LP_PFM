### Запуск сервера FLASK
```
Linux, Mac и Windows: flask run --debug
```

### Создаем таблицы из метаданных Base.metadata.create_all(engine)
Вызывается только один раз при пустой базе
`python3 app/user/models.py` - Linux
`python3 app\user\models.py` - Windows

### Линтеры
#### black
`black -v --check --diff --color --config black.cfg app` - для проверки, не будет автоматом исправлять - выведет в 
консоль замечания.

`black --config black.cfg app` - для автоматического исправления

#### isort
`isort -v --check-only --diff --color  app` - для проверки, не будет автоматом исправлять - выведет в 
консоль замечания.

`isort app` - для автоматического исправления

#### flake8
`flake8 app` - проверит код на ошибки

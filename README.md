### Деплоймент на прод
#### CI
##### с использованием *poetry*
`poetry install --without dev, test --no-root`

##### с использованием *pip*
`pip install -r requirements/prod.txt`

### Среда разработки
##### с использованием *poetry*
`poetry install --with dev --no-root`

##### с использованием *pip*
`pip install -r requirements/dev.txt`

### Среда тестирования
##### с использованием *poetry*
`poetry install --with test --no-root`

##### с использованием *pip*
`pip install -r requirements/test.txt`


### Запуск сервера FLASK
```
Linux, Mac и Windows: flask run --debug
```

### Создаем таблицы из метаданных Base.metadata.create_all(engine)
Вызывается только один раз при пустой базе
```
python3 models.py
```

### Линтеры
#### black
`black -v --check --diff --color app` - для проверки, не будет автоматом исправлять - выведет в 
консоль замечания.

`black app` - для автоматического исправления

#### isort
isort -v --check-only --diff --color  app - для проверки, не будет автоматом исправлять - выведет в 
консоль замечания.

`isort app` - для автоматического исправления

#### flake8
`flake8 app` - проверит код на ошибки

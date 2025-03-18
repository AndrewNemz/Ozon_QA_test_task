# Ozon_QA_test_task

# Как запустить

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AndrewNemz/Ozon_QA_test_task.git

cd Ozon_QA_test_task
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

### Для *nix-систем:

```
source venv/bin/activate
```

### Для windows-систем:

```
source venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Для запуска тестов:

```
python -m unittest get_my_hero_func_tests
```

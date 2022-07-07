# 1)
# python3 -m venv venv - создаем виртуальное окружение
# source venv/bin/activate - активируем
# pip freeze - показывает список установленных библиотек
# deactivate - выйти из виртуального окружения

#########################################

# 2) requirements.txt
    # django
    # djangorestframework

# 3) pip install -r requirements.txt


# 4) django-admin startproject name_project . - создаем главное приложение нашего проекта  

# 5) django-admin startapp new_name_app - создаем определенное приложение
# ./manage.py startapp new_name_app

# 6)
# ./manage.py makemigrations - создает миграцию
# ./manage.py migrate - применяет ее

# ./manage.py createsuperuser - создает супер юзера

# ./manage.py runserver
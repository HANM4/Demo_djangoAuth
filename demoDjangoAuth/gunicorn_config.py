bind = "0.0.0.0:80" #Порт, который будет слушать Django
workers = 3 # Кол-во запущенных процессов
user = "root" #Пользователь, от имени которого будет запущен Django
raw_env = "DJANGO_SETTINGS_MODULE=demoDjangoAuth.settings" #Переменная окружения с setting.py
loglevel = "debug"
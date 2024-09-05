# Start
## First start project(with base DB) with Docker
1. `docker-compose build`
2. `docker-compose up -d`

## First start project(sans base DB) with Docker
1. Удаляем папку data/postgres
2. `docker-compose build`
3. `docker-compose up -d`
Запоминаем CONTAINER_ID_djnago -- меняем на айди вашего контейнера django который выводится командой `docker ps`
4. `docker exec -it CONTAINER_ID_djnago /bin/bash`
5. `./docker_first_up.sh` запуск скрипта для первого запуска проекта (создаём статик файлы, запускаем миграцию, создаем супер пользователя)
6. `exit` или ctrl +z выход из терминала контейнера

#  Здравствуйте, уважаемый проверяющий!

#### Представляю Вам мое решение технического задания:
https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit

****

#### Для запуска контейнеров - необходимо:

------------


1.  Установить все необходимое в файле *.env*:

	- DJANGO ключ
	- Публичный STRIPE ключ
	- Секретный STRIPE ключ


2. Построить сервисы с помощью комманды *docker-compose up -d --build*

`docker-compose up -d --build`

3. Перейти в режим конфигурации контейнеров в фоновом режиме.

`docker-compose up -d`

4. Применить к контейнеру web миграции с помощью следующих комманд:

`docker-compose exec web python manage.py makemigrations`

`docker-compose exec web python manage.py migrate`

5.  Для просмотра моделей в админке Django необходимо создать superuser'а

 `docker-compose exec web python createsuperuser`

# ГОТОВО!

###### После всех операций можно идти в админку `localhost/admin` и создавать тестовые заказы и предметы. Для просмотра и тестовой покупи объектов надо перейти на главную страницу проекта `localhost`. 

#### Буду очень благодарен, если Вы поделитесь мнением о моей работе.
# Спасибо за внимание! :smile:

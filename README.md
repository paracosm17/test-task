# Тестовое задание

## Задачи
1. Поднять Django 3
2. Сделать авторизацию
3. Сделать возможность редактирования своего профиля по API
4. Описать методы в redoc/swagger
5. Обернуть в Docker
6. Запушить на GitHub
7. Выгрузить на сервер и развернуть (доступ пришлю по ключу)
8. Настроить автодеплой (https://github.com/artempy/Git-Auto-Deploy)
9. Настроить уведомление на мой email об успешном автодеплое (реализован в Git-Auto-Deploy)

## Реализация
Реализована модель кастомного пользователя, а также модель автомобиля. У пользователя есть поля email, password,
username, country, first_name, last_name. Также каждому пользователю можно добавить
владение автомобилем. У автомобиля есть поля make, model, year, color. 

Реализовано создание, обновление пользователей с помощью API (drf). Доступ к апи получается с помощью
JWT токенов. После регистрации пользователю выдается бессрочный JWT токен, который можно использовать при запросах к апи.
Также его можно получить после входа в аккаунт.

Также есть динамическая генерация документации API на redoc (drf_yasg)

* GET api/user/ - Просмотр информации об аккаунте
* POST api/register/ - регистрация аккаунта
* POST api/login/ - Вход в аккаунт
* GET api/cars/ - Список автомобилей текущего пользователя
* POST api/cars/ - Добавить текущему пользоваптелю автомобиль
* PATCH api/user/ - Обновить данные профиля

Для авторизации по токену передавать заголовок `Authorization: JWT your_token`

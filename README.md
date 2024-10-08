# Yatube API

## Описание проекта

Yatube — это платформа для блогов. Проект реализует REST API для взаимодействия с платформой, предоставляя возможности для создания, редактирования, удаления и получения информации о постах, комментариях, группах и подписках. API может использоваться для разработки мобильных приложений, чат-ботов, а также для взаимодействия с фронтендом.

## Установка

### Клонирование репозитория

```
git clone https://github.com/<ваш_github>/api_final_yatube.git
```

### Создание виртуального окружения

```
python3 -m venv env
```

### Активация виртуального окружения

* Linux/macOS:

```
source env/bin/activate
```

* Windows:

```
source env/scripts/activate
```

### Установка зависимостей

```
pip install -r requirements.txt
```

### Выполнение миграций

```
python3 manage.py migrate
```

## Запуск проекта

```
python3 manage.py runserver
```

### Документация

Документация API в формате Redoc доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

## Аутентификация

Для аутентификации используются JWT-токены. Получить токены можно, отправив POST-запрос на endpoint `/api/v1/jwt/create/`.

## Права доступа

* Неаутентифицированные пользователи имеют доступ к API только на чтение. Исключение - endpoint `/api/v1/follow/`, доступ к которому предоставляется только аутентифицированным пользователям.

* Аутентифицированные пользователи могут изменять и удалять свой контент. В остальных случаях доступ предоставляется только для чтения.

## Примеры запросов

### Получение списка всех публикаций

```
GET /api/v1/posts/
```

### Создание новой публикации

```
POST /api/v1/posts/

{
  "text": "Текст новой публикации"
}
```

### Получение всех подписок пользователя

```
GET /api/v1/follow/

Authorization: Bearer <JWT-токен>
```

### Подписка на пользователя

```
POST /api/v1/follow/

{
  "following": "username_пользователя"
}

Authorization: Bearer <JWT-токен>
```

## Автор

Богданов Дмитрий

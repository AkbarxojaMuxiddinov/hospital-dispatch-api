<div align="center">
  <img src="assets/siren-response.svg" alt="SIREN — система управления экстренными вызовами" width="100%">
  <br>
  <img src="https://img.shields.io/badge/Django-REST-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Django REST">
  <img src="https://img.shields.io/badge/JWT-auth-111827?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/OpenAPI-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=111827" alt="OpenAPI">
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <p><strong>Вызов принят. Ресурс назначен. Статус виден.</strong></p>
</div>

**SIREN** — backend API для учёта больниц, машин скорой помощи и экстренных вызовов. В проекте есть роли пациента, водителя, врача и администратора, JWT-вход и интерактивная документация.

## Сценарий диспетчеризации

```mermaid
sequenceDiagram
    participant P as Пациент
    participant API as SIREN API
    participant DB as База данных
    participant A as Скорая помощь
    P->>API: Создать экстренный вызов
    API->>DB: Найти доступную машину
    alt Машина доступна
        API->>A: Назначить и отметить BUSY
        API->>DB: Сохранить вызов DISPATCHED
    else Свободной машины нет
        API->>DB: Сохранить вызов PENDING
    end
    API-->>P: Вернуть карточку вызова
```

Назначение в текущей реализации выбирает первую доступную машину; выбор по расстоянию не реализован.

## Маршруты

| Метод | Путь | Назначение |
|---|---|---|
| `POST` | `/api/accounts/register/` | Зарегистрировать пользователя и роль |
| `POST` | `/api/accounts/login/` | Получить JWT пару |
| `POST` | `/api/accounts/token/refresh/` | Обновить access токен |
| `GET/POST` | `/api/hospital/hospitals/` | Список больниц / создание |
| `GET/POST` | `/api/hospital/ambulances/` | Список машин / создание |
| `GET/POST` | `/api/hospital/calls/` | Просмотр или создание вызова |
| `GET` | `/api/docs/` | Swagger UI |
| `GET` | `/api/redoc/` | ReDoc |

При чтении вызовов пациент получает собственные записи, водитель — вызовы назначенной ему машины. Доступ к маршрутам дополнительно зависит от роли.

## Модель данных

```text
Hospital ──< Ambulance >── Driver
                  │
                  └──< EmergencyCall >── Patient
```

Вызов хранит координаты, описание симптомов, приоритет и статус. Машина имеет состояние `AVAILABLE`, `BUSY` или `MAINTENANCE`; у больницы ведётся число доступных мест.

## Запуск

```bash
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте `http://127.0.0.1:8000/api/docs/` для Swagger UI. Локальные настройки проекта используют SQLite.

## Технологии

`Python` · `Django REST Framework` · `SimpleJWT` · `drf-spectacular` · `SQLite`

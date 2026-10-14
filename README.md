# 🏥 Hospital & Ambulance Dispatch System API

Production-grade backend API, разработанный с использованием **Django REST Framework (DRF)** для управления ресурсами больниц, экстренными вызовами (SOS) и автоматического распределения машин скорой помощи.

---

## 🚀 Основные возможности
- **Кастомная модель пользователя и роли:** Разграничение прав доступа для ролей `PATIENT` (Пациент), `DRIVER` (Водитель), `DOCTOR` (Врач) и `ADMIN` (Администратор).
- **JWT-аутентификация:** Безопасный вход и обработка запросов с помощью `djangorestframework-simplejwt`.
- **Автоматическое назначение (Auto-dispatch):** Система автоматически находит свободную скорую помощь, переводит ее статус в `BUSY` и привязывает к новому экстренному вызову.
- **Кастомные права доступа (Custom Permissions):** Строгие правила на уровне объектов, гарантирующие, что пользователи имеют доступ только к разрешенным данным.
- **Документация API:** Интерактивные интерфейсы Swagger UI (`/api/docs/`) и Redoc (`/api/redoc/`), реализованные через `drf-spectacular`.

---

## 🛠️ Технологический стек
- **Python 3.x / Django**
- **Django REST Framework (DRF)**
- **PostgreSQL / SQLite**
- **SimpleJWT**
- **drf-spectacular (OpenAPI 3)**

---

## ⚙️ Установка и локальный запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/hospital-dispatch-api.git](https://github.com/YOUR_USERNAME/hospital-dispatch-api.git)
   cd hospital-dispatch-api
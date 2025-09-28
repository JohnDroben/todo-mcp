# 📝 To-Do MCP Project

Простой демонстрационный проект:
- MCP-сервер (FastAPI) хранит список задач
- API (FastAPI) — прокси к MCP
- Telegram-бот — интерфейс для пользователя

## 🚀 Локальный запуск

1. Установите зависимости:

```bash
pip install -r requirements.txt
```

2. Запустите MCP-сервер:

```bash
uvicorn mcp_server.server:app --port 8000
```

3. Запустите API:

```bash
uvicorn api.main:app --port 8001
```

4. Запустите бота (вставьте токен в `bot/bot.py`):

```bash
python bot/bot.py
```

## GitHub Actions: сборка и публикация образов в GHCR

Этот репозиторий содержит workflow `.github/workflows/build-and-push.yml`, который автоматически собирает Docker-образы и пушит их в GitHub Container Registry (GHCR) при пуше в ветку `main`.

### Секреты

Добавьте secret в репозиторий для аутентификации в GHCR:

- `GHCR_PAT` — Personal Access Token с правами `write:packages` (рекомендуется fine-grained token с правом `Write packages`). Если `GHCR_PAT` не задан, workflow попытается использовать `GITHUB_TOKEN` и права `packages: write`.

Создание PAT:

1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token (fine-grained).
2. Выберите owner (ваша учётная запись) и scopes: `Write packages`, `Read packages`.
3. Скопируйте токен и добавьте его в репо: Settings → Secrets and variables → Actions → New repository secret → `GHCR_PAT`.

### Что делает workflow

- Строит Docker-образы по `todo-mcp/Dockerfile`.
- Тегирует их как `ghcr.io/<owner>/todo-mcp-api:latest`, `ghcr.io/<owner>/todo-mcp-mcp-server:latest`, `ghcr.io/<owner>/todo-mcp-bot:latest`.
- Пушит образы в GHCR.

Если вам нужно, могу добавить версионирование тегов (по git tag или sha) — скажите формат.

---
Спасибо! На сегодня все изменения зафиксированы и запушены в `main`.
# 📝 To-Do MCP Project

Простой демонстрационный проект:
- MCP-сервер (FastAPI) хранит список задач
- API (FastAPI) — прокси к MCP
- Telegram-бот — интерфейс для пользователя

## 🚀 Запуск

1. Установи зависимости:
```bash
pip install -r requirements.txt


Запусти MCP-сервер:

uvicorn mcp_server.server:app --port 8000


Запусти API:

uvicorn api.main:app --port 8001


Вставь свой токен в bot/bot.py и запусти бота:

python bot/bot.py


В Telegram:

/add купить молоко

/list

/done 1



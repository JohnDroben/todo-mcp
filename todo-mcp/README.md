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



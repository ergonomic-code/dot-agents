# Подключение контекста задачи

При первом пользовательском запросе сессии ровно один раз передай его дословно через stdin в `python3 framework_checkout_root/src/task-workdir/load_task_context.py --repo-root "$(git rev-parse --show-toplevel)"`.
Используй stdout как контекст задачи до конца сессии.
Если загрузчик сообщает `Active task: none`, укажи это в чате и продолжай без контекста задачи.

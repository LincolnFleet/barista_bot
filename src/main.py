# /src/main.py
import os as OS
import tasks.core as TasksCore
import tasks.admin as TasksAdmin
import tasks.util as TasksUtil

# service should be determined on init, hardcoded for now
chat_service = "discord"

# globals
DEFAULT_TRIGGER_CHAR = "?"
DEFAULT_ARGS_DELIMITER = ";"

match chat_service:
  case "discord":
    import integrations.discord
  case "slack":
    import integrations.slack
    # not yet implemented
  case _:
    print(f"Barista_bot - Unrecognized chat_service: {chat_service}")

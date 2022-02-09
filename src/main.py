# /src/main.py
import tasks.core as TasksCore
import tasks.admin as TasksAdmin
import tasks.util as TasksUtil

# this could be determined during bot's handshake with service
# hardcoded for now 
chat_service = "discord"

match chat_service:
  case "discord":
    import integrations.discord
  case "slack":
    import integrations.slack
    # not yet implemented
  case _:
    print(f"Barista_bot - Unrecognized chat_service: {chat_service}")

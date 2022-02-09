# /src/integrations/discord/main.py

# import slack as SLACK # official lib - async
import OS
import message as Message

# integration bindings
slack_args_delimiter = DEFAULT_ARGS_DELIMITER
slack_bot_token = OS.environ['SLACK_BOT_TOKEN']
slack_client = None # not yet implemented
slack_trigger_char = DEFAULT_TRIGGER_CHAR

if message.content.startswith(slack_trigger_char):
	{ original, trigger, action, arguments } = Message.parse(message)

slack_client.run(slack_bot_token)

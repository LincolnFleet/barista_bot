# /src/integrations/discord/main.py

import slack as SLACK # official lib - async
import os
import parse_message as ParseMessage
import message_actions as MessageActions

# package globals
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_TRIGGER_CHAR = "?"
SLACK_CLIENT = SLACK.client()
SLACK_ARG_DELIMITER = ";"

# bot globals
BOT_TOKEN = SLACK_BOT_TOKEN
TRIGGER_CHAR = SLACK_TRIGGER_CHAR
CLIENT = SLACK_CLIENT

# on_ready: fires when bot has successfully init
@SLACK_CLIENT.event
async def on_ready():
  print(f"Bot has logged in as {SLACK_CLIENT.user}")

# on_message: fires when a message is posted in any channel the bot has access to
# Message shape
# {
#   author: {String},
#   content: {String},
# }
@SLACK_CLIENT.event
async def on_message(message):
  # ignore if message is from bot
  if message.author == SLACK_CLIENT.user:
    return

  # remove beginning and end whitespace from message content
  message.content = message.content.strip()

  if message.content.startswith(SLACK_trigger):
    { original, trigger, action, arguments } = parse_message_SLACK(message)

SLACK_CLIENT.run(SLACK_BOT_TOKEN)

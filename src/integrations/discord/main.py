# /src/integrations/discord/main.py

import discord as DISCORD # official lib - async
import os as OS
import message as Message

# integration bindings
discord_args_delimiter = DEFAULT_ARGS_DELIMITER
discord_bot_token = OS.environ['DISCORD_BOT_TOKEN']
discord_client = DISCORD.Client()
discord_trigger_char = DEFAULT_TRIGGER_CHAR

# on_ready: fires when bot has successfully init
@discord_client.event
async def on_ready():
  print(f"Bot has logged in as {discord_client.user}")

# on_message: fires when a message is posted in any channel the bot has access to
# Message shape
# {
#   author: {String},
#   content: {String},
# }
@discord_client.event
async def on_message(message):
  # ignore if message is from bot
  if message.author == discord_client.user:
    return

  # remove beginning and end whitespace from message content
  message.content = message.content.strip()

  if message.content.startswith(discord_trigger):
    { original, trigger, action, arguments } = Message.parse(message)

discord_client.run(discord_bot_token)

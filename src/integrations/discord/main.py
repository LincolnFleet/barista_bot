# /src/integrations/discord/main.py

import discord as DISCORD # official lib - async
import os
import message as Message
import 

# package globals
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
DISCORD_TRIGGER_CHAR = "?"
DISCORD_CLIENT = DISCORD.client()
DISCORD_ARG_DELIMITER = ";"

# bot globals
BOT_TOKEN = DISCORD_BOT_TOKEN
TRIGGER_CHAR = DISCORD_TRIGGER_CHAR
CLIENT = DISCORD_CLIENT

# on_ready: fires when bot has successfully init
@DISCORD_CLIENT.event
async def on_ready():
  print(f"Bot has logged in as {DISCORD_CLIENT.user}")

# on_message: fires when a message is posted in any channel the bot has access to
# Message shape
# {
#   author: {String},
#   content: {String},
# }
@DISCORD_CLIENT.event
async def on_message(message):
  # ignore if message is from bot
  if message.author == DISCORD_CLIENT.user:
    return

  # remove beginning and end whitespace from message content
  message.content = message.content.strip()

  if message.content.startswith(discord_trigger):
    { original, trigger, action, arguments } = parse_message_discord(message)

DISCORD_CLIENT.run(DISCORD_BOT_TOKEN)

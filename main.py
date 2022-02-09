import discord as DISCORD
import os as OS

client = DISCORD.Client()
bot_token = OS.environ['DISCORD_BOT_TOKEN']
trigger_char = "?"

@client.event
async def on_ready():
	print (f"barista_bot has logged in as {client.user}")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith(f"{trigger_char} hello"):
		await message.channel.send("Hello back!")

client.run(bot_token)

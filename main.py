import discord as DISCORD
import os as OS
import random

client = DISCORD.Client()
bot_token = OS.environ['DISCORD_BOT_TOKEN']
trigger_char = "?"

inspiring_quotes = [
	"Cheer up!",
	"Suck it up!",
	"Stop breaking shit!",
	"You weren't this pathetic this morning. What happened?"
]

indicators_of_sadness = [
	"sad",
	"depressed",
	"overwhelmed",
	"imposter",
	"failure"
]

@client.event
async def on_ready():
	print (f"barista_bot has logged in as {client.user}")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	msg = message.content

	# ignore any message that doesn't start with trigger
	if msg.startswith(f"{trigger_char} "):
		if msg[2:].startswith("hello"):
			await message.channel.send("Hello back!")
		if msg[2:].startswith("goodbye"):
			await message.channel.send("Until next time!")
	# tasks which don't require the message to start with trigger
	else:
		if any(word in msg for word in indicators_of_sadness):
			await message.channel.send(random.choice(inspiring_quotes))

	

client.run(bot_token)

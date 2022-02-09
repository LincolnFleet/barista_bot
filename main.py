import discord as DISCORD
import os as OS
import random as Random
import requests as Requests
import json as JSON
from replit import db as DB

client = DISCORD.Client()
bot_token = OS.environ['DISCORD_BOT_TOKEN']
trigger_char = "?"

DB["encouragements"] = [
	"Cheer up!",
	"Suck it up!",
	"Stop breaking shit!",
	"You weren't this pathetic this morning. What happened?"
]

DB["indicators_of_sadness"] = [
	"sad",
	"depressed",
	"overwhelmed",
	"imposter",
	"failure"
]

def get_inspiring_quote():
	response = Requests.get("https://www.zenquotes.io/api/random")
	data = JSON.loads(response.text)
	return data[0]['q'] + "\n - " + data[0]['a']

def add_encouragement(new_msg):
	if "encouragements" in DB.keys():
		encouragements = DB["encouragements"]
		encouragements.append(new_msg)
		DB["encouragements"] = encouragements
	else:
		DB["encouragements"] = [new_msg]

def delete_encouragement(target_idx):
	encouragements = DB["ecouragements"]
	if len(encouragements) > target_idx:
		del encouragements[target_idx]
		DB["encouragements"] = encouragements

@client.event
async def on_ready():
	print (f"barista_bot has logged in as {client.user}")

@client.event
async def on_message(message):
	# Guard: if message author is barista_bot, skip
	if message.author == client.user : return

	msg = message.content

	# ignore any message that doesn't start with trigger
	if msg.startswith(trigger_char):

		if msg.startswith("?hello"):
			await message.channel.send("Hello back!")

		if msg.startswith("?goodbye"):
			await message.channel.send("Until next time!")

		if msg.startswith("?inspire"):
			await message.channel.send(get_inspiring_quote())
		
		if msg.startswith("?new "):
			new_entry = msg.split("?new ", 1)
			if new_entry.startswith("encouragement "):
				new_msg = new_entry.split("encouragement ", 1)
				add_encouragement(new_msg)


	# tasks which don't require the message to start with trigger
	else:
		if any(word in msg for word in DB["indicators_of_sadness"]):
			await message.channel.send(Random.choice(DB["encouragements"]))

client.run(bot_token)

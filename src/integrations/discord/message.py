# /src/integrations/discord/message.py
import re as Regex

# parses discord's event messages into a common API
class Message:
	def __init__(self, message):
		rgx = Regex.compile(f"^({discord_trigger_char})\s*)(\w+\s*)(.*)")
		match = rgx.match(message.content.strip())
		
		self.original		= message
		self.author			= message.author
		self.content		= message.content
		self.trigger		= match.group(1).strip()
		self.action			= match.group(2).strip()
		self.arguments	= [arg.strip() for arg in match.group(3).split(discord_args_delimiter)]

	def as_json(self):
		return {
			"original"	: self.message,
			"author"		: self.author,
			"content"		: self.content,
			"trigger"		: self.trigger,
			"action"		: self.action,
			"arguments"	: self.arguments
		}

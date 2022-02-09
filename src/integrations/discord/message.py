# /src/integrations/discord/message.py
import re as Regex

# parses discord's event messages into a common API
def parse(message):
  # strip off trigger portion
  rgx = Regex.compile(f"^({discord_trigger_char})\s*)(\w+\s*)(.*)")
  match = rgx.match(message.content)
  
  return {
		"message": message,
    "original": match.group(0),
    "trigger": match.group(1).strip(),
    "action": match.group(2).strip(),
    "arguments": [arg.strip() for arg in match.group(3).split(discord_args_delimiter)]
  }

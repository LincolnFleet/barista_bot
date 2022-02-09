# /src/integrations/discord/message.py

import re as Regex

# parses discord's event messages into a common API
def parse(message):
  # strip off trigger portion
  rgx = Regex.compile(f"^({DISCORD_TRIGGER})\s*)(\w+\s*)(.*)")
  match = rgx.match(message.content)
  
  return {
    "original": match.group(0),
    "trigger": match.group(1).strip(),
    "action": match.group(2).strip(),
    "arguments": [arg.strip() for arg in match.group(3).split(DISCORD_ARG_DELIMITER)]
  }

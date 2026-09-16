"""
load and store enviroment variables from the .env
"""

import os
import sys
import typing

from dotenv import load_dotenv

from utils import Log

IS_MISSING: bool = False

DISCORD_BOT_TOKEN: str
DISCORD_GUILD_ID: str

load_dotenv()
annotations = typing.get_type_hints(sys.modules[__name__])

for env_variable_name in annotations:
    if env_variable_name == "IS_MISSING":
        continue

    if globals().get(env_variable_name) is not None:
        continue

    env_variable = os.getenv(env_variable_name)

    if not env_variable:
        Log.error("ENV", f"missing {env_variable_name}")
        IS_MISSING = True
        continue

    globals()[env_variable_name] = env_variable

if IS_MISSING:
    sys.exit(1)

import discord
import sqlite3
from loader import *

from discord.ext import commands, tasks
con = essential.con
client = essential.client

from dotenv import load_dotenv
try:
    load_dotenv()
except:
    nothing=5

client.run(os.getenv('TOKEN'))

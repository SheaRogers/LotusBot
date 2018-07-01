import discord
from functions.status import StatusFuncs
import signal

TOKEN = 'NDYzMDIzNjMyNzcyMzY2MzM4.DhqYMw.GtsWxLsNse84J7bfIQxnhwp58Lo'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!alerts'):
        stat = StatusFuncs()
        msg = stat.Alerts()
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

try:
    client.run(TOKEN)
except KeyboardInterrupt:
    print("W: interrupt received, stopping…")
finally:
    client.close()
    quit

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

    cmd = message.content.split(' ')
    if cmd[0] == "~alerts":
        await client.delete_message(message)
        stat = StatusFuncs()
        if len(cmd) == 2:
            msg = stat.Alerts(cmd[1])
        else:
            msg = stat.Alerts()
        await client.send_message(message.channel, msg)
    # ~sortie - Shows details on the current sortie
    if cmd[0] == "~sortie":
        await client.delete_message(message)
        stat = StatusFuncs()
        msg = stat.Sortie()
        await client.send_message(message.channel, msg)
    # !purge - purges all output for the bot
    elif cmd[0] == "~purge":
        await client.delete_message(message)
        botMsg = []  # list of messages from bot
        async for x in client.logs_from(message.channel, limit=20):
            if x.author.id == client.user.id:  # ensure message came from bot
                botMsg.append(x)
        await client.delete_messages(botMsg)


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

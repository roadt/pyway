

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
    
        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient(proxy="http://192.168.1.3:8123")
client.run('NzA2NDcxNDQwMTg2MDgxMjgw.Xq6u9Q.4ZacAMuNkNrU__tU7LJEnmSfevU')
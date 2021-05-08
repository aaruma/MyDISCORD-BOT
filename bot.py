import discord
import time 
import asyncio

def token():
    with open ("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = token()

client = discord.Client()

# Wecloming Users 
@client.event
async def on_member_join(member):
    for channel in member.server.channels: # Servers the member joined
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server! {member.mention}""")


# MESSAGES
@client.event
async def on_message(message):
    id = client.get_guild(808863023350415430) # Server id  
    # channels = ["music", "general", etc..]
    bad_words = ["ugly", "gay", "fudge", "Fudge", "FUDGE", "fuck", "bitch", "BITCH", "Bitch", "nigga", "coon", "COON", "Coon", "nigger", "fucking", "cunt", "FUCK", "Fuck", "NIGGER", "NIGGA", "CUNT", "Cunt", "Nigger", "Nigga", "Fucking"]
    troll_words = ["TROLLIN", "Troll"]
    
    for words in troll_words:
        if message.content.count(words) == True:
            print("Some1's trolling")
            await message.channel.send(f"""Stop trolling!!!""")

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit = 1) 

    if str(message.channel) in channels:
        print(message.content) # Checks messages in terminal
       
        if message.content == "!help":
            embed = discord.Embed(title = "Help on BOT", description = "This bot removes bad words and here are some useful commands")
            embed.add_field(name = "!hello", value = "Greets user")
            embed.add_field(name = "!users", value = "Number of members")
            embed.add_field(name = "R u better than Rani?", value = "Shows whose boss")
            embed.add_field(name = "Taken?", value = "Current Relationship status")
            embed.add_field(name = "Troll", value = "Sends a special message")
            await message.channel.send(content = None, embed = embed)

        if message.content == "!hello":
            await message.channel.send(f"""Wassup""")
        if message.content == "!users": 
            await message.channel.send(f"""# of Members {id.member_count}""")
        if message.content == "R u better than Rani?":
            await message.channel.send(f"""OFC I'm better than her, tell that hoe to fight me anytime!!!""")  
        if message.content == "Taken?":
            await message.channel.send(f"""Yessir, Arjen's my man :kissing_heart:.""")
        else: 
            print(f"""User: {message.author} tried to command {message.content}, in channel {message.channel}""")

client.run(token)
import discord

def token():
    with open ("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = token()

client = discord.Client()

@client.event
async def on_member_join(member)
    for channel in member.server.channels: # Servers the member joinned
        if str(channel) = "general":
            await client.send_message(f"""Welcome to the server! {member.mention}""")



@client.event
async def on_message(message):
    id = client.get_guild(808863023350415430) # Server id  
    channels = ["music"]

    if str(message.channel) in channels:
        print(message.content) # Checks messages in terminal
        if message.content.find ("!hello") != -1:
            await message.send("Wassup")
        elif message.content == "!users": 
            await message.channel.send(f"""# of Members {id.member_count}""") 
        else: 
            print("""User: {message.author} tried to command {message.content}, in channel {message.channel}""")
    



client.run(token)
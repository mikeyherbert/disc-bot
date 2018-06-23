import discord

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!welcome'):
        data = message.content.split(" ")
        if(len(data) > 1):
            if(data[1].startswith("<@") and data[1].endswith(">")):
                await client.send_message(message.server.get_channel('459422821718818817'), "Please welcome " + data[1] + " to the server as a full member! " + data[1] + ", you have been promoted to Programmer. If you prove to <@334376933771182080>, a member of @&Management, or another @&Expert that you are worthy of the title of *Expert*, then you will be promoted duely. For now, please do not hesitate to read the *Rules*, and make your way over to *General* and the other member-only channels!")
                memID = data[1].strip("<@").strip(">")
                mem = message.server.get_member(memID)
                role1 = discord.utils.get(message.server.roles, name="Recruit")
                role2 = discord.utils.get(message.server.roles, name="Programmer")
                await client.remove_roles(mem, role1)
                await client.add_roles(mem, role2)
                
        else:
            await client.send_message(message.channel, "Please specify user")
            print("Please specify user")
            
    
    if message.content.startswith('!promote-to-expert'):
        data = message.content.split(" ")
        if len(data) > 1:
            if data[1].startswith("<@") and data[1].endswith(">"):
                await client.send_message(message.server.get_channel('459992736662290442'),"Congratulations " + data[1] + ", you have been promoted to . You have proved to be worthy of this title over the time you have spent as a *Programmer*. We implore you to help others and demonstrate your knowledge by helping others to succeed.")
                memID = data[1].strip("<@").strip(">")
                mem = message.server.get_member(memID)
                role1 = discord.utils.get(message.server.roles, name="Programmer")
                role2 = discord.utils.get(message.server.roles, name="Expert")
                await client.remove_roles(mem, role1)
                await client.add_roles(mem, role2)
                
        else:
            await client.send_message(message.channel, "Please specify user")
            print("Please specify user")
            
    if message.content.startswith('!promote-to-manager'):
        data = message.content.split(" ")
        if len(data) > 1:
            if data[1].startswith("<@") and data[1].endswith(">"):
                await client.send_message(message.server.get_channel('459992736662290442'),"Congratulations " + data[1] + ", you have been promoted to become a member of the @&Management team. You have proved to be worthy of this title over the time you have spent as an Expert. We implore you to help others and demonstrate your knowledge by helping others to succeed, while keeping the server in good running order and carrying out the tasks required of you. Should you not wish to undertake this role, contact <@334376933771182080>, and you will be promoted to *Senior Expert*, showing that you have the required level of knowledge for *Management*, but do not wish to have the same levels of responsibility.")
                memID = data[1].strip("<@").strip(">")
                mem = message.server.get_member(memID)
                role1 = discord.utils.get(message.server.roles, name="Expert")
                role2 = discord.utils.get(message.server.roles, name="Management")
                await client.remove_roles(mem, role1)
                await client.add_roles(mem, role2)
                
        else:
            await client.send_message(message.channel, "Please specify user")
            print("Please specify user")
            
    if message.content.startswith('!promote-to-SE'):
        data = message.content.split(" ")
        if len(data) > 1:
            if data[1].startswith("<@") and data[1].endswith(">"):
                await client.send_message(message.server.get_channel('459992736662290442'),"Congratulations " + data[1] + ", you have been promoted to become a *Senior Expert*. You have proved your expertise time and time again and because of this <@334376933771182080> has decided to promote you to *Senior Expert*. Please demonstrate your immense bank of knowledge by helping others and producing awesome code.")
                memID = data[1].strip("<@").strip(">")
                mem = message.server.get_member(memID)
                role1 = discord.utils.get(message.server.roles, name="Expert")
                role2 = discord.utils.get(message.server.roles, name="Senior Expert")
                await client.remove_roles(mem, role1)
                await client.add_roles(mem, role2)
                
        else:
            await client.send_message(message.channel, "Please specify user")
            print("Please specify user")
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
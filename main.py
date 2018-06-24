import discord

f = open("key.txt")
TOKEN = f.read().strip("\n")  # this is to make sure I don't steal your bot
f.close()

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
                mem = message.mentions[0]
                role1 = discord.utils.get(message.server.roles, name="Recruit")
                role2 = discord.utils.get(message.server.roles, name="Programmer")
                await client.remove_roles(mem, role1)
                await client.add_roles(mem, role2)
                
        else:
            await client.send_message(message.channel, "Please specify user")
            print("Please specify user")
    
    roles = [["expert", "SE", "manager"], ["Expert", "Senior Expert", "Management"]]
    if message.content.startswith('!promote'):
        data = message.content.split(' ')
        if (data[1].startswith("<@") and data[1].endswith(">")) and (data[2] in roles[0]):  # check valid command
            mem = message.mentions[0]
            newrole = roles[1][(roles[0].index(data[2]))]
            role = discord.utils.get(message.server.roles, name=newrole)
            await client.add_roles(mem, role)
            await client.send_message(message.server.get_channel('459992736662290442'),"Congratulations " + data[1] + ", you have been promoted to become a *" + newrole + "*. You have proved your expertise time and time again and because of this <@334376933771182080> has decided to promote you to *" + newrole + "*. Please demonstrate your immense bank of knowledge by helping others and producing awesome code.")
            
        else:
            await client.send_message(message.channel, "Usage:\n`!promote <@username> <role>`\nAvailable roles:\n`expert`, `SE`, `manager`")
            
    helpers = []  # format: [["word", "helper1", "helper2"], ["word", "helper1", "helper2"]]
    if message.content.startswith('!help'):
        # we then search for words and ping people
        i = 0
        pings = ""
        while True:  # maybe re-order the list to use a different searching algorithm?
            try:
                if helpers[i][0] in message.content:
                    for ping in helpers[i]:  # this will also include the word that triggered it. Maybe we could format it better?
                        pings += ping + " "
            except IndexError:  # when we've gone through the list
                break
                
        await client.send_message(message.channel, "Maybe these people can help:\n" + pings)
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

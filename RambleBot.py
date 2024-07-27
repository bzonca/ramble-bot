# Main script
# Invite link:  https://discordapp.com/oauth2/authorize?client_id=478762645428633612&scope=bot
import discord
from discord.ext import commands
import json


color_help = discord.colour.Colour(0xff8233)
color_success = discord.colour.Colour(0x33ffbd)

#Load config data, set token, and set prefix
with open("config.json", "r") as config_file:
    data = json.load(config_file)
    client = commands.Bot(command_prefix = data["prefix"])
    TOKEN = data["token"]

client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Test JSON by printing out config
@client.command()
async def testJSON():
    with open("config.json", "r") as config_file:
        #data is dictionary
        data = json.load(config_file)
        prefix = data["prefix"]
        token = data["token"]
        print("Object type of data : " + str(type(data)))
    print("Prefix : " + prefix)
    print("Token : " + token)

@client.command()
async def testWrite():

    # Convert JSON data from file to dictionary
    with open("config.json", "r") as config_file:
        data = json.load(config_file)

    #Add/Remove/Modify data
    data['New Key'] = 'New value'

    #Write data back to file
    with open('config.json', 'w') as config_file:
        # Write dictionary data to output file (config.json)
        json.dump(data, config_file, indent=4, sort_keys=True)

def writeToConfig(key, value):
    # Convert JSON data from file to dictionary
    with open("config.json", "r") as config_file:
        data = json.load(config_file)

    #Add/Remove/Modify data
    data[key] = value

    #Write data back to file
    with open('config.json', 'w') as config_file:
        # Write dictionary data to output file (config.json)
        json.dump(data, config_file, indent=4, sort_keys=True)

@client.command()
async def sub(name):
    output = name;
    await client.say(output)

@client.command()
async def unsub(name):
    output = name;
    await client.say(output)

@client.command()
async def echo(*args):
    output = ""
    for word in args:
        output += word
        output += ' '

    await client.say(output)


#Commands to give user option to set methods
@client.command()
async def set(*args):

    property = ""
    newValue = ""
    try:
        property = args[0]
        newValue = args[1]
    except IndexError:
        embed = discord.Embed(title=" ", color=color_help)
        embed.set_author(name="Set Help ")
        embed.add_field(name= client.command_prefix + 'set', value='Shows this help menu', inline=False)
        embed.add_field(name= client.command_prefix + 'set prefix ______', value='Set the command prefix to something else. It could be a character or word', inline=False)
        await client.say(embed=embed)
        pass
    else:
        if property == "prefix":
            print ("Set prefix to " + newValue)
            client.command_prefix = args[1]
            writeToConfig("prefix", client.command_prefix)
            embed=discord.Embed(color=color_success)
            embed.add_field(
                name="Command prefix updated to " + client.command_prefix,
                value="All commands now use " + client.command_prefix + " before them. Type " + client.command_prefix +
                "help for more info", inline=False
            )
            await client.say(embed=embed)
        else:
            await client.say("Not a valid property to set")
        pass

@client.command()
async def help():

    embed = discord.Embed(title=" ", color=color_help)
    embed.set_author(name="Ramble Bot Help ")
    embed.add_field(name= client.command_prefix + 'help', value='Shows this help menu', inline=False)
    embed.add_field(name= client.command_prefix + 'set', value='Shows the set menu. Used to set preferences', inline=False)
    await client.say(embed=embed)

client.run(TOKEN)

import os
import json
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

def unwrap(name):#unwrap the json sheet into a unested dict
    sheet = {}
    with open('output.json') as f:
        data = json.load(f)

    for key,value in data[name].items():#this is the loop to get all nested dictionaries, 3 levels in, and unwrap in a unested dict
        if type(value) == dict:
            for key1,value1 in value.items():
                if type(value1) == dict:
                    for key2 in value1.keys():
                            sheet[key2] = data[name][key][key1][key2]                                  
                else:
                    sheet[key2] = data[name][key][key1]   
        else:
            sheet[key] = data[name][key]      
    return sheet

@bot.command(name = "init")
async def initiative(ctx, name):
    sheet = unwrap(name)
    result = 0
    result = int(sheet["dexterity"]) + int(sheet["wits"]) + int(sheet["alertness"])
    result += random.choice(range(1, 10 + 1))
    await ctx.channel.send(result)


@bot.command(name='print')
async def print(ctx, name, char):
    response=""

    sheet = unwrap(name)
    
    response = char + ": " + sheet[char]
    await ctx.channel.send(response)

@bot.command(name='roll', help='roll from saved sheet \n format: difficulty name characteristic1 characteristic2(optional)')
async def roll(ctx, diff: int, name, *args):


    sheet= {}
    sheet = unwrap(name)                 

    number_of_dice = 0
    for arg in args:
        number_of_dice += int(sheet[arg])

    dice = [
        int(random.choice(range(1, 10 + 1)))
        for _ in range(number_of_dice)
    ]
    dice.sort()
    failure = dice.count(1)
    i=0
    success = 0
    while number_of_dice-1 >= i:
        if dice[i] >= diff:
            success+= 1
        i+=1

    if success == 0 and failure>0:
        result = "CRITICAL FAILURE"
    else:
        result= str(success- failure) + " successes"

    message = name + str(dice) + "\n" + str(number_of_dice) + " dice rolled for " + result

    await ctx.send(message)

@bot.command(name='roll_dice', help='Simulates rolling any dice.')
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice) + " rolled")





bot.run(TOKEN)

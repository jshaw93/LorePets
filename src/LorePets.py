import os
from dotenv import load_dotenv
from twitchio.ext import commands
import asyncio
import random
import json
import locale
from dateutil.parser import parse
import time

locale.setlocale(locale.LC_ALL, 'en_US')
spoke = False
join = False
first_launch = False
pet_dict = {}
playerdatadir = 'Data/playerdata.json'
bossdatadir = 'Data/bosses.json'
expdatadir = 'Data/experience.json'

if not os.path.exists('Data'):
    os.mkdir('Data')
if not os.path.exists(playerdatadir):
    first_launch = True
    print('Launching first time setup!')
    with open('playerdata.json', 'r') as myfile:
        my_content = json.load(myfile)
    with open(playerdatadir, 'w+') as jsonfile:
        json.dump(my_content, jsonfile, indent=4)
if not os.path.exists('Data/.env'):
    if not first_launch:
        first_launch = True
        print('Launching first time setup!')
    with open('.env', 'r') as myfile:
        x = myfile.read()
    with open('Data/.env', 'w+') as file:
        file.write(x)
if first_launch:
    print('First time setup complete, please update data in build/Data/.env!')
    time.sleep(60)
    exit(0)

load_dotenv()

bot = commands.Bot(
    irc_token=os.getenv('TMI_TOKEN'),
    client_id=os.getenv('CLIENT_ID'),
    nick=os.getenv('BOT_NICK'),
    prefix=os.getenv('BOT_PREFIX'),
    initial_channels=[os.getenv('CHANNEL')]
)


async def save(dictionary):
    print('Saving...')
    with open(playerdatadir, 'w') as myfile:
        json.dump(dictionary, myfile, indent=4)


async def save_timer():
    global pet_dict
    await asyncio.sleep(300)
    await save(pet_dict)
    await save_timer()


async def on_start():
    global pet_dict
    with open(playerdatadir, 'r') as jsonfile:
        pet_dict = json.load(jsonfile)
    await save_timer()


async def reset_all():
    for i in pet_dict['Players']:
        pet_dict['Players'][i]['Used'] = 'False'
        pet_dict['Players'][i]['Bossused'] = 'False'


async def async_range(*args):
    for i in range(*args):
        yield i


async def add_pet(ctx, name, pettype, rarity):
    global pet_dict
    name = name.lower()
    try:
        if pettype in pet_dict['Players'][name]['Pets']:
            await ctx.channel.send(f'{name}, you feel like you would have been followed.')
            print(pettype + f'{name}***********************************************')
            return
    except:
        pet_dict['Players'].update({name: {}})
        pet_dict['Players'][name].update({'Pet': {}})
        pet_dict['Players'][name].update({'Gold': {}})
        pet_dict['Players'][name].update({'Used': 'False'})
        pet_dict['Players'][name].update({'Bossused': 'False'})
        pet_dict['Players'][name].update({'Selected': pettype})
        pet_dict['Players'][name].update({"Petlist": []})
        pet_dict['Players'][name].update({'Timestamp': ''})
        pet_dict['Players'][name].update({'BossTimestamp': ''})
        pet_dict['Players'][name].update({'BossTimeLeft': 0})
        pet_dict['Players'][name].update({'Duelselect': ""})
        pet_dict['Players'][name].update({'Duelaccept': "False"})
        pet_dict['Players'][name].update({'Pets': {}})
    pet_dict['Players'][name]['Pet'] = 'True'
    if type(pet_dict['Players'][name]['Gold']) == dict:
        pet_dict['Players'][name]['Gold'] = 0
    pet_dict['Players'][name]['Petlist'].append(pettype)
    pet_dict['Players'][name]['Pets'].update({pettype: {'Type': pettype,
                                                             'Name': 'unnamed',
                                                             'Level': 1,
                                                             'Rarity': rarity,
                                                            'Pets': []}})
    await ctx.channel.send(f'{name} has found a Chat Pet!  An unnamed {pettype}' +
                            ' finds its way into their backpack.')


@bot.event
async def event_ready():
    await on_start()
    await reset_all()
    print('Bot is online!')


@bot.event
async def event_message(ctx):
    global join
    if ctx.author.name.lower() == os.getenv('BOT_NICK').lower():
        return
    await bot.handle_commands(ctx)
    if not join:
        await ctx.channel.send('I have arrived!  !pethelp')
        join = True
    name = ctx.author.name
    petgen = random.randint(1, 5000)
    subpetgen = random.randint(1, 3000)
    petgen2 = random.randint(1, 10000)
    subpetgen2 = random.randint(1, 5000)
    petgen3 = random.randint(1, 14000)
    subpetgen3 = random.randint(1, 7000)
    petgen4 = random.randint(1, 18000)
    subpetgen4 = random.randint(1, 9000)
    petgen5 = random.randint(1, 20000)
    if petgen == 3822:
        if not ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Internet Troll', 1)
        else:
            print(f'{name} rolled for an Internet Troll but was a subscriber!')
    if subpetgen == 2756:
        if ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Internet Troll', 1)
        else:
            print(f'{name} rolled for an Internet Troll but wasn\'t a subscriber!')
    if petgen2 == 6883:
        if not ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Molanisk', 2)
        else:
            print(f'{name} rolled for a Molanisk but was a subscriber!')
    if subpetgen2 == 423:
        if ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Molanisk', 2)
        else:
            print(f'{name} rolled for a Molanisk but wasn\'t a subscriber!')
    if petgen3 == 12766:
        if not ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Nihil', 3)
        else:
            print(f'{name} rolled for a Nihil but was a subscriber!')
    if subpetgen3 == 5622:
        if ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Nihil', 3)
        else:
            print(f'{name} rolled for a Nihil but wasn\'t a subscriber!')
    if petgen4 == 17444:
        if not ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Infernal Demonling', 4)
        else:
            print(f'{name} rolled for an Infernal Demonling but was a subscriber!')
    if subpetgen4 == 6338:
        if ctx.author.is_subscriber:
            await add_pet(ctx, name, 'Infernal Demonling', 4)
        else:
            print(f'{name} rolled for an Infernal Demonling but wasn\'t a subscriber!')
    if petgen5 == 19999:
        await add_pet(ctx, name, 'Chibi Lore', 5)
        print(f'{name} found a Chibi Lore!')
    frostdragonroll = random.randint(1, 30000)
    if frostdragonroll == 27743:
        await ctx.channel.send(f'{name}, you\'ve found an extremely rare, secret pet!')
        await asyncio.sleep(2)
        await add_pet(ctx, name, 'Frost Dragon', 6)
    spiritbeastroll = random.randint(1, 60000)
    if spiritbeastroll == 334:
        await ctx.channel.send(f'{name}, you\'ve found an extremely rare, secret pet!')
        await asyncio.sleep(2)
        await add_pet(ctx, name, 'Spirit Beast', 7)
    gnomechild = random.randint(1, 100000)
    if gnomechild == 9968:
        await ctx.channel.send(f'{name}, you\'ve found an extremely rare, secret pet!')
        await asyncio.sleep(2)
        await add_pet(ctx, name, 'One True Gnome Child', 8)


@bot.command(name='gold')
async def gold(ctx):
    global pet_dict
    name = ctx.author.name
    try:
        goldamount = pet_dict['Players'][name]['Gold']
        goldamount = locale.format_string("%d", goldamount, grouping=True)
        await ctx.send(f'{name}, you have {goldamount} gold!')
    except:
        await ctx.send(f'{name}, you do not own a pet!')


@bot.command(name='sendpet')
async def sendpet(ctx):
    global pet_dict
    name = str(ctx.author.name.lower())
    timestamp = str(ctx.message.timestamp)
    try:
        if 'True' not in pet_dict['Players'][name]['Pet']:
            print('This command is not working correctly!')
            return
        if 'False' in pet_dict['Players'][name]['Used']:
            pet_dict['Players'][name]['Timestamp'] = timestamp
        if 'True' in pet_dict['Players'][name]['Used']:
            d1 = parse(timestamp)
            d2 = parse(pet_dict['Players'][name]['Timestamp'])
            time_left = d2 - d1
            seconds = time_left.total_seconds()
            minutes = int((seconds % 3600) // 60)
            if minutes <= 0:
                pet_dict['Players'][name]['Used'] = 'False'
                await ctx.send(f'{name}, please use the command again!  If it still does not work, contact a mod.')
                return
            await ctx.send(f'{name}, you\'ve already used this command!  Please wait {minutes} minutes ' +
                            'before you use it again!')
            return
        pet_dict['Players'][name]['Used'] = 'True'
        petgold = random.randint(0, 50000)
        randgold = random.randint(1, 5000)
        pettype = pet_dict['Players'][name]['Selected']
        petgold = petgold + (pet_dict['Players'][name]['Pets'][pettype]['Rarity'] * randgold)
        golddata = pet_dict['Players'][name]['Gold']
        petname = pet_dict['Players'][name]['Pets'][pettype]['Name']
        await ctx.send(f'{name}, your {pettype}, {petname}, has left to find some treasure!')
        await asyncio.sleep(1800)
        print(f'{name}\'s pet is halfway done with their farming run!')
        await asyncio.sleep(1800)
        print(f'{name}\'s pet has returned!')
        pet_dict['Players'][name]['Gold'] = golddata + petgold
        newgolddata = locale.format_string("%d", petgold + golddata, grouping=True)
        petgold = locale.format_string("%d", petgold, grouping=True)
        await ctx.send(f'{name}, your {pettype}, {petname}, has returned, and collected {petgold} gold, ' +
                       f'you now have {newgolddata} gold!')
        pet_dict['Players'][name]['Used'] = 'False'
    except:
        await ctx.send(f'{name}, you do not own a pet!')


@bot.command(name='resetpet')
async def resetpet(ctx, name):
    global pet_dict
    if not ctx.author.is_mod:
        return
    name = name.lower().replace('@', '')
    try:
        pet_dict['Players'][name]['Used'] = 'False'
        pet_dict['Players'][name]['Bossused'] = 'False'
        await ctx.send(f'{ctx.author.name}, {name}\'s pet timer has been reset!')
    except:
        await ctx.send('That user does not own a pet!')


@bot.command(name='petpay')
async def petpay(ctx, name, amount):
    global pet_dict
    targname = name.lower().replace('@', '')
    name = ctx.author.name.lower()
    try:
        amount = int(amount)
    except:
        await ctx.channel.send(f'{name}, please input a number for that argument!')
        return
    try:
        gold = pet_dict['Players'][name]["Gold"]
    except:
        await ctx.channel.send(f'{name}, you do not own a pet, and therefore have no gold!')
        return
    try:
        targgold = pet_dict['Players'][targname]['Gold']
    except:
        await ctx.channel.send(f'{name}, that player does not own a pet, and therefore cannot own gold!')
        return
    if gold - amount < 0:
        await ctx.channel.send(f'{name}, you do not have that much gold!')
        return
    pet_dict['Players'][targname]['Gold'] = targgold + amount
    pet_dict['Players'][name]['Gold'] = gold - amount
    formatgold = locale.format_string("%d", amount, grouping=True)
    await ctx.channel.send(f'{name}, you have paid {targname} {formatgold} gold.')


@bot.command(name='renamepet')
async def renamepet(ctx, newname, name2=None, name3=None):
    global pet_dict
    name = ctx.author.name.lower()
    if name2 is not None:
        newname = newname + ' ' + name2
        if name3 is not None:
            newname = newname + ' ' + name3
    try:
        pettype = pet_dict['Players'][name]['Selected']
        pet_dict['Players'][name]['Pets'][pettype]['Name'] = newname
        await ctx.send(f'{ctx.author.name}, your {pettype} has been named {newname}!')
    except:
        await ctx.send(f'{ctx.author.name}, you do not own a pet!')


@bot.command(name='pethelp')
async def pethelp(ctx):
    await ctx.send('https://docs.google.com/document/d/1tlozgA_Y-HYJjM2Cqc47LLnmM1lszbSgB-ap56rDxko/edit?usp=sharing')


@bot.command(name='pet')
async def pet(ctx):
    global pet_dict
    name = ctx.author.name.lower()
    try:
        pettype = pet_dict['Players'][name]['Selected']
        petname = pet_dict['Players'][name]['Pets'][pettype]['Name']
        petlevel = pet_dict['Players'][name]['Pets'][pettype]['Level']
        if 'True' not in pet_dict['Players'][name]['Pet']:
            await ctx.send(f'{name}, you do not own a pet!  !pethelp')
            return
        await ctx.send(f'{name} displays their level {petlevel} {pettype}, {petname}!')
    except:
        await ctx.send(f'{name}, you do not own a pet!  !pethelp')


@bot.command(name='levelup')
async def levelup(ctx, goldvar=None):
    global pet_dict
    gold_cost = 0
    name = ctx.author.name.lower()
    target_gold = goldvar
    try:
        if pet_dict['Players'][name]['Used'] == 'True':
            await ctx.channel.send(f'{ctx.author.name}, please wait until your pet has returned to level up!')
            return
        pettype = pet_dict['Players'][name]['Selected']
        levelvar = pet_dict['Players'][name]['Pets'][pettype]['Level']
        gold = pet_dict['Players'][name]['Gold']
        with open(expdatadir, 'r') as jsonfile:
            json_content = json.load(jsonfile)
            exp_var = json_content['Experience'][str(levelvar)]
            if target_gold is not None:
                if gold < int(target_gold):
                    await ctx.send(f'{ctx.author.name}, you do not have that much gold!')
                    return
                new_gold = int(target_gold)
            else:
                new_gold = gold
            if exp_var > new_gold:
                await ctx.send(f'{ctx.author.name}, you do not have enough gold for the next level! ' +
                               f'{locale.format_string("%d", exp_var, grouping=True)} gold')
                return
            iteration = 0
            async for num in async_range(levelvar, 151):
                if gold_cost >= new_gold:
                    exp_var = json_content['Experience'][str(num - 1)]
                    gold_cost -= exp_var
                    levelvar -= 1
                    print(f'{levelvar} levelvar {iteration} iteration {gold_cost} gold cost {exp_var} exp')
                    break
                levelvar += 1
                iteration += 1
                exp_var = json_content['Experience'][str(num)]
                gold_cost += exp_var
                print(f'{levelvar} levelvar {iteration} iteration {gold_cost} gold cost {exp_var} exp')
            gold -= gold_cost
        pet_dict['Players'][name]['Gold'] = gold
        pet_dict['Players'][name]['Pets'][pettype]['Level'] = levelvar
        petname = pet_dict['Players'][name]['Pets'][pettype]['Name']
        await ctx.send(f'{ctx.author.name}, your {pettype}, {petname} is now level {levelvar}, at the cost of ' +
                       f'{locale.format_string("%d", gold_cost, grouping=True)} gold!')
    except:
        await ctx.send(f'{ctx.author.name}, you do not own a pet!')
        return


@bot.command(name='selectpet')
async def pets(ctx, selection=None):
    global pet_dict
    name = ctx.author.name.lower()
    try:
        if selection is None:
            string = f'{name}, your available pets are: '
            joinlist = []
            joinstring = ', '
            iteration = 0
            for i in pet_dict['Players'][name]['Petlist']:
                joinlist.append(str(iteration) + ': ' + i)
                iteration += 1
            print(joinlist)
            joinstring = joinstring.join(joinlist)
            await ctx.channel.send(string + joinstring)
            return
        try:
            if type(int(selection)) != int:
                await ctx.send(f'{name}, please only use integers (0-9) as the argument for this command!')
                return
        except:
            await ctx.send(f'{name}, please only use integers (0-9) as the argument for this command!')
        else:
            pet_dict['Players'][name]['Selected'] = pet_dict['Players'][name]['Petlist'][int(selection)]
            selected_pet = pet_dict['Players'][name]['Petlist'][int(selection)]
            selected_name = pet_dict['Players'][name]['Pets'][selected_pet]['Name']
            await ctx.send(f'{name}, you have selected your {selected_pet}, {selected_name}, as your active pet!')
            return
    except:
        await ctx.send(f'{name}, you do not own a pet!')


@bot.command(name='petboss')
async def unlock(ctx, target=None, target2=None, target3=None):
    global pet_dict
    name = ctx.author.name.lower()
    timestamp = str(ctx.message.timestamp)
    if target is None:
        with open(bossdatadir, 'r') as jsonfile:
            try:
                pettype = pet_dict['Players'][name]['Selected']
            except:
                await ctx.channel.send(f'{name}, you do not own a pet!')
                return
            pettype = pet_dict['Players'][name]['Selected']
            petlevel = pet_dict['Players'][name]['Pets'][pettype]['Level']
            string = f'{name}, your available bosses are: '
            joinlist = []
            joinstring = ', '
            bosses = json.load(jsonfile)
            for i in bosses['Bosses']:
                if petlevel >= bosses['Bosses'][i]['Level']:
                    i = i.lower()
                    i = i.title()
                    joinlist.append(i)
            joinstring = joinstring.join(joinlist)
            await ctx.channel.send(string + joinstring)
        return
    try:
        pettype = pet_dict['Players'][name]['Selected']
    except:
        await ctx.channel.send(f'{name}, you do not own a pet!')
        return
    timeleft = round(pet_dict['Players'][name]['BossTimeLeft'] / 60)
    if target.lower() == 'time':
        if pet_dict['Players'][name]['Bossused'] == 'False':
            if pet_dict['Players'][name]['Used'] == 'True':
                await ctx.channel.send(f'{name}, you must wait for your pet to return before you can attempt ' +
                                       'a boss!')
                return
            await ctx.channel.send(f'{name}, you can attempt another boss!')
            return
        d1 = parse(timestamp)
        d2 = parse(pet_dict['Players'][name]['BossTimestamp'])
        time_left = d1 - d2
        seconds = time_left.total_seconds()
        minutes = int(seconds / 60)
        timeleft = timeleft - minutes
        await ctx.channel.send(f'{name}, your pet must wait another {timeleft} ' +
                               'minutes before it can do another boss!')
        return
    if target != 'time':
        target = target.upper()
        if target2 is not None:
            target = target.upper() + ' ' + target2.upper()
            if target3 is not None:
                target = target.upper() + ' ' + target3.upper()
    pettype = pet_dict['Players'][name]['Selected']
    petname = pet_dict['Players'][name]['Pets'][pettype]['Name']
    petlevel = pet_dict['Players'][name]['Pets'][pettype]['Level']
    petrarity = pet_dict['Players'][name]['Pets'][pettype]['Rarity']
    gold = pet_dict['Players'][name]['Gold']
    with open(bossdatadir, 'r') as bossjson:
        boss_content = json.load(bossjson)
        bosslist = []
        for i in boss_content['Bosses']:
            bosslist.append(i)
        if target.upper() not in bosslist:
            await ctx.channel.send(f'{name}, that boss does not exist!')
            return
        pet_dict['Players'][name]['BossTimeLeft'] = round((
                                    boss_content['Bosses'][target]['Strength'] / petrarity) + 60) * 60
    if 'True' in pet_dict['Players'][name]['Used']:
        d1 = parse(timestamp)
        d2 = parse(pet_dict['Players'][name]['Timestamp'])
        time_left = d2 - d1
        seconds = time_left.total_seconds()
        minutes = int((seconds % 3600) // 60)
        if minutes <= 0:
            pet_dict['Players'][name]['Used'] = 'False'
            await ctx.send(f'{name}, please use the command again!  If it still does not work, contact a mod.')
            return
        await ctx.send(f'{name}, you\'ve already used this command!  Please wait {minutes} minutes ' +
                       'before you use it again!')
        return
    elif 'True' in pet_dict['Players'][name]['Bossused']:
        print('egg')
        d1 = parse(timestamp)
        d2 = parse(pet_dict['Players'][name]['BossTimestamp'])
        time_left = d1 - d2
        seconds = time_left.total_seconds()
        minutes = int(seconds / 60)
        timeleft = timeleft - minutes
        await ctx.channel.send(f'{name}, your pet must wait another {timeleft} ' +
                               'minutes before it can do another boss!')
        return
    if 'False' in pet_dict['Players'][name]['Bossused']:
        if 'False' in pet_dict['Players'][name]['Used']:
            pet_dict['Players'][name]['Timestamp'] = timestamp
            pet_dict['Players'][name]['BossTimestamp'] = timestamp
    bosslist = []
    boss_str = boss_content['Bosses'][target]['Strength']
    boss_gold = boss_content['Bosses'][target]['Gold']
    boss_pets = boss_content['Bosses'][target]['Pets']
    player_pets = boss_content['Bosses'][target]['Player Pets']
    for i in boss_content['Bosses']:
        if petlevel >= boss_content['Bosses'][i]['Level']:
            bosslist.append(i)
    if target.upper() not in bosslist:
        boss_lvl = boss_content['Bosses'][target]['Level']
        await ctx.channel.send(f'{name}, you need a level {boss_lvl} pet!')
        return
    await ctx.channel.send(f'{name}, your pet {pettype}, {petname}, has left to combat a strong creature!')
    pet_dict['Players'][name]['Used'] = 'True'
    pet_dict['Players'][name]['Bossused'] = 'True'
    await asyncio.sleep(1800)
    print(f'{name}\'s pet is halfway done with their run!')
    await asyncio.sleep(1800)
    cooldown = (boss_str * 60) / petrarity
    newgold = gold + random.randint(1, 100000 * petrarity) + boss_gold
    bringgold = newgold - gold
    bossroll = random.randint(1, 5000)
    if bossroll == 3223:
        petchoice = random.choice(boss_pets)
        pet_dict['Players'][name]['Pets'][pettype]['Pets'].append(petchoice)
        await ctx.channel.send(f'{name}, your pet has returned with a pet {petchoice}!')
    playerpetroll = random.randint(1, 5000)
    if playerpetroll == 4846:
        if player_pets is not None:
            await add_pet(ctx, name, random.choice(player_pets), 100)
    await asyncio.sleep(3)
    pet_dict['Players'][name]['Gold'] = newgold
    await ctx.channel.send(f'{name}, your pet {pettype}, {petname}, has returned with ' +
                           f'{locale.format_string("%d", bringgold, grouping=True)}, you now have ' +
                           f'{locale.format_string("%d", newgold, grouping=True)} gold!  Your {pettype} must' +
                           ' rest for a while before attempting another boss.')
    pet_dict['Players'][name]['Used'] = 'False'
    await asyncio.sleep(cooldown)
    pet_dict['Players'][name]['Bossused'] = 'False'
    print(f'{name}, your {pettype} {petname}, is ready to fight another boss!')
    print(f'{name}\'s pet has returned from their boss run!')


@bot.command(name='petpets')
async def petpets(ctx):
    global pet_dict
    name = ctx.author.name.lower()
    try:
        pettype = pet_dict['Players'][name]['Selected']
    except:
        await ctx.channel.send(f'{name}, you do not own a pet!')
        return
    pets = pet_dict['Players'][name]['Pets'][pettype]['Pets']
    petname = pet_dict['Players'][name]['Pets'][pettype]['Name']
    petlist = []
    joinstring = ', '
    newstring = f'{name}, your {pettype} {petname} has the following pets: '
    for i in pets:
        petlist.append(i)
    if not petlist:
        await ctx.channel.send(f'{name}, your selected pet does not have any pets!')
        return
    joinstring = joinstring.join(petlist)
    await ctx.channel.send(f'{newstring}{joinstring}')


@bot.command(name='petduel')
async def petduel(ctx, arg1, arg2):
    global pet_dict
    name = ctx.author.name.lower()
    arg1 = arg1.replace('@', '')
    try:
        test = pet_dict['Players'][name]['Selected']
    except:
        await ctx.channel.send(f'{name}, you do not own a pet, and therefore have no money to stake!')
        return
    try:
        test = pet_dict['Players'][arg1.lower()]['Selected']
    except:
        await ctx.channel.send(f'{name}, that player does not own a pet, and therefore cannot stake!')
        return
    if int(arg2) > pet_dict['Players'][name]['Gold']:
        await ctx.channel.send(f'{name}, you do not have that much gold!')
        return
    if int(arg2) > pet_dict['Players'][arg1.lower()]['Gold']:
        await ctx.channel.send(f'{name}, that player does not have that much gold!')
        return
    pet_dict['Players'][name]['Duelselect'] = arg1.lower()
    goldvar = int(arg2)
    arg2 = f'{locale.format_string("%d", int(arg2), grouping=True)}'
    await ctx.channel.send(f'@{arg1}, {name} has requested a duel for {arg2} gold!' +
                           '  Type !accept within 30 seconds to accept the duel!')
    await asyncio.sleep(30)
    player1_gold = pet_dict['Players'][name]['Gold']
    player2_gold = pet_dict['Players'][arg1.lower()]['Gold']
    if pet_dict['Players'][arg1.lower()]['Duelaccept'] != 'True':
        print('Command timeout')
        return
    else:
        coin_flip = random.randint(1, 2)
        if coin_flip == 1:
            await ctx.channel.send(f'{name}, your pet won!  You have gained {arg2} gold from {arg1.lower()}!')
            pet_dict['Players'][name]['Gold'] = player1_gold + goldvar
            pet_dict['Players'][arg1.lower()]['Gold'] = player2_gold - goldvar
        elif coin_flip == 2:
            await ctx.channel.send(f'{arg1.lower()}, your pet won!  You have gained {arg2} gold from {name}!')
            pet_dict['Players'][arg1.lower()]['Gold'] = player2_gold + goldvar
            pet_dict['Players'][name]['Gold'] = player1_gold - goldvar
    pet_dict['Players'][name]['Duelselect'] = ""
    pet_dict['Players'][arg1.lower()]['Duelaccept'] = "False"


@bot.command(name='accept')
async def accept(ctx):
    global pet_dict
    name = ctx.author.name.lower()
    for i in pet_dict['Players']:
        if pet_dict['Players'][i]['Duelselect'] == name:
            pet_dict['Players'][name]['Duelaccept'] = "True"
            return


if __name__ == '__main__':
    bot.run()

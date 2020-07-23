import os
from dotenv import load_dotenv
from twitchio.ext import commands
import asyncio
import random
import json
import locale
from dateutil.parser import parse

locale.setlocale(locale.LC_ALL, 'en_US')
spoke = False
join = False
load_dotenv()

bot = commands.Bot(
    irc_token=os.getenv('TMI_TOKEN'),
    client_id=os.getenv('CLIENT_ID'),
    nick=os.getenv('BOT_NICK'),
    prefix=os.getenv('BOT_PREFIX'),
    initial_channels=[os.getenv('CHANNEL')]
)


async def reset_all():
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        for i in json_content['Players']:
            json_content['Players'][i]['Used'] = 'False'
            json_content['Players'][i]['Bossused'] = 'False'
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)


async def async_range(*args):
    for i in range(*args):
        yield i


async def add_pet(ctx, name, pettype, rarity):
    name = name.lower()
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        try:
            if pettype in json_content['Players'][name]['Pets']:
                await ctx.channel.send(f'{name}, you feel like you would have been followed.')
                print(pettype + f'{name}***********************************************')
                return
            test = json_content['Players'][name]
            print(test['Selected'])
            print(f'{name} got a {pettype}***********************************************')
        except:
            json_content['Players'].update({name: {}})
            json_content['Players'][name].update({'Pet': {}})
            json_content['Players'][name].update({'Gold': {}})
            json_content['Players'][name].update({'Used': 'False'})
            json_content['Players'][name].update({'Bossused': 'False'})
            json_content['Players'][name].update({'Selected': pettype})
            json_content['Players'][name].update({"Petlist": []})
            json_content['Players'][name].update({'Timestamp': ''})
            json_content['Players'][name].update({'BossTimestamp': ''})
            json_content['Players'][name].update({'BossTimeLeft': 0})
            json_content['Players'][name].update({'Duelselect': ""})
            json_content['Players'][name].update({'Duelaccept': "False"})
            json_content['Players'][name].update({'Pets': {}})
        json_content['Players'][name]['Pet'] = 'True'
        if type(json_content['Players'][name]['Gold']) == dict:
            json_content['Players'][name]['Gold'] = 0
        json_content['Players'][name]['Petlist'].append(pettype)
        json_content['Players'][name]['Pets'].update({pettype: {'Type': pettype,
                                                                 'Name': 'unnamed',
                                                                 'Level': 1,
                                                                 'Rarity': rarity,
                                                                'Pets': []}})
        with open('playerdata.json', 'w') as jsondump:
            json.dump(json_content, jsondump, indent=4)
        await ctx.channel.send(f'{name} has found a Chat Pet!  An unnamed {pettype}' +
                                ' finds its way into their backpack.')


@bot.event
async def event_ready():
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
        await ctx.channel.send(f'{name}, you\'ve found an extremely rare, secret, pet!')
        await asyncio.sleep(2)
        await add_pet(ctx, name, 'Frost Dragon', 6)
    spiritbeastroll = random.randint(1, 60000)
    if spiritbeastroll == 334:
        await ctx.channel.send(f'{name}, you\'ve found an extremely rare, secret, pet!')
        await asyncio.sleep(2)
        await add_pet(ctx, name, 'Spirit Beast', 7)
    gnomechild = random.randint(1, 100000)
    if gnomechild == 9968:
        await ctx.channel.send(f'{name}, you\'ve found an extremely rare, secret, pet!')
        await asyncio.sleep(2)
        await add_pet(ctx, name, 'One True Gnome Child', 8)


@bot.command(name='addpet')
async def addpet(ctx, name):
    if 'loreosrs' != ctx.author.name.lower():
        return
    name = name.replace('@', '')
    await add_pet(ctx, name, 'Internet Troll', 1)


@bot.command(name='gold')
async def gold(ctx):
    name = ctx.author.name
    try:
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            goldamount = json_content['Players'][name]['Gold']
            goldamount = locale.format_string("%d", goldamount, grouping=True)
        await ctx.send(f'{name}, you have {goldamount} gold!')
    except:
        await ctx.send(f'{name}, you do not own a pet!')


@bot.command(name='sendpet')
async def sendpet(ctx):
    name = str(ctx.author.name.lower())
    timestamp = str(ctx.message.timestamp)
    try:
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            if 'True' not in json_content['Players'][name]['Pet']:
                print('This command is not working correctly!')
                return
            if 'False' in json_content['Players'][name]['Used']:
                json_content['Players'][name]['Timestamp'] = timestamp
            if 'True' in json_content['Players'][name]['Used']:
                d1 = parse(timestamp)
                d2 = parse(json_content['Players'][name]['Timestamp'])
                time_left = d2 - d1
                seconds = time_left.total_seconds()
                minutes = int((seconds % 3600) // 60)
                if minutes <= 0:
                    json_content['Players'][name]['Used'] = 'False'
                    with open('playerdata.json', 'w') as eggfile:
                        json.dump(json_content, eggfile, indent=4)
                    await ctx.send(f'{name}, please use the command again!  If it still does not work, contact a mod.')
                    return
                await ctx.send(f'{name}, you\'ve already used this command!  Please wait {minutes} minutes ' +
                                'before you use it again!')
                return
            json_content['Players'][name]['Used'] = 'True'
        with open('playerdata.json', 'w') as tacofile:
            json.dump(json_content, tacofile, indent=4)
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            petgold = random.randint(0, 50000)
            randgold = random.randint(1, 5000)
            pettype = json_content['Players'][name]['Selected']
            petgold = petgold + (json_content['Players'][name]['Pets'][pettype]['Rarity'] * randgold)
            golddata = json_content['Players'][name]['Gold']
            petname = json_content['Players'][name]['Pets'][pettype]['Name']
            await ctx.send(f'{name}, your {pettype}, {petname}, has left to find some treasure!')
        await asyncio.sleep(1800)
        print(f'{name}\'s pet is halfway done with their farming run!')
        await asyncio.sleep(1800)
        print(f'{name}\'s pet has returned!')
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            json_content['Players'][name]['Gold'] = golddata + petgold
        with open('playerdata.json', 'w') as jsonfile:
            json.dump(json_content, jsonfile, indent=4)
        newgolddata = locale.format_string("%d", petgold + golddata, grouping=True)
        petgold = locale.format_string("%d", petgold, grouping=True)
        await ctx.send(f'{name}, your {pettype}, {petname}, has returned, and collected {petgold} gold, ' +
                       f'you now have {newgolddata} gold!')
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            json_content['Players'][name]['Used'] = 'False'
        with open('playerdata.json', 'w') as jsonfile:
            json.dump(json_content, jsonfile, indent=4)
    except:
        await ctx.send(f'{name}, you do not own a pet!')


@bot.command(name='resetpet')
async def resetpet(ctx, name):
    if not ctx.author.is_mod:
        return
    name = name.lower().replace('@', '')
    try:
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            json_content['Players'][name]['Used'] = 'False'
            json_content['Players'][name]['Bossused'] = 'False'
        with open('playerdata.json', 'w') as jsonfile:
            json.dump(json_content, jsonfile, indent=4)
        await ctx.send(f'{ctx.author.name}, {name}\'s pet timer has been reset!')
    except:
        await ctx.send('That user does not own a pet!')


@bot.command(name='petpay')
async def petpay(ctx, name, amount):
    targname = name.lower().replace('@', '')
    name = ctx.author.name.lower()
    try:
        amount = int(amount)
    except:
        await ctx.channel.send(f'{name}, please input a number for that argument!')
        return
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        try:
            gold = json_content['Players'][name]["Gold"]
        except:
            await ctx.channel.send(f'{name}, you do not own a pet, and therefore have no gold!')
            return
        try:
            targgold = json_content['Players'][targname]['Gold']
        except:
            await ctx.channel.send(f'{name}, that player does not own a pet, and therefore cannot own gold!')
            return
        if gold - amount < 0:
            await ctx.channel.send(f'{name}, you do not have that much gold!')
            return
        json_content['Players'][targname]['Gold'] = targgold + amount
        json_content['Players'][name]['Gold'] = gold - amount
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)
    formatgold = locale.format_string("%d", amount, grouping=True)
    await ctx.channel.send(f'{name}, you have paid {targname} {formatgold} gold.')


@bot.command(name='renamepet')
async def renamepet(ctx, newname, name2=None, name3=None):
    name = ctx.author.name.lower()
    if name2 is not None:
        newname = newname + ' ' + name2
        if name3 is not None:
            newname = newname + ' ' + name3
    try:
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            pettype = json_content['Players'][name]['Selected']
            json_content['Players'][name]['Pets'][pettype]['Name'] = newname
        with open('playerdata.json', 'w') as jsonfile:
            json.dump(json_content, jsonfile, indent=4)
        await ctx.send(f'{ctx.author.name}, your {pettype} has been named {newname}!')
    except:
        await ctx.send(f'{ctx.author.name}, you do not own a pet!')


@bot.command(name='pethelp')
async def pethelp(ctx):
    await ctx.send('https://docs.google.com/document/d/1tlozgA_Y-HYJjM2Cqc47LLnmM1lszbSgB-ap56rDxko/edit?usp=sharing')


@bot.command(name='petgiveaway')
async def petgiveaway(ctx):
    if 'loreosrs' != ctx.author.name.lower():
        return
    namelist = []
    await ctx.send('A pet giveaway has been started!  Type !petjoin in order to join the giveaway!')
    await asyncio.sleep(60)
    await ctx.send('One minute remaining!')
    await asyncio.sleep(30)
    await ctx.send('30 seconds remaining!')
    await asyncio.sleep(30)
    await ctx.send('Pet giveaway has ended!')
    with open('names.txt', 'r') as myfile:
        for i in myfile:
            namelist.append(i.lower().replace('\n', ''))
    namelist.remove('loreosrs')
    choice = random.choice(namelist)
    await add_pet(ctx, choice, 'Internet Troll', 1)
    namelist.remove(choice)


@bot.command(name='petjoin')
async def petjoin(ctx):
    name = ctx.author.name.lower()
    with open('names.txt', 'r') as myfile:
        if ctx.author.name.lower() in myfile:
            return
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        if 'True' in json_content['Players'][name]['Pet']:
            await ctx.send(f'{name}, you\'ve already gotten a pet!')
            return
    with open('names.txt', 'a') as myfile:
        myfile.write(ctx.author.name.lower() + '\n')


@bot.command(name='pet')
async def pet(ctx):
    name = ctx.author.name.lower()
    try:
        with open('playerdata.json', 'r') as jsonfile:
            json_content = json.load(jsonfile)
            pettype = json_content['Players'][name]['Selected']
            petname = json_content['Players'][name]['Pets'][pettype]['Name']
            petlevel = json_content['Players'][name]['Pets'][pettype]['Level']
            if 'True' not in json_content['Players'][name]['Pet']:
                await ctx.send(f'{name}, you do not own a pet!  !pethelp')
                return
        await ctx.send(f'{name} displays their level {petlevel} {pettype}, {petname}!')
    except:
        await ctx.send(f'{name}, you do not own a pet!  !pethelp')


exp_var = 0
levelvar = 1
gold_cost = 0
new_gold = 0


@bot.command(name='levelup')
async def levelup(ctx, goldvar=None):
    global levelvar
    global exp_var
    global gold_cost
    global new_gold
    gold_cost = 0
    exp_var = 0
    levelvar = 1
    new_gold = 0
    name = ctx.author.name.lower()
    target_gold = goldvar
    try:
        with open('playerdata.json', 'r') as playerfile:
            player_content = json.load(playerfile)
            if player_content['Players'][name]['Used'] == 'True':
                await ctx.channel.send(f'{ctx.author.name}, please wait until your pet has returned to level up!')
                return
            pettype = player_content['Players'][name]['Selected']
            levelvar = player_content['Players'][name]['Pets'][pettype]['Level']
            gold = player_content['Players'][name]['Gold']
            with open('experience.json', 'r') as jsonfile:
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
            player_content['Players'][name]['Gold'] = gold
            player_content['Players'][name]['Pets'][pettype]['Level'] = levelvar
            petname = player_content['Players'][name]['Pets'][pettype]['Name']
        await ctx.send(f'{ctx.author.name}, your {pettype}, {petname} is now level {levelvar}, at the cost of ' +
                       f'{locale.format_string("%d", gold_cost, grouping=True)} gold!')
        with open('playerdata.json', 'w') as playerfile:
            json.dump(player_content, playerfile, indent=4)
    except:
        await ctx.send(f'{ctx.author.name}, you do not own a pet!')
        return


@bot.command(name='selectpet')
async def pets(ctx, selection=None):
    name = ctx.author.name.lower()
    try:
        if selection is None:
            string = f'{name}, your available pets are: '
            joinlist = []
            joinstring = ', '
            iteration = 0
            with open('playerdata.json', 'r') as jsonfile:
                json_content = json.load(jsonfile)
                for i in json_content['Players'][name]['Petlist']:
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
            with open('playerdata.json', 'r') as jsonfile:
                json_content = json.load(jsonfile)
                json_content['Players'][name]['Selected'] = json_content['Players'][name]['Petlist'][int(selection)]
                selected_pet = json_content['Players'][name]['Petlist'][int(selection)]
                selected_name = json_content['Players'][name]['Pets'][selected_pet]['Name']
            with open('playerdata.json', 'w') as jsonfile:
                json.dump(json_content, jsonfile, indent=4)
            await ctx.send(f'{name}, you have selected your {selected_pet}, {selected_name}, as your active pet!')
            return
    except:
        await ctx.send(f'{name}, you do not own a pet!')


@bot.command(name='petboss')
async def unlock(ctx, target=None, target2=None, target3=None):
    name = ctx.author.name.lower()
    timestamp = str(ctx.message.timestamp)
    if target is None:
        with open('bosses.json', 'r') as jsonfile:
            with open('playerdata.json', 'r') as playerfile:
                player_content = json.load(playerfile)
                try:
                    pettype = player_content['Players'][name]['Selected']
                except:
                    await ctx.channel.send(f'{name}, you do not own a pet!')
                    return
                pettype = player_content['Players'][name]['Selected']
                petlevel = player_content['Players'][name]['Pets'][pettype]['Level']
            string = f'{name}, your available bosses are: '
            joinlist = []
            joinstring = ', '
            json_content = json.load(jsonfile)
            for i in json_content['Bosses']:
                if petlevel >= json_content['Bosses'][i]['Level']:
                    i = i.lower()
                    i = i.title()
                    joinlist.append(i)
            joinstring = joinstring.join(joinlist)
            await ctx.channel.send(string + joinstring)
        return
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        try:
            pettype = json_content['Players'][name]['Selected']
        except:
            await ctx.channel.send(f'{name}, you do not own a pet!')
            return
        timeleft = round(json_content['Players'][name]['BossTimeLeft'] / 60)
        if target.lower() == 'time':
            if json_content['Players'][name]['Bossused'] == 'False':
                if json_content['Players'][name]['Used'] == 'True':
                    await ctx.channel.send(f'{name}, you must wait for your pet to return before you can attempt ' +
                                           'a boss!')
                    return
                await ctx.channel.send(f'{name}, you can attempt another boss!')
                return
            d1 = parse(timestamp)
            d2 = parse(json_content['Players'][name]['BossTimestamp'])
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
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        pettype = json_content['Players'][name]['Selected']
        petname = json_content['Players'][name]['Pets'][pettype]['Name']
        petlevel = json_content['Players'][name]['Pets'][pettype]['Level']
        petrarity = json_content['Players'][name]['Pets'][pettype]['Rarity']
        gold = json_content['Players'][name]['Gold']
        with open('bosses.json', 'r') as bossjson:
            boss_content = json.load(bossjson)
            bosslist = []
            for i in boss_content['Bosses']:
                bosslist.append(i)
            if target.upper() not in bosslist:
                await ctx.channel.send(f'{name}, that boss does not exist!')
                return
            json_content['Players'][name]['BossTimeLeft'] = round((
                                        boss_content['Bosses'][target]['Strength'] / petrarity) + 60) * 60
        if 'True' in json_content['Players'][name]['Used']:
            d1 = parse(timestamp)
            d2 = parse(json_content['Players'][name]['Timestamp'])
            time_left = d2 - d1
            seconds = time_left.total_seconds()
            minutes = int((seconds % 3600) // 60)
            if minutes <= 0:
                json_content['Players'][name]['Used'] = 'False'
                with open('playerdata.json', 'w') as eggfile:
                    json.dump(json_content, eggfile, indent=4)
                await ctx.send(f'{name}, please use the command again!  If it still does not work, contact a mod.')
                return
            await ctx.send(f'{name}, you\'ve already used this command!  Please wait {minutes} minutes ' +
                           'before you use it again!')
            return
        elif 'True' in json_content['Players'][name]['Bossused']:
            print('egg')
            d1 = parse(timestamp)
            d2 = parse(json_content['Players'][name]['BossTimestamp'])
            time_left = d1 - d2
            seconds = time_left.total_seconds()
            minutes = int(seconds / 60)
            timeleft = timeleft - minutes
            await ctx.channel.send(f'{name}, your pet must wait another {timeleft} ' +
                                   'minutes before it can do another boss!')
            return
        if 'False' in json_content['Players'][name]['Bossused']:
            if 'False' in json_content['Players'][name]['Used']:
                json_content['Players'][name]['Timestamp'] = timestamp
                json_content['Players'][name]['BossTimestamp'] = timestamp
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)
    with open('bosses.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        bosslist = []
        boss_str = json_content['Bosses'][target]['Strength']
        boss_gold = json_content['Bosses'][target]['Gold']
        boss_pets = json_content['Bosses'][target]['Pets']
        player_pets = json_content['Bosses'][target]['Player Pets']
        for i in json_content['Bosses']:
            if petlevel >= json_content['Bosses'][i]['Level']:
                bosslist.append(i)
        if target.upper() not in bosslist:
            boss_lvl = json_content['Bosses'][target]['Level']
            await ctx.channel.send(f'{name}, you need a level {boss_lvl} pet!')
            return
    await ctx.channel.send(f'{name}, your pet {pettype}, {petname}, has left to combat a strong creature!')
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        json_content['Players'][name]['Used'] = 'True'
        json_content['Players'][name]['Bossused'] = 'True'
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)
    await asyncio.sleep(1800)
    print(f'{name}\'s pet is halfway done with their run!')
    await asyncio.sleep(1800)
    cooldown = (boss_str * 60) / petrarity
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        newgold = gold + random.randint(1, 100000 * petrarity) + boss_gold
        bringgold = newgold - gold
        bossroll = random.randint(1, 5000)
        if bossroll == 3223:
            petchoice = random.choice(boss_pets)
            json_content['Players'][name]['Pets'][pettype]['Pets'].append(petchoice)
            await ctx.channel.send(f'{name}, your pet has returned with a pet {petchoice}!')
        playerpetroll = random.randint(1, 5000)
        if playerpetroll == 4846:
            if player_pets is not None:
                await add_pet(ctx, name, random.choice(player_pets), 100)
        await asyncio.sleep(3)
        json_content['Players'][name]['Gold'] = newgold
        await ctx.channel.send(f'{name}, your pet {pettype}, {petname}, has returned with ' +
                               f'{locale.format_string("%d", bringgold, grouping=True)}, you now have ' +
                               f'{locale.format_string("%d", newgold, grouping=True)} gold!  Your {pettype} must' +
                               ' rest for a while before attempting another boss.')
        json_content['Players'][name]['Used'] = 'False'
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)
    await asyncio.sleep(cooldown)
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        json_content['Players'][name]['Bossused'] = 'False'
        print(f'{name}, your {pettype} {petname}, is ready to fight another boss!')
        print(f'{name}\'s pet has returned from their boss run!')
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)


@bot.command(name='petpets')
async def petpets(ctx):
    with open('playerdata.json', 'r') as playerfile:
        player_content = json.load(playerfile)
        name = ctx.author.name.lower()
        try:
            pettype = player_content['Players'][name]['Selected']
        except:
            await ctx.channel.send(f'{name}, you do not own a pet!')
            return
        pets = player_content['Players'][name]['Pets'][pettype]['Pets']
        petname = player_content['Players'][name]['Pets'][pettype]['Name']
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
    name = ctx.author.name.lower()
    arg1 = arg1.replace('@', '')
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        try:
            test = json_content['Players'][name]['Selected']
        except:
            await ctx.channel.send(f'{name}, you do not own a pet, and therefore have no money to stake!')
            return
        try:
            test = json_content['Players'][arg1.lower()]['Selected']
        except:
            await ctx.channel.send(f'{name}, that player does not own a pet, and therefore cannot stake!')
            return
        if int(arg2) > json_content['Players'][name]['Gold']:
            await ctx.channel.send(f'{name}, you do not have that much gold!')
            return
        if int(arg2) > json_content['Players'][arg1.lower()]['Gold']:
            await ctx.channel.send(f'{name}, that player does not have that much gold!')
            return
        json_content['Players'][name]['Duelselect'] = arg1.lower()
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)
    goldvar = int(arg2)
    arg2 = f'{locale.format_string("%d", int(arg2), grouping=True)}'
    await ctx.channel.send(f'@{arg1}, {name} has requested a duel for {arg2} gold!' +
                           '  Type !accept within 30 seconds to accept the duel!')
    await asyncio.sleep(30)
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        player1_gold = json_content['Players'][name]['Gold']
        player2_gold = json_content['Players'][arg1.lower()]['Gold']
        if json_content['Players'][arg1.lower()]['Duelaccept'] != 'True':
            print('Command timeout')
            return
        else:
            coin_flip = random.randint(1, 2)
            if coin_flip == 1:
                await ctx.channel.send(f'{name}, your pet won!  You have gained {arg2} gold from {arg1.lower()}!')
                json_content['Players'][name]['Gold'] = player1_gold + goldvar
                json_content['Players'][arg1.lower()]['Gold'] = player2_gold - goldvar
            elif coin_flip == 2:
                await ctx.channel.send(f'{arg1.lower()}, your pet won!  You have gained {arg2} gold from {name}!')
                json_content['Players'][arg1.lower()]['Gold'] = player2_gold + goldvar
                json_content['Players'][name]['Gold'] = player1_gold - goldvar
        json_content['Players'][name]['Duelselect'] = ""
        json_content['Players'][arg1.lower()]['Duelaccept'] = "False"
    with open('playerdata.json', 'w') as jsonfile:
        json.dump(json_content, jsonfile, indent=4)


@bot.command(name='accept')
async def accept(ctx):
    name = ctx.author.name.lower()
    with open('playerdata.json', 'r') as jsonfile:
        json_content = json.load(jsonfile)
        for i in json_content['Players']:
            if json_content['Players'][i]['Duelselect'] == name:
                json_content['Players'][name]['Duelaccept'] = "True"
                with open('playerdata.json', 'w') as dumpfile:
                    json.dump(json_content, dumpfile, indent=4)
                return


if __name__ == '__main__':
    bot.run()

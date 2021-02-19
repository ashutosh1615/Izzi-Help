import discord,db,Utility,time,math
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
prefix = ["x","X","x ","X "]
bot_invite="https://discord.com/api/oauth2/authorize?client_id=809710116098015232&permissions=536935424&scope=bot"
Official_server="https://discord.gg/g84AGfy6"
db_cur = None
embed_colour = 0xEE82EE
db_cur=db.connect(db_cur)
client = commands.Bot(command_prefix=prefix, case_insensitive=True,intents=intents)
client.remove_command('help')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Xhelp prefix = x"))

@client.event
async def on_message(message):
    if message.content.lower().startswith('yuki'):
        await message.channel.send("A man with a courage #firstdonator")
    await client.process_commands(message)

@client.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@client.command()
async def loc(ctx,*, message = None):
     db_cur.execute(f'SELECT Name,zone,floor1 from public."IzziHelp" where name like \'%{message}%\'')
     ls =  db_cur.fetchone()
     name = ls[0]
     zone = ls[1]
     floor = ls[2]
  
     embedVar = discord.Embed(title=name.upper(), color=embed_colour)
     embedVar.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
     embedVar.add_field(name="ZONE", value=zone, inline=True)
     embedVar.add_field(name="Floors", value=floor, inline=True)
     embedVar.set_footer()
     await ctx.send(embed=embedVar)

@client.command()
async def help(ctx):
    await ctx.send(f"go and check all commands in server in #about-izzi-help {Official_server}")

@client.command()
async def invite(ctx):
    await ctx.send(f"Invite link to bot is {bot_invite} \n  and the support server is {Official_server}") 

@client.command(aliases=['math','calc'])
async def cal(ctx,*,message):
    cont= message.split(' ')
    operator = cont[1]
    if operator == '+':
        await ctx.send(Utility.add(operator,float(cont[0]),float(cont[2])))
    if operator == '-':
        await ctx.send(Utility.subtract(operator,float(cont[0]),float(cont[2])))    
    if operator == '*':
        await ctx.send(Utility.multiply(operator,float(cont[0]),float(cont[2])))
    if operator == '/':
        await ctx.send(Utility.divide(operator,float(cont[0]),float(cont[2])))
    if operator == '**':
        await ctx.send(Utility.power(operator,float(cont[0]),float(cont[2])))  

@client.command()
async def card(ctx,*,message):
    cont= message.split(' ')
    ls = Utility.card(int(cont[0]),int(cont[1]))
    rarity = [ls[1],ls[2],ls[3]]
    name = ['Silver','Gold','Platinum']
    cost=math.ceil(ls[0]/5)
    embed_var = discord.Embed(title = 'ENCHANTMENT',colour = embed_colour)
    embed_var.set_footer(text= f"total experience = {ls[0]} and total cost = {cost}")
    embed_var.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
    embed_var.add_field(name= "**Amount of card with different name needed:**" , value=f"from lvl between {cont[0]} to {cont[1]}" ,inline= False)
    for i in range(3):
        embed_var.add_field(name =name[i], value= f'**TOTAL CARDS** :**{rarity[i]}**' , inline =True)
    embed_var.add_field(name="**Amount of card with same name needed**",value=f"from lvl between {cont[0]} to {cont[1]}",inline = False)
    for j in range(3):
        embed_var.add_field(name = name[j], value= f'**TOTAL CARDS** :**{(math.ceil(rarity[j]/3))}**' , inline =True)
    await ctx.send(embed=embed_var)

@client.command()
async def compare(ctx,*, message =None):
    n=3
    if ctx.author.id==575735373209272328:
       n = 6     
    cont = message.split(' ')
    Name = []
    types = []
    passiveness = []
    attack = []
    health = []
    defence = []
    speed = []
    intelligence = []
    if len(cont)<=n:
     for i in range(len(cont)):
        db_cur.execute(f'select name,type,passiveness,attack,health,defence,speed,intelligence from public."IzziHelp" where name like \'%{cont[i]}%\'')
        ls=db_cur.fetchone()
        Name.append(ls[0])
        types.append(ls[1])
        passiveness.append(ls[2])
        attack.append(ls[3])
        health.append(ls[4])
        defence.append(ls[5])
        speed.append(ls[6])
        intelligence.append(ls[7])
     embedVar = discord.Embed(title='Comparison', color=embed_colour)
     embedVar.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
     for i in range(len(cont)):
      embedVar.add_field(name=Name[i].capitalize(), value=f'**TYPE** : {(types[i].capitalize())}\n **ABILITY** : {(passiveness[i].capitalize())}\n **ATK** : {attack[i]}\n **HP** : {health[i]}\n **DEF** : {defence[i]}\n **SPD** : {speed[i]}\n **INT** : {intelligence[i]}\n ', inline=True)
     await ctx.send(embed=embedVar)
    else:
        await ctx.send('```Maximum number of comparison is 3```') 




@client.command()
async def say(ctx,*, message : commands.clean_content):
    await ctx.message.delete()
    await ctx.send(message)

@client.command(pass_context=True)
async def servers(ctx):
    await ctx.send("I'm in " + str(len(client.guilds)) +" servers")    

@client.command()
async def hplay(ctx,message=None):
    content = None
    if message==None:
        file1=open("how_to_play.txt","r")
        content = file1.read()
        
    elif message == '2':
        file1 = open("how_to_play2.txt","r")
        content = file1.read()
    else:
        await ctx.send("Provide a valid value")
    if content is not None:        
        embedVar = discord.Embed(title='How to play', description =content ,color=embed_colour)
        if message == None:
            embedVar.set_footer(text = 'use ```xhplay 2``` for the next page')
        await ctx.send(embed= embedVar)
        
client.run("ODA5NzEwMTE2MDk4MDE1MjMy.YCZDTw.STVd_YXqbqnu5vuGyINHgg0p9e0")
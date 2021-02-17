import discord,db,Utility
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
prefix = "i."
bot_invite="https://discord.com/api/oauth2/authorize?client_id=809710116098015232&permissions=536935424&scope=bot"
Official_server="https://discord.gg/g84AGfy6"
db_cur = None
embed_colour = 0xEE82EE
db_cur=db.connect(db_cur)
client = commands.Bot(command_prefix=prefix, case_insensitive=True,intents=intents, help_command=PrettyHelp())
client.remove_command('help')
@client.command(name="ping")
async def _ping(ctx):
   await ctx.send('Pong! {0}'.format(round(client.latency, 0)))
                       
@client.command()
async def loc(ctx,*, message = None):
     db_cur.execute(f'SELECT Name,zone,floor1 from public."IzziDB" where name like \'%{message}%\'')
     ls =  db_cur.fetchone()
     name = ls[0]
     zone = ls[0]
     floor = ls[2]
  
     embedVar = discord.Embed(title=name.upper(), color=embed_colour)
     embedVar.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
     embedVar.add_field(name="ZONE", value=zone, inline=True)
     embedVar.add_field(name="Floors", value=floor, inline=True)
     embedVar.set_footer()
     await ctx.send(embed=embedVar)

@client.command()
async def invite(ctx):
    await ctx.send(f"Invite link to bot is {bot_invite} \n  and the server is {Official_server}") 

@client.command()
async def math(ctx,*,message):
    cont= message.split(' ')
    operator = cont[1]
    if operator == '+':
        await ctx.send(Utility.add(operator,int(cont[0]),int(cont[2])))
    if operator == '-':
        await ctx.send(Utility.subtract(operator,int(cont[0]),int(cont[2])))    
    if operator == '*':
        await ctx.send(Utility.multiply(operator,int(cont[0]),int(cont[2])))
    if operator == '/':
        await ctx.send(Utility.divide(operator,int(cont[0]),int(cont[2])))
    if operator == '**':
        await ctx.send(Utility.power(operator,int(cont[0]),int(cont[2])))  

@client.command()
async def card(ctx,*,message):
    cont= message.split(' ')
    ls = Utility.card(int(cont[0]),int(cont[1]))
    silver = ls[0]
    gold = ls[1]
    platinum = ls[2]
    cost=[(silver*40),(gold*50),(platinum*60)]
    embed_var = discord.Embed(title = 'ENCHANTMENT',colour = embed_colour)
    embed_var.set_author(name=ctx.author.display_name, icon_url = ctx.author.avatar_url)
    embed_var.add_field(name= "Amount of card needed:" , value="if you have same name divide the card by 3" ,inline= False)
    embed_var.add_field(name = "silver", value= f'**TOTAL CARDS** :{silver} \n **TOTAL COST** :{cost[0]}' , inline =True)
    embed_var.add_field(name = "gold", value= f'**TOTAL CARDS** :{gold} \n **TOTAL COST** :{cost[1]}' , inline =True)
    embed_var.add_field(name = "platinum", value= f'**TOTAL CARDS** :{platinum} \n **TOTAL COST** :{cost[2]}' , inline =True)
    await ctx.send(embed=embed_var)

@client.command()
async def compare(ctx,*, message =None):
    cont = message.split(' ')
    Name = []
    types = []
    passiveness = []
    attack = []
    health = []
    defence = []
    speed = []
    intelligence = []
    if len(cont)<=2:
     for i in range(len(cont)):
        db_cur.execute(f'select name,type,passiveness,attack,health,defence,speed,intelligence from public."IzziDB" where name like \'%{cont[i]}%\'')
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
      embedVar.add_field(name=Name[i], value=f'**TYPE** : {types[i]}\n **ABILITY** : {passiveness[i]}\n **ATK** : {attack[i]}\n **HP** : {health[i]}\n **DEF** : {defence[i]}\n **SPD** : {speed[i]}\n **INT** : {intelligence[i]}\n ', inline=True)
     await ctx.send(embed=embedVar)
    else:
        await ctx.send('```Maximum number of comparison is 2```') 




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
        embedVar.set_footer(text = 'use ```ihplay 2``` for the next page')
        await ctx.send(embed= embedVar)
        
client.run("ODA5NzEwMTE2MDk4MDE1MjMy.YCZDTw.STVd_YXqbqnu5vuGyINHgg0p9e0")
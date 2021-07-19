import discord,Utility,time,math
from discord.ext import commands
from discord import DMChannel
import db as dbs
intents = discord.Intents.default()
intents.members = True
prefix = ["x","X","x ","X "]
Spc =['rem','shiro','uta','kon','sora','hiro', 'mine']
bot_invite="https://discord.com/api/oauth2/authorize?client_id=809710116098015232&permissions=536935424&scope=bot"
Official_server="https://discord.gg/kfk5twftDg"
db_cur = None
embed_colour = 0xEE82EE
db=dbs.connect()
client = commands.Bot(command_prefix=prefix, case_insensitive=True,intents=intents)
client.remove_command('help')

async def page(ctx,message,number,pages):
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('🗑')
    def check(reaction, user):
        return user == ctx.author
    i = 0
    reaction = None
  
    while True:  
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i <= number:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '🗑':
            await message.delete()
        
        try:
            reaction, user = await ctx.bot.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break
    await message.clear_reactions()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Xhelp prefix = x"))

@client.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')
    
@client.command()
async def sad_life(ctx):
    embedV=discord.Embed(name=None,color=discord.Color.random())
    embedV.add_field(name="yas my life was sad lol but now you come here i am happy",value=" I m not a programmer XD so for opening the gate of heaven you need a will and power to see it.\n I am **announcing that 'I can't sell my friend'** -just **smile** whenever you see this and i will open the gate of heaven and you will need to say god code loud where you can chill and listen music \n Hint- for god code try to go in past and hear god saying again**")
    await ctx.send(embed=embedV)

@client.command()
async def mana(ctx,*,message=None):
    if message == None:
        await ctx.send("Provide a valid value ```xmana <Your initial mana> <Your Max mana>```")
    else:
        en= message.split(' ')
        seconds=Utility.mana_cal(int(en[0]),int(en[1]))
        await ctx.send(f"```Remaining time is {(Utility.convert(seconds))}```")

def in_guild(guild_id: list):  
  async def predicate(ctx):
    if not ctx.guild:
      return False
    if ctx.guild.id in guild_id:
       return True
  return commands.check(predicate)   


@in_guild([811410080313770014,784087004806774815])
@client.command()
async def fadd(ctx,*,message =None):
        if message ==None:
            await ctx.send("Please add the valid name,rate you need the fooder for and  amount example ```xfadd izaya,130,500``` ||rate should be between 100 and 200 done for avoiding troll||")
        else:
            cont = message.split(',')
            if int(cont[1])>=100 and int(cont[1])<=200:
                amount=int(cont[1])*int(cont[2])
                db.cur.execute("""insert into farm(user_name,id,card,rate,amount,total) values(%s,%s,%s,%s,%s,%s)""",(ctx.author.name,ctx.author.id,cont[0],cont[1],cont[2],amount))
                db.conn.commit()
                db.cur.execute("""select index from farm where id=%s and card=%s and rate=%s and amount=%s""",(ctx.author.id,cont[0],cont[1],cont[2]))
                embed=discord.Embed(name=None, value=None, color=discord.Color.random())
                embed.add_field(name="Success", value=f"Your order has beed added to farming list and your id is {db.cur.fetchone()[0]} use xfremove <id> to remove your order when you get a farmer", inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No trolling allowed rate should be between 100 and 200 ")

@client.command()
async def fremove(ctx,message):
    if message==None:
        await ctx.send("send the id of your order xfremove <id>")
    else:
        db.cur.execute("""select exists(select index from farm where index=%s and id=%s)""",(int(message),ctx.author.id))    
        if db.cur.fetchone()[0]:
            db.cur.execute("""delete from farm where index = %s and id=%s""",(message,ctx.author.id) )
            db.conn.commit()
            await ctx.send("Your order being removed")
        else:
            await ctx.send("This order id not exist provide a valid one")

@client.command()
async def flist(ctx):
    db.cur.execute("""select index,user_name,card,rate,amount,total from farm""")
    ls=db.cur.fetchall()
    pages=[]
    x=0


    for j in range((len(ls)//10)+1):
      pages.append(discord.Embed(title="Farming List", description="ALL THE FARMING ORDERS", colour=discord.Color.random()))
      pages[j].set_author(name=ctx.author, icon_url=ctx.author.avatar_url)  
      pages[j].set_footer(text=f"Page :{j+1}/{(len(ls)//10)+1} | Total order: {len(ls)}")
    for i in range(len(ls)):
      ls_=ls[i]
      pages[x].add_field(name=f"**#{i+1} | {ls_[1]} | Card Required {ls_[2]}**", value= f"Rate {ls_[3]} | Amount of cards {ls_[4]} | Total cost {ls_[5]} | ID : {ls_[0]}",inline=False)
      if ((i+1) % 10) ==0:
        x=x+1   
    message = await ctx.send(embed=pages[0])
    await page(ctx,message,(len(ls)//10),pages)
        





@client.event
async def on_message(message):
    if message.content.lower().startswith('3247'):
        me = await client.fetch_user('575735373209272328')
        await DMChannel.send(me,message.author)
    await client.process_commands(message)

@client.command(aliases=("souls","seal"))
async def soul(ctx,*,message=None):
    embedVar = discord.Embed(title="Guild",color=embed_colour)
    if message ==None:
        embedVar.add_field(name="Error",value="Provide a valid value ```xsouls <Your current guild level>```",inline=True)
    else:
        ls = Utility.souls(int(message))
        names=["souls","seals","gold"]
        embedVar.add_field(name=names[0], value =f"Total {names[0]} required ={ls[0]}" , inline=True)
        embedVar.add_field(name=names[1], value =f"Total {names[1]} required ={ls[1]}" , inline=True)
        embedVar.add_field(name=names[2], value =f"Total {names[2]} required ={ls[2]}" , inline=True)
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

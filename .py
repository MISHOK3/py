import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send('Здравствуйте, выберете команду')
    await ctx.send('/buy')
    await ctx.send('/eco_fakt')

@bot.command()
async def eco_fakt(ctx):
    await ctx.send('Биоразлагаемые пакеты: Решение для экологических проблем')
    await ctx.send('Биоразлагаемые пакеты уменьшают загрязнение окружающей среды пластиковыми отходами. Они разлагаются естественным образом, снижая вредное воздействие на природу.')

    await ctx.send('Что такое биоразлагаемые пакеты?')
    await ctx.send('Биоразлагаемые пакеты изготавливаются из биопластиков или натуральных полимеров, разлагающихся под воздействием микроорганизмов, влаги и кислорода в течение нескольких месяцев или лет.')

    await ctx.send('Основные материалы')
    await ctx.send('PLA (полимолочная кислота): Из кукурузы или сахарного тростника, разлагается в промышленных условиях.')
    await ctx.send('PHA (поли-гидроксиалканоаты): Производятся микроорганизмами, разлагаются в природе.')
    await ctx.send('Крахмал: Натуральный полимер, разлагается микроорганизмами и влагой.')
    await ctx.send('Целлюлоза: Растительные волокна, быстро разлагаются.')

    await ctx.send('Преимущества')
    await ctx.send('Экологическая безопасность: Снижают пластиковые отходы.')
    await ctx.send('Сокращение углеродного следа: Из возобновляемых источников.')
    await ctx.send('Круговая экономика: Возвращаются в почву как питательные вещества.')

    await ctx.send('Вызовы')
    await ctx.send('Стоимость: Биопластики дороже традиционных пластиков.')
    await ctx.send('Условия разложения: Требуются специальные условия.')

    await ctx.send('Заключение')
    await ctx.send('Биоразлагаемые пакеты уменьшают пластиковые отходы и поддерживают экологически ответственный образ жизни, защищая планету для будущих поколений.')
    
    with open('images/bio.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def buy(ctx):
    await ctx.send('Что вы желаете купить?(Выберете команду)')    
    await ctx.send('/bike')
    await ctx.send('/scooter') 
  
    await ctx.send('/car')   
    await ctx.send('/bike')
    await ctx.send('/scooter') 
  

@bot.command()
async def car(ctx):
    await ctx.send('Выберете ваш бюджет')    
    await ctx.send('/small')
    await ctx.send('/medium') 
    await ctx.send('/big')     

@bot.command()
async def small(ctx):
    await ctx.send('1. 2024 Nissan Leaf') 
    with open('images/cars3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 30.000$')        
    await ctx.send('В смешанном режиме езды можно проехать до 270 км')  
    await ctx.send('В городском режиме езды можно проехать до 389 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')


    await ctx.send('2. 2024 Chevrolet Bolt EV') 
    with open('images/cars1.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 28.000$')        
    await ctx.send('Одного заряда хватает на до 350 км')  
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('3. BYD Dolphin') 
    with open('images/cars2.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 25.000$')        
    await ctx.send('На одном заряде акамулятора можно проехать до 301 км')



@bot.command()
async def big(ctx):
    await ctx.send('1. Tesla Model S Long Range') 
    with open('images/carb1.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 100.000$')        
    await ctx.send('Одного заряда хватает на 600 км')  
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Porsche Taycan 4S') 
    with open('images/carb2.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 100.000$')        
    await ctx.send('На одном заряде можно проехать до 460 км, но это в идеальных условиях')  
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('3. Audi e-tron GT') 
    with open('images/carb3.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 100.000$')        
    await ctx.send('На одном заряде можно проехать до 436 км')  



@bot.command()
async def medium(ctx):
    await ctx.send('1. Tesla Model 3 Long Range') 
    with open('images/carm1.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 65.000$')        
    await ctx.send('На одном заряде акамулятора можно проехать до 523 км')  
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Ford Mustang Mach-E') 
    with open('images/carm2.png', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 60.000$')        
    await ctx.send('На одном заряде можно проехать до 435 км')  
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('3. Chevrolet Bolt EUV') 
    with open('images/carm3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 40.000$')        
    await ctx.send('Одного заряда хватает на 402 км')
    
  


@bot.command()
async def bike(ctx):
    await ctx.send('Выберете ваш бюджет') 
    await ctx.send('/little')
    await ctx.send('/average') 
    await ctx.send('/large')     



@bot.command()
async def little(ctx):
    await ctx.send('1. Lectric XP Lite') 
    with open('images/bikl1.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 800$')        
    await ctx.send('На одном заряде акамулятора можно проехать до 40 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Ancheer 250W Electric Bike') 
    with open('images/bikl2.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 500$')        
    await ctx.send('Акамулятора хватает примерно на 50 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')

   

    await ctx.send('3. Swagtron EB-6 Bandit') 
    with open('images/bikl3.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 600$')        
    await ctx.send('Батареи хватает примерно 30 км.')



@bot.command()
async def average(ctx):
    await ctx.send('1. Aventon Level Step-Over') 
    with open('images/bika1.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 1.800$')        
    await ctx.send('Батареи хватает примерно на 90 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. El Diablo 500W Electric Bike') 
    with open('images/bika2.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 2.000$')        
    await ctx.send('На одной зарядке можно проехать около 65 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')

   

    await ctx.send('3. Ride1Up 700 Series Review') 
    with open('images/bika3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 1.700$')        
    await ctx.send('На одном заряде акамулятора можно проехать до 60 км.')



@bot.command()
async def large(ctx):
    await ctx.send('1. Specialized Turbo Levo SL Expert') 
    with open('images/bike1.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 6.500$')        
    await ctx.send('В етих режымах можно проехать:')
    await ctx.send('Режым "Eco" до 65 км')
    await ctx.send('Режым "Trail" до 40 км')
    await ctx.send('Режым "Turbo" до 30 км')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Trek Rail 9.9') 
    with open('images/bike2.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 8.000$')        
    await ctx.send('На одной зарядке можно проехать:')
    await ctx.send('Режым "Eco" до 90 км')
    await ctx.send('Режым "Tour" до 65 км')
    await ctx.send('Режым "eMTB" до 50 км')
    await ctx.send('Режым "Turbo" до 30 км')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')

   

    await ctx.send('3. Giant Trance E+ Pro') 
    with open('images/bike3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture) 
    await ctx.send('Стоимость около 6.000$')        
    await ctx.send('На одном заряде акамулятора можно проехать:')
    await ctx.send('Режым "Eco" до 100 км')
    await ctx.send('Режым "Normal" до 60 км')
    await ctx.send('Режым "Sport" до 45 км')
    await ctx.send('Режым "Turbo" до 30 км')



@bot.command()
async def scooter(ctx):
    await ctx.send('Выберете ваш бюджет') 
    await ctx.send('/tiny')
    await ctx.send('/middle') 
    await ctx.send('/greater')  



@bot.command()
async def tiny(ctx):
    await ctx.send('1. Xiaomi Mi Electric Scooter Essential')
    with open('images/sctt1.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 300$')
    await ctx.send('На одном заряде акамулятора можно проехать около 25 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Ninebot KickScooter E22')
    with open('images/sctt3.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 350$')
    await ctx.send('Заряда акамулятора хватает до 22 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')




    await ctx.send('3. Kugoo S1')
    with open('images/sctt2.webp', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 250$')
    await ctx.send('Полной зарядки хватает на 30 км.')




@bot.command()
async def middle(ctx):
    await ctx.send('1. Xiaomi Mi Electric Scooter Pro 2')
    with open('images/sctm1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 500$')
    await ctx.send('Батареи хватает примерно на 45 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Segway Ninebot ES4')
    with open('images/sctm2.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 500$')
    await ctx.send('На одном заряде можно проехать около 30 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('3. Kugoo S3 Pro')
    with open('images/sctm3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 450$')
    await ctx.send('Полной зарядки хватаен до 30 км.')



@bot.command()
async def greater(ctx):
    await ctx.send('1. Segway Ninebot MAX G30')
    with open('images/sctg1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 800$')
    await ctx.send('Одной зарядки хватает примерно на 65 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('2. Apollo City')
    with open('images/sctg2.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 800$')
    await ctx.send('От полного заряда акамулятора можно проехать примерно 45 км.')
    await ctx.send('.')
    await ctx.send('.')
    await ctx.send('.')



    await ctx.send('3. GoTrax GXL V2')
    with open('images/sctg3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send('Стоимость около 750$')
    await ctx.send('Батарея быдает 45 км до следующей зарядки.')



bot.run('ВАШ ТОКЕН БОТА')

import psutil
import requests
from pyrogram import  Client  as Mbot
from database import dbcount
from database import dbcount as db
from database import dbcount as dib
from sys import platform,
from pyrogram.errors import FloodWait



@Mbot.on_message(filters.command('stats') & filters.incoming) 
 async def get_ststs(bot, message): 
     try: 
         rju = await message.reply('Fetching stats..') 
         total_users = await db.total_users_count() 
         totl_chats = await dib.get_total_file_count() 
         size = await db.get_db_size() 
         siz=await dib.get_db_size() 
         free = 536870912 - size 
         fre = 536870912 - siz 
         size = get_size(size) 
         free = get_size(free) 
         siz =get_size(siz) 
         fre=get_size(fre) 
         co = await db.count_prem() 
         cpu_percentages = psutil.cpu_percent(interval=1, percpu=True) 
         cpu_usages=[] 
         n=0 
         for core, usage in enumerate(cpu_percentages): 
             cpu_usages.append(f"\ncore{n}: {usage}%") 
             n += 1 
         cpu_usage =  psutil.cpu_percent(interval=0) 
         cpu_free = 100 - cpu_usage 
         response = requests.get("https://api.telegram.org") 
         resp= response.elapsed.total_seconds() * 1000 
         respose = requests.get("https://api.spotify.com") 
         rsp= respose.elapsed.total_seconds() * 1000 
         ram = psutil.virtual_memory() 
         rspt = ram.percent 
         ram_available = ram.available // (1024 * 1024) 
         total_ram_mb = ram.total / (1024 * 1024) 
         used_ram_mb = ram.used / (1024 * 1024) 
         sendmsg=f"""Spotify Server Status  
  
 Server OS 
  
 Operating System Type: Linux 
 linux_type = {platform.platform()} 
  
 Cpu Status 
  
 Cpu Cores: {os.cpu_count()} 
 cpu Usage: {cpu_usage}% 
 Cpu Free: {cpu_free}% 
 {''.join(cpu_usages)} 
  
 Response Status 
  
 Telegram Api  Response Time: round({resp}) milliseconds 
 Spotify Api Response Time : {rsp} milliseconds 
  
 Memory Status 
  
 Total Ram: {total_ram_mb:.2f} MB 
 Ram Usage: {rspt:.2f}% 
 Ram Available: {ram_available} MB 
 Used Ram: {used_ram_mb:.2f} MB 
  
 Database Status 
  
 DB 1 Used Size: {size} 
 DB 1 Free Size: {free} 
 DB 2 Used Size: {siz} 
 DB 2 Free Size: {fre} 
  
 Users Status 
  
 Total Users:{total_users} 
 Total Files:{totl_chats} 
 Total Premium Users:{co}""" 
         await rju.edit(sendmsg) 
     except FloodWait as e : 
         pass 
         await sleep(e.value) 
         return await rju.edit(sendmsg) 
     except Exception as e: 
         pass 
         await rju.edit(e)

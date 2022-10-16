from telethon import TelegramClient
from telethon import TelegramClient
from telethon.tl.functions.messages import DeleteMessagesRequest
import asyncio
import asyncio
import time
from time import sleep
from telethon.sync import TelegramClient, events

# Use your own values from my.telegram.org
api_id = int(input("[+] API ID: "))
api_hash = input("[+] API HASH: ")
se = input("[+] Posts word: ")
 #The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('Se', api_id, api_hash) as client:    
   @client.on(events.NewMessage(pattern=f'{se}'))
   async def handler(event):
      await event.delete()
      while True:
          a = '''
- متوفر بنلات digital Ocean ضمان شهر بـ 13$ اسيا | 8$ بتك ( تاخذ كمية سعر يختلف ) .
- مدة البنل  شهرين مع كردت 100$ ♻️ .
- تقدر تصنع من 1 إلى 16 رام ✅ .
- البنك  (0 - 1) + النت ( +5000 ) 🚀 .
- تكدر تسوي rdp و vps 🔥 .
          '''
          c ='''
🔥 متوفر حسابات نتفلكس | NETFLIX 🔥
| المدة : شهر ( ضمان ) ✅
| الباقة : PREMIUM ✅
| الدقة : 4K ✅
| عدد الشاشات و الأجهزة التي تستطيع دخولها : 5 ✅
| سعر الشهري ( المفرد ) : 2$ اسيا او زين كاش او 1$ بتك 
| سعر الشهري ( الكمية ) : 1$ اسيا أو زين كاش او 50 سنت بتك ✅ 
| سعر السنوي ( المفرد ) : 8$ اسيا أو زين كاش او 5$ بتك ✅ 
| سعر السنوي ( الكمية ) : 5$ اسيا أو زين كاش او 2$ بتك ✅
          '''
          d ='''
🔥 متوفر سيرفرات VPS + RDP 🔥

- VPS = root | RDP = Adminnistrator ✅
- VPS & RDP RAM 1 + CPU 1 ✅
- VPS & RDP RAM 2 + CPU 1 ✅
- VPS & RDP RAM 4 + CPU 2 ✅
- VPS & RDP RAM 8 + CPU 4 ✅
- VPS & RDP RAM 16 + CPU 8 ✅
- VPS & RDP RAM 32 + CPU 8✅
- اسعار فل بايو ⭐
- متوفر تجهيز مواصفات حسب الطلب 🔥
- متوفر عادي + قانوني من هوست خاص ضمان شهر ✅
- مورد بنلات + ارديبي ( panel او بنل ) aws - azure - digital Ocean  🔥
          '''    
          await event.reply(a)
          await asyncio.sleep(1200)
          await event.reply(c)
          await asyncio.sleep(1250)
          await event.reply(d)
          await asyncio.sleep(1250)
   client.run_until_disconnected()
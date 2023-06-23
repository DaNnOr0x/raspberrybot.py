#########################################################
#                  RaspyGram Bot 1.0                     #
#Comandare Raspberry Pi e Hotspot DSTAR Tramite Telegram #
#                 - C0d3r: DaNnO r0x -                   #
##########################################################
import commands 
import sys
import telepot
import time

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print 'mi e\' arrivato il comando: %s' % command

        if command == '/start':
                bot.sendMessage(chat_id, 'Benvenuto, per la lista dei comandi digitare /help')

        if command == 'ciao':
                bot.sendMessage(chat_id, 'ciao a te')
        
        if command == 'dashboard':
                bot.sendMessage(chat_id, 'Dashboard: http://.......')
        
        if command == 'Ciao':
                bot.sendMessage(chat_id, 'ciao a te')

        elif command == '/help':
                help = commands.getoutput("tail -n 1 /home/pi/help.txt")
                bot.sendMessage (chat_id, help)

        elif command == '/info':
                info = commands.getoutput("uname -a")
                bot.sendMessage(chat_id, info)

        elif command == '/@reboot@':
                reboot = commands.getoutput("shutdown -r now")
                bot.sendMessage(chat_id, 'Riavvio in Corso')
                bot.sendMessage(chat_id, reboot)

        elif command == '/superoot':
                root = commands.getoutput("sudo -s")
                bot.sendMessage(chat_id, root)
         
        elif command == '/ip':
                  ip = commands.getoutput("tail -n 1 /home/pi/ip.txt")
                  bot.sendMessage(chat_id, ip)   
       
        elif command == '/xrf075d':
                  md = commands.getoutput("sh link_modulod.sh")
                  bot.sendMessage (chat_id, md)

        elif command == '/xrf075b':
                  mb = commands.getoutput("sh link_modulob.sh")
                  bot.sendMessage (chat_id, mb)
                  

        elif command == '/xrf075z':
                  mz = commands.getoutput("sh link_moduloz.sh")
                  bot.sendMessage (chat_id, mz)

        elif command == '/xrf075k':
                  mk = commands.getoutput("sh link_modulok.sh")
                  bot.sendMessage (chat_id, mk)

        elif command == '/xrf075a':
                  ma = commands.getoutput("sh link_moduloa.sh")
                  bot.sendMessage (chat_id, ma)

        elif command == '/xrf075c':
                  mc = commands.getoutput("sh link_moduloc.sh")
                  bot.sendMessage (chat_id, mc)
        
        elif command == '/xrf075e':
                  me = commands.getoutput("sh link_moduloe.sh")
                  bot.sendMessage (chat_id, me)

        elif command == '/xrf075f':
                  mf = commands.getoutput("sh link_modulof.sh")
                  bot.sendMessage (chat_id, mf)

        elif command == '/xrf075g':
                  mg = commands.getoutput("sh link_modulog.sh")
                  bot.sendMessage (chat_id, mg)

        elif command == '/xrf075h':
                  mh = commands.getoutput("sh link_moduloh.sh")
                  bot.sendMessage (chat_id, mh)

        elif command == '/xrf075i':
                  mi = commands.getoutput("sh link_moduloi.sh")
                  bot.sendMessage (chat_id, mi)

        elif command == '/xrf075l':
                  ml = commands.getoutput("sh link_modulol.sh")
                  bot.sendMessage (chat_id, ml)

        elif command == '/xrf075m':
                  mm = commands.getoutput("sh link_modulom.sh")
                  bot.sendMessage (chat_id, mm)        	

        elif command == '/xrf075n':
                  mn = commands.getoutput("sh link_modulon.sh")
                  bot.sendMessage (chat_id, mn)
      
        elif command == '/xrf075o':
                  mo = commands.getoutput("sh link_moduloo.sh")
                  bot.sendMessage (chat_id, mo)

        elif command == '/xrf075p':
                  mp = commands.getoutput("sh link_modulop.sh")
                  bot.sendMessage (chat_id, mp)

        elif command == '/xrf075q':
                  mq = commands.getoutput("sh link_moduloq.sh")
                  bot.sendMessage (chat_id, mq)

        elif command == '/xrf075r':
                  mr = commands.getoutput("sh link_modulor.sh")
                  bot.sendMessage (chat_id, mr)

        elif command == '/xrf075s':
                  ms = commands.getoutput("sh link_modulos.sh")
                  bot.sendMessage (chat_id, ms)

        elif command == '/xrf075t':
                  mt = commands.getoutput("sh link_modulot.sh")
                  bot.sendMessage (chat_id, mt)

        elif command == '/xrf075u':
                  mu = commands.getoutput("sh link_modulou.sh")
                  bot.sendMessage (chat_id, mu)

        elif command == '/xrf075v':
                  mv = commands.getoutput("sh link_modulov.sh")
                  bot.sendMessage (chat_id, mv)

        elif command == '/xrf075w':
                  mw = commands.getoutput("sh link_modulow.sh")
                  bot.sendMessage (chat_id, mw)

        elif command == '/xrf075x':
                  mx = commands.getoutput("sh link_modulox.sh")
                  bot.sendMessage (chat_id, mx)

        elif command == '/xrf075y':
                  my = commands.getoutput("sh link_moduloy.sh")
                  bot.sendMessage (chat_id, my)

        elif command == '/xrf075z':
                  mz = commands.getoutput("sh link_moduloz.sh")
                  bot.sendMessage (chat_id, mz)


	elif command[0:5] == '/temp':
		temp = commands.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
		temperatura = int(temp) / 1000
		temp = str(temperatura)
		bot.sendMessage(chat_id, temp)
		out = commands.getoutput("texttransmit it9dlm__c -text '%s gradi'" % temp)
	
	elif command[0:5] == '/link':
                link = commands.getoutput("cat /var/log/Links.log")
                bot.sendMessage(chat_id, link)

	elif command[0:4] == '/who':
                who = commands.getoutput("tail -n 1 /var/log/Headers.log")
                bot.sendMessage(chat_id, who)


bot = telepot.Bot('280845382:AAFA2SscO6aaVJiajYls8uW8oDSguyGS148')
bot.message_loop(handle)
print 'sono in ascolto....'

while 1:
        time.sleep(10)





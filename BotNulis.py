import requests, json
import sys

#Copyrights 2020
#Code By Zhirrr With API

#Banner
print('''

----------------------------------------------------------
                        Bot Nulis
----------------------------------------------------------
############################################################
     [+] Author : Zhirrr
     [+] Follow My IG : zhirr_ajalah
     [+] Follow My GitHub : Zhirrr
############################################################

''')

msg = input("Masukkan Tulisan: ")
r = requests.get("https://tools.zone-xsec.com/api/nulis.php?q="+msg)
j = json.loads(r.text)
print ("URL BotNulis: "+j["image"])

d= input("Simpan? (Y/n): ")
if d == "Y" or d == "y":
	r = requests.get(j["image"]).content
	open('/storage/emulated/0/botnulis.jpg', 'wb').write(r)
	
	if d == "N" or d =="n":
		sys.exit()
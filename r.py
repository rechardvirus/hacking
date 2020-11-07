###################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal, getpass, requests
os.system("clear")
###################################################################
'''
     Facebook Information 
'''
###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	W = "\033[96m"
        G = '\033[32;1m'
        R = '\033[33;1m'
        A = '\033[31;1m'
        B = '\033[33;1m'
        C = '\033[32;1m'
        D = '\033[34;1m'
        E = '\033[35;1m'
        F = '\033[38;5;208m'
else:
	W = ''
	G = ''
	R = ''
	A = ''
	B = ''
	C = ''
	D = ''
	E = ''
	F = ''
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def banner():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

	except (KeyError,IOError):
		r = requests.get(r'http://jsonip.com')
		ip= r.json()['ip']
		print("\033[01;30m")
		print(open("ryflaiavirus.txt", "r").read())
		print("\033[00m")
		print("\033[01;33m\t\t         ..:: RyflaiaVirus 0.1.0 ::..\033[00m") 
		print("\033[01;34m\t\t----------------------------------------------\033[00m")
		print("\t\t If you don't know how to use it, type help.")
		print("\033[01;34m\t\t----------------------------------------------\033[00m")
		print("\t\t Your IP : ") + ip
		print("\033[01;34m\t\t----------------------------------------------\n\033[00m")
###############################################################################
#                         help

def help():

	print("\033[01;32m\t\t----------------------------------------------")
	print("\t\tshow command   :   Shows you all the commands.")
	print("\t\tclear          :   clear screen.")
	print("\t\tquit           :   quit.")
	print("\033[01;32m\t\t----------------------------------------------\033[00m")
###############################################################################
#                         Main

def main():
  global target_id

  try:
	cek = raw_input(" (RyflaiaVirus ) : ")

	if cek.lower() == 'help':
		help()
		main()
		
	elif cek.lower() == 'clear':
		os.system("clear")
		main()
		
	elif cek.lower() == 'quit':
		os.system("exit")
		
	elif cek.lower() == 'ip':
		os.system("sh rvip.sh")
		main()
		
		
	elif cek.lower() == 'shing':
		os.system("bash rvphishing.sh")
		main()
			
	elif cek.lower() == 'db':
		os.system("python2 rvdbhack.py")
		main()
		
	elif cek.lower() == 'wifi':
		os.system("python rsf.py")
		main()

	elif cek.lower() == 'hi':
		print ''
		main()
  
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
#
######################################################################################################################
#

if __name__ == '__main__':

	banner()
	main()
	

#
##########################################################################
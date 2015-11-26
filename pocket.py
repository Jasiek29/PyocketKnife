from itertools import product
from string import ascii_lowercase
from time import time
import os
import random
from key import Key


letter_frequencies = {
	'a': 0.08167,
	'b': 0.01492,
	'c': 0.02782,
	'd': 0.04253,
	'e': 0.12702,
	'f': 0.02228,
	'g': 0.02015,
	'h': 0.06094,
	'i': 0.06966,
	'j': 0.00153,
	'k': 0.00772,
	'l': 0.04025,
	'm': 0.02406,
	'n': 0.06749,
	'o': 0.07507,
	'p': 0.01929,
	'q': 0.00095,
	'r': 0.05987,
	's': 0.06327,
	't': 0.09056,
	'u': 0.02758,
	'v': 0.00978,
	'w': 0.02360,
	'x': 0.00150,
	'y': 0.01974,
	'z': 0.00074
		
		}
		
bigram_frequencies = {
		"th": 1.52,       "en": 0.55,       "ng": 0.18,
		"he": 1.28,       "ed": 0.53,       "of": 0.16,
		"in": 0.94,       "to": 0.52,       "al": 0.09,
		"er": 0.94,       "it": 0.50,       "de": 0.09,
		"an": 0.82,       "ou": 0.50,       "se": 0.08,
		"re": 0.68,       "ea": 0.47,       "le": 0.08,
		"nd": 0.63,       "hi": 0.46,       "sa": 0.06,
		"at": 0.59,       "is": 0.46,       "si": 0.05,
		"on": 0.57,       "or": 0.43,       "ar": 0.04,
		"nt": 0.56,       "ti": 0.34,       "ve": 0.04,
		"ha": 0.56,       "as": 0.33,       "ra": 0.04,
		"es": 0.56,       "te": 0.27,       "ld": 0.02,
		"st": 0.55,       "et": 0.19,       "ur": 0.02	
		}

		

def letter_score(stringus):
	score=0
	for letter in stringus:
		score = score+ letter_frequencies[letter]
	return score/len(stringus)
	
def chi_score(stringus):
	suma = 0
	num = 0
	#stime = time()
	lenstr = len(stringus)
	
	for lett in "abcdefghijklmnopqrstuvwxyz":
		expect = lenstr * letter_frequencies[lett]
		for er in stringus:
			if lett==er :
				num = num+1

		suma = suma + ( (num-expect)*(num-expect) )/expect
		num = 0

	
	#etime= time()
	#print str(etime-stime)
	return suma



alph = {
"a":1,"f":6,"k":11,"p":16,"u":21,"z":26,
"b":2,"g":7,"l":12,"q":17,"v":22,
"c":3,"h":8,"m":13,"r":18,"w":23,
"d":4,"i":9,"n":14,"s":19,"x":24,
"e":5,"j":10,"o":15,"t":20,"y":25
}

bet = {
0:"?",# dont ask
1:"a",6:"f",11:"k",16:"p",21:"u",26:"z",
2:"b",7:"g",12:"l",17:"q",22:"v",
3:"c",8:"h",13:"m",18:"r",23:"w",
4:"d",9:"i",14:"n",19:"s",24:"x",
5:"e",10:"j",15:"o",20:"t",25:"y"
}



def has_vowels(stringie):
	for letter in stringie:
		if letter in "aeiouy":
			return True
	return False
	
	
	
def encode_it(lista,key):
	temp =""
	pair = key.map(lista)
	result = []
	for inda,word in enumerate(lista):
		for indb,letter in enumerate(word):
			numl = (alph[pair[inda][indb]] + alph[letter] - 1)
			if numl>26:
				#numl+=0
				numl = numl%26
			temp+= bet[numl]
		result.append(temp)
		temp =""
	return result

def decode_it(lista,key):
	temp =""
	pair = key.map(lista)
	result = []
	for inda,word in enumerate(lista):
		for indb,letter in enumerate(word):
			numl = ( alph[letter] - alph[pair[inda][indb]]  + 1)
			if numl<0:
			#	numl+=26
				numl = numl%26
			elif numl ==0:
				numl = 26
			
			temp+= bet[numl]
		result.append(temp)
		temp =""
	return result



class PocketKnife:
	raw_key =""
	kasiski = ""
	sliced =[]
	smarties = ["dr","am","we","me","go","he","of", "is", "in", "on", "an", "to", "it","be","do","by","up","if","us","so","st","or","oh","no","my","id","as"]
	
	# transforms regular tekst to a sliced table for cracking
	def adjust(self,text):
		tekst = text.lower()
		result = ""
		for lettr in tekst:
			if  lettr.isalpha() or lettr == " ":
				result+=lettr
			else:
				result +=" "
		return result.split()
	
	def __init__(self,key):
		self.raw_key  = key
		self.sliced = self.adjust(key)
		self.kasiski = "".join(self.sliced)
	def __repr__(self):
		return "Raw key: %s \nSliced key: %s \nCharacter string: %s \n" % (self.raw_key,str(self.sliced),self.kasiski)
	
	
	def checker(self,a):
		count = 0
		tmp = False
		for x in a:
			if len(x) == 1:
				if x!="i" and x!="a" and x!="s"and x!="t":
					return False
			if len(x) == 2:
				tmp = False
				for y in self.smarties:
					if x==y :
						tmp = True
				if not tmp:
					return False
			if len(x) >2:
				if not has_vowels(x):
					return False
		return True
	
	def smart_score(self,a):
		count = 0
		for x in a:
			if len(x) == 1:
				if x=="i" or x=="a" or x=="s" or x=="t":
					count = count + 1
			if len(x) == 2:
				for y in self.smarties:
					if x==y :
						count = count + 1
		return count
	
	
	
	def smart_crack(self,p):
		stime = time()
		lolz=[]
		summ = open('summary.txt','a')
		f = open('test_smart.txt','w')

		for combo in product(ascii_lowercase, repeat=p):
			temp = Key(''.join(combo))
			print temp
			lolz = decode_it(self.sliced,temp)
			if self.checker(lolz):
				f.write( "Key:%s\n" % (''.join(combo))+"\n" + str(lolz)+"\n\n" )
		f.close()
		etime = time()
		summ.write("\nSmart Test:\nTime elapsed: %s\nMax_key_lenght: %s\nFile size: %s\n"% (str(etime-stime),p,os.path.getsize("test_smart.txt")))
		summ.close()
		return True
		
	def recursive_crack(self,p):
		

		
		stime = time()
		lolz=[]
		parent = ""
		champion = ""
		candidate = ""
		fr_score = 0
		for x in range(0,p):
			parent = parent + 'a'
		for y in range(0,p):
			for combo in product(ascii_lowercase, repeat=1):
				liste = list(parent)
				liste[y] = ''.join(combo)
				candidate = ''.join(liste)
				temp = Key(candidate)
				lolz = decode_it(self.sliced,temp)
				stringer = "".join(lolz)
				if (letter_score(stringer)>fr_score):
					champion = candidate
					fr_score = letter_score(stringer)
			fr_score = 0
			parent = champion
			
		for z in range(0,p):
			for combo in product(ascii_lowercase, repeat=1):
				liste = list(parent)
				liste[p-(1+z)] = ''.join(combo)
				candidate = ''.join(liste)
				temp = Key(candidate)
				lolz = decode_it(self.sliced,temp)
				stringer = "".join(lolz)
				if (letter_score(stringer)>fr_score):
					champion = candidate
					fr_score = letter_score(stringer)
			fr_score = 0
			parent = champion
		
			
		print "The key found: %s\n" % parent
		puk = Key(parent)
		lolek = decode_it(self.sliced,puk)
		print "Decrypted message: %s\n" % " ".join(lolek)
		summ = open('summary.txt','a')
		f = open('test_recursive.txt','w')
		f.close()
		etime = time()
		summ.write("\nRecursive Test:\nTime elapsed: %s\nMax_key_lenght: %s\nFile size: %s\n"% (str(etime-stime),p,os.path.getsize("test_recursive.txt")))
		summ.close()
		return True

	def recursive_chi_crack(self,p):
		

		
			stime = time()
			lolz=[]
			parent = ""
			champion = ""
			candidate = ""
			fr_score = 20000000
			for x in range(0,p):
				parent = parent + 'a'
			for y in range(0,p):
				for combo in product(ascii_lowercase, repeat=1):
					liste = list(parent)
					liste[y] = ''.join(combo)
					candidate = ''.join(liste)
					temp = Key(candidate)
					lolz = decode_it(self.sliced,temp)
					stringer = "".join(lolz)
					if (chi_score(stringer)<fr_score):
						champion = candidate
						fr_score = chi_score(stringer)
				fr_score = 20000000
				parent = champion
				
			for z in range(0,p):
				for combo in product(ascii_lowercase, repeat=1):
					liste = list(parent)
					liste[p-(1+z)] = ''.join(combo)
					candidate = ''.join(liste)
					temp = Key(candidate)
					lolz = decode_it(self.sliced,temp)
					stringer = "".join(lolz)
					if (chi_score(stringer)<fr_score):
						champion = candidate
						fr_score = chi_score(stringer)
				fr_score = 20000000
				parent = champion
			
			print "The key found: %s\n" % parent
			puk = Key(parent)
			lolek = decode_it(self.sliced,puk)
			print "Decrypted message: %s\n" % " ".join(lolek)
			summ = open('summary.txt','a')
			etime = time()
			summ.write("\nRecursive Test:\nTime elapsed: %s\nMax_key_lenght: %s\nFile size: %s\n"% (str(etime-stime),p,os.path.getsize("test_recursive.txt")))
			summ.close()
			return True
		
		
	def Kasiski(self):
		tekst = self.kasiski
		tmp=[]
		maxim =1

		if len(tekst)<10:
			print "Musisz podac dluzszy kod"
			return 0
		for x in range(0,len(tekst)-2):
			klu = tekst[x]+tekst[x+1]+tekst[x+2]
			print klu
			for y in range(0,len(tekst)-2):
				cz = tekst[y]+tekst[y+1]+tekst[y+2]
				if klu ==cz and x!=y:
					print abs(y-x)
					tmp.append(abs(y-x))
		print "Fcuk"
		for licz in range(2,21):
			multi = True
			for num in tmp:
				if num % licz != 0:
					multi=False
			if multi and maxim < licz:
				maxim = licz
		print tmp
		if tmp == []:
			print "Mr. Kasiski cannot help you :("
			return 876		
		print maxim
		return maxim
# KEYWORD : Simulated annealing		
	def eris_crack(self,p):
		stime = time()
		lolz=[]
		parent = ""
		candidate = ""
		count = 0
		fr_score = 20000000
		smart_scr =0
		for x in range(0,p):
			parent = parent + bet[random.randint(1,26)]
		print parent
		
		while count < 1000:
			liste = list(parent)
			liste[random.randint(0,p-1)] =   bet[random.randint(1,26)]
			candidate = ''.join(liste)
			temp = Key(candidate)
			lolz = decode_it(self.sliced,temp)
			stringer = "".join(lolz)
			if (chi_score(stringer)<fr_score):
				parent = candidate
				fr_score = chi_score(stringer)
			else:
				count = count + 1
			

			
		print "The key found: %s\n" % parent
		puk = Key(parent)
		lolek = decode_it(self.sliced,puk)
		print "Decrypted message: %s\n" % " ".join(lolek)
		etime = time()
		summ = open('summary.txt','a')
		summ.write("\nRecursive Test:\nTime elapsed: %s\nMax_key_lenght: %s\nFile size: %s\n"% (str(etime-stime),p,os.path.getsize("test_recursive.txt")))
		summ.close()
		return True

	def dict_slicer(self):
		
		f = open('american-english', 'r')
		flist = f.readlines()
		f.close()
		
		dicts = []
		dic =[]
		
		for i in range(1,21):
			for line in flist:
				if len(line.strip()) == i:
					dic.append(line.strip().lower())
			dicts.append(dic)

			dic =[]
		return dicts
			

	def dict_check(self,lol,dicts):
		
		numer = 0
		den = len(lol)
	#	stime = time()
		
		for a in lol:
			for line in dicts[len(a)-1]:
				if a == line:

					numer += 1
					
	#	etime = time()
	#	print str(etime - stime)
					
	
		return float(numer)/den

#optymalny dla klucza o dlugosci do 6 wlacznie

	def prototype(self,p):
		# laduje zmienne do petli
		
		if p<= 7:
			plc = 0
		else:
			plc = p-7
		
		count = 0
		outtie = 0
		tnum = 0
		before = 0
		after = 0
		stime = time()
		lolz=self.sliced
		dict_score =0
		# laduje zeslicowany slownik i pliki
		
		summ = open('summary.txt','a')
		f = open('test_smeeris.txt','w')
		
		dicts = self.dict_slicer()
		
		#lista popularnych slowek 3 literowych
		lyst = ['the' ,'and' ,'for' ,'not' ,'you' ,'but','say','her','she','all','one','out','who','get','can','him','see','now','did','big']
		#lista wkladow do szablonu hasla
		wklady = []
		surowka = []
		
		
		#wyrabianie wkladow
		
		for word in self.sliced:
			if len(word) == 3:
				surowka.append(word)
				break
		
		for combo in product(ascii_lowercase, repeat=3):
			temp = Key(''.join(combo))
			print temp
			outus = decode_it(surowka,temp)
			if outus[0] in lyst:
				wklady.append(temp.to_string())
		
		#koniec wyrabiania wkladow
		
		#robienie szablonu
		tnum = 0
		dict_score=0
		for ex in lolz:
			if not len(ex) == 3 :
				tnum += len(ex)
			else:
				passw = p*'*'
								
				mess = list(passw) 
								

				tnum = tnum % p
				stri = "123"

				numerra = 0
				for iks in range(tnum,tnum+3 ):
					print iks
					safe = iks % p
					mess[safe] = stri[numerra]
					numerra +=1
								
				numerra = 0
				passw = "".join(mess)
				break
		available = []
		passer = ""
		for a in range(0,len(passw)):
			if passw[a] == '*':
				available.append(a)
				passer += 'a'
			else:
				passer += passw[a]
		print wklady
		print passer
	#	return True
		print available
		combos= []
		for kombo in product(ascii_lowercase, repeat=len(available)):
			combos.append(kombo)
		
		for part in wklady:
			my_key = ""
			dict_score=0 
			
			for letter in passer:
				
				if letter == "1":
					my_key += part[0]
				if letter == "2":
					my_key += part[1]
				if letter == "3":
					my_key += part[2]
				if letter == "a":
					my_key += "a"
					
			dict_cracks = False
			for nummie in combos:
				liste = list(my_key)

				for av in range(0,len(nummie)):	
					liste[available[av]] =   nummie[av]
				candidate = ''.join(liste)

				if dict_cracks==False and 	candidate[available[plc]] == "l":
					break			
					
				print candidate
							
				temp = Key(candidate)
				lolz = decode_it(self.sliced,temp)
				stringer = "".join(lolz)
				# wynik analizy slownikowej
				if(60 > chi_score(stringer)):
					result = self.dict_check(lolz,dicts)
					dict_cracks = True	
					if ( result > dict_score and result > float(1)/len(lolz)):
						my_key = candidate
						dict_score = self.dict_check(lolz,dicts)
						f.write( "Key:%s\n" % (my_key)+"\n" + str(lolz)+"\n\n  " + str(chi_score(stringer)) +"\n\n" )
					
								
		f.close()
		etime = time()
		summ.write("\Proto Test:\nTime elapsed: %s\nMax_key_lenght: %s\nFile size: %s\n"% (str(etime-stime),p,os.path.getsize("test_smeeris.txt")))
		summ.close()
		#print combos
		return True 

	def wise_guy(self,p):
		return True

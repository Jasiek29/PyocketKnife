import timeit
from key import Key
from time import time



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
stime = time()

print decode_it(["wfdfsdfe","sdhyjdcsyo","dsgftrgtr"],Key("awesd"))

etime = time()
print str(etime-stime)

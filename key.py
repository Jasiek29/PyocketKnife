

class Key():
	key =""
	def __init__(self,key):
		self.key  = key
	def __repr__(self):
		return  self.key 
	def to_string(self):
		return  self.key 
	def map(self,liste):
		temp = 0
		str_temp = ""
		result = []
		for word in liste:
			for letter in word:
				str_temp = str_temp + self.key[temp]
				temp += 1
				if temp>= len(self.key):
					temp = 0
			result.append(str_temp)
			str_temp = ""
		return result

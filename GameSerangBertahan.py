class Agent: #template

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor

	#Method tanpa return, tanpa argumen
	def siapa(self):
		print("Namaku adalah " + self.name)
	
	#Method dengan argumen, tanpa return
	def healthUp(self,up):
		self.health += up
	
	#Method dengan return
	def getHealth(self):
		return self.health

agent1 = Agent("astra", 100, 50, 30)
agent2 = Agent("viper", 100, 40, 40)
agent3 = Agent("omen", 100, 70, 10)

agent1.siapa()
agent1.healthUp(50)

agent2.siapa()
agent2.healthUp(40)

print(agent1.getHealth())

print(agent2.getHealth())

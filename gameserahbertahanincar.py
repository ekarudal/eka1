class Agent:
    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, musuh, attackPowerMusuh):
        print(self.name + ' diserang ' + musuh.name)
        attackDiterima = attackPowerMusuh/self.armorNumber
        print('Serangan terasa : ' + str(attackDiterima))
        self.health -= attackDiterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

        
astra= Agent('astra',100,10,5)
viper= Agent('viper',200,20,10)

astra.serang(viper)
print ('\n')
viper.serang(astra)
print ('\n')
viper.serang(astra)
print ('\n')
viper.serang(astra)

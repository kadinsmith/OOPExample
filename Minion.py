from Card import Card


class Minion(Card):
    #attributes

    


    def __init__(self,cost,name, damage, life):
        Card.__init__(self, cost, name, damage, life)
        #assign parameters to the object
        self.damage = damage
        self.life = life

def printMinionInfo(self):
    print('The card cost: ' + str(self.cost))
    print('The card name: ' + str(self.name))
    print('damage' + str(self.damage))
    print('life'+ str(self.life))
#Card class is a blueprint of the Card object
#Parent Class --base Class
class Card: 

    #initializer to create the attributes of every class object
    #constructor
    def __init__(self, cost, name, damage, life):
        self.cost = cost
        self.name = name
        self.damage = damage
        self.life = life
        #Attributes - describes the object ()
        # give the card a cost attribute
        # give the card a name attribute
        

#behaviors - methods - functions
    def printCardInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + str(self.name))
        print('damage' + str(self.damage))
        print('life'+ str(self.life))
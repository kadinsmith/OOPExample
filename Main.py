from Card import Card
from Minion import Minion
def main():
    # create the townCrier Card
    # cost = 1 and name = 'townCrier'
    #instantiate an instance of the object
    # creating an instance of trhe class
    townCrier = Minion(1,'Town Crier', 1, 2)

   
    #creat an instance of the class called redbandWasp
    #attributes cost = 2 and the name = Redband Wasp
    redbandWasp = Minion(2, 'Redband Wasp', 1, 3)

    #creat an instance of the class called warpath
    #attributes cost = 2 and the name = Warpath
    warpath = Card(2, 'Warpath', 1, 3)
    #show the player the details of the card
    

    townCrier.printCardInfo()
    townCrier.printMinionInfo()


    redbandWasp.printCardInfo()
    warpath.printCardInfo()

if __name__=="__main__":
    main()
from generic_player import GenericPlayer
from test_player import test_player
from moves import Move
from game import Game

def tryHit(myHand, enHand, myOtherHand, enOtherHand):
    if(myHand == 0 or enHand == 0):
        return -1   # nehituj nuly nebo nulama

    result = myHand + enHand
    if (result >= 5):
        return result # kill
    else:
        if (myOtherHand == 0):
            if (myHand + myHand + enHand >= 5 and myHand + enOtherHand >= 5):
                return -1  # nehituj do game overu
            else:
                return result
        else:
            return result
            
                

class CustomPlayer(GenericPlayer):
    def move(self):        
        
        # prejmenovani pro prehlednost
            
        enLeft = self.get_opponent_left()
        enRight = self.get_opponent_right()
        myLeft = self.get_my_left()
        myRight = self.get_my_right()


        # start 1 1 1 1
        #########################################################
        #   CHALLENGER HLASKA
        if (myLeft == 1 and myRight == 1 and enLeft == 1 and enRight == 1):
            print('I AM AFRAID YOU HAVE LIGMA')

        #########################################################
        #   HITOVANI - pokud bude kill, ale ne game over

        testHits = [tryHit(myLeft, enLeft, myRight, enRight), tryHit(myLeft, enRight, myRight, enLeft), tryHit(myRight, enLeft,  myLeft, enRight), tryHit(myRight, enRight,  myLeft, enLeft)]
        moves = [Move.LEFT_TO_LEFT, Move.LEFT_TO_RIGHT, Move.RIGHT_TO_LEFT, Move.RIGHT_TO_RIGHT]

        #########################################################
        #   WIN SITUACE  en: 1 0  my: 2 1

        if (enLeft + enRight == 1 and myLeft + myRight == 3):
            if (myLeft < myRight):
                if( myLeft == 1):
                    return Move.SWITCH(3,0)
                else:  # uz mame 3 0, resime dal
                    pass
            else:
                if(myRight == 1):
                    return Move.SWITCH(3,0)
                else:  # uz mame 0 3, resime dal
                    pass


        #########################################################
        #   WIN SITUACE  en: 3 1  my: 3 0

        if (enLeft + enRight == 4 and myLeft + myRight == 3):
            if (enLeft == 1 and enRight == 3):
                if(myLeft == 0):
                    print('VICTORY IS MINE!!!')
                    return Move.RIGHT_TO_RIGHT
                elif(myRight == 0):
                    print('VICTORY IS MINE!!!')
                    return Move.LEFT_TO_RIGHT
            elif (enLeft == 3 and enRight == 1):
                if(myLeft == 0):
                    print('VICTORY IS MINE!!!')
                    return Move.RIGHT_TO_LEFT
                elif(myRight == 0):
                    print('VICTORY IS MINE!!!')
                    return Move.LEFT_TO_LEFT
        

        #########################################################
        #   WINNING KILL
        if (enLeft == 0):
            if (testHits[1] >= 5):
                print('LIGMA BALLS, BITCH!!!')
                return Move.LEFT_TO_RIGHT
            elif (testHits[3] >= 5):
                print('LIGMA BALLS, BITCH!!!')
                return Move.RIGHT_TO_RIGHT
        if (enRight == 0):
            if (testHits[0] >= 5):
                print('LIGMA BALLS, BITCH!!!')
                return Move.LEFT_TO_LEFT
            elif (testHits[2] >= 5):
                print('LIGMA BALLS, BITCH!!!')
                return Move.RIGHT_TO_LEFT

        #########################################################
        
        
        #########################################################
        #   GAME OVER CHECK
        if (myLeft+myRight > 1):
            if (myLeft == 0):
                #prepni jednu doleva
                return Move.SWITCH(1, myRight-1)
            elif (myRight == 0):
                #prepni doprava
                return Move.SWITCH(myLeft-1, 1);
        else:
            pass # hitni tou jednickou zmrda


        ########################################################
        #   KILL HIT pokud neni do game over - viz tryHit()
        # killuj maximalni hodnotu
        maxKill = 5
        killIndex = -1

        for i in range(len(testHits)):    
            if (testHits[i] >= maxKill):
                killIndex = i
                maxKill = testHits[i]
            elif (testHits[i] == -1):
                pass
        if(killIndex >= 0):
            print('OVERKILL %d000 DMG' % (testHits[killIndex]))
            return moves[killIndex]
        

	##########################################################
        # hituj nejnizsi nejnizsi kdyz nic z vyse uvedeneho neprobehne

        print('TVOJE PRSTICKY CHYTILY LIGMA')

        if (myLeft <= myRight):
                if ( myLeft > 0):
                        if( enLeft <= enRight):
                                if (enLeft > 0):
                                    return Move.LEFT_TO_LEFT
                                else:
                                    return Move.LEFT_TO_RIGHT
                        else:
                                if( enRight > 0):
                                    return Move.LEFT_TO_RIGHT
                                else:
                                    return Move.LEFT_TO_LEFT		
                else:
                        if( enLeft <= enRight):
                                if (enLeft > 0):
                                    return Move.RIGHT_TO_LEFT
                                else:
                                    return Move.RIGHT_TO_RIGHT
                        else:
                                if( enRight > 0):
                                    return Move.RIGHT_TO_RIGHT
                                else:
                                    return Move.RIGHT_TO_LEFT	
        else:
                if ( myRight > 0):
                        if( enLeft <= enRight):
                                if (enLeft > 0):
                                    return Move.RIGHT_TO_LEFT
                                else:
                                    return Move.RIGHT_TO_RIGHT
                        else:
                                if( enRight > 0):
                                    return Move.RIGHT_TO_RIGHT
                                else:
                                    return Move.RIGHT_TO_LEFT	
                else:	
                        if( enLeft <= enRight):
                                if (enLeft > 0):
                                    return Move.LEFT_TO_LEFT
                                else:
                                    return Move.LEFT_TO_RIGHT
                        else:
                                if( enRight > 0):
                                    return Move.LEFT_TO_RIGHT
                                else:
                                    return Move.LEFT_TO_LEFT	

#    def zeroCheck():
#        return [bool(get_opponent_left), bool(get_opponent_right), bool(get_my_left), bool(get_my_right)]




        

### CHANGE THE NAME
custom_player_blue = CustomPlayer("BLUEBUFFEDv3")
### END CHANGE

'''
GenericPlayer class



return Move.LEFT_TO_RIGHT
or
return Move.LEFT_TO_LEFT
or
return Move.RIGHT_TO_RIGHT
or
return Move.RIGHT_TO_LEFT
or
return Move.SWITCH(3, 4)

self.get_my_left() # Returns current number of fingers on your left hand
self.get_my_right() # Returns current number of fingers on your right hand
self.get_opponent_left() # Returns current number of fingers on opponents left hand
self.get_opponent_right() # Returns current number of fingers on opponents right hand
self.get_history() # Returns and array of all the moves within the game.
self.get_current_round() # Returns the number of current round
self.get_starting_player() # Returns the name of the starting player

'''

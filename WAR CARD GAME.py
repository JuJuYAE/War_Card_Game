#!/usr/bin/env python
# coding: utf-8

# In[32]:


#CARD 
#RANK, SUIT, VALUE 


#DECK CLASS 


#PLAYER 
import random 
from random import shuffle 
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three" : 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack" : 11, "Queen" : 12, "King": 13, "Ace": 14}


# In[33]:


#START WITH CARD CLASS


# In[34]:


class Card(): 
    def __init__ (self,suit,rank): 
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
        


# In[35]:


#DECK CLASS


# In[36]:


class Deck() : 
    def __init__ (self): 
        self.all_cards = []
        
        
        for suit in suits : 
            for rank in ranks : 
                #Create the card object 
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self) : 
        shuffle(self.all_cards)
        
    def deal_one(self): 
        return self.all_cards.pop()
        


# In[37]:


from random import shuffle 


# In[38]:


#PLAYER CLASS 


# In[39]:


class Player : 
    def __init__ (self, name): 
        self.name = name 
        self.all_cards = []
        
    def remove_one(self) : 
        return self.all_cards.pop(0) 

    def add_card(self,new_cards): 
        if type(new_cards) == type([]) : 
            self.all_cards.extend(new_cards)
        else : 
            self.all_cards.append(new_cards)
    
    def __str__ (self) : 
        return f"Player {self.name} has {len(self.all_cards)} cards."


# In[40]:


#Game setup
player_one = Player ("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range (26)  : 
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())


# In[41]:


game_on = True 


# In[42]:


round_num = 0 
while game_on : 
    round_num +=1 
    print (f"Round {round_num}")
    
    if len(player_one.all_cards) == 0 : 
        print("Player 1, out of cards\n")
        print ("Player 2 Wins!")
        game_on = False 
        break
        
        
    if len(player_two.all_cards) == 0 : 
        print("Player 2, out of cards\n")
        print ("Player 1 Wins!")
        game_on = False 
        break
        
        
#Start new Round 
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True 
    while at_war : 
        if player_one_cards[-1].value > player_two_cards[-1].value : 
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False 
            
        elif player_one_cards[-1].value < player_two_cards[-1].value : 
            player_two.add_card(player_two_cards)
            player_two.add_card(player_one_cards)
            at_war = False 
            
        else : 
            print("WAR!!")
            
            if len(player_one.all_cards) < 3 : 
                print("Player 1 unable to enter war\n")
                print("Player 2 wins")
                game_on = False 
                
            if len(player_two.all_cards) < 3 : 
                print("Player 2 unable to enter war\n")
                print("Player 1 wins")
                game_on = False 
                
            else : 
                for num in range (3) :
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


# In[ ]:





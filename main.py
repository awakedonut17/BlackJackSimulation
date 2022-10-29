#setup
#imports the random and csv module 
import random
import csv

#defines the different cards in the game
cards=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
#defines a variable to contain the scores and defines different possible outcomes for each starrting card
score = {}
for card in cards:
  score[card]={17:0,18:0,19:0,20:0,21:0,"Loss":0}


#function which will determine the worth of each card
def evalcard(card):
  if card == "A":
    #if it is an ace, returns  11, an aces maximum value and tells the program that there was an ace, so that it can be reducede to a 1 if needed
    return (11, 1)
  elif card == "K" or card=="Q" or card=="J":
    #if the card is a royalty card, it's value is 10
    return(10,0)
  else:
    #if the card is a number card, returns the cards number
    return (card,0)


#simulation; runs for each card
for card in cards:
  #message to let the user now which card the program is working on
  print(f"working on card {card}")
  #runs simulation loop 1 million times per card for better accuracy
  for run in range(1000000):
    #evaluates the value of the card as per the earlier defined function
    evalresult=evalcard(card)
    #sets the number of aces and starting total according to the card
    runaces=evalresult[1]
    runtotal=evalresult[0]
    
    while runtotal<17:
      addcard = random.choice(cards)
      #evaluates the value of the card as per the earlier defined function
      evalresult=evalcard(addcard)
      #adds to the total and the number of aces according to the card
      runaces+=evalresult[1]
      runtotal+=evalresult[0]
      #if the total is above 21 and aces are available the program will turn those aces into 1s until there are no more aces left or the total is below 21
      while runtotal>21 and runaces>0 :
        runtotal += -10
        runaces += -1

    #once the card is over 16 the dealer stops hitting.
    #if the total is then already over 21 the dealer  loses     
    if runtotal>21:
      score[card]["Loss"]+=1
    #otherwise the whoever has the higher card wins. the total achieved is talliedd.
    else:
      score[card][runtotal]+=1


#this section prints the results annd writes them to a csv file
with open ("results.csv", "w", encoding="UTF8") as file:
  #initialises the csv writer
  writer = csv.writer(file)
  #writes the firsrt row with descriptions for subsequent rows
  writer.writerow(["card", 17, 18, 19, 20, 21, "Loss"])
  #for every card...
  for card in cards:
    #clears variable for next row
    newrow = []
    #adds the card to the first colllum
    newrow.append(card)
    #prints the card
    print (card)
    #for each possible result...
    for result in score[card]:
      #adds the result to the row (as a decimal
      newrow.append(score[card][result]/1000000)
      #printss the result
      print(f"{result}:{score[card][result]/10000}%", end=" ")
    #writes the row
    writer.writerow(newrow)
    #leaves a gap before the next row                    
    print("\n")



      

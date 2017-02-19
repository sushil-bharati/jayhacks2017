# The famous Rock, Paper and Scissor game -- No, we do not have Spock!
def rockPaperScissor(sel):
    import random
    #print("==Rock Paper Scissor == Choose one: ")
    sel = sel.lower()
    if sel == "quit":
        return "quit"
    lst = ['rock', 'paper', 'scissor']
    comp = random.choice(lst)
    returnvar4=[]
    if sel == "rock":
        if comp == "paper":
            returnvar4=" Computer says paper.. You win"
        elif comp == sel:
            returnvar4=" Computer says paper..It's a draw"
        else:
            returnvar4=(" Computer says paper..You lose")
    elif sel == "paper":
        if comp == "scissor":
            returnvar4=" Computer says scissor..You lose"
        if comp == "rock":
            returnvar4=" Computer says scissor..You win"
        else:
            returnvar4=" Computer says  scissor..It's a draw"

    elif sel == "scissor":
        if comp == "rock":
            returnvar4 =" Computer says rock..You lose"
        elif comp == "paper":
            returnvar4 =" Computer says rock..You win"
        else:
            returnvar4 =" Computer says rock..It's a draw"
    else:
        returnvar4 ="Wrong entry, Type correctly"
    return returnvar4



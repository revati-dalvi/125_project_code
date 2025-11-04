import turtle as trtl 
import random as rand
#-------set-up--------
'''setting up all lists and turtles'''
#setting up screen
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)

'''letters for key binds (positve and negative)'''
point_increase_binds:["A", "S", "D", "F", "G", "H", "B", "C", "E", "I", "J", "K", "L", "M"] 
point_decrese_binds: ["A", "S", "D", "F", "G", "H", "B", "C", "E", "I", "J", "K", "L", "M"] 

''' set up positive targert'''
postarget_count= 10 
postarget_list= []
postarget_keybinds= {}
'''set up for negative targets'''
negtarget_count= 5
negtarget_list= []
negtarget_keybinds= {}

'''creating positive targets'''
for i in range (postarget_count): 
    postarget = trtl.Turtle()   
    postarget.shape("circle")  #setting shape of target
    postarget.penup() #make sure there is no line drawn 
    postarget.pensize(100) #setting size of target
    postarget.color("blue") #setting color of target
    postarget.hideturtle() #hiding target until needed 
    postarget_list.append(postarget) #adds new target to the list 

'''creating negative targets'''
for i in range (negtarget_count): 
    negtarget = trtl.Turtle() 
    negtarget.penup() #make sure there is no line drawn 
    negtarget.goto(0, -50) #seperate the two targets from each other  
    negtarget.shape("circle")  #setting shape of target
    negtarget.pensize(100) #setting size of target
    negtarget.color("red") #setting color of target
    negtarget.hideturtle() #hiding target until needed
    negtarget_list.append(postarget) #adds new target to the list 

#----all functions------

"function that assignns pos targets a keybind "
def postarget_bind (active_pos):
    #selects letters that have NOT been used before for keybinds
    available_keybinds = [l for l in point_increase_binds if l not in postarget_keybinds]
    #makes sure to clear postarget_keybinds when there a no "fresh" keybinds left
    if not available_keybinds: 
        postarget_keybinds.clear()
        available_keybinds= postarget_bind

    #randomizes the selection of letters for keybinds 
    pos_letter= rand.choice(available_keybinds)

    #clears old pos_targets on the screen 
    active_pos.clear()
    active_pos.penup()

    #make sure drawing actions are stll executd in the background (no visual chances for the user)
    wn.tracer(False)

    #target is on random place on the screen 
    active_pos.goto(rand.randint(-250,250), rand.randint(-25, 180))

    #setting placement of letter onto the cicle 
    active_pos.color("black") #sets color of the apple 
    active_pos.sety(active_pos.ycor()-10)
    active_pos.write(pos_letter, align= "center", font=("Arial", 150, "bold"))
    active_pos.sety(active_pos.ycor()+40)

    #show target by refreshing screen 
    active_pos.showtrutle()
    wn.tracer(True)
    wn.update

    #remebering letters 
    postarget_keybinds[pos_letter]= active_pos
    







wn=trtl.Screen()
wn.mainloop()

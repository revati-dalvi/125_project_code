import turtle as trtl 
import random as rand
#-------set-up--------
'''setting up all lists and turtles'''
#setting up screen
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.tracer(False)

'''letters for key binds (positve and negative)'''
point_increase_binds = ["A", "S", "D", "F", "G", "H", "B", "C", "E", "I", "J", "K", "L", "M"] 
point_decrese_binds = ["A", "S", "D", "F", "G", "H", "B", "C", "E", "I", "J", "K", "L", "M"] 

''' set up positive targert'''
postarget_count= 10 
postarget_list= []
postarget_keybinds= {}
postarget_index = 0

'''set up for negative targets'''
negtarget_count= 5
negtarget_list= []
negtarget_keybinds= {}
negtarget_index = 0


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
for i in range(negtarget_count):
    negtarget = trtl.Turtle()
    negtarget.shape("circle")
    negtarget.penup()
    negtarget.pensize(100)
    negtarget.color("red")
    negtarget.hideturtle() #hiding target until needed
    negtarget_list.append(negtarget) #adds new target to the list 

#----all functions------

"function that assignns pos targets a keybind "
def postarget_bind (active_pos):
    #selects letters that have NOT been used before for keybinds
    available_keybinds = [l for l in point_increase_binds if l not in postarget_keybinds]
    #makes sure to clear postarget_keybinds when there a no "fresh" keybinds left
    if not available_keybinds: 
        postarget_keybinds.clear()
        available_keybinds= point_increase_binds 

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
    active_pos.color("blue") #sets color of the apple 
    active_pos.sety(active_pos.ycor()-10)
    active_pos.write(pos_letter, font=("Arial", 25, "bold")) #wrote on target 
    
    active_pos.showturtle() 
    wn.update() 

    #adds to keybinds dictionary 
    postarget_keybinds[pos_letter] = active_pos

"function that assignns neg targets a keybind "
def negtarget_bind (active_neg):
    #selects letters that have NOT been used before for keybinds
    available_keybinds = [l for l in point_decrese_binds if l not in negtarget_keybinds]
    #makes sure to clear negtarget_keybinds when there a no "fresh" keybinds left
    if not available_keybinds: 
        negtarget_keybinds.clear()
        available_keybinds= point_decrese_binds 

    #randomizes the selection of letters for keybinds 
    neg_letter= rand.choice(available_keybinds)

    #clears old neg_targets on the screen 
    active_neg.clear()
    active_neg.penup()

    #make sure drawing actions are stll executd in the background (no visual chances for the user)
    wn.tracer(False)

    #target is on random place on the screen 
    active_neg.goto(rand.randint(-250,250), rand.randint(-25, 180))

    #setting placement of letter onto the cicle 
    active_neg.color("red") #sets color of the apple 
    active_neg.sety(active_neg.ycor()-10)
    active_neg.write(neg_letter, font=("Arial", 25, "bold")) #wrote on target 
    
    active_neg.showturtle() 
    wn.update() 

    #adds to keybinds dictionary 
    negtarget_keybinds[neg_letter] = active_neg

# Function to handle key presses and cycle targets
def handle_click(key):
    global postarget_index
    global negtarget_index

    key = key.upper() # Ensure key comparison is case-insensitive

    # Check if the key corresponds to an active positive target
    if key in postarget_keybinds:
        # Hide the target
        target = postarget_keybinds.pop(key)
        target.hideturtle()
        target.clear()
        
        # Move to the next target in the list (cycling back to 0 if at the end)
        postarget_index = (postarget_index + 1) % postarget_count
        new_target = postarget_list[postarget_index]
        
        # Bind the new target
        postarget_bind(new_target)

    # Check if the key corresponds to an active negative target
    elif key in negtarget_keybinds:
        # Hide the target
        target = negtarget_keybinds.pop(key)
        target.hideturtle()
        target.clear()
        
        # Move to the next target in the list (cycling back to 0 if at the end)
        negtarget_index = (negtarget_index + 1) % negtarget_count
        new_target = negtarget_list[negtarget_index]
        
        # Bind the new target
        negtarget_bind(new_target)
        
    wn.update()

#----running the program----

# Initial call to display the first positive target
if postarget_list:
    postarget_bind(postarget_list[postarget_index]) 

# Initial call to display the first negative target
if negtarget_list:
    negtarget_bind(negtarget_list[negtarget_index])

# Set up key listeners 
# The lambda function ensures the key value is passed correctly to handle_click
all_keys = set(point_increase_binds + point_decrese_binds)
for key in all_keys:
    wn.onkey(lambda k=key: handle_click(k), key)
    wn.onkey(lambda k=key: handle_click(k), key.lower())

wn.listen()
wn.mainloop()

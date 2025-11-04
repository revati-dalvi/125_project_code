import turtle as trtl 
import random as rand

"setting up all lists and turtles"
#setting up screen
wn=trtl.Screen()
wn.setup(width=1.0, height=1.0)

#letters that pop up 
point_increase_binds:["A", "S", "D", "F", "G", "H", "B", "C", "E", "I", "J", "K", "L", "M"] 
point_decrese_binds: ["A", "S", "D", "F", "G", "H", "B", "C", "E", "I", "J", "K", "L", "M"] 
#things for the targets 
postarget_count= 10 
#things for the positve targets 
postarget_count= 10 
postarget_list= []
postarget_keybinds= {}

#things for the negative targets 
negtarget_count= 5
negtarget_list= []
negtarget_keybinds= {}

#creating positve targets 
for i in range (postarget_count): 
    postarget = trtl.Turtle()   
    postarget.shape("circle")  #setting shape of target
    postarget.pensize(100) #setting size of target
    postarget.color("red") #setting color of target
    postarget.hideturtle() #hiding target until needed 
    postarget.penup() #make sure not lines are drawn from target
    postarget_list.append(postarget) #adds new target to the list 

#creating negative targets 
for i in range (negtarget_count): 
    negtarget = trtl.Turtle() 
    negtarget.goto(0, -50)  
    negtarget.shape("circle")  #setting shape of target
    negtarget.pensize(100) #setting size of target
    negtarget.color("blue") #setting color of target
    negtarget.hideturtle() #hiding target until needed 
    negtarget.penup() #make sure not lines are drawn from target
    negtarget_list.append(postarget) #adds new target to the list 










wn=trtl.Screen()
wn.mainloop()

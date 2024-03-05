print("Name: Tommy Yu")

#problem 1 

def game_introduction(): 
    print("At its core, Minecraft is a game where players place blocks and go on adventures.")

game_introduction()

#problem 2 

def update_health(current_health, health_change): 
    print(f"Your current health is {current_health}")
    
    final_health = current_health + health_change
  #      80               100             -20
  
    print(f"Your health is now {final_health}")
    
    
    
update_health(8200, -1020)

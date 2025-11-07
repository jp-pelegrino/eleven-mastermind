import os
import time
import secret
import spacing

# Set max attempts for the game
attempts = 0 # intitialization | DO NOT EDIT
max_attempts = 10 # parameter: how many tries a player will have
to_guess = 4 # parameter: how many colors to guess in the game

secret_code_grid = [f"❔" for i in range(to_guess)]

# adapt a new grid generation to account to dynamic parameters
guess_grid = [["🔘" for i in range(to_guess)] for n in range (max_attempts)]
result_grid = [["🔳" for i in range(to_guess)] for n in range (max_attempts)]
pointer_grid = [f"⬛" for i in range(max_attempts)]

def render (delay):
      #clear console using os module
      os.system('cls' if os.name == 'nt' else 'clear')

      #UI Rendering

      time.sleep(delay) # graphical adjustments, allow delay rendering row-by-row

      #spacing module to dynamically add borders based on the game `max_attempts` instead of hardcoded string
      spacing.border("╠","╦","╣",max_attempts)

      #GUESS GRID#
      for e in range(to_guess):
            row = ["║"]
            for i in range(max_attempts):
                  row.append(f" {guess_grid[i][e]} ") #emoji with spaces in-between
                  row.append(f"║") #closing bracket
            row.append(f"  {secret_code_grid[e]}  ║") #append secret code
            print("".join(row))
            time.sleep(delay)
      ###

      # DIVIDER #
      spacing.border("╠","╬","╣",max_attempts)
      time.sleep(delay)

      #RESULT GRID#
      for e in range(to_guess):
            row = ["║"]
            for i in range(max_attempts):
                  row.append(f" {result_grid[i][e]} ") #emoji with spaces in-between
                  row.append(f"║") #closing bracket

            if e == 0:
                  row.append("GUESS:║")
            elif e == 1:
                  row.append(f"{attempts+1:02d}    ║")
            elif e == 2:
                  row.append(f"--of--║")
            elif e == 3:
                  row.append(f"    {max_attempts:02d}║")
            else:
                  row.append(f"      ║")

            print("".join(row))
            time.sleep(delay)

      #DIVIDER
      spacing.border("╠","╬","╣",max_attempts)
      time.sleep(delay)  

      ui_pt = ["║"]
      for i in range(max_attempts):
            ui_pt.append(f" {pointer_grid[i]} ")
            ui_pt.append("║")
      ui_pt.append("      ║")

      time.sleep(delay)
      print("".join(ui_pt))
      spacing.border("╠","╩","╣",max_attempts)

      time.sleep(delay)
      print("║      [R]🔴  [G]🟢  [B]🔵   [Y]🟡   [W]⚪   [O]🟠" + ("     "*(max_attempts-10)) + "       ║")

      time.sleep(delay)
      spacing.border("╚","═","╝",max_attempts)

      return

#print the initital UI render with delay 0.15 seconds
render(0.15)

while attempts < max_attempts:
      guess = [] # initialize/reset the attempt guess input list

      # Reset the previous column back to default
      pointer_grid[attempts-1] = "⬛"
      # Set the pointer to the current column using the attempt integer to map
      pointer_grid[attempts] = "🔼"
      render(0) # call a render here so that the changes made for the new attempt is accounted for

      for c in range(0,4):
            while True:
                  order = ["first", "second", "third", "fourth"] # for numerical to word conversion
                  g = input(f"[Attempt {attempts+1}/{max_attempts}] Input your {order[c]} color: ")

                  if g.lower() == "r":
                        g = "🔴"
                        break
                  elif g.lower() == "g":
                        g = "🟢"
                        break
                  elif g.lower() == "b":
                        g = "🔵"
                        break
                  elif g.lower() == "y":
                        g = "🟡"
                        break
                  elif g.lower() == "w":
                        g = "⚪"
                        break
                  elif g.lower() == "o":
                        g = "🟠"
                        break
                  else:
                        render(0)
                        print("Invalid color. Please choose again.")
                        continue # loop back

            guess.append(g) # append to this attempt guess input list

            # simplified and improved mapping to account to dynamic parameters
            guess_grid[attempts][c] = g 

            render(0)
      
      attempts += 1

"""
=====================================================================
PYTHON CODING CHALLENGE: MY FIRST ADVENTURE GAME!
=====================================================================

MISSION OBJECTIVE:
Your mission is to use the print() and input() functions to create the
opening scene of your very own text-based adventure game. You will
write a program that tells a story and asks the player for their name
and a choice.

INSTRUCTIONS:
1.  Read through the example code in Part 1 to understand how it works.
2.  Run this file to see the example in action.
3.  To write your own game, "comment out" the example code in Part 1
    by adding a # at the beginning of each line in that section.
4.  Write your own adventure game code in the space provided in Part 2.
5.  Try the Bonus Challenge in Part 3! Be as creative as you would like! 

"""

# =====================================================================
# PART 1: EXAMPLE CODE - A MYSTERIOUS LIBRARY
# =====================================================================
# Read through this code to see how an adventure game can start.
# When you're ready to write your own, you can "comment out" this
# entire section by putting a # at the start of each line below.

print("--- Example Adventure ---")
print("Running the example code from Part 1...")
print("-" * 25)

# Use print() to set the scene for the player. This is how you tell the story!
print("You stand at the entrance of a mysterious, ancient library.")
print("Two large doors stand before you.")

# Use input() to ask for the player's name and store it in a variable.
player_name = input("What is your adventurer's name? ")

# Use input() again to ask the player to make a choice.
door_choice = input("One door is marked 'Wisdom,' the other 'Fortune.' Which door do you choose? ")

# Use a final print() statement to react to the player's choices.
# Notice how we combine text with the variables using the '+' sign.
print()  # This adds a blank line to make the output easier to read.
print("Good luck, " + player_name + "! The Door of " + door_choice + " creaks open...")

print("-" * 25)
print("\n" * 2) # Add a couple of blank lines before the next part


# =====================================================================
# PART 2: YOUR TURN TO CODE! - CREATE YOUR OWN ADVENTURE
# =====================================================================
# Now it's your turn! Write your code below this line.
# Think of a cool setting: a spooky castle, a futuristic spaceship,
# or a magical forest?

print("--- My Adventure Game ---")
print("Write your code below to begin!")

# 1. Set your scene with at least two print() statements.
# print("You find yourself in a dark cave, lit only by glowing mushrooms.")
# print("Ahead, you see two tunnels. One echoes with the sound of dripping water, the other is silent.")

# 2. Ask for the player's name with input() and save it to a variable.
# hero_name = input("What is your name, brave explorer? ")

# 3. Ask the player to make a choice specific to your scene.
# tunnel_choice = input("Do you enter the 'dripping' tunnel or the 'silent' one? ")

# 4. Print the final message, including the player's name and choice.
# print("Be careful,", hero_name + ". The", tunnel_choice, "tunnel is dark and mysterious...")


# =====================================================================
# PART 3: BONUS CHALLENGE!
# =====================================================================
# If you finished Part 2, try expanding your story here!
#
# IDEAS:
# - Ask the player a *second* question (e.g., "You find a torch and a map. Which do you take?").
# - Add more print() statements to describe what happens after their first choice.

print("\n--- Bonus Challenge ---")

# your_bonus_code_goes_here = "You can start writing your bonus code now!"
# print(your_bonus_code_goes_here)


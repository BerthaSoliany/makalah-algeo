import numpy as np
import time

class CharacterRoute:
    def __init__(self, name, matrix, thresholds, story_mode):
        """
        Initialize the character's route with a name, SPL matrix, thresholds, and story mode.
        :param name: Name of the character
        :param matrix: Matrix containing coefficients for SPL
        :param thresholds: Threshold values for each ending [bad, bad relationship, good, normal]
        :param story_mode: The story mode this character belongs to (Casual, Deep, Another)
        """
        self.name = name
        self.matrix = matrix
        self.thresholds = thresholds
        self.story_mode = story_mode
        self.is_locked = False  # Lock status for self character's route
        self.hearts = 0  # Hearts for self character

    def determine_ending(self, choices, story_mode):
        """
        Determine the player's outcome for this character's route based on choices and story mode.
        :param choices: List of player choices [x1, x2, x3].
        :param story_mode: Selected story mode (Casual, Deep, Another).
        :return: Outcome string for the character's route.
        """
        if self.is_locked:
            return f"Route locked. {self.name}'s route already achieved."

        # Hitung dot product
        results = np.dot(self.matrix, choices)

        if story_mode == "Casual":
            if results[2] >= self.thresholds[2] and choices[2] >= 10:
                return f"Good Ending: Congratulations! You have become lover with {self.name}"
            if results[3] >= self.thresholds[3] and choices[2] <= 9:
                return f"Normal Ending: You have a good time with {self.name}"
            if results[1] >= self.thresholds[1] and choices[0] < 0.3:
                return f"Bad Relationship Ending: You disappoint {self.name}"
            if results[0] >= self.thresholds[0] and choices[0] == 1 and choices[1] == 1 and choices[2] == 1:
                return "Bad Ending: Why aren't you try harder?"

        elif story_mode == "Deep":
            if results[2] >= self.thresholds[2] and choices[2] >= 10:
                return f"Good Ending: Congratulations! You have become lover with {self.name}"
            if results[3] >= self.thresholds[3] and choices[2] <= 9:
                return f"Normal Ending: You have a good time with {self.name}"
            if results[1] >= self.thresholds[1] and choices[0] < 0.3:
                return f"Bad Relationship Ending: You disappoint {self.name}"
            if results[0] >= self.thresholds[0] and choices[0] == 1 and choices[1] == 1 and choices[2] == 1:
                return "Bad Ending: Why aren't you try harder?"

        elif story_mode == "Another":
            if results[2] >= self.thresholds[2] and choices[2] >= 17:
                return f"Good Ending: Congratulations! You have become lover with {self.name}"
            if results[3] >= self.thresholds[3] and choices[2] <= 16:
                return f"Normal Ending: You have a good time with {self.name}"
            if results[1] >= self.thresholds[1] and choices[0] < 0.3:
                return f"Bad Relationship Ending: You disappoint {self.name}"
            if results[0] >= self.thresholds[0] and choices[0] == 1 and choices[1] == 1 and choices[2] == 1:
                return "Bad Ending: Why aren't you try harder?"

        return "No Ending Achieved"


    def add_hearts(self, hearts):
        """Add hearts to this character."""
        self.hearts += hearts


def determine_story_route(story_mode, characters):
    """
    Determine the character route based on story mode and hearts.
    :param story_mode: Selected story mode (Casual, Deep, Another)
    :param characters: List of CharacterRoute objects
    :return: The selected character's route
    """
    # Filter characters by story mode
    eligible_characters = [char for char in characters if char.story_mode == story_mode]

    if not eligible_characters:
        return None  # No characters available for the selected story mode

    # Determine character with highest hearts
    selected_character = max(eligible_characters, key=lambda char: char.hearts)

    return selected_character

def mode_bad_ending(story_mode, characters):
    """
    Check if Story Mode Bad Ending should be triggered.
    :param story_mode: Selected story mode
    :param characters: List of CharacterRoute objects
    :return: True if Story Mode Bad Ending should be triggered, False otherwise
    """
    # Find character with highest hearts
    character_with_highest_hearts = max(characters, key=lambda char: char.hearts)

    # Check if the character with highest hearts is eligible for the selected story mode
    if character_with_highest_hearts.story_mode != story_mode:
        return True 
    return False


# Initialize data for story mode
universal_matrix = np.array([
    [1, 1, 1],   # Bad Ending
    [0.3, 1, 1], # Bad Relationship Ending
    [1, 1, 1],   # Good Ending
    [1, 1, 1]    # Normal Ending
])

thresholds_casual = [3, 2.3, 12, 9]  # Casual Story mode
thresholds_deep = [3, 2.3, 12, 9]    # Deep Story mode
thresholds_another = [3, 2.3, 17, 16]  # Another Story mode

# Initialize data for all characters
characters = []

# Casual Story Mode Characters
characters.append(CharacterRoute("Jaehee", universal_matrix, thresholds_casual, "Casual"))
characters.append(CharacterRoute("Zen", universal_matrix, thresholds_casual, "Casual"))
characters.append(CharacterRoute("Yoosung", universal_matrix, thresholds_casual, "Casual"))

# Deep Story Mode Characters
characters.append(CharacterRoute("Jumin", universal_matrix, thresholds_deep, "Deep"))
characters.append(CharacterRoute("707", universal_matrix, thresholds_deep, "Deep"))

# Another Story Mode Characters
characters.append(CharacterRoute("V", universal_matrix, thresholds_another, "Another"))
characters.append(CharacterRoute("Ray", universal_matrix, thresholds_another, "Another"))


# Main program
print("Welcome to Mystic Messenger Ending Determinant!")
print("No, this program can not predict the real ending of the game.")
print("This program is just a simple project that use system of linear equations to implement a branching storylines")
print("You will be asked to answer a series of questions until the program tell you the ending of the game")
print("Enjoy!")

# Story mode
while True:
    print("\nSelect your story mode:")
    print("1. Casual Story")
    print("2. Deep Story")
    print("3. Another Story")
    story_mode_input = input("Enter your choice (1/2/3): ")

    story_mode_map = {
        "1": "Casual",
        "2": "Deep",
        "3": "Another"
    }
    selected_story_mode = story_mode_map.get(story_mode_input, "Invalid")
    if selected_story_mode == "Invalid":
        print("Invalid choice. Please try again.")
    else:
        break
print(f"You have selected the {selected_story_mode} Story Mode.")

time.sleep(1)


# Prologue
prologue_choices = []

print("\nPrologue")
print("Note that there's a bad ending if all choices are the same (specific choice).")
print("\nThere's suddenly a strange app on your phone. It is a chatroom app. You decide to open it.")

prologue_dialogues = [
    "You see a message pop up on the app. It says to do crime. What will you do?",
    "This app feels strange... Are you sure about your choice?",
    "The chatroom becomes more intense. Is this your final answer?",
    "Are you sure you want to continue? The app is getting weirder."
]

for i in range(4):
    time.sleep(1)
    print("\n"+prologue_dialogues[i])
    print("1. GLADLY!")
    print("2. I'm sorry, I can't do that")
    print("3. Pff, pay me first")
    print("4. I'm calling the police")
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please try again.")
            i -= 1
            continue
        prologue_choices.append(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        i -= 1

if prologue_choices == [4,4,4,4]:
    time.sleep(1)
    print("\nThe screen flickers. You feel like something's watching you.")
    print("\nBad Ending: Just don't call the police...")
    exit()
else:
    time.sleep(1)
    print("\nWhatever your choices, atleast you're not insisting to call the police 4 times. Let's move on.")

time.sleep(1)

# Simulating player choices
print("\nNow, let's simulate the determinant factor of the story.")
print("Each ending have different requirements.")
print("Good Ending requires the player to obtain a specific chatroom and number of guests.\nThe same goes to Normal Ending but with less guests than Good Ending.")
print("Bad Relationship Ending requires specific chatroom and story\nalong side with the route character's hearts is less than the others.")
print("Bad Ending requires specific chatroom and story. The player choices also determined")
print("You will be given a set of predefined choices to determine the outcome of the story.")
print("\nYou can also add hearts to characters.")
print("The character with the highest hearts will determine the route.")
print("\nLet's begin!")

time.sleep(1)

# Hearts
while True:
    print("\nAdd hearts to characters:")
    for char in characters:
        print(f"{char.name}: {char.hearts} hearts")
    char_name = input("Enter character name to add hearts (or 'done' to finish): ")
    if char_name.lower() == "done":
        break
    for char in characters:
        if char.name.lower() == char_name.lower():
            try:
                hearts = int(input(f"Enter hearts for {char.name}: "))
                char.add_hearts(hearts)
                time.sleep(1)
            except ValueError:
                print("Invalid input. Skipping.")
            break
    else:
        print("Character not found. Please try again.")
        time.sleep(1)

time.sleep(1)

# Deciding character route
selected_character = determine_story_route(selected_story_mode, characters)
if selected_character is None:
    print("\nNo characters available for the selected story mode.")
    exit()
else:
    print(f"\n{selected_character.name}'s Route obtained with {selected_character.hearts} hearts.")

if mode_bad_ending(selected_story_mode, characters):
    if selected_story_mode == "Casual":
        print("\nBad Ending triggered! You must have either Jaehee's, Zen's, or Yoosung's heart highest.")
    elif selected_story_mode == "Deep":
        print("\nBad Ending triggered! You must have either 707's or Jumin's heart highest.")
    elif selected_story_mode == "Another":
        print("\nBad Ending triggered! You must have either V's or Ray's heart highest.")
    else:
        print("\nBad Ending triggered! No character route available.")
    exit()  

# Predefined choices
while True:
    print("\nPredefined choices:")
    if selected_story_mode == "Casual" or selected_story_mode == "Deep":
        print("1. For Good Ending: 10, 1, 10")
        print("2. For Normal Ending: 10, 1, 9")
        print("3. For Bad Relationship Ending: 0.2, 1, 1")
        print("4. For Bad Ending: 1, 1, 1")
        choice_input = input("Enter your choice (1/2/3/4): ")
        if choice_input == "1":
            player_choices = [10, 1, 10]
            break
        elif choice_input == "2":
            player_choices = [10, 1, 9]
            break
        elif choice_input == "3":
            player_choices = [0.2, 1, 1]
            break
        elif choice_input == "4":
            player_choices = [1, 1, 1]
            break
        else:
            print("Invalid choice. Please try again.")
    elif selected_story_mode == "Another":
        print("1. Choice for Good Ending: 10, 1, 17")
        print("2. Choice for Normal Ending: 10, 1, 12")
        print("3. Choice for Bad Relationship Ending: 0.2, 1, 1")
        print("4. Choice for Bad Ending: 1, 1, 1")
        choice_input = input("Enter your choice (1/2/3/4): ")
        if choice_input == "1":
            player_choices = [10, 1, 17]
            break
        elif choice_input == "2":
            player_choices = [10, 1, 12]
            break
        elif choice_input == "3":
            player_choices = [0.2, 1, 1]
            break
        elif choice_input == "4":
            player_choices = [1, 1, 1]
            break
        else:
            print("Invalid choice. Please try again.")

time.sleep(1)

# Determined Ending
print(f"\nEvaluating ending for {selected_character.name}'s Route...")
ending = selected_character.determine_ending(player_choices, selected_story_mode)
time.sleep(1)
print(f"{ending}")
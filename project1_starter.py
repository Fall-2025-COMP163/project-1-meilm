##############################
##############################          THIS IS NOT MY CODE! I AM TESTING TO SEE IF THE IsSUE IS WITH MY CODE OR NOT!!
##############################

"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Will Webster]
Date: [10/29/2025]

AI Usage: ChatGPT (GPT-5) helped with function implementation logic, formatting, and documentation.
"""

# Function to create a new character
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1  # All new characters start at level 1
    
    # Calculate base stats based on class and level
    strength, magic, health = calculate_stats(character_class, level)
    
    # Base gold for all characters
    gold = 100

    # Store all character data in a dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


# Function to calculate stats based on class and level
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    # Base stats by class
    if character_class.lower() == "warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 120 + (level * 10)
    elif character_class.lower() == "mage":
        strength = 3 + (level * 1)
        magic = 15 + (level * 5)
        health = 80 + (level * 5)
    elif character_class.lower() == "rogue":
        strength = 7 + (level * 3)
        magic = 7 + (level * 2)
        health = 90 + (level * 6)
    elif character_class.lower() == "cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 4)
        health = 100 + (level * 8)
    else:
        # Default fallback for unknown class
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 100 + (level * 5)

    return (strength, magic, health)


# Function to save a character to a text file
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    (No try/except allowed)
    """
    if filename == "":
        return False  # Empty filename is invalid

    import os

    # Extract directory path from filename
    directory = os.path.dirname(filename)

    # If a directory is specified AND it does not exist → fail
    if directory != "" and not os.path.exists(directory):
        return False

    # Open file in write mode and save character data line by line
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()

    return True


# Function to load a character from a text file
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    (No try/except used)
    """
    import os
    if not os.path.exists(filename):
        return None  # File does not exist

    # Read all lines from the file
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # Parse file lines into key/value pairs
    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(": ", 1)
            data[key] = value

    # Convert string values to proper types and return character dictionary
    character = {
        "name": data.get("Character Name", ""),
        "class": data.get("Class", ""),
        "level": int(data.get("Level", 1)),
        "strength": int(data.get("Strength", 0)),
        "magic": int(data.get("Magic", 0)),
        "health": int(data.get("Health", 0)),
        "gold": int(data.get("Gold", 0))
    }

    return character


# Function to display a character sheet
def display_character(character):
    """
    Prints formatted character sheet
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# Function to level up a character and recalculate stats
def level_up(character):
    """
    Increases character level and recalculates stats
    """
    character["level"] += 1  # Increment level by 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health


# Main program area for testing
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    
    # Create a sample character
    char = create_character("Aria", "Mage")
    display_character(char)

    print("\nSaving character...")
    save_character(char, "aria.txt")

    print("\nLoading character...")
    loaded = load_character("aria.txt")
    display_character(loaded)

    print("\nLeveling up character...")
    level_up(loaded)
    display_character(loaded)

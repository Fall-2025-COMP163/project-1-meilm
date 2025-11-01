'''
COMP 163 - Project 1: Character Creator & Saving/Loading

    Name: Isaac Manson
    Date: 31 October 2025

    AI USAGE: AI used: Perplexity

'''
# 
    # Helped me create the namedtuple logic in the "caculate_stats" function
    # Showed me how to format f-strings to work across multiple lines
    # Taught me what try contitionals are, and showed me how I can use them to check if "save_character" executed succesfully or not
    # Helped me see how to reformat the save file data to be able to turn it into a dictionary in "load_character"
    # Helped me debug Value Errors caused by me erroneously using ".isalnum()" instead of ".isnumeric()" "load_character"
    # Solved a logic error causing the dictionary keys to break when reading from "load_character" caused by me omitting the parenthesis from an ".lower()" string operation
    # Showed me how to use .update() to directly modify "char" from inside "level_up" while still passing all the test_cases
    

from collections import namedtuple
import math
import os

class_list = ['warrior', 'mage', 'rogue', 'cleric']
def create_character(name, character_class):
    '''
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    '''
    if character_class.lower() not in class_list:
        character_class = 'Warrior'
        print("That is not a valid class. As a fallback, your class has been set to: Warrior.")
    character_dict = {}
    character_dict['name'] = name
    character_dict['class'] = character_class
    character_dict['level'] = 1
    character_stats = calculate_stats(character_class, 1)
    character_dict['strength'] = character_stats.strength
    character_dict['magic'] = character_stats.magic
    character_dict['health'] = character_stats.health
    character_dict['gold'] = 100
    return character_dict
def calculate_stats(character_class, level):
    '''
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Formulas (simplified)
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    '''
    
    character_stats = namedtuple('stats', ['strength', 'magic', 'health'])
    if character_class == 'Warrior' or character_class == 'warrior':
        character_stats_namedtuple = character_stats(
            strength = 14 + level,
            magic = 3 + (level // 2),
            health = 90 + (10 * level)
            )
    elif character_class == 'Mage' or character_class == 'mage':
        character_stats_namedtuple = character_stats(
            strength = 4 + level,
            magic = 15 + level,
            health = 55 + (10 * level)
            )
    elif character_class == 'Rogue' or character_class == 'rogue':
        character_stats_namedtuple = character_stats(
            strength = 9 + level,
            magic = 7 + math.ceil(level / 2),
            health = 70 + (5 * level) 
            )
    elif character_class == 'Cleric' or character_class == 'cleric':
        character_stats_namedtuple = character_stats(
            strength = 7 + level,
            magic = 11 + round(level * 1.25),
            health = 75 + (5 * level)
            )
    else:
        print('\n\nERROR in func "calculate_stats" - Invalid input "character_class"\n\n')
    return character_stats_namedtuple

def save_character(character, filename):
    '''
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    File format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    '''
    
    try:
        with open(filename, 'w') as save_file:
            save_file.write(f'''Character Name: {character['name']}
Class: {character['class']}
Level: {character['level']}
Strength: {character['strength']}
Magic: {character['magic']}
Health: {character['health']}
Gold: {character['gold']}''')
    except Exception: return False
    else: return True

def load_character(filename):
    '''
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    '''

    character_dict = {}
    key = 0
    value = 1
    if os.path.exists(filename):
        with open(filename, 'r') as save_data:
            for line in save_data:
                key_value_pair = line.split(': ')
                if key_value_pair[value].strip().isnumeric():
                    character_dict[key_value_pair[key].lower()] = int(key_value_pair[value])
                else: character_dict[key_value_pair[key].split(' ')[-1].lower()] = key_value_pair[value].strip()
        return character_dict
    else: return None
    
def display_character(character):
    '''
    Prints formatted character sheet
    Returns: None
    
    Output format:
    === CHARACTER SHEET ===
    Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    '''    
    print(f'''=== CHARACTER SHEET ===
Name: {character['name']}
Class: {character['class']}
Level: {character['level']}
Strength: {character['strength']}
Magic: {character['magic']}
Health: {character['health']}
Gold: {character['gold']}''')

def level_up(character):
    '''
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    '''
    global char
    character['level'] += 1
    character_updated_stats = calculate_stats(character['class'], character['level'])
    character['strength'] = character_updated_stats.strength
    character['magic'] = character_updated_stats.magic
    character['health'] = character_updated_stats.health
    char.update(character)

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    

    name = input('\nEnter your character\'s name:\n')
    char_class = input('Enter your character\'s class:\nWarrior, Mage, Rogue, or Cleric: ')
    print('creating dict...')
    char = create_character(name, char_class)
    print('displaying dict...')
    display_character(char)
    print('levelling up...')
    level_up(char)
    display_character(char)
    save_file_name = input('\nWhat is the name of the file you want to save your character to?\n')
    print('saving data...')
    print(save_character(char, save_file_name))
    print('loading data...')
    print(load_character(save_file_name))
    print(char)
    print('Sucess! No errors!')
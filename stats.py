# function to return total word count in provided book
def get_word_count(book):
    return len(book.split())    #split book by white space then return the length

# function to return the total number of times a character is used in provided book
def get_character_count(book):
    char_dict = {}              # empty dictionary to hold characters
    lowercase = book.lower()    # convert all characters to lowercase, prevents duplicate characters entering dictionary
    for char in lowercase:      # for each character in lowercase string, if already in char_dict: increment count, else: add to char_dict
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[f"{char}"] = 1
    return char_dict

# function to return a dictionary of characters and their counts and return a sorted list of dictionariesd
def list_of_dictionaries_by_char(char_dict):
    character_dictionaries = []             # empty list to hold each character dictionary

    def sort_on(items):
        return items["num"]

    for k,v in char_dict.items():           # for key,value in each dictionary item
        new_dict = {}                       # empty list refresh for each k,v in char_dict

        new_dict["char"] = k                # separate k and v into their own item
        new_dict["num"] = v

        character_dictionaries.append(new_dict) #append to list

    character_dictionaries.sort(reverse=True, key=sort_on)
    return character_dictionaries
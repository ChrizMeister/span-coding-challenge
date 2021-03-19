# Code by Christopher Sommerville
# Span coding challenge

# Part 2

import json
import os
import os.path
from os import path

from NotificationModFunctions import remove_duplicates

def main():
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)

    # Prompt user for input file
    input_prompt = "Enter an input file to de-duplicate (.json) or press enter to use default data: "
    input_name = input(input_prompt)

    # Re-prompt the user for a file name or default data if an invalid file is entered
    while not path.exists(input_name) or input_name[-5:] != ".json":
        if input_name == "":
            input_name =  os.getcwd() + "\data\\" + 'notifications_new.json'
            break
        input_name = input("Invalid file name. Enter an input file (.json) or press enter to use default data")

    # Load input file
    with open(input_name) as in_file:
        data = json.load(in_file)

    # Remove duplicates
    deduped_data = remove_duplicates(data)

    # Prompt user for output destination
    output_prompt = "Enter the name of the file to output to or press enter to output results to console: "
    output_option = input(output_prompt)

    
    if output_option == "": # Output to Console
        formatted_data = json.dumps(deduped_data, indent=2)
        print("De-duplicated data:\n")
        print(formatted_data)
        input("\nFinished. Press any key to exit.")
    else: # Output deduplicated data to file
        output_name = output_option # ex: 'deduped_notifications.json'
        with open(output_name, 'w') as out_file:
            json.dump(deduped_data, out_file, ensure_ascii=False, indent=2)
        input("\nFinished. Data output to file '" + output_name + "'. Press any key to exit.")
    

if __name__ == "__main__":
    main()
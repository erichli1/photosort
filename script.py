import glob
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

INPUT_DIRECTORY = 'input'
OUTPUT_DIRECTORY = 'output'
SLASH = '/'

VALID_INPUTS = []

most_recent_folder_name = ''
most_recent_original_filename = ''
most_recent_new_filename = ''

filenames = sorted(glob.iglob(f'{INPUT_DIRECTORY}/*'))

for original_filename in filenames:
    valid_command_flag = False
    star_flag = False

    base_name = os.path.basename(original_filename)

    # open image
    plt.imshow(mpimg.imread(original_filename))
    plt.ion()
    plt.show()

    # loop until a valid command
    while not valid_command_flag:
        valid_command_flag = True
        command = input('Please enter the input: ')

        if command == '':
            folder_name = most_recent_folder_name
            break
        
        if command == 'back':
            os.rename(most_recent_new_filename, most_recent_original_filename)
            valid_command_flag = False
            print('Added file back to input folder: ' + most_recent_original_filename)
            continue

        # process for input checking
        processed_command = command.lower() # make all lowercase
        inputs = processed_command.split()
        inputs = [*set(inputs)] # remove duplicates

        # check to make sure all inputs are in VALID_INPUTS
        for input_val in inputs:
            if input_val not in VALID_INPUTS:
                print(input_val + ' was not in VALID_INPUTS')
                valid_command_flag = False
                break

        # process for actions
        inputs.sort()
        if inputs[0] == '*':
            star_flag = True
            inputs = inputs[1:]
        folder_name = ', '.join(inputs)
        most_recent_folder_name = folder_name


    # close the image
    plt.clf()

    # act on command
    new_folder_path = OUTPUT_DIRECTORY + SLASH + folder_name
    print(base_name + ' -> ' + new_folder_path)
    if not os.path.exists(new_folder_path): # if folder doesn't exist, create new one
        os.mkdir(new_folder_path)

    # move image to new folder
    new_filename = new_folder_path + SLASH
    if star_flag:
        new_filename = new_filename + 'STAR-' + base_name
    else:
        new_filename = new_filename + base_name
    os.rename(original_filename, new_filename)

    # track for 'back' and '' commands
    most_recent_original_filename = original_filename
    most_recent_new_filename = new_filename

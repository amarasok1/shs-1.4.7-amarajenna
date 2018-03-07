'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

def change_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """

    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
            image_list, file_list = get_images(directory)  
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        print n
        # Round the corners with radius = 30% of short side
        new_image = add_icon(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)  
def add_icon():       
    # Open the files in the same directory as the Python script
    directory = os.path.dirname(os.path.abspath(__file__))  
    student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
    student_img = PIL.Image.open(student_file)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
    axes[1].imshow(student_img, interpolation='none')
    axes[1].set_xticks(range(1050, 1410, 100))
    axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
    axes[1].set_ylim(1100, 850)

# Open, resize, and display earth
    earth_file = os.path.join(directory, 'earth.png')
    earth_img = PIL.Image.open(earth_file)
    earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
    fig2, axes2 = plt.subplots(1, 2)
    axes2[0].imshow(earth_img)
    axes2[1].imshow(earth_small)

# Paste earth into right eye and display
# Uses alpha from mask
    student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
    fig3, axes3 = plt.subplots(1, 2)
    axes3[0].imshow(student_img, interpolation='none')
    fig3.show()
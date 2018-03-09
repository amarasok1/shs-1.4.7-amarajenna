'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              
      
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'mainhardt.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(100, 150, 100))
axes[1].set_xlim(100, 150) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(200, 150)

# Open, resize, and display earth
yin_file = os.path.join(directory, 'yinyang.png')
yin_img = PIL.Image.open(yin_file)
yin_small = yin_img.resize((31, 31)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(yin_img)
axes2[1].imshow(yin_small)

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(yin_small, (150,200), mask=yin_small) 
# Display
fig3, axes3 = plt.subplots(1)
axes3[0].imshow(student_img, interpolation='none')
fig3.show()
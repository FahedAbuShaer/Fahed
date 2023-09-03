# %%
import numpy as np
# 1) Input and Output with Numpy
# We already saw how to read file in Python 
# However, the creators of numpy have made it even easier

# Fill in 
Data = np.loadtxt(r"Day 4\Data\ReadFile.csv", delimiter=",", dtype=int) #unpack transpose the matrix to take the columns alone instead of rows
print(Data)
a = 5
print(f"a = {a}")
# Write the file using numpy
# Fill in 

# array = np.arange(0, 100)
# np.savetxt(r"Day 4\Data", array, delimiter=",", fmt = int)

# %%
# If we have a more complex array, we can use another  
# type of file format, called pickle file format
# It is a binary file format, so it is not human    
# readable but it is very fast to read and write
# numpy has it's own version of pickle, called .npy    
# and .npz
np.save('Day 4/Data/WriteFile.npy', Data)
X = np.load('Day 4/Data/WriteFile.npy')
# npy is for single array, npz is for multiple arrays
Y = np.vstack((Data,Data))
np.savez('Day 4/Data/WriteFile.npz', X, Y)
X,Y = np.load('Day 4/Data/WriteFile.npz')
# %%
# 2) Plotting with Matplotlib
# Matplotlib is the most popular plotting library in Python
# Basic Plotting 
# PLot a cos function and a sin function from 0 to 2pi

import matplotlib.pyplot as plt

# Plot a cos function and a sin function from 0 to 2pi
# Fill in
X = np.linspace(0, 2 * np.pi, 1000)
Y = np.cos(X)
Y2 = np.sin(X)

plt.plot(X, Y, label = "cos", color = "red")
# plt.title("y = cos(x)")
# plt.legend()

plt.plot(X, Y2, "k:", label = "sin") #fmt = "k:" also works
# plt.title("y = sin(x)")
plt.legend()
plt.show()


# Change the color of the lines
# Fill in



# change the line style
# Fill in




# %%

# Histogram
# Let's plot a histogram of random numbers
# For a uniform distribution
# Fill in
x = np.random.uniform(0,100,10000)
plt.hist(x, bins = 100)
plt.savefig("uniform.png")
plt.show()

# For a normal distribution
x = np.random.normal(0,100,10000)
# Fill in 
plt.hist(x, bins = 100)
plt.show()

# For an exponential distribution
x = np.random.exponential(10,10000)
# Fill in
plt.hist(x, bins = 100)
plt.show()

# %%
# 3-D Plotting
# We can also plot 3-D plots

zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# Plot a 3-D line
# Fill in
fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot3D(xline, yline, zline)

# Data for three-dimensional scattered points
# Fill in
ax.scatter3D(xdata, ydata, zdata)
plt.show()



# Animation
from matplotlib.animation import FuncAnimation
# Make an animation of a particle moving in a circle

# Fill in 
fig = plt.figure()
def animate(i):
    i = i/5
    x = np.cos(i)
    y = np.sin(i)
    plt.clf() #clear the graph
    plt.scatter(x, y, color = 'r', s = 100)
    plt.axis('square')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.grid()
anim = FuncAnimation(fig, animate, frames = int(np.ceil(2*np.pi*5)), interval = 50)
anim.save('Animation.gif')

# %%
# Read Images in Python
# Let's read 'Image1.png' in Python
# We will use the PIL library
# to install PIL, use the following command pip install pillow
from PIL import Image, ImageOps
# Fill in 
im = Image.open("Day 4\Data\Image1.png")
plt.imshow(im)
plt.axis("off")
plt.show()

# PIL also has also image processing functions
# Let's convert the image to grayscale
# Fill in
img = ImageOps.grayscale(im)
plt.imshow(img, cmap = "Greys_r")
plt.show()

# There are many other functions, such as resize, rotate, crop, etc.
# You can convert the image to numpy array using np.array
# Fill in
array = np.array(img)
print(array)

# %%
# The opposite is also possible
# You can convert a numpy array to an image
# First load the Image2.txt file that I provided
# Then convert it to an image
# plot the image using plt.imshow 
# NOTE: The image is a grayscale image so
# you need to use cmap = 'Grays_r' option
# Then save it as a png file
# Fill in
im = np.loadtxt("Day 4\Data\Image2.txt", dtype = int, delimiter = ",")
plt.imshow(im)
plt.show()
# %%
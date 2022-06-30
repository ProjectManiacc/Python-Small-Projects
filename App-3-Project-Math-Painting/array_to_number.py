import webcolors
#create 3D numpy array of zeros,, then replace zeros (black pixels) with yellow pixels

# data = np.zeros((10,20,3),dtype=np.uint8) # fills matrix with zeros
# data[:]= [255,100,0] # assigns value to all elements of matrix
#
# # Blue patch on row
# data[1:3]=[0,0,255]
# # Green patch on column
# data[:,5:15]= [0,255,0]
# # Red patch on row and column
# data[7:9,8:12]= [255,0,0]
# img = Image.fromarray(data,'RGB') # Generates an image from matrix
# img.save('canvas.png')
a = "red"
color = webcolors.name_to_rgb(a)
print(color.red)


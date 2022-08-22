
# Import Modules
import os
import numpy as np
#Specify paths of the desired folder

path =r"C:\Users\ameyk\Desktop\testhtml"

# Change the directory
os.chdir(path)

# Read text File and find the counts of the desired words and return the counts as arrays

def read_text_file(file_path):
    
    with open(file_path, 'r', encoding="utf8") as f:
     
     data=f.read()
     k1=data.count("Bengaluru")
     k2=data.count("Bangalore")
     k=k1+k2
     c=data.count("Chennai")
     p=data.count("Pune")
     m=data.count("Mumbai")
     g=data.count("Gurgaon")
     h=np.array([k,c,p,m,g])
     return h
     
# iterate through all files in the directry and keep updating the frequency array
summ=np.array([0,0,0,0,0])
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        var1 = read_text_file(file_path)                
        summ=summ+var1
print("Number of Jobs having Bengaluru as an option",summ[0],"\nNumber of Jobs having Chennai as an option",summ[1],"\nNumber of Jobs having Pune as an option",summ[2],"\nNumber of Jobs having Mumbai as an option",summ[3],"\nNumber of jobs having Gurgaon as an option",summ[4])

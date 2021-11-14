import re

file = open("wow.txt", "r")
fileRead = file.read()
fileRead = re.sub(r"\n", " ", fileRead)

if "Mr." in fileRead:  
    fileRead = fileRead.replace("Mr.", "Mister")
if "Mrs." in fileRead: 
    fileRead = fileRead.replace("Mrs.", "Miss")
if "Dr." in fileRead: 
    fileRead = fileRead.replace("Dr.", "Doctor")
if "Jr." in fileRead: 
    fileRead = fileRead.replace("Jr.", "Junior")

fileRead = re.sub(r"\.\s([A-Z])", r".\n\1", fileRead)  
fileRead = re.sub(r"!\s", "!\n", fileRead)  
fileRead = re.sub(r"\?\s", "?\n", fileRead)  


if "Mister" in fileRead:  
    fileRead = fileRead.replace("Mister", "Mr.")
if "Miss" in fileRead:  
    fileRead = fileRead.replace("Miss", "Mrs.")
if "Doctor" in fileRead:  
    fileRead = fileRead.replace("Doctor", "Dr.")
if "Junior" in fileRead:  
    fileRead = fileRead.replace("Junior", "Jr.")

print(fileRead)
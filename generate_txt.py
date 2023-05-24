import os

path = "C:/Users/nose/Desktop/New folder/reality/test/test"
savepath = "C:/Users/nose/Desktop/New folder/"
dir_list = os.listdir(path)

with open(savepath+"test.txt", 'w') as f:
    for item in dir_list:
        if(item[-4:] == '.png' or item[-4:] == '.jpg'):
            f.write(f"data/test/{item}\n")

print("done")

import os
import csv

path = "./images"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)
dir_list.sort()
print(dir_list)
lst=[dir_list]
rows=zip(dir_list)
with open('courses.csv', 'w',newline='') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    # write.writerow(fields)
    write.writerows(rows)
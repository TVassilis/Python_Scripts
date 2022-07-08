import pandas as pd
import glob
import os 

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#Big DataFrame
all_df = pd.DataFrame()

for file in all_filenames:
    #check if a csv file is empty
    if os. stat(file).st_size == 0: 
        print(file)
        os.remove(file)
    #merge csv to one DataFrame
    else:
        df = pd.read_csv(file)
        all_df = pd.concat([df,all_df], ignore_index=True) 

#Merge the DataFrame into a csv file
all_df.to_csv("Merged_CSV.csv", index=False, encoding='utf-8-sig')

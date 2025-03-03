import csv
import pandas as pd 
from tqdm import tqdm
df = pd.read_csv("dataset/amazon_reviews_multilingual_US_v1_00.tsv/amazon_reviews_multilingual_US_v1_00.tsv", sep="\t", on_bad_lines="skip")
print(df.columns)
 
# open .tsv file
# with open("dataset/amazon_reviews_multilingual_US_v1_00.tsv/amazon_reviews_multilingual_US_v1_00.tsv", encoding="utf8") as file:
       
#     # Passing the TSV file to  
#     # reader() function
#     # with tab delimiter 
#     # This function will
#     # read data from file
#     tsv_file = csv.reader(file, delimiter="\t")
#     i = 0
#     # printing data line by line
#     for line in tsv_file:
#         # print(line)
#         i+=1
#         if i > 3231470:
#             print("length of line:",len(line))
#         else:
#             print(i)
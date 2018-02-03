
import requests as request
import os as os
# this create a file inside the titanic/src/data folder with name generate for us
# this script can be run from command line.
def extract_data(url,file_path):
    # with is like, using in c# rather 
    # than have try catch finally to close
    # close we use with in python
    with open(file_path,"w") as handle:
        response = request.get(url).text
        handle.write(response.replace('\n',''))
        #print(response.strip("\n"))

train_csv = "https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/master/train.csv"
test_csv = "https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/master/test.csv"

# get path of titanic/data/raw 
raw_data_path = os.path.join(os.path.pardir,"data","raw")

# create path for train.csv and test.csv file /data/raw/
train_data_path = os.path.join(raw_data_path,"train.csv")
test_data_path = os.path.join(raw_data_path,"test.csv")

extract_data(train_csv,train_data_path)
extract_data(train_csv,test_data_path)
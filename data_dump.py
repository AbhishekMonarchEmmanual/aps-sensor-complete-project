import pandas as pd
import pymongo 
import json

client = pymongo.MongoClient("mongodb+srv://abhimonarch:Abhi123$@cluster0.6wagv.mongodb.net/?retryWrites=true&w=majority")

data_file_path = "E:/INEURON_PROJECT_MACHINE LEARNING/aps_failure_training_set1.csv"
database_name = "aps"
collection_name = "sensor"


if __name__ == "__main__":
    
    #df = pd.read_csv(data_file_path)
    
    #df.reset_index(drop= True, inplace =True)
    
    #print(df.head(3))
    
   
    #json_record = list(json.loads(df.T.to_json()).values())
    
    
    #print(json_record[0])
    
   # client[database_name][collection_name].insert_many(json_record)
  
    
    client = pymongo.MongoClient("mongodb+srv://abhimonarch:Abhi123$@cluster0.6wagv.mongodb.net/?retryWrites=true&w=majority")
    
    


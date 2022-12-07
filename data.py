import pandas as pd
import os
from mysql import connector


data_dir = "data/"
data_files  = os.listdir(data_dir)

pat_files = []
res_files = []

for file in data_files:
    if file.startswith('p_'):
        pat_files.append(file)
    elif file.startswith('r_'):
        res_files.append(file)



def DataLib():
    patterns = pd.DataFrame(columns = ['pattern', 'tag'])
    responses = pd.DataFrame(columns = ['response', 'tag'])
    
    
    for i in range(len(pat_files)):
        
        pattern = pd.read_csv(os.path.join(data_dir, pat_files[i]))
        response = pd.read_csv(os.path.join(data_dir, res_files[i]))
    
        patterns = patterns.append(pattern, ignore_index = True)
        responses = responses.append(response, ignore_index = True)

        # Droping null values
        patterns.dropna(inplace = True) 
        responses.dropna(inplace = True)
        
    return patterns, responses



def db_con():
    mydb = connector.connect(
            host="localhost",
            user="sam",
            password='Samrat@999',
            database="maya_dataset"
            )
    
    cursor = mydb.cursor()
    return mydb,cursor


def get_dataset():
    mydb, cursor = db_con()
    
    patterns = pd.DataFrame(columns = ['pattern', 'tag'])
    responses = pd.DataFrame(columns = ['response', 'tag'])
    
    cursor.execute("show tables")
    results = cursor.fetchall()
    tables = [result[0] for result in results]
    
    for table in tables:
        query = f"select pattern, tag from {table}"
        pattern = pd.read_sql(query, mydb)
        patterns = patterns.append(pattern, ignore_index = True)
        
    
        query = f"select response, tag from {table}"
        response = pd.read_sql(query, mydb)
        responses = responses.append(response, ignore_index = True)
    
    
    # Droping null values
        patterns.dropna(inplace = True) 
        responses.dropna(inplace = True)
        
    return patterns, responses


        
        
    



if __name__ == "__main__":
    p , r = get_dataset()
    print(p,"\n\n")
    print(r)
    
 
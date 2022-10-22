import pandas as pd
import os


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


if __name__ == "__main__":
    p , r = DataLib()
    print(p,"\n\n")
    
    print(r)
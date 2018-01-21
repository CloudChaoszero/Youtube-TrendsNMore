#Convert Pivot table to DataFrame
import pandas as pd
import numpy as np

def pivotTab_toDF(dataset, value, indices, aggregFunct):
    #Pivot table
    dFrame = dataset.pivot_table(values = value, index= [ \
        indices], aggfunc = aggregFunct).sort_values(by = value, ascending = False)
    
    #Convert Pivot Table to a Dataframe
    dFrame = pd.DataFrame(dFrame.to_records())
    
    #Labeling for aggregation from pivot table
    dFrame.columns = [indices,"total_%s" % value]
    
    return(dFrame)
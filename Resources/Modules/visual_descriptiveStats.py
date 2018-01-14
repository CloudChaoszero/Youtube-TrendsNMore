import matplotlib.pyplot as plt
import string
def dataframe_stats(desired_feature,statistics, countries, dtype, datasetList):
    columns = ["views","likes","dislikes","comment_count"]
    ca_graph = datasetList[0].describe(include = [dtype])[columns]
    usa_graph = datasetList[1].describe(include = [dtype])[columns]
    gb_graph = datasetList[2].describe(include = [dtype])[columns]
    fr_graph = datasetList[3].describe(include = [dtype])[columns]
    de_graph = datasetList[4].describe(include = [dtype])[columns]

    temp_list = [ca_graph, usa_graph, gb_graph, fr_graph, de_graph]
    means = []
    std = []
    
    for stats in statistics:
        for i in range(0,5):
            if stats is "mean":
                means.append(temp_list[i].loc[stats,desired_feature])
            else:
                std.append(temp_list[i].loc[stats,desired_feature])
                
    max_ofMeans = max(means)
    max_ofStd = max(std)
    
    maxIndex_means = means.index(max_ofMeans)
    maxIndex_std = std.index(max_ofStd)
    
    li = list(ca_graph.columns)
    
    indexes_ofRegion = range(0,5)
    for stat in statistics:
        
        plt.xticks(indexes_ofRegion, countries )
        plt.title("%s of Youtube %s for each Country" % (stat.upper(), string.capwords(desired_feature) ))
        if stat is "mean":
            visualization = plt.bar(indexes_ofRegion, means, color='blue')
            visualization[maxIndex_means].set_color('r')
        else:
            visualization = plt.bar(indexes_ofRegion,std,color='blue')
            visualization[maxIndex_std].set_color('r')
        plt.show()

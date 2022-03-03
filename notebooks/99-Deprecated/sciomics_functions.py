'''
Functions to simplify sciomics notebook
Written by Stephanie Ting 1/25/2022
University of North Carolina at Chapel Hill
Last updated: 1/27/2022
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import pearsonr
import pandas as pd

'''
Creates 3D Scatterplot in matplotlib with 3 groups for the purpose of visualizing the 
3 component PCA across our 3 conditions. Plots scatterplot and does not return anything.
'''
def grouped_scatterplot_3d(values_df, group_key, colors, file_path):
    '''
    values_df - pandas DataFrame of values to plot
    group_key - dict mapping <group>:<datapoint title in df>
    file_path - file path to save figures
    '''
    
    fig=plt.figure(figsize=(10,10), dpi=100)
    ax=fig.gca(projection='3d')
    for i, j in zip(group_key, colors):
        xs=values_df.loc[group_key[i], 0].values
        ys=values_df.loc[group_key[i], 1].values
        zs=values_df.loc[group_key[i], 2]
        ax.scatter(xs, ys, zs, c=j, s=400)

    ax.legend(labels=group_key.keys())
    plt.show()
    fig.savefig(file_path)

'''
Parses results of statsmodels.stats.multicomp.pairwise_tukeyhsd for smoother processing of many 
comparisons at once. Returns pandas DataFrame with adjusted p-values for each combination of conditions.
'''
def tukeyhsd_get_significant_comparisons(tukeyhsd_results, include_CI=True, only_sig_comparisons=True):
        
    '''
    tukeyhsd_results - output of statsmodels.stats.multicomp.pairwise_tukeyhsd
    include_CI - boolean value for whether to include the confidence interval
    only_sig_comparisons - boolean value for whether to only include comparisons where we can
                            reject the null hypothesis

    '''

    summary_df=pd.DataFrame(tukeyhsd_results._results_table.data[1:], 
            columns=tukeyhsd_results._results_table.data[0])
    
    desired_comparisons = [True] if only_sig_comparisons else [True, False]  
      
    a=summary_df.loc[:,['p-adj', 'reject']]
        
    if include_CI:
            
        a['CI'] = [[i[0] for i in zip(summary_df.loc[j, ['lower', 'upper']])] for j in summary_df.index]
      
    a.index=[i+'_'+j for i,j in summary_df.loc[:,['group1', 'group2']].values]
        
    return a.loc[[True if i in desired_comparisons else False for i in summary_df['reject']]]


'''
Function to calculate Pearson correlation between columns of a DataFrame.
Returns (pandas DataFrame of Pearson correlations between columns, pandas DataFrame of p-values)
'''

def matrix_pearson(df):

    '''
    df - pandas DataFrame of values for which to calculate correlation
    '''

    pearsons={}
    pvals={}
    for column0 in df:
       pearsons[column0]=[]
       pvals[column0]=[]
       for column1 in df:
           r, p=pearsonr(df[column0], df[column1])
           pearsons[column0].append(r)
           pvals[column0].append(p)
    return(pd.DataFrame(pearsons), pd.DataFrame(pvals, dtype=float))

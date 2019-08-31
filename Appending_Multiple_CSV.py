import os
import glob  #glob to match the pattern match '.csv'
import pandas

#function Def & Input and Output Paths
def concatenate(indir=r"C:\Users\Dell\Desktop\csv",
                outfile=r"C:\Users\Dell\Desktop\Concatenated.csv"):

    #Change Directory
    os.chdir(indir)
    #
    fileList=glob.glob("*.csv")
    print(fileList)
    
    dfList=[]
    colnames=["filename","file_size","file_attributes","region_count","region_id","region_shape_attributes",
"region_attributes"]
    for filename in fileList:
        print(filename)
        df=pandas.read_csv(filename, header=None)
        dfList.append(df)
    concatDf=pandas.concat(dfList, axis=0)
    concatDf.columns=colnames
    concatDf.to_csv(outfile, index=None)
    
#function calling    
concatenate()
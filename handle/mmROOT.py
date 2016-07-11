# -*- coding:utf-8 -*-
from ROOT import *
import pandas as pd
import numpy as np

def mmSaveAsROOT(data,rootfile):
  columns = data.columns
  num_columns = data.shape[1]
  file = TFile(rootfile,'RECREATE')
  treeName = rootfile.split('.')[0]
  tree = TTree(treeName,treeName)
  b_date = np.zeros(1,dtype='int')
  b_vale = np.zeros((num_columns-1,1),dtype='float')
  i = 0
  for column in columns:
    if column=='date':
      leaf = column+'/I'
      tree.Branch(column,b_date,leaf)
    else:
      leaf = column+'/D'
      tree.Branch(column,b_vale[i],leaf)
      i = i+1
  num_rows = data.shape[0]
  for irow in range(0,num_rows):
    i = 0
    for column in columns:
      if column =='date':
        sdate =  str(data[column][irow]).split('-')
        year = int(sdate[0])
        month = int(sdate[1])
        day = int(sdate[2])
        stamp = TTimeStamp(year,month,day,8,0,0)
        print stamp.GetSec()
        b_date[0] = stamp.GetSec()
      else:
        b_vale[i][0] = data[column][irow]
        i = i+1
    tree.Fill()
  file.cd()
  tree.Write()
  file.Close()


if __name__=="__main__":
  data = pd.read_csv('wuliangye.csv')
  
  mmSaveAsROOT(data,'pp.root')

  # for column in columns:
  #   if column=='date':
  #     pass
  #   else:
  #     pass
  # col_date = data['date']
  #print col_date
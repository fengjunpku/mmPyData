# -*- coding:utf-8 -*-
import tushare as ts
import ROOT
import pandas as pd
import numpy as np
import datetime
def mmStockMonth(StcokCode):
  todayNow = str(datetime.date.today())
  monthAgo = str(datetime.date.today() - datetime.timedelta(days = 30))
  return ts.get_hist_data(StcokCode,start=monthAgo,end=todayNow)

def mmStockTodayAll():
  df = ts.get_today_all()
  df.to_csv('today.csv',encoding='utf-8')

def mmReadData(datafile):
  return pd.read_csv(datafile)

def mmSaveToRoot(data,rootfile):
  file = ROOT.TFile(rootfile,'RECREATE')
  treeName = rootfile.split('.')[0]
  tree = ROOT.TTree(treeName,treeName)
  graph = ROOT.TGraph()
  bdate = np.zeros(1,dtype=int)
  bval = np.zeros(1,dtype=float)
  tree.Branch('date',bdate,'data/I')
  tree.Branch('open',bval,'open/D')
	#data = data.sort_values(['date'],ascending=False)
  data = data.sort(['date'],ascending=False)
  col_date = data['date']
  col_open = data['open']
  size = len(col_date)
  i = 0
  while i < size:
    bdate[0] = int(col_date[i].replace('-',''))
    bval[0] = col_open[i]
    graph.SetPoint(i,bdate[0],bval[0])
    tree.Fill()
    i = i+1
  # for item in data.columns:
  #   if item == 'date':
  #     print 1
  #   else:
  #     print 0
  #print data.sort(columns='date').head(1)
  #file.cd()
  tree.Write()
  graph.Write()
  file.Close()

def mmHistory(stockcode,start='',end=''):
  #data = ts.get_hist_data(stockcode)
  #data.to_csv('wuliangye.csv')
  data = mmReadData('wuliangye.csv')
  mmSaveToRoot(data,'x.root')

if __name__=="__main__":
  mmHistory('000858')# 858 means 五 粮 液
  #mmStockTodayAll()
  #data = mmReadData()
  #data = data.ix[data.name=='小康股份',['code']]
  #index = list(data.index)[0]
  #print data.code[index]
  #line = mmReadData('today.csv')
  #line = line.ix[line.name=='万科']
  #data = line.ix[line.name=='五 粮 液']
  #print data
  #print line.loc[:,['code','name']]
  #data = mmStockMonth('sh')
  #data = mmStockTodayAll()
  #data = data.ix[data.name=='小康股份']
  #print data
  #ma5 = data.loc[:,'p_change']
  #length = len(ma5)
  #file = ROOT.TFile('data.root','RECREATE')
  #hist = ROOT.TH1D('ma5','ma5',length+1,-0.5,length+0.5)
  #while length>0:
  #  length = length-1
  #  hist.Fill(19-length,ma5[length])
  #  #print ma5.index[length].replace('-','')+" "+str(ma5[length])
  #file.cd()
  #hist.Write()
  #file.Close()

# -*- coding:utf-8 -*-
import tushare as ts
import ROOT
import pandas as pd
import datetime
def mmStockMonth(StcokCode):
  todayNow = str(datetime.date.today())
  monthAgo = str(datetime.date.today() - datetime.timedelta(days = 30))
  return ts.get_hist_data(StcokCode,start=monthAgo,end=todayNow)

def mmStockTodayAll():
  df = ts.get_today_all()
  df.to_csv('today.csv',encoding='utf-8')

def mmReadData():
  return pd.read_csv('today.csv')

if __name__=="__main__":
  #mmStockTodayAll()
  #data = mmReadData()
  #data = data.ix[data.name=='小康股份',['code']]
  #index = list(data.index)[0]
  #print data.code[index]
  line = mmReadData()
  #line = line.ix[line.name=='万科']
  print line.name
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
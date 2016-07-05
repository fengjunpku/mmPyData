# -*- coding:utf-8 -*-
import tushare as ts
import ROOT
import time
import datetime
def mmStockMonth(StcokCode):
  todayNow = str(datetime.date.today())
  monthAgo = str(datetime.date.today() - datetime.timedelta(days = 30))
  return ts.get_hist_data(StcokCode,start=monthAgo,end=todayNow)

if __name__=="__main__":
  data = mmStockMonth('sh')
  ma5 = data.loc[:,'p_change']
  length = len(ma5)
  file = ROOT.TFile('data.root','RECREATE')
  hist = ROOT.TH1D('ma5','ma5',length+1,-0.5,length+0.5)
  while length>0:
    length = length-1
    hist.Fill(19-length,ma5[length])
    #print ma5.index[length].replace('-','')+" "+str(ma5[length])
  file.cd()
  hist.Write()
  file.Close()
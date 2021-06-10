from django.http import HttpResponse
from django.shortcuts import render
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
import matplotlib.pyplot as plt
import datetime

def index(self):
    return render(self,'datareader/form.html')

def datareader(request):
        st=datetime.datetime.now()
        symbols = get_nasdaq_symbols()
        si=symbols.index[120:125]
        global data,day_len
        data={}
        day_len=[]
        start=request.POST['start']
        end=request.POST['end']
        for i in si:
            try:
                try:
                    data[i]=web.DataReader(str(i),"yahoo",str(start),str(end))
                except RemoteDataError:
                    pass
            except NameError:
                pass
    
        for i in data:
            day_len.append(len(data[i]))   
        et=datetime.datetime.now()
        params={
            "data.keys":data.keys(),
            "time":et-st,
            "data":data,
            "day_len":max(day_len)
        }
        return render(request,'datareader/datareader.html',params)
         
def hundred(request):
    max_len=max(day_len)
    st=datetime.datetime.now()
    global ma_dic
    ma_dic={}
    list=[]
    ma_list=[]
    for k in data.keys():
        if len(data[k])>=200:
            try:
                for i in range(max_len):
                    list=[]
                    for j in range(100):
                        list.append(data[k]["Close"][i+j])
                    moving_average=sum(list)/100
                    list=[]
                    ma_list.append(moving_average)
        
            except IndexError:
                pass
            ma_dic[k]=ma_list
            ma_list=[] 
        else:
            pass
    et=datetime.datetime.now()
    params={
        "time":"所要時間は"+str(et-st)+"秒です。",
        "ma_dic":ma_dic
    }
    return render(request,'datareader/hundred.html',params)

def twohundred(request):
    st=datetime.datetime.now()
    max_len=max(day_len)
    global ma_dic2
    ma_dic2={}
    list=[]
    ma_list=[]
    for k in data.keys():
        if len(data[k])>=200:
            try:
                for i in range(max_len):
                    list=[]
                    for j in range(200):
                        list.append(data[k]["Close"][i+j])
                    moving_average=sum(list)/200
                    list=[]
                    ma_list.append(moving_average)
        
            except IndexError:
                pass
            ma_dic2[k]=ma_list
            ma_list=[]
    et=datetime.datetime.now()        
    params={
        "time":"所要時間は"+str(et-st)+"秒です。",
        "ma_dic2":ma_dic2
    }
    return render(request,"datareader/twohundred.html",params)
def graphmaker(request):
    st=datetime.datetime.now()
    sml=len(ma_dic.keys())
    sml=sml-sml%4+4
    j=1
    fig=plt.figure(figsize=(25,25))
    for i in ma_dic.keys():
        plt.subplot(sml,4,j)
        term=data[i][99:].index
        term2=data[i][199:].index
        plt.plot(term,ma_dic[i],label="100days avarage")
        plt.plot(term2,ma_dic2[i],label="200days avarage")
        plt.ylabel("100 or 200days_average")
        #plt.ylim([100,1800])
        plt.title(i,fontsize=18)
        plt.legend()
        j+=1
    et=datetime.datetime.now()
    fig.savefig("static/datareader/img.png")
    params={
        "time":"所要時間は"+str(et-st)+"秒です。",
    }
    return render(request,"datareader/graph.html",params)
    

def test(request):
    return render(request,"datareader/test.html")
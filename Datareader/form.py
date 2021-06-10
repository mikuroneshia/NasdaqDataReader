from django import forms
from django.shortcuts import render
import pandas_datareader.data as web
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols
import matplotlib.pyplot as plt
import datetime

class TermForm(forms.Form):
    start=forms.CharField(label="start")
    end=forms.CharField(label="end")

def datareader(request):
        st=datetime.datetime.now()
        symbols = get_nasdaq_symbols()
        si=symbols.index[120:125]
        data={}
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
    
        print(data.keys())
        print(len(data.keys()))
        for i in data:
            print(len(data[i]))
            
        et=datetime.datetime.now()
        params={
            "data":data.keys(),
            "time":et-st
        }
        return render(request,'datareader/datareader.html',params)
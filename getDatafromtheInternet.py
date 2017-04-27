import matplotlib.pyplot as plt
import numpy as np
import urllib
import re
import datetime as dt
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):

    fig=plt.figure()
    ax1=plt.subplot2grid((1,1),(0,0))
    
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,                                                         
                                                          converters={0: bytespdate2num('%Y%m%d')})
                
##    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
##                                                          delimiter=',',
##                                                          unpack=True)                                                         
##    dateconv=np.vectorize(dt.datetime.fromtimestamp)
##    date=dateconv(date)
    
    ax1.plot_date(date, closep,'-', label='Price',color='orange')
    ax1.fill_between(date,closep,closep[0],where=(closep  > closep[0]),facecolor='purple',alpha=0.5,color='purple')
    ax1.axhline(closep[0],color='c',linewidth=3)
    ax1.fill_between(date,closep,closep[0],where=(closep  < closep[0]),facecolor='blue',alpha=0.5,color='blue')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)
    #ax1.xaxis.label.set_color('c')
    #ax1.yaxis.label.set_color('c')


    ax1.spines['left'].set_linewidth(5)

    ax1.tick_params(axis='x',colors='#f06215')
    
    ax1.set_yticks([0,10,20,30,40])
    ax1.spines['left'].set_color('c')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_color('c')
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.20,right=0.94,top=0.93,wspace=0.2,hspace=0)
    plt.show()


graph_data('EBAY')

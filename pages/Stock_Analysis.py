import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime



from plotly.express.imshow_utils import dtype_range

from pages.utils.plotly_figure import plotly_table as pt
from pages.utils.plotly_figure import filter_data,close_chart,candlestick,RSI,Moving_Average,MACD

st.set_page_config(
page_title='Stock_analysis',
    page_icon='page_with_curl',
    layout='wide'
)
st.title('Stock Analysis')
today=datetime.date.today()

col1 , col2 , col3=st.columns(3)
with col1:
    ticker =st.text_input('Stock_Ticker','TSLA')
with col2:
    start_date=st.date_input('Choose start date',datetime.date(today.year-1,today.month,today.day))
with col3:
    end_date=st.date_input('Choose End Date',datetime.date(today.year,today.month,today.day))

st.subheader(ticker)

stock=yf.Ticker(ticker)
stock_info = stock.info  # Store the response once


st.write(stock_info.get('longBusinessSummary', 'Data not available'))
st.write('***Sector :***', stock_info.get('sector', 'N/A'))
st.write('***Number of full-time employees:***', stock_info.get('fullTimeEmployees', 'N/A'))
st.write('***Website Link:***', stock_info.get('website', 'N/A'))


col1 ,col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index=['Market Cap', 'Beta', 'EPS', 'PE Ratio'])
    df[''] = [
        stock_info.get('marketCap', 'N/A'),
        stock_info.get('beta', 'N/A'),
        stock_info.get('trailingEps', 'N/A'),
        stock_info.get('trailingPE', 'N/A')
    ]
    df.index.names = [' ']
    st.plotly_chart(pt(df), use_container_width=True)

with col2:
    df = pd.DataFrame(index=['Quick Ratio', 'Revenue per Share', 'Profit Margins', 'Debt to Equity', 'Return on Equity'])
    df[''] = [
        stock_info.get('quickRatio', 'N/A'),
        stock_info.get('revenuePerShare', 'N/A'),
        stock_info.get('profitMargins', 'N/A'),
        stock_info.get('debtToEquity', 'N/A'),
        stock_info.get('returnOnEquity', 'N/A')
    ]
    df.index.names = [' ']
    st.plotly_chart(pt(df), use_container_width=True)


data=yf.download(ticker,start=start_date,end=end_date)


col1,col2,col3=st.columns(3)
change=dict(data['Close'].iloc[-1]-data['Close'].iloc[-2])
change=round(change[ticker],2)

lastval=dict(data['Close'].iloc[-1])
lastval=round(lastval[ticker],2)

col1.metric("Daily Change",lastval,change)

data = data.reset_index()
data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
data = data.set_index("Date")
last_10_df = data.tail(10).sort_index(ascending=True).round(3)

st.write('##### Historical Data (Last 10 Days)')
st.plotly_chart(pt(last_10_df))

col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12=st.columns([1,1,1,1,1,1,1,1,1,1,1,1,])

num_period=''
with col1:
    if st.button('5D'):
        num_period='5D'
with col2:
    if st.button('1M'):
        num_period='1mo'
with col3:
    if st.button('6M'):
        num_period='6mo'
with col4:
    if st.button('YTD'):
        num_period = 'ytd'
with col5:
    if st.button('1Y'):
        num_period='1y'
with col6:
    if st.button('5Y'):
        num_period='5y'
with col7:
    if st.button('MAX'):
        num_period='max'
col1,col2,col3=st.columns([1,1,4])
with col1:
    chart_type=st.selectbox('',('Candle','Line'))
with col2:
    if chart_type=='Candle':
        indicator=st.selectbox('',('RSI','MACD'))
    else:
        indicator=st.selectbox('',('RSI','Moving Average','MACD'))

ticker_=yf.Ticker(ticker)

new_df1=ticker_.history(period='max')
data1=ticker_.history(period='max')

if num_period=='':

    if chart_type=='Candle' and indicator=='RSI':
        st.plotly_chart(candlestick(data1,'1y'),use_container_width=True)
        st.plotly_chart(RSI(data1,'1Y'),use_container_width=True)

    if chart_type=='Candle' and indicator=='MACD':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width=True)
        st.plotly_chart(MACD(data1, '1Y'), use_container_width=True)

    if chart_type=='Line' and indicator=='RSI':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width=True)
        st.plotly_chart(RSI(data1, '1Y'), use_container_width=True)
    if chart_type=='Line' and indicator=='Moving Average':
        st.plotly_chart(Moving_Average(data1, '1y'), use_container_width=True)
        st.plotly_chart(MACD(data1, '1Y'), use_container_width=True)
    if chart_type=='Line' and indicator=='MACD':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width=True)
        st.plotly_chart(MACD(data1, '1Y'), use_container_width=True)
else:
    if chart_type=='Candle' and indicator=='RSI':
        st.plotly_chart(candlestick(data1,num_period),use_container_width=True)
        st.plotly_chart(RSI(data1,num_period),use_container_width=True)
    if chart_type=='Candle' and indicator=='MACD':
        st.plotly_chart(candlestick(data1, num_period), use_container_width=True)
        st.plotly_chart(MACD(data1, num_period), use_container_width=True)

    if chart_type=='Line' and indicator=='RSI':
        st.plotly_chart(close_chart(data1, num_period), use_container_width=True)
        st.plotly_chart(RSI(data1, num_period), use_container_width=True)
    if chart_type=='Line' and indicator=='Moving Average':
        st.plotly_chart(close_chart(data1, num_period), use_container_width=True)
        st.plotly_chart(Moving_Average(data1, num_period), use_container_width=True)
    if chart_type=='Line' and indicator=='MACD':
        st.plotly_chart(close_chart(data1, num_period), use_container_width=True)
        st.plotly_chart(MACD(data1, num_period), use_container_width=True)








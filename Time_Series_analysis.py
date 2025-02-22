import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime


st.set_page_config(
page_title='Trading App',
    page_icon='chart_with_upwards_trend:',
    layout='wide'
)

st.title("Trading guide app :bar_chart:")
st.header("we provide the Greatest platform for you to collect all information prior ro investing in stock")
st.image('app.png')

st.markdown('#### we provide following information ')

st.markdown("#### :one: Stock Information")  
st.write(  
    "Get real-time stock details, historical performance, and key indicators. "
    "Explore company trends, market fluctuations, and price movements to make informed investment decisions."
)

st.markdown("#### :two:  Stock Prediction")  
st.write(  
    "Using advanced forecasting models, predict the closing prices for the next 30 days based on historical data. "
    "Analyze future trends and volatility to stay ahead in the market. "
    "Make data-driven investment decisions with our AI-powered predictions!"
)

st.markdown("#### :three:  Interactive Visualizations")  
st.write(  
    "Visualize stock trends with interactive charts, historical comparisons, and key metrics. "
    "Use intuitive graphs and data-driven insights to understand stock performance better."
)

st.markdown("#### :four:  How It Works")  
st.write(  
    "1. **Choose a Page Based on Your Needs:** \n"
    "   - Go to the **Stock Analysis** page to explore historical trends and key indicators. \n"
    "   - Go to the **Stock Prediction** page to forecast stock prices for the next 30 days. \n\n"
    "2. **Enter a Stock Ticker:** Select a stock from the available US-listed companies. \n\n"
    "3. **Explore Insights:** \n"
    "   - On the **Stock Analysis** page, view price trends, historical data, and key market insights. \n"
    "   - On the **Stock Prediction** page, generate AI-powered forecasts for future stock prices. \n\n"
    "4. **Make Informed Decisions:** Use interactive charts and insights to enhance your investment strategy."
)

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

st.markdown('#### :one: Stock Information')
st.write('Through this page, you can see all the information about stocks.')

st.markdown("#### :two: Stock prediction")
st.write('You can explore predicted closing price for nexxt 30 days based on historical data and advance forecasting model. Use this tool to gain valuable insights into market trend and make informed investment Decisions')

st.markdown('#### :three: CAPM Returns')
st.write(' Discover how the capital asset pricing model (CAPM) calculates the expected return of different stock asset')

st.markdown('#### :four: CAPM Beta')
st.write('calculates beta and expected returns for individual stocks')

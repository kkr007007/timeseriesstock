import streamlit as st
import pandas as pd

from pages.Stock_Analysis import ticker
from pages.utils.plotly_figure import plotly_table, Moving_Average, Moving_Average_forecast
from pages.utils.models_fit import  get_data,get_rolling_mean,get_differencing_order,scaling,evaluate_model,stationary_check,fit_model,get_forecast,inverse_scaling

st.set_page_config(
page_title='Trading App',
    page_icon='chart_with_upwards_trend:',
    layout='wide'
)
st.title('Stock Prediction Using Statistical Model')
col1,col2,col3=st.columns(3)

with col1:
    ticker=st.text_input('Stock Ticker','AAPL')

rmse=0
st.subheader('Predicting Next 30 days Close Price '+ticker)
close_price=get_data(ticker)
rolling_price=get_rolling_mean(close_price)
differncing_order=get_differencing_order(rolling_price)
scaled_data,scaler=scaling(rolling_price)
rmse=evaluate_model(scaled_data,differncing_order)

st.write('***Model RMSE Score***',rmse)
forecast=get_forecast(scaled_data,differncing_order)

forecast['Close']=inverse_scaling(scaler,forecast['Close'])
st.write('##### Forecast Data(Next 30 Days)')
fig_tail=plotly_table(forecast.sort_index(ascending=True).round(3))
fig_tail.update_layout(height=220)
st.plotly_chart(fig_tail,use_container_width=True)

# forecast=pd.concat([rolling_price,forecast])
print(forecast)
print(rolling_price)


st.plotly_chart(Moving_Average_forecast(forecast,rolling_price,ticker),use_container_width=True)


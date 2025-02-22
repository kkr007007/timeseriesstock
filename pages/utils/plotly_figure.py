import numpy as np
import pandas as pd
import datetime
import dateutil.relativedelta
import plotly.graph_objects as go
import pandas_ta as pta
from matplotlib.pyplot import margins, legend

npNaN = np.nan
def plotly_table(dataframe):
    headerColor = 'grey'
    rowEvenColor = '#f8fafd'
    rowOddColor = 'white'
    dataframe = dataframe.reset_index()

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["<b>" + str(i)[:10] + "</b>" for i in dataframe.columns],
            line_color='#0078ff',
            fill_color='#0078ff',
            font=dict(color='white', size=16),
            height=40
        ),
        cells=dict(
            values=[dataframe[i].astype(str) for i in dataframe.columns],
            fill_color=[[rowOddColor, rowEvenColor] * (len(dataframe) // 2)],
            align='left',
            line_color='white',
            font=dict(color='black', size=15),
            height=35
        )
    )])

    fig.update_layout(height=500, margin=dict(l=0, r=0, t=0, b=0))
    return fig


def filter_data(dataframe, num_period):
    last_date = dataframe.index[-1]

    if num_period == '1mo':
        date = last_date + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = last_date + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '6mo':
        date = last_date + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == '1y':
        date = last_date + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period == '5y':
        date = last_date + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period == 'ytd':
        date = datetime.datetime(last_date.year, 1, 1,tzinfo=last_date.tz)
    else:
        date = dataframe.index[0]

    return dataframe[dataframe.index >= date]



def close_chart(dataframe, num_period=False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe['Open'], mode='lines', name='Open',
                             line=dict(width=2, color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe['Close'], mode='lines', name='Close',
                             line=dict(width=2, color='black')))
    fig.add_trace(
        go.Scatter(x=dataframe.index, y=dataframe['Low'], mode='lines', name='Low', line=dict(width=2, color='red')))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor='white', paper_bgcolor='#e1efff',
                      legend=dict(yanchor='top', xanchor='right'))
    return fig


def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=dataframe.index,
                                 open=dataframe['Open'], high=dataframe['High'],
                                 low=dataframe['Low'], close=dataframe['Close']))
    fig.update_layout(showlegend=False)
    return fig


def RSI(dataframe, num_period):
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe['RSI'], name='RSI', line=dict(width=2, color='orange')))
    fig.add_trace(go.Scatter(x=dataframe.index, y=[70] * len(dataframe), name='Overbought',
                             line=dict(width=2, color='red', dash='dash')))
    fig.add_trace(go.Scatter(x=dataframe.index, y=[30] * len(dataframe), fill='tonexty', name='Oversold',
                             line=dict(width=2, color='#79da84', dash='dash')))

    fig.update_layout(yaxis_range=[0, 100], height=200, plot_bgcolor='white', paper_bgcolor='#e1efff',
                      margin=dict(l=0, r=0, t=0, b=0),
                      legend=dict(orientation='h', yanchor='top', y=1.02, xanchor='right', x=1))
    return fig


def Moving_Average(dataframe, num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe['SMA_50'], mode='lines', name='SMA 50',
                             line=dict(width=2, color='purple')))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500, margin=dict(l=0, r=20, t=20, b=0), plot_bgcolor='white', paper_bgcolor='#e1efff',
                      legend=dict(yanchor='top', xanchor='right'))
    return fig


def MACD (dataframe, num_period):
    macd = pta.macd(dataframe['Close'])
    dataframe['MACD'] = macd.iloc[:, 0]
    dataframe['MACD Signal'] = macd.iloc[:, 1]
    dataframe['MACD Hist'] = macd.iloc[:, 2]

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe['MACD'], name='MACD', line=dict(width=2, color='orange')))
    fig.add_trace(go.Scatter(x=dataframe.index, y=dataframe['MACD Signal'], name='MACD Signal',
                             line=dict(width=2, color='red', dash='dash')))

    fig.update_layout(height=200, plot_bgcolor='white', paper_bgcolor='#e1efff', margin=dict(l=0, r=0, t=0, b=0),
                      legend=dict(orientation='h', yanchor='top', y=1.02, xanchor='right', x=1))
    return fig


def Moving_Average_forecast(forecast, historical_data,ticker):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data[str(ticker)],
                             mode='lines', name='Close Price',
                             line=dict(width=2, color='black')))

    fig.add_trace(go.Scatter(x=forecast.index, y=forecast['Close'],
                             mode='lines', name='Future Close Price',
                             line=dict(width=2, color='red', dash='dash')))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500, margin=dict(l=10, r=20, t=20, b=0),
                      plot_bgcolor='white', paper_bgcolor='#e1efff',
                      legend=dict(yanchor='top', xanchor='right',font=dict(color="black")))

    return fig

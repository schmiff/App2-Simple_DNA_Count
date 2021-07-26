import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple Stock Price Viewer Web App

Shown are the stock closing price and volume of Intellia Therapeutics!

""")

# define ticker symbol
tickerSymbol = 'NTLA'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-6-26')
# Open High      Low Close     Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)




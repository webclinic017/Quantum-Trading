from fastapi import FastAPI, HTTPException
from sentiment import sentimentAnalysisClass
import threading
import time
import pandas as pd
import os

sentiment = FastAPI(title="Quantum Trading Sentiment Analysis API")

# Sentiment Analysis for each crypto
@sentiment.on_event("startup")
def startup_event():
    # Start the continuous task in a separate thread on application startup
    continuous_thread = threading.Thread(target=all_crypto_sa, daemon=True)
    continuous_thread.start()

# Endpoints
@sentiment.get('/')
async def root():
        return {'text':'Welcome to QuantumTrading Sentiment Analysis API'}

def all_crypto_sa():

    try:

        btc = sentimentAnalysisClass("BTC")
        eth = sentimentAnalysisClass("ETH")
        link = sentimentAnalysisClass("LINK")
        ltc = sentimentAnalysisClass("LTC")

        while True:
            btc.analyse()
            print("Updated BTC sentiment analysis")
            eth.analyse()
            print("Updated ETH sentiment analysis")
            link.analyse()
            print("Updated LINK sentiment analysis")
            ltc.analyse()
            print("Updated LTC sentiment analysis")

            time.sleep(5)

    except Exception as e:
        # Print or log the exception details
        print(f"Exception: {e}")
        return {"error": f"Internal server error: {e}"}
        
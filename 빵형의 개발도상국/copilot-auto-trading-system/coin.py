# Make Upbit bitcoin trading bot

import time
import pyupbit
import datetime

access = "your-access"          # 본인 값으로 변경
secret = "your-secret"          # 본인 값으로 변경
myToken = "your-token"          # 본인 값으로 변경

# def print(token, channel, text):
#     response = requests.post("https://slack.com/api/chat.postMessage",
#         headers={"Authorization": "Bearer "+token},
#         data={"channel": channel,"text": text}
#     )
    
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=1)
    start_time = df.index[0]
    return start_time

def get_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

def get_ma10(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=10)
    ma10 = df['close'].rolling(10).mean().iloc[-1]
    return ma10

def get_ma20(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=20)
    ma20 = df['close'].rolling(20).mean().iloc[-1]
    return ma20

def get_ma60(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=60)
    ma60 = df['close'].rolling(60).mean().iloc[-1]
    return ma60

def get_ma120(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute1", count=120)
    ma120 = df['close'].rolling(120).mean().iloc[-1]
    return ma120

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC", interval="minute1", count=7)
    ror = df['close'].pct_change()[-2]
    return ror

# 로그인
upbit = pyupbit.Upbit(access, secret)
print ("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC") #9:00
        end_time = start_time + datetime.timedelta(days=1) #9:00 + 1일

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.5)
            ma5 = get_ma5("KRW-BTC")
            ma10 = get_ma10("KRW-BTC")
            ma20 = get_ma20("KRW-BTC")
            ma60 = get_ma60("KRW-BTC")
            ma120 = get_ma120("KRW-BTC")
            current_price = pyupbit.get_current_price("KRW-BTC")
            if target_price < current_price and ma5 < ma60 :
            #    krw = upbit.get_balance("KRW")
            #    if krw > 5000:
            #        upbit.buy_market_order("KRW-BTC", krw*0.9995)
                print("이 가격에 삼 : " +str(current_price))
        else:
            btc = upbit.get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
                print("이 가격에 팜 : " +str(current_price))
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
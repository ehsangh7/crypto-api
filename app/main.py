from fastapi import FastAPI
from pycoingecko import CoinGeckoAPI


app = FastAPI()

cg = CoinGeckoAPI()

@app.get("/")
def root():
    return cg.get_coins_list()

@app.get("/coins/list")
def get_coins_list():
    return cg.get_coins_list()


@app.get("/coins/markets")
def get_coins_markets():
    return cg.get_coins_markets(vs_currency='usd')


@app.get("/coins/{id}")
def get_coin_by_id(id: str):
    return cg.get_coin_by_id(id=id)



@app.get("/coins/{id}/ticker")
def get_coin_ticker_by_id(id: str):
    return cg.get_coin_ticker_by_id(id=id)



@app.get("/coins/{id}/history")
def get_coin_history_by_id(id: str, date: str):
    return cg.cg.get_coin_history_by_id(id=id, date=date, localization='false')


@app.get("/global")
def get_global():
    return cg.get_global()

@app.get("/exchanges")
def get_exchanges_list():
    return cg.get_exchanges_list()

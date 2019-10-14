from kumex.marketData.marketData import MarketData
from kumex.trade.trade import TradeData
from kumex.user.user import UserData
from kumex.wsConnectToken.token import GetToken


class Market(MarketData):
    pass


class User(UserData):
    pass


class Trade(TradeData):
    pass


class WsToken(GetToken):
    pass



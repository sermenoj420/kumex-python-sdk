import ssl
import asyncio
from kumex.client import WsToken
from kumex.ws_client import KumexWsClient
from kumex.client import Trade
from kumex.client import Market
from kumex.client import User

context = ssl._create_unverified_context()

# async def main():
#     async def deal_msg(msg):
#         if msg['topic'] == '/contractMarket/level3:XBTUSDM':
#             print(msg["data"])
#         elif msg['topic'] == '/contractMarket/level3:XBTMH20':
#             print(f'Get XBTUSDM level3:{msg["data"]}')
#
#     # is public
#     # client = WsToken()
#     # is private
#     client = WsToken(key='', secret='', passphrase='')
#     # is sandbox
#     # client = WsToken(is_sandbox=True)
#     ws_client = await KumexWsClient.create(None, client, deal_msg, private=False)
#     # await ws_client.subscribe('/contract/instrument:XBTUSDM')
#     await ws_client.subscribe('/contractMarket/level3:XBTMZ19,XBTMH20,XBTUSDM')
#     while True:
#         await asyncio.sleep(60, loop=loop)


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    client = Market()
    # client = User('', '', '',is_sandbox=True)
    # data = client.create_limit_order("XBTUSDM", 'buy', '10', '10000', '6500')
    data = client.l3_order_book('XBTUSDM')
    print(data)



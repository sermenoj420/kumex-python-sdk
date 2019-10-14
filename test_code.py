import asyncio
from kumex.client import WsToken
from kumex.ws_client import KumexWsClient


async def main():
    async def deal_msg(msg):
        if msg['topic'] == '/contractMarket/level2:XBTUSDM':
            print(f'Get XBTUSDM tick:{msg["data"]}')

    # is public
    # client = WsToken()
    # is private
    client = WsToken(key='', secret='', passphrase='')
    # is sandbox
    # client = WsToken(is_sandbox=True)
    ws_client = await KumexWsClient.create(loop, client, deal_msg)
    await ws_client.subscribe('/contractMarket/level2:XBTUSDM')
    while True:
        await asyncio.sleep(60, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

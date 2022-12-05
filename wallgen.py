from mnemonic import Mnemonic
from web3 import Web3
print('print qty of wallets')
cnt = int(input())
print('print rpc address, exapmple: https://rpc.ankr.com/eth')
rpc = input()
counter = 0
while counter <= cnt:
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    MAIN_NET_HTTP_ENDPOINT = rpc
    w3 = Web3(Web3.HTTPProvider(MAIN_NET_HTTP_ENDPOINT))
    account = w3.eth.account.enable_unaudited_hdwallet_features()
    account = w3.eth.account.from_mnemonic(words)
    private_key = account.privateKey
    private_key = private_key.hex(private_key)
    public_key = account.address
    print(public_key)
    with open('wallets.txt', 'a') as file:
        file.write(f'\n address: {public_key} , private_key: {private_key} , seed: {words}')
    counter += 1

print(f'Generated {cnt} wallets')


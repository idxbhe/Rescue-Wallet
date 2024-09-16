import requests
from web3 import Web3
import json

BLOXROUTE_AUTH_HEADER = 'AUTH HEADER HERE'
RPC_URL = 'ENTER RPC URL HERE' # BSC RPC URL
HACKED_PRIVATE_KEY = 'COMPROMISED PRIVATE KEY HERE'
DONATOR_PRIVATE_KEY = 'DONATOR PRIVATE KEY'
BNB_AMOUNT = 0.001 # BNB AMOUNT SEND IN FIRST TRANSACTION BUNDLE TO HACKED WALLET

TOKEN_SC = 'TOKEN ADDRESS HERE'
TOKEN_DECIMAL = 18
TOKEN_AMOUNT = 200 # WITHDRAW TOKEN AMOUNT TO DONATOR WALLET

TOKEN_ABI = [{
        "constant": False,
        "inputs": [{"name": "_to", "type": "address"},{"name": "_value","type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "","type": "bool"}],
        "type": "function"}]


provider = Web3(Web3.HTTPProvider(RPC_URL))
hacked_wallet = provider.eth.account.from_key(HACKED_PRIVATE_KEY)
donator_wallet = provider.eth.account.from_key(DONATOR_PRIVATE_KEY)

# FIRST TRANSACTION BUNDLE
# DONATOR --------> BNB(for fee) --------> HACKED
# you can adjust Gas and Gas Limit here
tx1 = {
    "to": hacked_wallet.address,
    "value": Web3.to_wei(BNB_AMOUNT, 'ether'),
    "gas": 21000,
    "gasPrice": Web3.to_wei(5, 'gwei'),
    "nonce": provider.eth.get_transaction_count(donator_wallet.address),
    "chainId": 56
}
signed_tx1 = provider.eth.account.sign_transaction(tx1, DONATOR_PRIVATE_KEY)
raw_tx1 = signed_tx1.raw_transaction.hex()


# SECOND TRANSACTION BUNDLE
# DONATOR <-------- TOKEN <-------- HACKED
token = provider.eth.contract(address=TOKEN_SC, abi=TOKEN_ABI)
wei_token_amount = TOKEN_AMOUNT * (10 ** TOKEN_DECIMAL) # TO WEI UNIT

# you can adjust Gas and Gas Limit here
tx2 = token.functions.transfer(donator_wallet.address, wei_token_amount).build_transaction({
    'chainId': 56,  
    'gas': 110000, # Gas Limit
    'gasPrice': Web3.to_wei(5, 'gwei'),
    'nonce': provider.eth.get_transaction_count(hacked_wallet.address)
})
signed_tx2 = provider.eth.account.sign_transaction(tx2, HACKED_PRIVATE_KEY)
raw_tx2 = signed_tx2.raw_transaction.hex()


# SENDING BUNDLE TO MEV BUILDER / BLOXROUTE
# adjust the "after" if the BUNDLE is fail
after = 10
block_number = hex(provider.eth.get_block_number() + after)

request_data = {
    "id":"1",
    "method":"blxr_submit_bundle",
    "params":{"transaction":[raw_tx1, raw_tx2],
              "blockchain_network":"BSC-Mainnet",
              "block_number":block_number,
              "mev_builders":{"all":""}
              }
    }
url = "https://mev.api.blxrbdn.com"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"{BLOXROUTE_AUTH_HEADER}"
}
response = requests.post(url, headers=headers, data=json.dumps(request_data))

print(response.status_code)
print(response.json())
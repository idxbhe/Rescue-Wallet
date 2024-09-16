# Rescue-Wallet
Simple Python Script to rescue compromised wallet from Sweeper Bot using BloXRoute MEV Bundle Service. see docs: [BloXRoute](https://docs.bloxroute.com/apis/mev-solution/bsc-bundle-submission)

### Prerequisites
1. Have +- 0.005 BNB in Donator Wallet.
2. Bloxroute Auth Header. you can get it for free with Sign Up : [Bloxroute Site](https://portal.bloxroute.com/registration)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/idxbhe/Rescue-Wallet.git
cd Rescue-Wallet
```

2. Install required python module:
```bash
pip install -r requirements.txt
```

### How to Use

Fill all what you need to fill in this code:
```python
BLOXROUTE_AUTH_HEADER = 'AUTH HEADER HERE'
RPC_URL = 'ENTER RPC URL HERE' # BSC RPC URL
HACKED_PRIVATE_KEY = 'COMPROMISED PRIVATE KEY HERE'
DONATOR_PRIVATE_KEY = 'DONATOR PRIVATE KEY'
BNB_AMOUNT = 0.001 # BNB AMOUNT SEND IN FIRST TRANSACTION BUNDLE TO HACKED WALLET

TOKEN_SC = 'TOKEN ADDRESS HERE'
TOKEN_DECIMAL = 18
TOKEN_AMOUNT = 200 # WITHDRAW TOKEN AMOUNT TO DONATOR WALLET
```

and run the script:
```bash
python3 rescue-with-bundle.py
```

you will get **Bundle Hash** if your request success. 

**Checking Bundle Status**

However, bundle that are successfully sent will not necessarily be accepted by the validator. to check whether the bundle was accepted or rejected. run the `bundle-status.py` and see what message you get. 

```bash
python3 bundle-status.py
```

Bundle Status Message References : [Bloxroute Docs](https://docs.bloxroute.com/apis/bsc-bundle-trace)

Need Help?
**Telegram** :[@idxbhe](https://t.me/Kingbhe)

**Don't forget to give me tips** #1F600 
- ETH/BSC/POLYGON: `0xcc6a227e29848ca0b18b0c144332da2a4d2565e0`

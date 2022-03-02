# XMRavalanche
Recursive function to generate Monero outputs. The functon takes an array of monero-python account object arrays.
Because the transaction fees are unpredictable before creating the transaction the input is split into 15 outputs and 1 change output.
The number of outputs grow exponentially by the power of 15.

## Dependencies
https://github.com/urethiuui1/monero-python

## Start Wallet RPC on Stagenet
```
./monerod --stagenet
```
```
./monero-wallet-rpc --stagenet --wallet-file testwallet --password "" --rpc-bind-port 28088 --disable-rpc-login
```

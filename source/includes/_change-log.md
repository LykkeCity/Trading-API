# Change Log

## 2021-11-23 | All deposit addresses endpoint
Added new endpoint to get deposit addresses for all assets

## 2021-08-12 | API Blockchain Gateway

In this new upgrade, we introduce the possibility of performing blockchain withdrawals and deposits. 

To be able to use this feature, it is necessary to have a KYC-approved account in Lykke Wallet. Before making a deposit you need to create your deposit addresses, calling the method '/api/operations/deposits/addresses'.

To keep things secure, we have introduced a whitelist of addresses for you to manage. In this list, you will enter the details of the addresses that will be interacting with your API wallet. It is important to highlight, that any address addition, will become effective in 48 hours.

For testing and rollout purposes, at the moment, the only supported blockchain is ETC. However, very soon we plan to add the following assets:
* BTC
* ETH
* BCH
* LTC
* XLM
* ERC20
* XTZ (FA1.2 and FA2)
* DOT
* DOGE

** Warning: since this is a new feature, there might be errors/bugs that were not contemplated during the testing phase. If you find any, please do let us know by contacting support@lykke.com

** Warning: Before making a deposit you need to create your deposit addresses, calling the method '/api/operations/deposits/addresses'.

## 2021-05-03 | PageSize

Increased ```take``` parameter to 1000 in pagination requests.

## 2021-01-11 | Multiple orderbook updates

Added ```assetPairIds``` for orderbook updates stream request to get updates for multiple orderbooks.

## 2020-10-23 | Public trades endpoint

Added public trades rest api and grpc endpoints.

## 2020-09-02 | Public trades stream, fixes

Added public stream for trades. Fixed an issue with orderbook updates stream.

## 2020-08-25 | Side property in the Trade

Added ```Side``` property for the ```Trade```.

## 2020-08-10 | The new method in Private API

Added a new method [Get order by Id](#get-order-by-id) to search an order by ID.

Added to documentation details about default values to existing methods.

Added tp documentation information about [Request Rate Limits](#request-limits)

## 2020-07-01 | The release of a new HFT API.

The new release of the updated APIs now supports **gRPC protocol**. This protocol uses HTTP 2.0 Standard, WebSocket, and ProtoBuf, which helps to reduce latency, allows more efficient use of the CPU and provides access to network resources on the client's side.

The best part of the **gRPC** protocol is how easy it is to integrate the Lykke APIs in many programming languages by using the proto-files which generates a client library.[Proto files with contracts](https://github.com/LykkeCity/Trading-API/tree/master/grpc_proto_contracts). This generates a new response format, abstracted from the protocol itself, allowing you to work in a custom manner with the Lykke APIs regardless of the protocol.


The New Response of the server is no longer included in the **gRPC protocol**, enabling each user to work with the API in their unique manner. Additionally, the contracts in the **Rest API protocol** also had been updated. A new set of functions and models is being used, very similar to those of **gRPC protocol**.

Because of the **gRPC protocol**, the user now is able to receive Market Data Stream directly from the server:

* **Order book** - Get snapshots and changes in the orders book.
* **Prices** - Get snapshots and changes in current prices.
* **24hr Ticker Statistics** - Get a snapshot of the current ticker statistics and the stream of data updates.

We have also added the capability to receive data flow from your API account using **gRPC protocol**:

* **Balances** - Get a snapshot of your account balance and the flow of balance changes.
* **Transactions** - Get a flow of completed trades of your API account.
* **Orders** - Get a flow of changes in active orders of your API account.

We have enhanced the overall performance of the APIs by optimising different areas such as: reducing data backlogs, prices, book orders, balances and active orders.

We have also optimised the API Keys management and enhanced overall security.

* The secret key of the HFT account can only be received after creating or regenerating the key.
* The secret key of HFT account will only be regenerated when using 2FA.
* The transfer of funds between the HFT account and the Lykke Wallet Trading account will require 2FA authentication.

We have also increased the optimisation of internal serves and bug fixes.




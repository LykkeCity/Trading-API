# Change Log

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




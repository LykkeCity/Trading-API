# Change Log

## 2020-07-01 | The release of a new HFT API.

The new APIs now support the **gRPC** protocol. This protocol uses HTTP 2.0 standard, WebSocket, and ProtoBuf, helping to reduce latency, more efficient use of the CPU, and network resources on the client-side. 

The best part of the **gRPC** protocol is how easy it is to integrate the Lykke APIs in many programming languages by using the proto-files which generates a client library.[Proto files with contracts](https://github.com/LykkeCity/Trading-API/tree/master/grpc_proto_contracts). This generates a new response format, abstracted from the protocol itself, allowing you to work in a custom manner with the Lykke APIs regardless of the protocol.

A new response format from the server, abstracted from the protocol. Allows you to work in a custom manner with the API regardless of the protocol.
The contracts in the Rest API protocol have been updated as well. A new set of functions and models is being used, very similar to gRPC protocol. We have removed deprecated methods and created new methods. You can find them in [Swagger UI](https://hft-apiv2.lykke.com/swagger/ui/index.html).

Thanks to the **gRCP** protocol we added the ability to receive a market data stream from the server:

* **Order books** - Getting snapshots and changes in the order book.
* **Prices** - Getting snapshots and changes in current prices.
* **24hr Ticker Statistics** - Getting a snapshot of the current ticker statistics and the stream of data updates.

We have also added the ability to receive data flow from your API account  using **gRPC** protocol:

* **Balances** - Gets a snapshot of your account balance and the flow of balance changes.
* **Transactions** - Gets a flow of completed trades on your API account.
* **Orders** - Gets a flow of changes in active orders on your API account.

We have enhanced the overall performance of the APIs by optimizing different areas such as: reducing data backlogs, prices, order books, balances, and active orders.

We have also optimized the API Keys management and increased the overall security.

* You will be receiving the secret key of the HFT account only after creating or regenerating the key.
* The secret key of HFT account will only be regenerated when using 2FA.
* The transfer of funds between the HFT account and the Lykke Wallet Trading account will require 2FA authentication.

We have also increased the optimization of internal serves and bug fixes.




# Private Stream APIs

**Streaming API** allows you to subscribe to events from the server and receive them in streaming mode upon the occurrence of the event.

**Streaming API** is available only when working with the **gRPC protocol**. In the RestAPI protocol, streaming APIs are not available.

Private **Streaming API** allows you to receive your live API account data.


## Follow the current balance

Get the current balance from the account.

After subscribing you will get a data stream. The first packet in the stream will always contain a complete snapshot with the current balances of your API account. The following packages in the data stream will come after an asset balance change.

### Request

**gRPC:** `hft.PublicService.GetBalanceUpdates`

### Response

The array of balance by assets.

Property | Type | Description
-------- | ---- | -----------
assetId | string | Asset unique identifier.
available | [decimal](#decimal-type) | Available amount.
reserved | [decimal](#decimal-type) | Amount reserved in active orders.
timestamp | [TimeStamp](#timestamp-type) | Last balance update on current asset.


```protobuf
package hft;

service PrivateService {
  rpc GetBalanceUpdates (google.protobuf.Empty) returns (stream BalanceUpdate);
}

message BalanceUpdate {
    repeated Balance balances = 1;
}

message Balance {
    string assetId = 1;
    string available = 2;
    string reserved = 3;
    google.protobuf.Timestamp timestamp = 4;
}
```

## Follow trades

Get the flow of trades on the account.

After subscribing you will get a data stream. The packages in the data stream will come after the trade happen.

### Request

**gRPC:** `hft.PublicService.GetTradeUpdates`

### Response

Array of trades:

Property | Type | Description
-------- | ---- | -----------
id | string | Trade ID.
orderId | string | Order ID of this trade.
assetPairId | string | Trade asset pair ID (symbol).
timestamp | [TimeStamp](#timestamp-type) | Trade timestamp.
role | string | Trade role. `Maker` or `Taker`.
price | [decimal](#decimal-type) | Trade price.
baseVolume | [decimal](#decimal-type) | Trade volume in base asset.
quoteVolume | [decimal](#decimal-type) | Trade volume in quote asset.
baseAssetId | string | Base asset ID.
quoteAssetId | string | Quote asset ID.
fee | TradeFee | *(optional)* Trade Fee description.

**TradeFee**

Property | Type | Description
-------- | ---- | -----------
assetId | string | Asset ID
size | [decimal](#decimal-type) | Fee size

```protobuf
package hft;

service PrivateService {
  rpc GetTradeUpdates (google.protobuf.Empty) returns (stream TradeUpdate);
}

message TradeUpdate {
    repeated Trade trades = 1;
}

message Trade {
    string id = 1;
    google.protobuf.Timestamp timestamp = 2;
    string assetPairId = 3;
    string orderId = 4;
    string role = 5;
    string price = 6;
    string baseVolume = 7;
    string quoteVolume = 8;
    string baseAssetId = 9;
    string quoteAssetId = 10;
    TradeFee fee = 11;
}

message TradeFee {
    string size = 1;
    string assetId = 2;
}
```

## Follow updates by orders

Get the flow of orders updates from your API account.

After subscribing you will receive a data stream. Packets in the data stream will come after any changes with the active order - placing, matching, canceling, etc.

### Request

**gRPC:** `hft.PublicService.GetOrderUpdates`

### Response

Array with order state:

Property | Type | Description
-------- | ---- | -----------
id | string | Unique Order ID.
timestamp |  [TimeStamp](#timestamp-type) | Timestamp for order creation.
lastTradeTimestamp | [TimeStamp](#timestamp-type) | Timestamp for last trade by order.
status | string | Order status. List of statuses [here](#order-statuses).
assetPairId | string | Symbol unique identifier.
type | string | Order type: `Market` or `Limit`.
side | string | Order side: `Sell` or `Buy`.
price | [decimal](#decimal-type) | Order price (in quote asset for one unit of base asset).
volume | [decimal](#decimal-type) | Order volume (in base asset).
filledVolume | [decimal](#decimal-type) | Order filled volume (in base asset).
remainingVolume | [decimal](#decimal-type) | Order remaining volume to be filled (in base asset).

```protobuf
package hft;

service PrivateService {
  rpc GetOrderUpdates (google.protobuf.Empty) returns (stream OrderUpdate);
}

message OrderUpdate {
    repeated Order orders = 1;
}

message Order {
    string id = 1;
    google.protobuf.Timestamp timestamp = 2;
    oneof optional_lastTradeTimestamp {
        google.protobuf.Timestamp lastTradeTimestamp = 3;
    }
    string status = 4;
    string assetPairId = 5;
    string type = 6;
    Side side = 7;
    string price = 8;
    string volume = 9;
    string filledVolume = 10;
    string remainingVolume = 11;
    string cost = 12;
}
```



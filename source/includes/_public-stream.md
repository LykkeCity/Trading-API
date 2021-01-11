# Public Stream APIs

**Streaming API** allows you to subscribe to events from the server and receive them in streaming mode upon the occurrence of the event.

**Streaming API** is available only when working with the **gRPC protocol**. In the RestAPI protocol, streaming APIs are not available.

Public **Streaming API** allows you to receive live market data without authorization.

## Follow the current prices

Get current prices online.

After subscribing you will get a data stream. The first packet in the stream will always contain a complete snapshot with the current prices. The following packages in the data stream will come after an asset price change.

### Request

**gRPC:** `hft.PublicService.GetPriceUpdates`

### Query Parameters

Parameter | Type | Default | Description
--------- | ---- | ------- | -----------
assetPairIds | array of string | null | Filter by Symbol unique ID. If the array is empty then the server return prices by all symbols.

### Response

Array of prices by symbols:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
timestamp | [TimeStamp](#timestamp-type) | Timestamp of last order book update.
bid | [decimal](#decimal-type) | Bid price.
ask | [decimal](#decimal-type) | Ask price.

```protobuf
package hft;

service PublicService {
  rpc GetPriceUpdates (PriceUpdatesRequest) returns (stream PriceUpdate);
}

message PriceUpdatesRequest {
    repeated string assetPairIds = 1;
}

message PriceUpdate {
    string assetPairId = 1;
    string bid = 2;
    string ask = 3;
    google.protobuf.Timestamp timestamp = 4;
}
```


## Follow current 24hr Statistics

Get current 24hr Ticker Price Change Statistics online.

After subscribing you will get a data stream. The first packet in the stream will always contain a complete snapshot with the current 24hr Ticker Price Change Statistics. The following packages in the data stream will come after a data change.

### Request

**gRPC:** `hft.PublicService.GetTickerUpdates`

### Response

Array with asset description:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
volumeBase | [decimal](#decimal-type) | Trading volume for the last 24h in base asset.
volumeQuote | [decimal](#decimal-type) | Trading volume for the last 24h in quote asset.
priceChange | [decimal](#decimal-type) | Price changes(in %) in the last 24h.
lastPrice | [decimal](#decimal-type) | The last trade price.
high | [decimal](#decimal-type) | The maximum trade price from the last 24h.
low | [decimal](#decimal-type) | The minimum trade price from the last 24h.
timestamp | [TimeStamp](#timestamp-type) | Last update timestamp.

```protobuf
package hft;

service PublicService {
  rpc GetTickerUpdates (google.protobuf.Empty) returns (stream TickerUpdate);
}

message TickerUpdate {
    string assetPairId = 1;
    string volumeBase = 2;
    string volumeQuote = 3;
    string priceChange = 4;
    string lastPrice = 5;
    string high = 6;
    string low = 7;
    google.protobuf.Timestamp timestamp = 8;
}
```

## Follow Order Book Ticker

Get current asset pair order books online.

After subscribing you will get a data stream. The first packet in the stream will always contain a complete snapshot with current order books. The follow packages in data stream will only contain changed levels in the order book.

Please note that if a level is deleted at a specific price, a packet containing the level with the specified price will be sent to the stream with zero volume.

### Query Parameters

Parameter | Type | Default | Description
--------- | ---- | ------- | -----------
assetPairId | string | null | *(Optional)* 
assetPairIds|string|Array of string|*(Optional)*
Identificator of specific symbol. By default return all symbols.

### Request

**gRPC:** `hft.PublicService.GetOrderbookUpdates`

### Response

Array with order books:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
timestamp | [TimeStamp](#timestamp-type) | Timestamp of last order book update.
bids | Array of PriceLevel | List of changed buy orders.
asks | Array of PriceLevel | List of changed sell orders.

**PriceLevel**:

Property | Type | Description
-------- | ---- | -----------
p | [decimal](#decimal-type) | Order price indicated in quoted asset per unit of base asset.
v | [decimal](#decimal-type) | Order volume indicated in base asset.

```protobuf
package hft;

service PublicService {
  rpc GetOrderbookUpdates (OrderbookUpdatesRequest) returns (stream Orderbook);
}

message OrderbookUpdatesRequest {
    string assetPairId = 1;
    repeated string assetPairIds = 2;
}

message Orderbook {
    string assetPairId = 1;
    google.protobuf.Timestamp timestamp = 2;
    repeated PriceVolume bids = 3;
    repeated PriceVolume asks = 4;

    message PriceVolume {
        string p = 1;
        string v = 2;
    }
}
```

## Get public trades

Get current public trades online.

After subscribing you will get 50 latest trades for provided asset pair. The first packet in the stream will always contain a complete snapshot with the 50 latest trades. The following packages in the data stream will come after the trade happen.

### Request

**gRPC:** `hft.PublicService.GetPublicTradeUpdates`

### Query Parameters

Parameter | Type | Default | Description
--------- | ---- | ------- | -----------
assetPairId | string | - | Filter by Symbol unique ID.

### Response

Array of trades by symbols:

Property | Type | Description
-------- | ---- | -----------
id | string | Trade ID.
assetPairId | string | Symbol unique identifier.
dateTime | [TimeStamp](#timestamp-type) | Timestamp of the trade.
volume | [decimal](#decimal-type) | Bid price.
price | [decimal](#decimal-type) | Ask price.
side | string | Trade side: `Sell` or `Buy`.

```protobuf
package hft;

service PublicService {
  rpc GetPublicTradeUpdates (PublicTradesUpdatesRequest) returns (stream PublicTradeUpdate);
}

message PublicTradesUpdatesRequest {
    string assetPairId = 1;
}

message PublicTradeUpdate {
    repeated PublicTrade trades = 1;
}

message PublicTrade {
    string id = 1;
    string assetPairId = 2;
    google.protobuf.Timestamp dateTime = 3;
    string volume = 4;
    string price = 5;
    string side = 6;
}
```

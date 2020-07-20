# Public APIs

## Get all assets

Get a list of supported assets with parameters.

### Request

**gRPC:** `hft.PublicService.GetAssets`

**Rest API:** `GET /api/assets`

### Response

Array of assets:

Parameter | Default | Description
--------- | ------- | -----------
assetId | string | Asset unique identifier.
name | string | Asset name.
symbol | string | Asset symbol.
accuracy | uint | Maximum number of digits after the decimal point which are supported by the asset.

```json
GET /api/assets

> Response 200 (application/json) - success response

{
    "payload": [
        {
            "assetId": "AUD",
            "name": "AUD",
            "displayName": "AUD",
            "accuracy": 2
        },
        {
            "assetId": "BTC",
            "name": "BTC",
            "displayName": "BTC",
            "accuracy": 8
        }
    ]
}
```

```protobuf
package hft;

service PublicService {
  rpc GetAssets (google.protobuf.Empty) returns (AssetsResponse);
}

message AssetsResponse {
    repeated Asset payload = 1;
    hft.common.Error error = 2;  // NULL
}

message Asset {
    string assetId = 1;  // BTC
    string name = 2;     // Bitcoin
    string symbol = 3;   // BTC
    int32 accuracy = 4;  // 8
}
```

## Get Asset by ID

Get information about a specific asset.

### Request

**gRPC:** `hft.PublicService.GetAsset`

**RestAPI:** `GET /api/assets/{assetId}`

### Query Parameters

Parameter | Type | Place | Description
--------- | ---- | ----- | -----------
assetId | string | path | Asset uniquie ID

### Response

Asset description:

Property | Type | Description
-------- | ---- | -----------
assetId | string | Asset unique identifier.
name | string | Asset name.
symbol | string | Asset symbol.
accuracy | uint | Maximum number of digits after the decimal point which are supported by the asset.

```json
GET /api/assets/{assetId}

> Response 200 (application/json) - success response

{
    "payload": {
        "assetId": "BTC",
        "name": "Bitcoin",
        "displayName": "BTC",
        "accuracy": 8
    }
}
```

```protobuf
package hft;

service PublicService {
  rpc GetAsset (AssetRequest) returns (AssetResponse);
}

message AssetRequest {
    string assetId = 1;   // BTC
}

message AssetResponse {
    Asset payload = 1;
    hft.common.Error error = 2;  // NULL
}

message Asset {
    string assetId = 1;  // BTC
    string name = 2;     // Bitcoin
    string symbol = 3;   // BTC
    int32 accuracy = 4;  // 8
}
```
## Get all asset pairs

Get all supported asset pairs (symbols).

### Request

**gRPC:** `hft.PublicService.GetAssetPairs`

**RestAPI:** `GET /api/assetpairs`

### Response

Array of trading instruments.

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
baseAssetId | string | Base asset unique identifier.
quoteAssetId | string | Quote asset unique identifier.
name | string | Trading instrument name.
priceAccuracy | uint | Trading instrument price accuracy.
baseAssetAccuracy | uint | Base asset accuracy.
quoteAssetAccuracy | uint | Quote asset accuracy.
minVolume | [decimal](#decimal-type) | Minimum order volume in base currency.
minOppositeVolume | [decimal](#decimal-type) | Minimum order volume in quote currency.

```json
GET /api/assetpairs

> Response 200 (application/json) - success response

{
  "payload": [
    {
      "assetPairId": "BTCUSD",
      "baseAssetId": "BTC",
      "quoteAssetId": "91960f78-7ea1-49f7-be27-34221a763b02",
      "name": "BTC/USD",
      "priceAccuracy": 3,
      "baseAssetAccuracy": 8,
      "quoteAssetAccuracy": 2,
      "minVolume": 0.0001,
      "minOppositeVolume": 1
    },
    {
      "assetPairId": "BTCLKK1Y",
      "baseAssetId": "BTC",
      "quoteAssetId": "LKK1Y",
      "name": "BTC/LKK1Y",
      "priceAccuracy": 2,
      "baseAssetAccuracy": 8,
      "quoteAssetAccuracy": 2,
      "minVolume": 0.0001,
      "minOppositeVolume": 4
    }
  ]
}
```

```protobuf
package hft;

service PublicService {
  rpc GetAssetPairs (google.protobuf.Empty) returns (AssetPairsResponse);
}

message AssetPairsResponse {
    repeated AssetPair payload = 1;
    hft.common.Error error = 2;      // NULL
}

message AssetPair {
    string assetPairId = 1;          // "BTCLKK1Y"
    string baseAssetId = 2;          // "BTC"
    string quoteAssetId = 3;         // "LKK1Y"
    string name = 4;                 // "BTC/LKK1Y"
    int32 priceAccuracy = 5;         // 2
    int32 baseAssetAccuracy = 6;     // 8
    int32 quoteAssetAccuracy = 7;    // 2
    string minVolume = 8;            // 0.0001
    string minOppositeVolume = 9;    // 4
}
```

## Get a specific asset pair

Get a specific asset pair.

### Request

**gRPC:** `hft.PublicService.GetAssetPair`

**RestAPI:** `GET /api/assetpairs/{assetPairId}`

### Query Parameters

Parameter | Type | Place | Description
--------- | ---- | ----- | -----------
assetPairId | string | path | Symbol unique ID

### Responce

Trading instrument:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
baseAssetId | string | Base asset unique identifier.
quoteAssetId | string | Quote asset unique identifier.
name | string | Trading instrument name.
priceAccuracy | uint | Trading instrument price accuracy.
baseAssetAccuracy | uint | Base asset accuracy.
quoteAssetAccuracy | uint | Quote asset accuracy.
minVolume | [decimal](#decimal-type) | Minimum order volume in base currency.
minOppositeVolume | [decimal](#decimal-type) | Minimum order volume in quote currency.

```json
GET /api/assetpairs/{assetPairId}

> Response 200 (application/json) - success response

{
  "payload":
    {
      "assetPairId": "BTCUSD",
      "baseAssetId": "BTC",
      "quoteAssetId": "91960f78-7ea1-49f7-be27-34221a763b02",
      "name": "BTC/USD",
      "priceAccuracy": 3,
      "baseAssetAccuracy": 8,
      "quoteAssetAccuracy": 2,
      "minVolume": 0.0001,
      "minOppositeVolume": 1
    }
}
```

```protobuf
package hft;

service PublicService {
  rpc GetAssetPair (AssetPairRequest) returns (AssetPairResponse);
}

message AssetPairResponse {
    AssetPair payload = 1;
    hft.common.Error error = 2;      // NULL
}

message AssetPair {
    string assetPairId = 1;          // "BTCLKK1Y"
    string baseAssetId = 2;          // "BTC"
    string quoteAssetId = 3;         // "LKK1Y"
    string name = 4;                 // "BTC/LKK1Y"
    int32 priceAccuracy = 5;         // 2
    int32 baseAssetAccuracy = 6;     // 8
    int32 quoteAssetAccuracy = 7;    // 2
    string minVolume = 8;            // 0.0001
    string minOppositeVolume = 9;    // 4
}
```

## Asset Pair Order Book Ticker

Get the Order Book by asset pair. The order books contain a list of Buy(Bid) and Sell(Ask) orders with their corresponding price and volume.

### Request

**gRPC:** `hft.PublicService.GetOrderbooks`

**RestAPI:** 

`GET /api/orderbooks`
`GET /api/orderbooks?assetPairId={assetPairId}&depth={depth}`

### Query Parameters

Parameter | Type | Place | Description
--------- | ---- | ----- | -----------
assetPairId | string | query | *(Optional)* Identificator of specific symbol. By default return all symbols.
depth | uint | query | *(Optional)* How many levels need to include in order books. By default include all levels.

### Response

Array of Order Books by instruments:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
timestamp | [TimeStamp](#timestamp-type) | Timestamp of last order book update.
bids | Array of PriceLevel | List of buy orders.
asks | Array of PriceLevel | List of sell orders.

**PriceLevel**:

Property | Type | Description
-------- | ---- | -----------
p | [decimal](#decimal-type) | Order price indicated in quoted asset per unit of base asset.
v | [decimal](#decimal-type) | Order volume indicated in the base asset.

```json
GET /api/orderbooks
GET /api/orderbooks?assetPairId={assetPairId}&depth={depth}

> Response 200 (application/json) - success response

{
  "payload": [
    {
      "assetPairId": "BTCUSD",
      "timestamp": 1594725117313
      "bids": [
        {
          "v": 0.06771538,
          "p": 9599
        },
        {
          "v": 0.05210805,
          "p": 9599
        }
      ],
      "asks": [
        {
          "v": -1.67230494,
          "p": 9633.613
        },
        {
          "v": -0.1,
          "p": 9641.42
        }
      ]
    }
  ]
}
```

```protobuf
package hft;

service PublicService {
  rpc GetOrderbooks (OrderbookRequest) returns (OrderbookResponse);
}

message OrderbookRequest {
    string assetPairId = 1;
    int32 depth = 2;
}

message OrderbookResponse {
    repeated Orderbook payload = 1;
    hft.common.Error error = 2;       // NULL
}

message Orderbook {
    string assetPairId = 1;           // "BTCUSD"
    google.protobuf.Timestamp timestamp = 2;  // "seconds": "1594742656", "nanos": 167000000
    repeated PriceVolume bids = 3;    // {p="9010", v="0.01"}, {p="9000", v="1.0"}
    repeated PriceVolume asks = 4;    // {p="9020", v="0.12"}, {p="9030", v="0.71001"}

    message PriceVolume {
        string p = 1;
        string v = 2;
    }
}
```

## 24hr Ticker Price Change Statistics

24-hour rolling-window price change statistics.

### Request

**gRPC:** `hft.PublicService.GetTickers`

**RestAPI:** 

`GET /api/tickers`
`GET /api/tickers?assetPairIds=BTCUSD&assetPairIds=BTCEUR`

### Query Parameters


Parameter | Type | Place | Description
--------- | ---- | ----- | -----------
assetPairIds | string | query | *(Optional)* Filter by symbols. By default returns all asset pairs information.

### Response

Asset description:

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



```json
`GET /api/tickers`
`GET /api/tickers?assetPairIds=BTCUSD&assetPairIds=BTCEUR`

> Response 200 (application/json) - success response

{
  "payload": [
    {
      "assetPairId": "BTCEUR",
      "volumeBase": 0.98657285,
      "volumeQuote": 8350.5868,
      "priceChange": 0.036057567781542336,
      "lastPrice": 8620,
      "high": 8620,
      "low": 8320,
      "timestamp": 1594725117313
    },
    {
      "assetPairId": "BTCUSD",
      "volumeBase": 2.15139075,
      "volumeQuote": 20649.0296,
      "priceChange": 0.023048622404312356,
      "lastPrice": 9637.117,
      "high": 9700,
      "low": 9397.999,
      "timestamp": 1594725117313
    }
  ]
}
```
```protobuf
package hft;

service PublicService {
  rpc GetTickers (TickersRequest) returns (TickersResponse);
}

message TickersRequest {
    repeated string assetPairIds = 1;
}

message TickersResponse {
    repeated TickerUpdate payload = 1;
    hft.common.Error error = 2;    // NULL
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

## Get current prices

Get current prices by symbols.

### Request

**gRPC:** `hft.PublicService.GetPrices`

**RestAPI:** 

`GET /api/prices`

`GET /api/prices?assetPairIds={AssetPairID-1}&assetPairIds={AssetPairID-2}&...`

### Query Parameters

Parameter | Type | Place | Description
--------- | ---- | ----- | -----------
assetPairIds | array of string | query | *(Optional)* List of identificators of specific symbols. By default return all symbols.

### Response

Array of prices by symbols:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
timestamp | [TimeStamp](#timestamp-type) | Timestamp of last order book update.
bid | [decimal](#decimal-type) | Bid price.
ask | [decimal](#decimal-type) | Ask price.

```json
GET /api/prices
GET /api/prices?assetPairId={assetPairId}&depth={depth}

> Response 200 (application/json) - success response

{
"payload": [
    {
      "assetPairId": "BTCEUR",
      "bid": 8089.122,
      "ask": 8149.614,
      "timestamp": 1594750211438
    },
    {
      "assetPairId": "BTCUSD",
      "bid": 9243.277,
      "ask": 9283.495,
      "timestamp": 1594750214503
    }
  ]
}
```

```protobuf
package hft;

service PublicService {
  rpc GetPrices (PricesRequest) returns (PricesResponse);
}

message PricesRequest {
    repeated string assetPairIds = 1;
}

message PricesResponse {
    repeated PriceUpdate payload = 1;
    hft.common.Error error = 2;
}

message PriceUpdate {
    string assetPairId = 1;
    string bid = 2;
    string ask = 3;
    google.protobuf.Timestamp timestamp = 4;
}
```



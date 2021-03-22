# Private APIs

This group method requires API Key Authentication.

If you would like to create your API key, please sign up in [here](https://wallet.lykke.com/?utm_source=github&utm_medium=api_doc&utm_campaign=api_documentation) and start trading with Lykke!. If you need a step by step guide you may check our Help Center in [here](https://support.lykke.com/hc/en-us/articles/360000552605-How-do-I-create-an-API-Wallet-).

## Get the current balance

Get the current balance from the API Key account.

### Request

**gRPC:** `hft.PrivateService.GetBalances`

**Rest API:** `GET /api/balance`

### Response

The array of balance by assets.

Property | Type | Description
-------- | ---- | -----------
assetId | string | Asset unique identifier.
available | [decimal](#decimal-type) | Available amount.
reserved | [decimal](#decimal-type) | Amount reserved in active orders.
timestamp | [TimeStamp](#timestamp-type) | Last balance update on current asset.


```json
GET /api/balance

> Response 200 (application/json) - success response

{
  "payload": [
    {
      "assetId": "BTC",
      "available": 2.433002,
      "reserved": 0.35,
      "timestamp": 1592928606187
    },
    {
      "assetId": "USD",
      "available": 0,
      "reserved": 0,
      "timestamp": 1592928506187
    },
  ]
}
```

```protobuf
package hft;

service PrivateService {
  rpc GetBalances (google.protobuf.Empty) returns (BalancesResponse);
}

message BalancesResponse {
    repeated Balance payload = 1;
    hft.common.Error error = 2;
}

message Balance {
    string assetId = 1;
    string available = 2;
    string reserved = 3;
    google.protobuf.Timestamp timestamp = 4;
}
```

## Get trade history

Gets the trading history of an account. Also, with the use of parameters, it can returns a single order.

### Request

**gRPC:** `hft.PrivateService.GetTrades`

**Rest API:**

`GET /api/trades`

`GET /api/trades/order/{orderId}`

### Query Parameters

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
assetPairId | string | query | null| *(optional)* Symbol unique identifier.
side | string | query | null | *(optional)* Side of trade: `buy` or `sell`.
offset | uint | query | 0 | *(optional)* Skip the specified number of elements.
take | uint | query | 100 |*(optional)* Take the specified number of elements.
from | [TimeStamp](#timestamp-type) | query | null | *(optional)* From timestamp.
to | [TimeStamp](#timestamp-type) | query | null | *(optional)* To timestamp.

### Query Parameters

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
orderId | string | path | - | Unique Order ID

### Response

Array of trades:

Property | Type | Description
-------- | ---- | -----------
id | string | Trade ID.
orderId | string | Order ID of this trade.
assetPairId | string | Trade asset pair ID (symbol).
timestamp | [TimeStamp](#timestamp-type) | Trade tamestamp.
role | string | Trade role. `Maker` or `Taker`.
price | [decimal](#decimal-type) | Trade price.
baseVolume | [decimal](#decimal-type) | Trade volume in base asset.
quoteVolume | [decimal](#decimal-type) | Trade volume in quote asset.
baseAssetId | string | Base asset ID.
quoteAssetId | string | Quote asset ID.
fee | TradeFee | *(optional)* Trade Fee description.
side | string | Trade side: `Sell` or `Buy`.

**TradeFee**

Property | Type | Description
-------- | ---- | -----------
assetId | string | Asset ID
size | [decimal](#decimal-type) | Fee size



```json
GET /api/trades
GET /api/trades/order/{orderId}

> Response 200 (application/json) - success response

{
  "payload": [
    {
      "id": "b3a25228-5384-4b5f-95c3-3eb31f7e9aee",
      "timestamp": 1592938116360,
      "assetPairId": "BTCUSD",
      "orderId": "616374a2-02d0-4f01-8dce-6266fc30d4a1",
      "role": "Taker",
      "price": 9575.823,
      "baseVolume": 0.0001,
      "quoteVolume": 0.9576,
      "baseAssetId": "BTC",
      "quoteAssetId": "USD",
      "fee": null,
      "side": "buy"
    },
    {
      "id": "ebceb096-7766-437a-8e98-e1f6532f0268",
      "timestamp": 1592938016360,
      "assetPairId": "BTGUSD",
      "orderId": "fa19c315-b8b2-49bd-a426-45f9384fbad3",
      "role": "Taker",
      "price": 8.5,
      "baseVolume": 0.01,
      "quoteVolume": 0.085,
      "baseAssetId": "a4954205-48eb-4286-9c82-07792169f4db",
      "quoteAssetId": "USD",
      "fee": null,
      "side": "buy"
    }]
}
```

```protobuf
package hft;

service PrivateService {
  rpc GetTrades (TradesRequest) returns (TradesResponse);
}

message TradesRequest {
    string assetPairId = 1;
    oneof optional_side {
        Side side = 2;
    }
    int32 offset = 3;
    int32 take = 4;
    string from = 5;
    string to = 6;
}

message TradesResponse {
    repeated Trade payload = 1;
    hft.common.Error error = 2;
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
    Side side = 12;
}

message TradeFee {
    string size = 1;
    string assetId = 2;
}
```

## Get active or closed orders

Get active orders or closed orders from history.

### Request

**gRPC:** 

`hft.PrivateService.GetActiveOrders`

`hft.PrivateService.GetClosedOrders`

**Rest API:**

`GET /api/orders/active`

`GET /api/orders/closed`

### Query Parameters


Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
assetPairId | string | query | null | *(optional)* Symbol unique identifier.
offset | uint | query | 0 | *(optional)* Skip the specified number of elements.
take | uint | query | 100 | *(optional)* Take the specified number of elements.


### Response

Response description:

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

```json
GET /api/orders/active
GET /api/orders/closed

> Response 200 (application/json) - success response

{
  "payload": [
    {
      "id": "0c336213-0a64-44a8-9599-e88bf6aa1b69",
      "timestamp": 1592928606187,
      "lastTradeTimestamp": null,
      "status": "Placed",
      "assetPairId": "BTCUSD",
      "type": "Limit",
      "side": "Buy",
      "price": 4000,
      "volume": 0.0001,
      "filledVolume": 0,
      "remainingVolume": 0.0001
    }
  ]
}
```

```protobuf
package hft;

service PrivateService {
  rpc GetActiveOrders (OrdersRequest) returns (OrdersResponse);
  rpc GetClosedOrders (OrdersRequest) returns (OrdersResponse);
}

message OrdersRequest {
    string assetPairId = 1;
    int32 offset = 2;
    int32 take = 3;
}

message OrdersResponse {
    repeated Order payload = 1;
    hft.common.Error error = 2;
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

## Get order by Id

Get order by id from history.

### Request

**gRPC:** 

`hft.PrivateService.GetOrder`

**Rest API:**

`GET /api/orders/{orderId}`

### Query Parameters


Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
orderId | string | query | null | Unique Order ID.

### Response

Response description:

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

```json
GET /api/orders/0c336213-0a64-44a8-9599-e88bf6aa1b69

> Response 200 (application/json) - success response

{
  "payload":
    {
      "id": "0c336213-0a64-44a8-9599-e88bf6aa1b69",
      "timestamp": 1592928606187,
      "lastTradeTimestamp": null,
      "status": "Placed",
      "assetPairId": "BTCUSD",
      "type": "Limit",
      "side": "Buy",
      "price": 4000,
      "volume": 0.0001,
      "filledVolume": 0,
      "remainingVolume": 0.0001
    }
}
```

```protobuf
package hft;

service PrivateService {
  rpc GetOrder (OrderRequest) returns (OrderResponse);
}

message OrderRequest {
    string orderId = 1;
}

message OrderResponse {
    Order payload = 1;
    hft.common.Error error = 2;
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

## Place a limit order

Place a limit order.

### Request

**gRPC:** `hft.PrivateService.PlaceLimitOrder`

**Rest API:** `POST /api/orders/limit`

### Request

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
assetPairId | string | body | - | Symbol unique identifier.
side | string | body | - | Order side: `Sell` or `Buy`.
volume | [decimal](#decimal-type) | body | - | Order volume (in base asset).
price | [decimal](#decimal-type) | body | - | Order price(in quote asset for one unit of base asset).
  
```json
> Request to create a limit order

{
  "assetPairId": "BTCUSD",
  "side": "buy",
  "volume": 0.0001,
  "price": 4000
}
```

### Response

Response description:

Property | Type | Description
-------- | ---- | -----------
orderId | string | Unique order ID

```json
POST /api/orders/limit

> Response 200 (application/json) - success response

{
  "payload": {
    "orderId": "0c336213-0a64-44a8-9599-e88bf6aa1b69"
  },
  "error": null
}
```


```protobuf
package hft;

service PrivateService {
  rpc PlaceLimitOrder (LimitOrderRequest) returns (LimitOrderResponse);
}

message LimitOrderRequest {
    string assetPairId = 1;
    Side side = 2;
    string volume = 3;
    string price = 4;
}

message LimitOrderResponse {
    LimitOrderPayload payload = 1;
    hft.common.Error error = 2;

    message LimitOrderPayload {
        string orderId = 1;
    }
}
```

## Place a market order 

Place a [Fill-Or-Kill](https://en.wikipedia.org/wiki/Fill_or_kill) market order.

### Request

**gRPC:** `hft.PrivateService.PlaceLimitOrder`

**Rest API:** `POST /api/orders/market`

### Request

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
assetPairId | string | body | - | Symbol unique identifier.
side | string | body | - | Order side: `Sell` or `Buy`.
volume | [decimal](#decimal-type) | body | - | Order volume (in base asset).

```json
> Request to create a market order

{
  "assetPairId": "BTCUSD",
  "side": "Buy",
  "volume": 1.554
}
```

### Response

Response description:

Property | Type | Description
-------- | ---- | -----------
orderId | string | Unique order ID.
price | [decimal](#decimal-type) | Market order result price.

```json
POST /api/orders/market

> Response 200 (application/json) - success response

{
  "payload": {
    "orderId": "string",
    "price": 6445.222311
  }
}
```

```protobuf
package hft;

service PrivateService {
  rpc PlaceMarketOrder (MarketOrderRequest) returns (MarketOrderResponse);
}

message MarketOrderRequest {
    string assetPairId = 1;
    Side side = 2;
    string volume = 3;
}

message MarketOrderResponse {
    MarketOrderPayload payload = 1;
    hft.common.Error error = 2;

    message MarketOrderPayload {
        string orderId = 1;
        string price = 2;
    }
}
```

## Place multiple limit orders

Place multiple limit orders in one package.
The method also allows you to replace orders in the order book. You can replace all orders completely, or each separately.

### Request

**gRPC:** `hft.PrivateService.PlaceBulkLimitOrder`

**Rest API:** `POST /api/orders/bulk`

### Request

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
assetPairId | string | body | - | Symbol unique identifier.
cancelPreviousOrders | bool | body | false | Cancel existing orders by AssetPair before placing new orders. Default: False.
cancelMode | string | body | null | Strategy for canceling orders if the "cancelPreviousOrders" parameter is activated. `bothSides`, `sellSide`, `buySide`.
orders | array of BulkOrder | body | List of new orders to place.

**BulkOrder (REST):**

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
orderAction | string | body | - | order side: `buy` or `sell`.
volume | [decimal](#decimal-type) | body | - | Order volume (in base asset).
price | [decimal](#decimal-type) | body | - | Order price(in quote asset for one unit of base asset).
oldId | string | body | null | Identifier of the order to be replaced. If the parameter is specified, the new order will replace the existing order with the specified ID. If there is no order with the specified ID, then the new order will not be placed.

  
```json
> Request to create a limit order

{
  "assetPairId": "BTCUSD",
  "cancelPreviousOrders": true,
  "cancelMode": "bothSides",
  "orders": [
    {
      "orderAction": "buy",
      "volume": 1,
      "price": 9600,
      "oldId": "0c336213-0a64-44a8-9599-e88bf6aa1b69"
    }
  ]
}
```

### Response

Response description:

Property | Type | Description
-------- | ---- | -----------
assetPairId | string | Symbol unique identifier.
statuses | array of BulkOrderItemStatus | Array with report about each new order.

**BulkOrderItemStatus:**

Property | Type | Description
-------- | ---- | -----------
id | string| Order ID
error | [ErrorCode](#error-codes) | Order result.
volume | [decimal](#decimal-type) | Order volume (in base asset).
price | [decimal](#decimal-type) | body | Order price(in quote asset for one unit of base asset).


```json
POST /api/orders/bulk

> Response 200 (application/json) - success response

{
  "payload": {
    "assetPairId": "BTCUSD",
    "statuses": [
      {
        "id": "0c113553-0a64-35a1-3221-a12bf6ba1564",
        "error": "success",
        "volume": 1,
        "price": 9600
      }
    ]
  },
  "error": null
}
```

```protobuf
package hft;

service PrivateService {
  rpc PlaceBulkLimitOrder (BulkLimitOrderRequest) returns (BulkLimitOrderResponse);
}

message BulkLimitOrderRequest {
    string assetPairId = 1;
    bool cancelPreviousOrders = 2;
    oneof optional_cancelMode {
        CancelMode cancelMode = 3;
    }
    repeated BulkOrder orders = 4;
}

message BulkLimitOrderResponse {
    BulkLimitOrderPayload payload = 1;
    hft.common.Error error = 2;

    message BulkLimitOrderPayload {
        string assetPairId = 1;
        repeated BulkOrderItemStatus statuses = 2;
    }
}

message BulkOrderItemStatus {
    string id = 1;
    hft.common.ErrorCode error = 2;
    string volume = 3;
    string price = 4;
}
```

## Mass cancel orders

Cancel all active orders or filter order to cancel by AssetPair or Side.

### Request

**gRPC:** `hft.PrivateService.CancelAllOrders`

**Rest API:** `DELETE /api/orders`

### Query Parameters

Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
assetPairId | string | query | null | *(Optional)* Symbol unique identifier (All asset pairs by default).
side | string | query | null | *(Optional)* Order side `Buy` or `Sell` (both sides by default).


### Response

No content

```json
DELETE /api/orders

> Response 200 (application/json) - success response

{
  "payload": null
}
```

```protobuf
package hft;

service PrivateService {
  rpc CancelAllOrders (CancelOrdersRequest) returns (CancelOrderResponse);
}

message CancelOrdersRequest {
    string assetPairId = 1;
    Side side = 2;
}

message CancelOrderResponse {
    bool payload = 1;
    hft.common.Error error = 2;
}
```

## Cancel orders by ID

Cancel a specific order by order ID.

### Request

**gRPC:** `hft.PrivateService.CancelAllOrders`

**Rest API:** `DELETE /api/orders/{orderId}`

### Query Parameters


Parameter | Type | Place | Default | Description
--------- | ---- | ----- | ------- | -----------
orderId | string | path | - | Unique Order ID.

### Response

No content

```json
DELETE /api/orders/{orderId}

> Response 200 (application/json) - success response

{
  "payload": null
}
```

```protobuf
package hft;

service PrivateService {
  rpc CancelOrder (CancelOrderRequest) returns (CancelOrderResponse);
}

message CancelOrderRequest {
    string orderId = 1;
}

message CancelOrderResponse {
    bool payload = 1;
    hft.common.Error error = 2;
}
```

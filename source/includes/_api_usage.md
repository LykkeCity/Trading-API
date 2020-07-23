# Protocol description

Lykke HFT API allows users to use 2 kinds of protocol `gRPC API` and `Rest API`. Both kinds of APIs support the same methods with the same data format, but only gRPC API supports receiving streaming data from the platform.

## gRPC API

The gRPC API utilizes a new generation of RPC framework that includes working with `HTTP 2`, `ProtoBuf`, and `WebSocket` for faster and more efficient interaction with the platform. The `gRPC framework` uses the declarative description of the contract in the `.proto` files. On the basis of which you can easily generate a client library in many [programming languages](https://grpc.io/docs/languages/). Also, the `gRPC framework` supports working with `stream`, which makes it easy to receive events from the server.

 **Lykke team strongly recommends using gRPC API protocol to communicate with the platform** 

Read more about `gRPC framework`: [https://grpc.io/](https://grpc.io/)

A useful tool for manual gRPC API requests: 

* [BloomRPC](https://github.com/uw-labs/bloomrpc) - UI tool to interact with gRPC servers (when using BloomRPC make sure to use TLS with server certificate (TLS button))
* [grpcurl](https://github.com/fullstorydev/grpcurl) - a command-line tool that lets you interact with gRPC servers

**API Endpoint**: 

* `hft-apiv2-grpc.lykke.com:443`

**Proto files**

* [common.proto](https://github.com/LykkeCity/Trading-API/blob/master/grpc_proto_contracts/common.proto) :Common data models
* [isalive.proto](https://github.com/LykkeCity/Trading-API/blob/master/grpc_proto_contracts/isalive.proto) : Is Alive API service
* [publicService.proto](https://github.com/LykkeCity/Trading-API/blob/master/grpc_proto_contracts/publicService.proto) : Public API service
* [privateService.proto](https://github.com/LykkeCity/Trading-API/blob/master/grpc_proto_contracts/privateService.proto) : Private API service

## Rest API

The rest API uses the classic HTTP based framework that includes working with `HTTP 1.1`, and `JSON`. Rest API allows users to just call RPC methods without streaming data from the server.

**Disclaimer:** The rest API has been added for backward compatibility. **The Lykke team recommends against using the Rest API protocol in favor of the gRPC protocol.**

A useful tool for manual rest API requests: [HFT API Swagger](https://hft-apiv2.lykke.com/swagger/ui/index.html)

**API Endpoint**: 

- https://hft-apiv2.lykke.com/api

# API usage


## Allowed HTTP Verbs
- `PUT` : Updates a resource.
- `POST` : Creates a resource.
- `GET` : Gets a resource or a list of resources.
- `DELETE` : Deletes a resource.

## Description Of Usual HTTP Server Responses
- 200 `OK` : The request was successful.
- 401 `Unauthorized` : Authentication failed.
- 404 `Not Found` : Endpoint was not found.
- 500 `Internal Server Error` : Server error.

## Response structure

Every response contains two fields - `payload` and `error`. A successful response will contain the response data in the `payload` field and the *null* in the `error` field, and vice versa for the error response.

Here you have a list of errors you might encounter in the paragraph **Error codes** at the end of the document.

> Successful response. Property `error` is null.

```json
{
    "payload": {
        ...
    },
    "error": null
}
```

```protobuf
package hft;

message Response {
    PayloadType payload = 1;
    hft.common.Error error = 2;  // error is NULL
}
```

> Error response. Property `error` is not null.

```json
{
    "error": {
        "code": "itemNotFound",
        "message": "Asset not found",
        "fields": {
            "assetId": "Asset not found"
        }
    },
    "payload": null
}
```

```protobuf
package hft.common;

message Error {
    ErrorCode code = 1;                  // 1100
    string message = 2;              // "Asset not found"
    map<string, string> fields = 3;  // "assetId" : "Asset not found"
}

enum ErrorCode {
    success = 0;
    runtimeError = 1001;
    itemNotFound = 1100;
    
/* Full list in the paragraph **Error codes** at the end of the document */

}

package hft;

message Response {
    PayloadType payload = 1;
    hft.common.Error error = 2;      // error is NOT NULL
}
```

## Authorization

You can create your API keys in [here](https://wallet.lykke.com/?utm_source=github&utm_medium=api_doc&utm_campaign=api_documentation). You can also check our step by step guide [here](https://support.lykke.com/hc/en-us/articles/360000552605-How-do-I-create-an-API-Wallet-).

To use the API keys you should just add a header `Authorization: Bearer <your API Key>` with the bearer token on your request.

> Request Header

```json
  "Authorization": "Bearer **********************************"
```

```protobuf
  "Authorization": "Bearer **********************************"
```

## Decimal type
Here you can see: How to manage decimal types (Price, Volume, Amount, etc) in API contract.

In the gRPC API contract, the decimal type is presented as a string type, with a textual representation of the number. This is done in order to avoid problems with the non-strict precision "double" type.

In the Rest API contact, the decimal type is presented as `number` with strict precision.

> Example with decimal type

```json
{
    "price": 222231.33420001911,
    "volume": 0.0000001
}
```

```protobuf
message Body {
    string price = 1;   // "222231.33420001911"
    string volume = 2;  // "0.0000001"
}
```

## Timestamp type
Here you can see: How to manage the `TimeStamp` type in the API contract.

<i>The timestamp is always used in the <b>time zone UTC+0</b></i>

In the Rest API contact, the `TimeStamp` type is presented as a `number` with "Milliseconds in Unix Epoch" format of date-time.

In the gRPC API contract, the `TimeStamp` type is presented as a `google.protobuf.Timestamp` type.

> Example with timestamp

```json
{
   "Timestamp": 1592903724406
}
```

```protobuf
import "google/protobuf/timestamp.proto";

google.protobuf.Timestamp time_name = 1;  // 1592903724406
```


## Order statuses

List of possible order states

Name | Meaning
---- | -------
Placed | Order in order book.
PartiallyMatched | Order in order book and partially filled.
Matched | Order is filled.
Pending | An order is pending a trigger to be placed in the order book.
Cancelled | Order is cancelled by user.
Replaced | Order is replaced (canceled) by the user.
Rejected | Order rejectd by the system.


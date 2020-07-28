# Installation and preparation

**Prerequisites**

* Python 2.7, or Python 3.4 or higher
* pip version 9.0.1 or higher

If necessary, upgrade your version of pip:

```
$ python -m pip install --upgrade pip
```

Install gRPC:

```
$ python -m pip install grpcio
```

To install gRPC tools, run:

```
$ python -m pip install grpcio-tools
```

# Generate a client code

### checkout proto files
Copy proto files into work folder

```
common.proto
isalive.proto
privateService.proto
publicService.proto
```

### generate code from proto files

For each proto file need to generate Python code:

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\common.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\isalive.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\privateService.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\publicService.proto
```

You should have several files with code:

```
common_pb2.py
common_pb2_grpc.py
isalive_pb2.py
isalive_pb2_grpc.py
privateService_pb2.py
privateService_pb2_grpc.py
publicService_pb2.py
publicService_pb2_grpc.py
```

# Call to the server

Now you are ready to work with Lykke Trading API.

### how to check IsAlive for API server

This exampel about how to connect to server and get ap version. 
Please pay attention that you need to use a secure channel with SSL

```python
import grpc

import isalive_pb2
import isalive_pb2_grpc

# use ssl creds
credentials = grpc.ssl_channel_credentials()

#create a channel
channel = grpc.secure_channel("hft-apiv2-grpc.lykke.com:443", credentials)

monitoring = isalive_pb2_grpc.MonitoringStub(channel)

isalive = monitoring.IsAlive(isalive_pb2.IsAliveRequest())

print("API description: " + isalive.name + " " + isalive.version)
```

### How to check account balance

```python
import grpc

import privateService_pb2
import privateService_pb2_grpc

import google.protobuf

# use ssl creds
ssl_credentials = grpc.ssl_channel_credentials()

# use auth creds
token_credentials = grpc.access_token_call_credentials("HFT-ACCOUNT-API-KEY")

# aggregate creds
credentials = grpc.composite_channel_credentials(ssl_credentials, token_credentials)

#create a channel
channel = grpc.secure_channel("hft-apiv2-grpc.lykke.com:443", credentials)

private_api = privateService_pb2_grpc.PrivateServiceStub(channel)

balances = private_api.GetBalances(google.protobuf.empty_pb2.Empty())

print("------------------------------------")
print("Error: " + balances.error.message)
print("------------------------------------")
print("Balances:")
for balance in balances.payload:
    print("  " + balance.assetId + ": " + balance.available)
print("------------------------------------")```













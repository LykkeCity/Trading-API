import grpc
import common_pb2
import common_pb2_grpc
import privateService_pb2
import privateService_pb2_grpc
import publicService_pb2
import publicService_pb2_grpc
import google.protobuf

ssl_credentials = grpc.ssl_channel_credentials()

# use auth creds
token_credentials = grpc.access_token_call_credentials("HFT-ACCOUNT-API-KEY")

# aggregate creds
credentials = grpc.composite_channel_credentials(ssl_credentials, token_credentials)

# create a channel
channel = grpc.secure_channel("hft-apiv2-grpc.lykke.com:443", credentials)

private_api = privateService_pb2_grpc.PrivateServiceStub(channel)
public_api = publicService_pb2_grpc.PublicServiceStub(channel)


def get_balances():
  balances = private_api.GetBalances(google.protobuf.empty_pb2.Empty())

  for balance in balances.payload:
    print(f"{balance.assetId}: {balance.available}")

def place_cancel_order():
  request = privateService_pb2.LimitOrderRequest()
  request.assetPairId = "ETHUSD"
  request.side = 1 #sell
  request.volume = "0.01"
  request.price = "100000"

  response = private_api.PlaceLimitOrder(request)

  print(f"orderId: {response.payload.orderId}")

  cancel_request = privateService_pb2.CancelOrderRequest()
  cancel_request.orderId = response.payload.orderId

  cancel_response = private_api.CancelOrder(cancel_request)

  print(f"Order cancel response: {cancel_response.payload}")

def get_quotes():
  request = publicService_pb2.PriceUpdatesRequest();
  request.assetPairIds.extend(["BTCUSD", "BTCEUR"]) # or [] for all asset pairs

  stream = public_api.GetPriceUpdates(request)

  try:
    for price in stream:
      print(f"{price.assetPairId} bid: {price.bid}, ask: {price.ask}, timestamp: {price.timestamp.ToDatetime()}")
  except KeyboardInterrupt:
    stream.cancel()

def get_trades():
  stream = private_api.GetTradeUpdates(google.protobuf.empty_pb2.Empty())

  try:
    for trade in stream:
      print(str(trade))
  except Exception as e:
    print(str(e))
    stream.cancel()

get_balances()
#place_cancel_order
#get_quotes()
#get_trades()

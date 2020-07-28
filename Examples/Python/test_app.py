import grpc

import isalive_pb2
import isalive_pb2_grpc

import privateService_pb2
import privateService_pb2_grpc

import google.protobuf


ssl_credentials = grpc.ssl_channel_credentials()
token_credentials = grpc.access_token_call_credentials("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IndhbGxldCIsImF1ZCI6ImhmdC1hcGl2Mi5seWtrZS5jb20iLCJrZXktaWQiOiIyZDkyYjMyYi1mZGYzLTRhZjgtYTAzZi1iNzNmYzY2MjJmZDQiLCJjbGllbnQtaWQiOiI3OGVmMzU2Ni03NTgzLTQzMzctYmRkNi0zYTQyYmUyOWVmNTEiLCJ3YWxsZXQtaWQiOiJlMmZiNzNjMS1jZGFhLTQ1YWEtYmNhYi1mMDY1NmE4MGVmZGIiLCJuYmYiOjE1ODk5MjA3NzQsImV4cCI6MTkwNTQ1MzU3NCwiaWF0IjoxNTg5OTIwNzc0fQ.rNa2xghIbDOBB55ERMxrWd4nRuv79nOVA0D8KG8uN2I")
credentials = grpc.composite_channel_credentials(ssl_credentials, token_credentials)

channel = grpc.secure_channel("hft-apiv2-grpc.lykke.com:443", credentials)

monitoring = isalive_pb2_grpc.MonitoringStub(channel)

isalive = monitoring.IsAlive(isalive_pb2.IsAliveRequest())

print("API description: " + isalive.name + " " + isalive.version)

print()

private_api = privateService_pb2_grpc.PrivateServiceStub(channel)

balances = private_api.GetBalances(google.protobuf.empty_pb2.Empty())


print("------------------------------------")
print("Error: " + balances.error.message)
print("------------------------------------")
print("Balances:")
for balance in balances.payload:
    print("  " + balance.assetId + ": " + balance.available)
print("------------------------------------")

# ConnectionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**remote_ip_address** | [**IPAddress**](IPAddress.md) |  | [optional] 
**remote_port** | **int** |  | [optional] 
**local_ip_address** | [**IPAddress**](IPAddress.md) |  | [optional] 
**local_port** | **int** |  | [optional] 
**client_certificate** | [**X509Certificate2**](X509Certificate2.md) |  | [optional] 

## Example

```python
from openapi_client.models.connection_info import ConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionInfo from a JSON string
connection_info_instance = ConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(ConnectionInfo.to_json())

# convert the object into a dict
connection_info_dict = connection_info_instance.to_dict()
# create an instance of ConnectionInfo from a dict
connection_info_from_dict = ConnectionInfo.from_dict(connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



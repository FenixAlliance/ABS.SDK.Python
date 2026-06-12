# WebSocketManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_web_socket_request** | **bool** |  | [optional] [readonly] 
**web_socket_requested_protocols** | **List[str]** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.web_socket_manager import WebSocketManager

# TODO update the JSON string below
json = "{}"
# create an instance of WebSocketManager from a JSON string
web_socket_manager_instance = WebSocketManager.from_json(json)
# print the JSON string representation of the object
print(WebSocketManager.to_json())

# convert the object into a dict
web_socket_manager_dict = web_socket_manager_instance.to_dict()
# create an instance of WebSocketManager from a dict
web_socket_manager_from_dict = WebSocketManager.from_dict(web_socket_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



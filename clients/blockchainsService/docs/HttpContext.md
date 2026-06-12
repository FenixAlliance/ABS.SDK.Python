# HttpContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[TypeObjectKeyValuePair]**](TypeObjectKeyValuePair.md) |  | [optional] [readonly] 
**request** | [**HttpRequest**](HttpRequest.md) |  | [optional] 
**response** | [**HttpResponse**](HttpResponse.md) |  | [optional] 
**connection** | [**ConnectionInfo**](ConnectionInfo.md) |  | [optional] 
**web_sockets** | [**WebSocketManager**](WebSocketManager.md) |  | [optional] 
**user** | [**ClaimsPrincipal**](ClaimsPrincipal.md) |  | [optional] 
**items** | **Dict[str, Optional[object]]** |  | [optional] 
**request_services** | **object** |  | [optional] 
**request_aborted** | [**CancellationToken**](CancellationToken.md) |  | [optional] 
**trace_identifier** | **str** |  | [optional] 
**session** | [**ISession**](ISession.md) |  | [optional] 

## Example

```python
from openapi_client.models.http_context import HttpContext

# TODO update the JSON string below
json = "{}"
# create an instance of HttpContext from a JSON string
http_context_instance = HttpContext.from_json(json)
# print the JSON string representation of the object
print(HttpContext.to_json())

# convert the object into a dict
http_context_dict = http_context_instance.to_dict()
# create an instance of HttpContext from a dict
http_context_from_dict = HttpContext.from_dict(http_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



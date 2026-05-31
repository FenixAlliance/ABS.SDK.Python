# WaitHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **object** |  | [optional] 
**safe_wait_handle** | [**SafeWaitHandle**](SafeWaitHandle.md) |  | [optional] 

## Example

```python
from openapi_client.models.wait_handle import WaitHandle

# TODO update the JSON string below
json = "{}"
# create an instance of WaitHandle from a JSON string
wait_handle_instance = WaitHandle.from_json(json)
# print the JSON string representation of the object
print(WaitHandle.to_json())

# convert the object into a dict
wait_handle_dict = wait_handle_instance.to_dict()
# create an instance of WaitHandle from a dict
wait_handle_from_dict = WaitHandle.from_dict(wait_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



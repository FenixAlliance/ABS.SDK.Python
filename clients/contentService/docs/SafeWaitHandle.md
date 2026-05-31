# SafeWaitHandle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_closed** | **bool** |  | [optional] [readonly] 
**is_invalid** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.safe_wait_handle import SafeWaitHandle

# TODO update the JSON string below
json = "{}"
# create an instance of SafeWaitHandle from a JSON string
safe_wait_handle_instance = SafeWaitHandle.from_json(json)
# print the JSON string representation of the object
print(SafeWaitHandle.to_json())

# convert the object into a dict
safe_wait_handle_dict = safe_wait_handle_instance.to_dict()
# create an instance of SafeWaitHandle from a dict
safe_wait_handle_from_dict = SafeWaitHandle.from_dict(safe_wait_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



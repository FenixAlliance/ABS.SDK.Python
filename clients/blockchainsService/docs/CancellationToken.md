# CancellationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cancellation_requested** | **bool** |  | [optional] [readonly] 
**can_be_canceled** | **bool** |  | [optional] [readonly] 
**wait_handle** | [**WaitHandle**](WaitHandle.md) |  | [optional] 

## Example

```python
from openapi_client.models.cancellation_token import CancellationToken

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationToken from a JSON string
cancellation_token_instance = CancellationToken.from_json(json)
# print the JSON string representation of the object
print(CancellationToken.to_json())

# convert the object into a dict
cancellation_token_dict = cancellation_token_instance.to_dict()
# create an instance of CancellationToken from a dict
cancellation_token_from_dict = CancellationToken.from_dict(cancellation_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



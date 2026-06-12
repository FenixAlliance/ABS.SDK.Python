# EmptyEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.empty_envelope import EmptyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EmptyEnvelope from a JSON string
empty_envelope_instance = EmptyEnvelope.from_json(json)
# print the JSON string representation of the object
print(EmptyEnvelope.to_json())

# convert the object into a dict
empty_envelope_dict = empty_envelope_instance.to_dict()
# create an instance of EmptyEnvelope from a dict
empty_envelope_from_dict = EmptyEnvelope.from_dict(empty_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BooleanEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.boolean_envelope import BooleanEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanEnvelope from a JSON string
boolean_envelope_instance = BooleanEnvelope.from_json(json)
# print the JSON string representation of the object
print(BooleanEnvelope.to_json())

# convert the object into a dict
boolean_envelope_dict = boolean_envelope_instance.to_dict()
# create an instance of BooleanEnvelope from a dict
boolean_envelope_from_dict = BooleanEnvelope.from_dict(boolean_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



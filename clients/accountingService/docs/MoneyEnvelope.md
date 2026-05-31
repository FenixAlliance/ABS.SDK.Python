# MoneyEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.money_envelope import MoneyEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyEnvelope from a JSON string
money_envelope_instance = MoneyEnvelope.from_json(json)
# print the JSON string representation of the object
print(MoneyEnvelope.to_json())

# convert the object into a dict
money_envelope_dict = money_envelope_instance.to_dict()
# create an instance of MoneyEnvelope from a dict
money_envelope_from_dict = MoneyEnvelope.from_dict(money_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



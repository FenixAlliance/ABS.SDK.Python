# PricingRuleDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PricingRuleDto]**](PricingRuleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.pricing_rule_dto_list_envelope import PricingRuleDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRuleDtoListEnvelope from a JSON string
pricing_rule_dto_list_envelope_instance = PricingRuleDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PricingRuleDtoListEnvelope.to_json())

# convert the object into a dict
pricing_rule_dto_list_envelope_dict = pricing_rule_dto_list_envelope_instance.to_dict()
# create an instance of PricingRuleDtoListEnvelope from a dict
pricing_rule_dto_list_envelope_from_dict = PricingRuleDtoListEnvelope.from_dict(pricing_rule_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



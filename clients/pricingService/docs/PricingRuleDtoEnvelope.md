# PricingRuleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PricingRuleDto**](PricingRuleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.pricing_rule_dto_envelope import PricingRuleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRuleDtoEnvelope from a JSON string
pricing_rule_dto_envelope_instance = PricingRuleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PricingRuleDtoEnvelope.to_json())

# convert the object into a dict
pricing_rule_dto_envelope_dict = pricing_rule_dto_envelope_instance.to_dict()
# create an instance of PricingRuleDtoEnvelope from a dict
pricing_rule_dto_envelope_from_dict = PricingRuleDtoEnvelope.from_dict(pricing_rule_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



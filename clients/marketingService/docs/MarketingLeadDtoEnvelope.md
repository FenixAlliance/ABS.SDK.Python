# MarketingLeadDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**MarketingLeadDto**](MarketingLeadDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.marketing_lead_dto_envelope import MarketingLeadDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingLeadDtoEnvelope from a JSON string
marketing_lead_dto_envelope_instance = MarketingLeadDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(MarketingLeadDtoEnvelope.to_json())

# convert the object into a dict
marketing_lead_dto_envelope_dict = marketing_lead_dto_envelope_instance.to_dict()
# create an instance of MarketingLeadDtoEnvelope from a dict
marketing_lead_dto_envelope_from_dict = MarketingLeadDtoEnvelope.from_dict(marketing_lead_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



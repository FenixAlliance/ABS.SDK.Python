# MarketingLeadDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[MarketingLeadDto]**](MarketingLeadDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.marketing_lead_dto_list_envelope import MarketingLeadDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingLeadDtoListEnvelope from a JSON string
marketing_lead_dto_list_envelope_instance = MarketingLeadDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(MarketingLeadDtoListEnvelope.to_json())

# convert the object into a dict
marketing_lead_dto_list_envelope_dict = marketing_lead_dto_list_envelope_instance.to_dict()
# create an instance of MarketingLeadDtoListEnvelope from a dict
marketing_lead_dto_list_envelope_from_dict = MarketingLeadDtoListEnvelope.from_dict(marketing_lead_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



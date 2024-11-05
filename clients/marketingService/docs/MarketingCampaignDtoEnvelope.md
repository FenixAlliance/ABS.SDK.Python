# MarketingCampaignDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**MarketingCampaignDto**](MarketingCampaignDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.marketing_campaign_dto_envelope import MarketingCampaignDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingCampaignDtoEnvelope from a JSON string
marketing_campaign_dto_envelope_instance = MarketingCampaignDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(MarketingCampaignDtoEnvelope.to_json())

# convert the object into a dict
marketing_campaign_dto_envelope_dict = marketing_campaign_dto_envelope_instance.to_dict()
# create an instance of MarketingCampaignDtoEnvelope from a dict
marketing_campaign_dto_envelope_from_dict = MarketingCampaignDtoEnvelope.from_dict(marketing_campaign_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MarketingCampaignUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**offer** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**proposed_start** | **datetime** |  | [optional] 
**proposed_end** | **datetime** |  | [optional] 
**actual_start** | **datetime** |  | [optional] 
**actual_end** | **datetime** |  | [optional] 
**code** | **str** |  | [optional] 
**allocated_budget** | **float** |  | [optional] 
**activity_cost** | **float** |  | [optional] 
**misc_cost** | **float** |  | [optional] 
**expected_response_percent** | **float** |  | [optional] 
**marketing_area_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_campaign_update_dto import MarketingCampaignUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingCampaignUpdateDto from a JSON string
marketing_campaign_update_dto_instance = MarketingCampaignUpdateDto.from_json(json)
# print the JSON string representation of the object
print(MarketingCampaignUpdateDto.to_json())

# convert the object into a dict
marketing_campaign_update_dto_dict = marketing_campaign_update_dto_instance.to_dict()
# create an instance of MarketingCampaignUpdateDto from a dict
marketing_campaign_update_dto_from_dict = MarketingCampaignUpdateDto.from_dict(marketing_campaign_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



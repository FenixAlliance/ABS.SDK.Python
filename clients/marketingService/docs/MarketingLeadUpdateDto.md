# MarketingLeadUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_lead_update_dto import MarketingLeadUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingLeadUpdateDto from a JSON string
marketing_lead_update_dto_instance = MarketingLeadUpdateDto.from_json(json)
# print the JSON string representation of the object
print(MarketingLeadUpdateDto.to_json())

# convert the object into a dict
marketing_lead_update_dto_dict = marketing_lead_update_dto_instance.to_dict()
# create an instance of MarketingLeadUpdateDto from a dict
marketing_lead_update_dto_from_dict = MarketingLeadUpdateDto.from_dict(marketing_lead_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



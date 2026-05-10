# MarketingLeadDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
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
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_lead_dto import MarketingLeadDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingLeadDto from a JSON string
marketing_lead_dto_instance = MarketingLeadDto.from_json(json)
# print the JSON string representation of the object
print(MarketingLeadDto.to_json())

# convert the object into a dict
marketing_lead_dto_dict = marketing_lead_dto_instance.to_dict()
# create an instance of MarketingLeadDto from a dict
marketing_lead_dto_from_dict = MarketingLeadDto.from_dict(marketing_lead_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



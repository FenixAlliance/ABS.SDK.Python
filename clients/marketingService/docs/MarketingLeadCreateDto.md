# MarketingLeadCreateDto


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
**notes** | **str** |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_lead_create_dto import MarketingLeadCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingLeadCreateDto from a JSON string
marketing_lead_create_dto_instance = MarketingLeadCreateDto.from_json(json)
# print the JSON string representation of the object
print(MarketingLeadCreateDto.to_json())

# convert the object into a dict
marketing_lead_create_dto_dict = marketing_lead_create_dto_instance.to_dict()
# create an instance of MarketingLeadCreateDto from a dict
marketing_lead_create_dto_from_dict = MarketingLeadCreateDto.from_dict(marketing_lead_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



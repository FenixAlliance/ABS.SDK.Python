# MarketingListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**locked** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**purpose** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**modified_on** | **datetime** |  | [optional] 
**last_used_on** | **datetime** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**marketing_list_type** | **int** |  | [optional] 
**marketing_list_target** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_list_dto import MarketingListDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingListDto from a JSON string
marketing_list_dto_instance = MarketingListDto.from_json(json)
# print the JSON string representation of the object
print(MarketingListDto.to_json())

# convert the object into a dict
marketing_list_dto_dict = marketing_list_dto_instance.to_dict()
# create an instance of MarketingListDto from a dict
marketing_list_dto_from_dict = MarketingListDto.from_dict(marketing_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



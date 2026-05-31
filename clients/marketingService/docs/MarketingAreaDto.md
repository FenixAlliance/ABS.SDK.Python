# MarketingAreaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_area_dto import MarketingAreaDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingAreaDto from a JSON string
marketing_area_dto_instance = MarketingAreaDto.from_json(json)
# print the JSON string representation of the object
print(MarketingAreaDto.to_json())

# convert the object into a dict
marketing_area_dto_dict = marketing_area_dto_instance.to_dict()
# create an instance of MarketingAreaDto from a dict
marketing_area_dto_from_dict = MarketingAreaDto.from_dict(marketing_area_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



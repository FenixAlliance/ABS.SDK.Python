# MarketingAreaCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_area_create_dto import MarketingAreaCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingAreaCreateDto from a JSON string
marketing_area_create_dto_instance = MarketingAreaCreateDto.from_json(json)
# print the JSON string representation of the object
print(MarketingAreaCreateDto.to_json())

# convert the object into a dict
marketing_area_create_dto_dict = marketing_area_create_dto_instance.to_dict()
# create an instance of MarketingAreaCreateDto from a dict
marketing_area_create_dto_from_dict = MarketingAreaCreateDto.from_dict(marketing_area_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



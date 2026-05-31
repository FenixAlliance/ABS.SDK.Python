# MarketingAreaUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.marketing_area_update_dto import MarketingAreaUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingAreaUpdateDto from a JSON string
marketing_area_update_dto_instance = MarketingAreaUpdateDto.from_json(json)
# print the JSON string representation of the object
print(MarketingAreaUpdateDto.to_json())

# convert the object into a dict
marketing_area_update_dto_dict = marketing_area_update_dto_instance.to_dict()
# create an instance of MarketingAreaUpdateDto from a dict
marketing_area_update_dto_from_dict = MarketingAreaUpdateDto.from_dict(marketing_area_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



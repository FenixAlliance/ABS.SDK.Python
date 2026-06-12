# LocalizationStringDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**base** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**country_language_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.localization_string_dto import LocalizationStringDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationStringDto from a JSON string
localization_string_dto_instance = LocalizationStringDto.from_json(json)
# print the JSON string representation of the object
print(LocalizationStringDto.to_json())

# convert the object into a dict
localization_string_dto_dict = localization_string_dto_instance.to_dict()
# create an instance of LocalizationStringDto from a dict
localization_string_dto_from_dict = LocalizationStringDto.from_dict(localization_string_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



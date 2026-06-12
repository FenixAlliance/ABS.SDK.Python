# LocalizationStringCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**base** | **str** |  | 
**comments** | **str** |  | [optional] 
**country_language_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.localization_string_create_dto import LocalizationStringCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationStringCreateDto from a JSON string
localization_string_create_dto_instance = LocalizationStringCreateDto.from_json(json)
# print the JSON string representation of the object
print(LocalizationStringCreateDto.to_json())

# convert the object into a dict
localization_string_create_dto_dict = localization_string_create_dto_instance.to_dict()
# create an instance of LocalizationStringCreateDto from a dict
localization_string_create_dto_from_dict = LocalizationStringCreateDto.from_dict(localization_string_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



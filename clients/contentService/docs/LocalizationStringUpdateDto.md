# LocalizationStringUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**country_language_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.localization_string_update_dto import LocalizationStringUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationStringUpdateDto from a JSON string
localization_string_update_dto_instance = LocalizationStringUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LocalizationStringUpdateDto.to_json())

# convert the object into a dict
localization_string_update_dto_dict = localization_string_update_dto_instance.to_dict()
# create an instance of LocalizationStringUpdateDto from a dict
localization_string_update_dto_from_dict = LocalizationStringUpdateDto.from_dict(localization_string_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



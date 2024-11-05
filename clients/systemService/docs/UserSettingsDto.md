# UserSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**page_size** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**currency_format** | **str** |  | [optional] 
**date_time_format** | **str** |  | [optional] 
**site_theme** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.user_settings_dto import UserSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsDto from a JSON string
user_settings_dto_instance = UserSettingsDto.from_json(json)
# print the JSON string representation of the object
print(UserSettingsDto.to_json())

# convert the object into a dict
user_settings_dto_dict = user_settings_dto_instance.to_dict()
# create an instance of UserSettingsDto from a dict
user_settings_dto_from_dict = UserSettingsDto.from_dict(user_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



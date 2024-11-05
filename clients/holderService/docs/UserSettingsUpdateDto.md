# UserSettingsUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** |  | [optional] 
**date_format** | **str** |  | 
**currency_format** | **str** |  | 
**date_time_format** | **str** |  | 
**site_theme** | **int** |  | 

## Example

```python
from openapi_client.models.user_settings_update_dto import UserSettingsUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsUpdateDto from a JSON string
user_settings_update_dto_instance = UserSettingsUpdateDto.from_json(json)
# print the JSON string representation of the object
print(UserSettingsUpdateDto.to_json())

# convert the object into a dict
user_settings_update_dto_dict = user_settings_update_dto_instance.to_dict()
# create an instance of UserSettingsUpdateDto from a dict
user_settings_update_dto_from_dict = UserSettingsUpdateDto.from_dict(user_settings_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



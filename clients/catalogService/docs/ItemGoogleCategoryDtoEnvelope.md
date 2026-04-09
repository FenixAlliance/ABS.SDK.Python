# ItemGoogleCategoryDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemGoogleCategoryDto**](ItemGoogleCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_google_category_dto_envelope import ItemGoogleCategoryDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemGoogleCategoryDtoEnvelope from a JSON string
item_google_category_dto_envelope_instance = ItemGoogleCategoryDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemGoogleCategoryDtoEnvelope.to_json())

# convert the object into a dict
item_google_category_dto_envelope_dict = item_google_category_dto_envelope_instance.to_dict()
# create an instance of ItemGoogleCategoryDtoEnvelope from a dict
item_google_category_dto_envelope_from_dict = ItemGoogleCategoryDtoEnvelope.from_dict(item_google_category_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



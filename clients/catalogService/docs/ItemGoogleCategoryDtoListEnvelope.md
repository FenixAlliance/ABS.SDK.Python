# ItemGoogleCategoryDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ItemGoogleCategoryDto]**](ItemGoogleCategoryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_google_category_dto_list_envelope import ItemGoogleCategoryDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemGoogleCategoryDtoListEnvelope from a JSON string
item_google_category_dto_list_envelope_instance = ItemGoogleCategoryDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemGoogleCategoryDtoListEnvelope.to_json())

# convert the object into a dict
item_google_category_dto_list_envelope_dict = item_google_category_dto_list_envelope_instance.to_dict()
# create an instance of ItemGoogleCategoryDtoListEnvelope from a dict
item_google_category_dto_list_envelope_from_dict = ItemGoogleCategoryDtoListEnvelope.from_dict(item_google_category_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



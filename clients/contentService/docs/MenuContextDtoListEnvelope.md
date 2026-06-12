# MenuContextDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[MenuContextDto]**](MenuContextDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.menu_context_dto_list_envelope import MenuContextDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MenuContextDtoListEnvelope from a JSON string
menu_context_dto_list_envelope_instance = MenuContextDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(MenuContextDtoListEnvelope.to_json())

# convert the object into a dict
menu_context_dto_list_envelope_dict = menu_context_dto_list_envelope_instance.to_dict()
# create an instance of MenuContextDtoListEnvelope from a dict
menu_context_dto_list_envelope_from_dict = MenuContextDtoListEnvelope.from_dict(menu_context_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



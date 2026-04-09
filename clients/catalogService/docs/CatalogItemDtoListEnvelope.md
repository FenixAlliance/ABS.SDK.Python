# CatalogItemDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[CatalogItemDto]**](CatalogItemDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_item_dto_list_envelope import CatalogItemDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemDtoListEnvelope from a JSON string
catalog_item_dto_list_envelope_instance = CatalogItemDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(CatalogItemDtoListEnvelope.to_json())

# convert the object into a dict
catalog_item_dto_list_envelope_dict = catalog_item_dto_list_envelope_instance.to_dict()
# create an instance of CatalogItemDtoListEnvelope from a dict
catalog_item_dto_list_envelope_from_dict = CatalogItemDtoListEnvelope.from_dict(catalog_item_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



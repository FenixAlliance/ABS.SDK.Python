# WarehouseDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[WarehouseDto]**](WarehouseDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_dto_list_envelope import WarehouseDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseDtoListEnvelope from a JSON string
warehouse_dto_list_envelope_instance = WarehouseDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(WarehouseDtoListEnvelope.to_json())

# convert the object into a dict
warehouse_dto_list_envelope_dict = warehouse_dto_list_envelope_instance.to_dict()
# create an instance of WarehouseDtoListEnvelope from a dict
warehouse_dto_list_envelope_from_dict = WarehouseDtoListEnvelope.from_dict(warehouse_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



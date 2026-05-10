# WarehouseDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WarehouseDto**](WarehouseDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_dto_envelope import WarehouseDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseDtoEnvelope from a JSON string
warehouse_dto_envelope_instance = WarehouseDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WarehouseDtoEnvelope.to_json())

# convert the object into a dict
warehouse_dto_envelope_dict = warehouse_dto_envelope_instance.to_dict()
# create an instance of WarehouseDtoEnvelope from a dict
warehouse_dto_envelope_from_dict = WarehouseDtoEnvelope.from_dict(warehouse_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



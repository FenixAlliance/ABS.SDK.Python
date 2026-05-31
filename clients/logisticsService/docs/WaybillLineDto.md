# WaybillLineDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**parent_document_type** | **str** |  | [optional] 
**seaway_bill_id** | **str** |  | [optional] 
**airway_bill_id** | **str** |  | [optional] 
**road_waybill_id** | **str** |  | [optional] 
**rail_waybill_id** | **str** |  | [optional] 
**line_number** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**gross_weight_kg** | **float** |  | [optional] 
**volume_m3** | **float** |  | [optional] 
**package_type** | **str** |  | [optional] 
**length_cm** | **float** |  | [optional] 
**width_cm** | **float** |  | [optional] 
**height_cm** | **float** |  | [optional] 
**hs_code** | **str** |  | [optional] 
**marks_and_numbers** | **str** |  | [optional] 
**declared_value** | **float** |  | [optional] 
**declared_value_currency_id** | **str** |  | [optional] 
**seal_number** | **str** |  | [optional] 
**container_number** | **str** |  | [optional] 
**chargeable_weight_kg** | **float** |  | [optional] 
**iata_rate_class** | **str** |  | [optional] 
**dangerous_goods_class** | **str** |  | [optional] 
**un_hazmat_number** | **str** |  | [optional] 
**wagon_number** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.waybill_line_dto import WaybillLineDto

# TODO update the JSON string below
json = "{}"
# create an instance of WaybillLineDto from a JSON string
waybill_line_dto_instance = WaybillLineDto.from_json(json)
# print the JSON string representation of the object
print(WaybillLineDto.to_json())

# convert the object into a dict
waybill_line_dto_dict = waybill_line_dto_instance.to_dict()
# create an instance of WaybillLineDto from a dict
waybill_line_dto_from_dict = WaybillLineDto.from_dict(waybill_line_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PointOfSaleDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[PointOfSaleDto]**](PointOfSaleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.point_of_sale_dto_list_envelope import PointOfSaleDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfSaleDtoListEnvelope from a JSON string
point_of_sale_dto_list_envelope_instance = PointOfSaleDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(PointOfSaleDtoListEnvelope.to_json())

# convert the object into a dict
point_of_sale_dto_list_envelope_dict = point_of_sale_dto_list_envelope_instance.to_dict()
# create an instance of PointOfSaleDtoListEnvelope from a dict
point_of_sale_dto_list_envelope_from_dict = PointOfSaleDtoListEnvelope.from_dict(point_of_sale_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



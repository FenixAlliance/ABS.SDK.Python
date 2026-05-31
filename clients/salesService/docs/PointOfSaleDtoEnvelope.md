# PointOfSaleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PointOfSaleDto**](PointOfSaleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.point_of_sale_dto_envelope import PointOfSaleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfSaleDtoEnvelope from a JSON string
point_of_sale_dto_envelope_instance = PointOfSaleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PointOfSaleDtoEnvelope.to_json())

# convert the object into a dict
point_of_sale_dto_envelope_dict = point_of_sale_dto_envelope_instance.to_dict()
# create an instance of PointOfSaleDtoEnvelope from a dict
point_of_sale_dto_envelope_from_dict = PointOfSaleDtoEnvelope.from_dict(point_of_sale_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



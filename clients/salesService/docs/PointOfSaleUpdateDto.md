# PointOfSaleUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.point_of_sale_update_dto import PointOfSaleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PointOfSaleUpdateDto from a JSON string
point_of_sale_update_dto_instance = PointOfSaleUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PointOfSaleUpdateDto.to_json())

# convert the object into a dict
point_of_sale_update_dto_dict = point_of_sale_update_dto_instance.to_dict()
# create an instance of PointOfSaleUpdateDto from a dict
point_of_sale_update_dto_from_dict = PointOfSaleUpdateDto.from_dict(point_of_sale_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



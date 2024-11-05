# DiscountCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**begin_quantity** | **float** |  | [optional] 
**end_quantity** | **float** |  | [optional] 
**percent** | **float** |  | [optional] 
**value** | **float** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.discount_create_dto import DiscountCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountCreateDto from a JSON string
discount_create_dto_instance = DiscountCreateDto.from_json(json)
# print the JSON string representation of the object
print(DiscountCreateDto.to_json())

# convert the object into a dict
discount_create_dto_dict = discount_create_dto_instance.to_dict()
# create an instance of DiscountCreateDto from a dict
discount_create_dto_from_dict = DiscountCreateDto.from_dict(discount_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



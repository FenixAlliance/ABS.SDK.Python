# DiscountUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.discount_update_dto import DiscountUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountUpdateDto from a JSON string
discount_update_dto_instance = DiscountUpdateDto.from_json(json)
# print the JSON string representation of the object
print(DiscountUpdateDto.to_json())

# convert the object into a dict
discount_update_dto_dict = discount_update_dto_instance.to_dict()
# create an instance of DiscountUpdateDto from a dict
discount_update_dto_from_dict = DiscountUpdateDto.from_dict(discount_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



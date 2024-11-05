# PriceListCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.price_list_create_dto import PriceListCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListCreateDto from a JSON string
price_list_create_dto_instance = PriceListCreateDto.from_json(json)
# print the JSON string representation of the object
print(PriceListCreateDto.to_json())

# convert the object into a dict
price_list_create_dto_dict = price_list_create_dto_instance.to_dict()
# create an instance of PriceListCreateDto from a dict
price_list_create_dto_from_dict = PriceListCreateDto.from_dict(price_list_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PriceListUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.price_list_update_dto import PriceListUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListUpdateDto from a JSON string
price_list_update_dto_instance = PriceListUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PriceListUpdateDto.to_json())

# convert the object into a dict
price_list_update_dto_dict = price_list_update_dto_instance.to_dict()
# create an instance of PriceListUpdateDto from a dict
price_list_update_dto_from_dict = PriceListUpdateDto.from_dict(price_list_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



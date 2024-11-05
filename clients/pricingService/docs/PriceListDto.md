# PriceListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**partner_visible** | **bool** |  | [optional] 
**unit_of_measure_dependant** | **bool** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.price_list_dto import PriceListDto

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListDto from a JSON string
price_list_dto_instance = PriceListDto.from_json(json)
# print the JSON string representation of the object
print(PriceListDto.to_json())

# convert the object into a dict
price_list_dto_dict = price_list_dto_instance.to_dict()
# create an instance of PriceListDto from a dict
price_list_dto_from_dict = PriceListDto.from_dict(price_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



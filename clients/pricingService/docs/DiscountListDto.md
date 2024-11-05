# DiscountListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.discount_list_dto import DiscountListDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountListDto from a JSON string
discount_list_dto_instance = DiscountListDto.from_json(json)
# print the JSON string representation of the object
print(DiscountListDto.to_json())

# convert the object into a dict
discount_list_dto_dict = discount_list_dto_instance.to_dict()
# create an instance of DiscountListDto from a dict
discount_list_dto_from_dict = DiscountListDto.from_dict(discount_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



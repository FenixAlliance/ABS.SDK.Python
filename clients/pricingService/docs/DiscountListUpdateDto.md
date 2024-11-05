# DiscountListUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrolment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.discount_list_update_dto import DiscountListUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountListUpdateDto from a JSON string
discount_list_update_dto_instance = DiscountListUpdateDto.from_json(json)
# print the JSON string representation of the object
print(DiscountListUpdateDto.to_json())

# convert the object into a dict
discount_list_update_dto_dict = discount_list_update_dto_instance.to_dict()
# create an instance of DiscountListUpdateDto from a dict
discount_list_update_dto_from_dict = DiscountListUpdateDto.from_dict(discount_list_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



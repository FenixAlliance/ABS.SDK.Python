# LoanUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_timestamp** | **datetime** |  | [optional] 
**payment_deadline** | **datetime** |  | [optional] 
**value** | **float** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**is_compund_interest_rate** | **bool** |  | [optional] 
**loan_type_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.loan_update_dto import LoanUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoanUpdateDto from a JSON string
loan_update_dto_instance = LoanUpdateDto.from_json(json)
# print the JSON string representation of the object
print(LoanUpdateDto.to_json())

# convert the object into a dict
loan_update_dto_dict = loan_update_dto_instance.to_dict()
# create an instance of LoanUpdateDto from a dict
loan_update_dto_from_dict = LoanUpdateDto.from_dict(loan_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



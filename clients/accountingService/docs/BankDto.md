# BankDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_dto import BankDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankDto from a JSON string
bank_dto_instance = BankDto.from_json(json)
# print the JSON string representation of the object
print(BankDto.to_json())

# convert the object into a dict
bank_dto_dict = bank_dto_instance.to_dict()
# create an instance of BankDto from a dict
bank_dto_from_dict = BankDto.from_dict(bank_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



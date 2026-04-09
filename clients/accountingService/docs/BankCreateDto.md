# BankCreateDto


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
from openapi_client.models.bank_create_dto import BankCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankCreateDto from a JSON string
bank_create_dto_instance = BankCreateDto.from_json(json)
# print the JSON string representation of the object
print(BankCreateDto.to_json())

# convert the object into a dict
bank_create_dto_dict = bank_create_dto_instance.to_dict()
# create an instance of BankCreateDto from a dict
bank_create_dto_from_dict = BankCreateDto.from_dict(bank_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



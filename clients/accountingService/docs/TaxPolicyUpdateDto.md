# TaxPolicyUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_free** | **bool** |  | [optional] 
**reduce** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**allow_international** | **bool** |  | [optional] 
**hours** | **int** |  | [optional] 
**days** | **int** |  | [optional] 
**weeks** | **int** |  | [optional] 
**months** | **int** |  | [optional] 
**years** | **int** |  | [optional] 
**value** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**custom_state** | **str** |  | [optional] 
**custom_city** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**zero** | **bool** |  | [optional] 
**reduced** | **bool** |  | [optional] 
**withholding** | **bool** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tax_policy_update_dto import TaxPolicyUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaxPolicyUpdateDto from a JSON string
tax_policy_update_dto_instance = TaxPolicyUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TaxPolicyUpdateDto.to_json())

# convert the object into a dict
tax_policy_update_dto_dict = tax_policy_update_dto_instance.to_dict()
# create an instance of TaxPolicyUpdateDto from a dict
tax_policy_update_dto_from_dict = TaxPolicyUpdateDto.from_dict(tax_policy_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PaymentTermCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**credit_days** | **float** |  | [optional] 
**credit_weeks** | **float** |  | [optional] 
**credit_months** | **float** |  | [optional] 
**credit_years** | **float** |  | [optional] 
**payment_mode_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_term_create_dto import PaymentTermCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTermCreateDto from a JSON string
payment_term_create_dto_instance = PaymentTermCreateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTermCreateDto.to_json())

# convert the object into a dict
payment_term_create_dto_dict = payment_term_create_dto_instance.to_dict()
# create an instance of PaymentTermCreateDto from a dict
payment_term_create_dto_from_dict = PaymentTermCreateDto.from_dict(payment_term_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



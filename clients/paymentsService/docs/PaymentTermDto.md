# PaymentTermDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
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
from openapi_client.models.payment_term_dto import PaymentTermDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTermDto from a JSON string
payment_term_dto_instance = PaymentTermDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTermDto.to_json())

# convert the object into a dict
payment_term_dto_dict = payment_term_dto_instance.to_dict()
# create an instance of PaymentTermDto from a dict
payment_term_dto_from_dict = PaymentTermDto.from_dict(payment_term_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



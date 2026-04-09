# PaymentTermUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**credit_days** | **float** |  | [optional] 
**credit_weeks** | **float** |  | [optional] 
**credit_months** | **float** |  | [optional] 
**credit_years** | **float** |  | [optional] 
**payment_mode_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_term_update_dto import PaymentTermUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTermUpdateDto from a JSON string
payment_term_update_dto_instance = PaymentTermUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentTermUpdateDto.to_json())

# convert the object into a dict
payment_term_update_dto_dict = payment_term_update_dto_instance.to_dict()
# create an instance of PaymentTermUpdateDto from a dict
payment_term_update_dto_from_dict = PaymentTermUpdateDto.from_dict(payment_term_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



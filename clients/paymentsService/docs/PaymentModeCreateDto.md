# PaymentModeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_mode_create_dto import PaymentModeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentModeCreateDto from a JSON string
payment_mode_create_dto_instance = PaymentModeCreateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentModeCreateDto.to_json())

# convert the object into a dict
payment_mode_create_dto_dict = payment_mode_create_dto_instance.to_dict()
# create an instance of PaymentModeCreateDto from a dict
payment_mode_create_dto_from_dict = PaymentModeCreateDto.from_dict(payment_mode_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



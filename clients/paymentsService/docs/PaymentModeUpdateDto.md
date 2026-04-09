# PaymentModeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_mode_update_dto import PaymentModeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentModeUpdateDto from a JSON string
payment_mode_update_dto_instance = PaymentModeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(PaymentModeUpdateDto.to_json())

# convert the object into a dict
payment_mode_update_dto_dict = payment_mode_update_dto_instance.to_dict()
# create an instance of PaymentModeUpdateDto from a dict
payment_mode_update_dto_from_dict = PaymentModeUpdateDto.from_dict(payment_mode_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



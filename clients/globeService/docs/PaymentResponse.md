# PaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | **bool** |  | [optional] 
**ip** | **str** |  | [optional] 
**bank** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**errors** | **object** |  | [optional] 
**response** | **str** |  | [optional] 
**auth_code** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**franchise** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**payment_status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.payment_response import PaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponse from a JSON string
payment_response_instance = PaymentResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentResponse.to_json())

# convert the object into a dict
payment_response_dict = payment_response_instance.to_dict()
# create an instance of PaymentResponse from a dict
payment_response_from_dict = PaymentResponse.from_dict(payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



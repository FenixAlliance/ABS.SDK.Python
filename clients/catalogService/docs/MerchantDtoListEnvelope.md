# MerchantDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[MerchantDto]**](MerchantDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_dto_list_envelope import MerchantDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantDtoListEnvelope from a JSON string
merchant_dto_list_envelope_instance = MerchantDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(MerchantDtoListEnvelope.to_json())

# convert the object into a dict
merchant_dto_list_envelope_dict = merchant_dto_list_envelope_instance.to_dict()
# create an instance of MerchantDtoListEnvelope from a dict
merchant_dto_list_envelope_from_dict = MerchantDtoListEnvelope.from_dict(merchant_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



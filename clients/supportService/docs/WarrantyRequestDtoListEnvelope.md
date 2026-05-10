# WarrantyRequestDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[WarrantyRequestDto]**](WarrantyRequestDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.warranty_request_dto_list_envelope import WarrantyRequestDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WarrantyRequestDtoListEnvelope from a JSON string
warranty_request_dto_list_envelope_instance = WarrantyRequestDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(WarrantyRequestDtoListEnvelope.to_json())

# convert the object into a dict
warranty_request_dto_list_envelope_dict = warranty_request_dto_list_envelope_instance.to_dict()
# create an instance of WarrantyRequestDtoListEnvelope from a dict
warranty_request_dto_list_envelope_from_dict = WarrantyRequestDtoListEnvelope.from_dict(warranty_request_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



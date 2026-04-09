# ShareClassDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ShareClassDto]**](ShareClassDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.share_class_dto_list_envelope import ShareClassDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassDtoListEnvelope from a JSON string
share_class_dto_list_envelope_instance = ShareClassDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ShareClassDtoListEnvelope.to_json())

# convert the object into a dict
share_class_dto_list_envelope_dict = share_class_dto_list_envelope_instance.to_dict()
# create an instance of ShareClassDtoListEnvelope from a dict
share_class_dto_list_envelope_from_dict = ShareClassDtoListEnvelope.from_dict(share_class_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



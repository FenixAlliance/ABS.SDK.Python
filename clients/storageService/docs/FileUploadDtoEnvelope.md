# FileUploadDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**FileUploadDto**](FileUploadDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.file_upload_dto_envelope import FileUploadDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadDtoEnvelope from a JSON string
file_upload_dto_envelope_instance = FileUploadDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(FileUploadDtoEnvelope.to_json())

# convert the object into a dict
file_upload_dto_envelope_dict = file_upload_dto_envelope_instance.to_dict()
# create an instance of FileUploadDtoEnvelope from a dict
file_upload_dto_envelope_from_dict = FileUploadDtoEnvelope.from_dict(file_upload_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



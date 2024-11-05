# BlobEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**Blob**](Blob.md) |  | [optional] 

## Example

```python
from openapi_client.models.blob_envelope import BlobEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BlobEnvelope from a JSON string
blob_envelope_instance = BlobEnvelope.from_json(json)
# print the JSON string representation of the object
print(BlobEnvelope.to_json())

# convert the object into a dict
blob_envelope_dict = blob_envelope_instance.to_dict()
# create an instance of BlobEnvelope from a dict
blob_envelope_from_dict = BlobEnvelope.from_dict(blob_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



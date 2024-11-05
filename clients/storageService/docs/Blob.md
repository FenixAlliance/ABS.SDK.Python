# Blob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **int** |  | [optional] 
**is_folder** | **bool** |  | [optional] [readonly] 
**is_file** | **bool** |  | [optional] [readonly] 
**folder_path** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**size** | **int** |  | [optional] 
**md5** | **str** |  | [optional] 
**created_time** | **datetime** |  | [optional] 
**last_modification_time** | **datetime** |  | [optional] 
**full_path** | **str** |  | [optional] 
**properties** | **Dict[str, Optional[object]]** |  | [optional] [readonly] 
**metadata** | **Dict[str, Optional[str]]** |  | [optional] [readonly] 
**is_root_folder** | **bool** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.blob import Blob

# TODO update the JSON string below
json = "{}"
# create an instance of Blob from a JSON string
blob_instance = Blob.from_json(json)
# print the JSON string representation of the object
print(Blob.to_json())

# convert the object into a dict
blob_dict = blob_instance.to_dict()
# create an instance of Blob from a dict
blob_from_dict = Blob.from_dict(blob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



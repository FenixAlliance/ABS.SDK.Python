# DownloadablesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask_file_names** | **bool** |  | [optional] 
**grant_access_after_payment** | **bool** |  | [optional] 
**downloads_require_login** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.downloadables_options import DownloadablesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadablesOptions from a JSON string
downloadables_options_instance = DownloadablesOptions.from_json(json)
# print the JSON string representation of the object
print(DownloadablesOptions.to_json())

# convert the object into a dict
downloadables_options_dict = downloadables_options_instance.to_dict()
# create an instance of DownloadablesOptions from a dict
downloadables_options_from_dict = DownloadablesOptions.from_dict(downloadables_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



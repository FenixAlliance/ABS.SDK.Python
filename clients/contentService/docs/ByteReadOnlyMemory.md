# ByteReadOnlyMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** |  | [optional] [readonly] 
**is_empty** | **bool** |  | [optional] [readonly] 
**span** | [**ByteReadOnlySpan**](ByteReadOnlySpan.md) |  | [optional] 

## Example

```python
from openapi_client.models.byte_read_only_memory import ByteReadOnlyMemory

# TODO update the JSON string below
json = "{}"
# create an instance of ByteReadOnlyMemory from a JSON string
byte_read_only_memory_instance = ByteReadOnlyMemory.from_json(json)
# print the JSON string representation of the object
print(ByteReadOnlyMemory.to_json())

# convert the object into a dict
byte_read_only_memory_dict = byte_read_only_memory_instance.to_dict()
# create an instance of ByteReadOnlyMemory from a dict
byte_read_only_memory_from_dict = ByteReadOnlyMemory.from_dict(byte_read_only_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



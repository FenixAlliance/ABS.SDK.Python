# PipeWriter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_get_unflushed_bytes** | **bool** |  | [optional] [readonly] 
**unflushed_bytes** | **int** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.pipe_writer import PipeWriter

# TODO update the JSON string below
json = "{}"
# create an instance of PipeWriter from a JSON string
pipe_writer_instance = PipeWriter.from_json(json)
# print the JSON string representation of the object
print(PipeWriter.to_json())

# convert the object into a dict
pipe_writer_dict = pipe_writer_instance.to_dict()
# create an instance of PipeWriter from a dict
pipe_writer_from_dict = PipeWriter.from_dict(pipe_writer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



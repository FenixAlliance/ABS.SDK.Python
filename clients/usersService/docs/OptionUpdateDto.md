# OptionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**frozen** | **bool** |  | [optional] 
**autoload** | **bool** |  | [optional] 
**transient** | **bool** |  | [optional] 
**expiration** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.option_update_dto import OptionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OptionUpdateDto from a JSON string
option_update_dto_instance = OptionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(OptionUpdateDto.to_json())

# convert the object into a dict
option_update_dto_dict = option_update_dto_instance.to_dict()
# create an instance of OptionUpdateDto from a dict
option_update_dto_from_dict = OptionUpdateDto.from_dict(option_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



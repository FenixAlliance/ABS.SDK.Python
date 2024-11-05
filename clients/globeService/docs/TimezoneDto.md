# TimezoneDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] [readonly] 
**utc_offset** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.timezone_dto import TimezoneDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDto from a JSON string
timezone_dto_instance = TimezoneDto.from_json(json)
# print the JSON string representation of the object
print(TimezoneDto.to_json())

# convert the object into a dict
timezone_dto_dict = timezone_dto_instance.to_dict()
# create an instance of TimezoneDto from a dict
timezone_dto_from_dict = TimezoneDto.from_dict(timezone_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



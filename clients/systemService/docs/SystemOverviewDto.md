# SystemOverviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptime** | **str** |  | [optional] 
**os_description** | **str** |  | [optional] 
**machine_name** | **str** |  | [optional] 
**process_name** | **str** |  | [optional] 
**product_version** | **str** |  | [optional] 
**private_memory_mb** | **int** |  | [optional] 
**paged_memory_mb** | **int** |  | [optional] 
**memory_working_set_mb** | **int** |  | [optional] 
**is_debug_mode** | **bool** |  | [optional] 
**is_dev_mode** | **bool** |  | [optional] 
**framework_description** | **str** |  | [optional] 
**runtime_identifier** | **str** |  | [optional] 
**os_architecture** | **str** |  | [optional] 
**os_platform** | **str** |  | [optional] 
**process_architecture** | **str** |  | [optional] 
**users_count** | **int** |  | [optional] 
**orders_count** | **int** |  | [optional] 
**contacts_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.system_overview_dto import SystemOverviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of SystemOverviewDto from a JSON string
system_overview_dto_instance = SystemOverviewDto.from_json(json)
# print the JSON string representation of the object
print(SystemOverviewDto.to_json())

# convert the object into a dict
system_overview_dto_dict = system_overview_dto_instance.to_dict()
# create an instance of SystemOverviewDto from a dict
system_overview_dto_from_dict = SystemOverviewDto.from_dict(system_overview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



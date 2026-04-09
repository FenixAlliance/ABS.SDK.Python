# ServiceCaseUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**taxable** | **bool** |  | [optional] 
**work_location** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_queue_id** | **str** |  | [optional] 
**service_case_type_id** | **str** |  | [optional] 
**service_level_agreement_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**receiver_business_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**territory_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**promised_start_date** | **datetime** |  | [optional] 
**promised_end_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.service_case_update_dto import ServiceCaseUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCaseUpdateDto from a JSON string
service_case_update_dto_instance = ServiceCaseUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ServiceCaseUpdateDto.to_json())

# convert the object into a dict
service_case_update_dto_dict = service_case_update_dto_instance.to_dict()
# create an instance of ServiceCaseUpdateDto from a dict
service_case_update_dto_from_dict = ServiceCaseUpdateDto.from_dict(service_case_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



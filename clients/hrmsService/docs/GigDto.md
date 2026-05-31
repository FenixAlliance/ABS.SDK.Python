# GigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**remote** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expected_delivery_date** | **datetime** |  | [optional] 
**min_budget** | **float** |  | [optional] 
**max_budget** | **float** |  | [optional] 
**location** | **str** |  | [optional] 
**views_count** | **int** |  | [optional] 
**data** | **str** |  | [optional] 
**data_label** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data1_label** | **str** |  | [optional] 
**data2** | **str** |  | [optional] 
**data2_label** | **str** |  | [optional] 
**data3** | **str** |  | [optional] 
**data3_label** | **str** |  | [optional] 
**data4** | **str** |  | [optional] 
**data4_label** | **str** |  | [optional] 
**data5** | **str** |  | [optional] 
**data5_label** | **str** |  | [optional] 
**data6** | **str** |  | [optional] 
**data6_label** | **str** |  | [optional] 
**data7** | **str** |  | [optional] 
**data7_label** | **str** |  | [optional] 
**data8** | **str** |  | [optional] 
**data8_label** | **str** |  | [optional] 
**data9** | **str** |  | [optional] 
**data9_label** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**employer_profile_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gig_dto import GigDto

# TODO update the JSON string below
json = "{}"
# create an instance of GigDto from a JSON string
gig_dto_instance = GigDto.from_json(json)
# print the JSON string representation of the object
print(GigDto.to_json())

# convert the object into a dict
gig_dto_dict = gig_dto_instance.to_dict()
# create an instance of GigDto from a dict
gig_dto_from_dict = GigDto.from_dict(gig_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



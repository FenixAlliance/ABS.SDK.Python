# JobOfferCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**remote** | **bool** |  | [optional] 
**expected_hire_date** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**technical_skills** | **str** |  | [optional] 
**non_technical_skills** | **str** |  | [optional] 
**certifications** | **str** |  | [optional] 
**project_experience** | **str** |  | [optional] 
**technologies** | **str** |  | [optional] 
**benefits** | **str** |  | [optional] 
**is_official_job_offer** | **bool** |  | [optional] 
**is_remote_job_offer** | **bool** |  | [optional] 
**is_mid_time_job_offer** | **bool** |  | [optional] 
**is_undergraduate_option** | **bool** |  | [optional] 
**min_overall_experience_years** | **int** |  | [optional] 
**availiable_positions_count** | **int** |  | [optional] 
**min_salary_amount** | **float** |  | [optional] 
**max_salary_amount** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**job_field_id** | **str** |  | [optional] 
**employer_profile_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**country_state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
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

## Example

```python
from openapi_client.models.job_offer_create_dto import JobOfferCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of JobOfferCreateDto from a JSON string
job_offer_create_dto_instance = JobOfferCreateDto.from_json(json)
# print the JSON string representation of the object
print(JobOfferCreateDto.to_json())

# convert the object into a dict
job_offer_create_dto_dict = job_offer_create_dto_instance.to_dict()
# create an instance of JobOfferCreateDto from a dict
job_offer_create_dto_from_dict = JobOfferCreateDto.from_dict(job_offer_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



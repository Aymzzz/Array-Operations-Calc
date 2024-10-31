# swagger_client.ArrayOpsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**max_array**](ArrayOpsApi.md#max_array) | **GET** /arrayops/findMax | 
[**min_array**](ArrayOpsApi.md#min_array) | **GET** /arrayops/findMin | 
[**multiply_arrays**](ArrayOpsApi.md#multiply_arrays) | **GET** /arrayops/multiplyArrays | 
[**sort_array**](ArrayOpsApi.md#sort_array) | **GET** /arrayops/sortArray | 
[**sum_arrays**](ArrayOpsApi.md#sum_arrays) | **GET** /arrayops/addArrays | 

# **max_array**
> int max_array(array_in)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi()
array_in = [56] # list[int] | 

try:
    api_response = api_instance.max_array(array_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->max_array: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_in** | [**list[int]**](int.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **min_array**
> int min_array(array_in)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi()
array_in = [56] # list[int] | 

try:
    api_response = api_instance.min_array(array_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->min_array: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_in** | [**list[int]**](int.md)|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multiply_arrays**
> list[int] multiply_arrays(array_in1, array_in2)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi()
array_in1 = [56] # list[int] | 
array_in2 = [56] # list[int] | 

try:
    api_response = api_instance.multiply_arrays(array_in1, array_in2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->multiply_arrays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_in1** | [**list[int]**](int.md)|  | 
 **array_in2** | [**list[int]**](int.md)|  | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sort_array**
> list[int] sort_array(array_in)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi()
array_in = [56] # list[int] | 

try:
    api_response = api_instance.sort_array(array_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->sort_array: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_in** | [**list[int]**](int.md)|  | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sum_arrays**
> list[int] sum_arrays(array_in1, array_in2)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi()
array_in1 = [56] # list[int] | 
array_in2 = [56] # list[int] | 

try:
    api_response = api_instance.sum_arrays(array_in1, array_in2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->sum_arrays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_in1** | [**list[int]**](int.md)|  | 
 **array_in2** | [**list[int]**](int.md)|  | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi(swagger_client.ApiClient(configuration))
array_in = [56] # list[int] | 

try:
    api_response = api_instance.max_array(array_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->max_array: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi(swagger_client.ApiClient(configuration))
array_in = [56] # list[int] | 

try:
    api_response = api_instance.min_array(array_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->min_array: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi(swagger_client.ApiClient(configuration))
array_in1 = [56] # list[int] | 
array_in2 = [56] # list[int] | 

try:
    api_response = api_instance.multiply_arrays(array_in1, array_in2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->multiply_arrays: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi(swagger_client.ApiClient(configuration))
array_in = [56] # list[int] | 

try:
    api_response = api_instance.sort_array(array_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->sort_array: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ArrayOpsApi(swagger_client.ApiClient(configuration))
array_in1 = [56] # list[int] | 
array_in2 = [56] # list[int] | 

try:
    api_response = api_instance.sum_arrays(array_in1, array_in2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrayOpsApi->sum_arrays: %s\n" % e)
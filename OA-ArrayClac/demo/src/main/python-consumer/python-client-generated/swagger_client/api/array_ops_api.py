# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ArrayOpsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def max_array(self, array_in, **kwargs):  # noqa: E501
        """max_array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.max_array(array_in, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.max_array_with_http_info(array_in, **kwargs)  # noqa: E501
        else:
            (data) = self.max_array_with_http_info(array_in, **kwargs)  # noqa: E501
            return data

    def max_array_with_http_info(self, array_in, **kwargs):  # noqa: E501
        """max_array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.max_array_with_http_info(array_in, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['array_in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method max_array" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'array_in' is set
        if ('array_in' not in params or
                params['array_in'] is None):
            raise ValueError("Missing the required parameter `array_in` when calling `max_array`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'array_in' in params:
            query_params.append(('arrayIn', params['array_in']))  # noqa: E501
            collection_formats['arrayIn'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/arrayops/findMax', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def min_array(self, array_in, **kwargs):  # noqa: E501
        """min_array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.min_array(array_in, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.min_array_with_http_info(array_in, **kwargs)  # noqa: E501
        else:
            (data) = self.min_array_with_http_info(array_in, **kwargs)  # noqa: E501
            return data

    def min_array_with_http_info(self, array_in, **kwargs):  # noqa: E501
        """min_array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.min_array_with_http_info(array_in, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in: (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['array_in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method min_array" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'array_in' is set
        if ('array_in' not in params or
                params['array_in'] is None):
            raise ValueError("Missing the required parameter `array_in` when calling `min_array`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'array_in' in params:
            query_params.append(('arrayIn', params['array_in']))  # noqa: E501
            collection_formats['arrayIn'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/arrayops/findMin', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def multiply_arrays(self, array_in1, array_in2, **kwargs):  # noqa: E501
        """multiply_arrays  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multiply_arrays(array_in1, array_in2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in1: (required)
        :param list[int] array_in2: (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.multiply_arrays_with_http_info(array_in1, array_in2, **kwargs)  # noqa: E501
        else:
            (data) = self.multiply_arrays_with_http_info(array_in1, array_in2, **kwargs)  # noqa: E501
            return data

    def multiply_arrays_with_http_info(self, array_in1, array_in2, **kwargs):  # noqa: E501
        """multiply_arrays  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.multiply_arrays_with_http_info(array_in1, array_in2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in1: (required)
        :param list[int] array_in2: (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['array_in1', 'array_in2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method multiply_arrays" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'array_in1' is set
        if ('array_in1' not in params or
                params['array_in1'] is None):
            raise ValueError("Missing the required parameter `array_in1` when calling `multiply_arrays`")  # noqa: E501
        # verify the required parameter 'array_in2' is set
        if ('array_in2' not in params or
                params['array_in2'] is None):
            raise ValueError("Missing the required parameter `array_in2` when calling `multiply_arrays`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'array_in1' in params:
            query_params.append(('arrayIn1', params['array_in1']))  # noqa: E501
            collection_formats['arrayIn1'] = 'multi'  # noqa: E501
        if 'array_in2' in params:
            query_params.append(('arrayIn2', params['array_in2']))  # noqa: E501
            collection_formats['arrayIn2'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/arrayops/multiplyArrays', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sort_array(self, array_in, **kwargs):  # noqa: E501
        """sort_array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sort_array(array_in, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in: (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sort_array_with_http_info(array_in, **kwargs)  # noqa: E501
        else:
            (data) = self.sort_array_with_http_info(array_in, **kwargs)  # noqa: E501
            return data

    def sort_array_with_http_info(self, array_in, **kwargs):  # noqa: E501
        """sort_array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sort_array_with_http_info(array_in, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in: (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['array_in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sort_array" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'array_in' is set
        if ('array_in' not in params or
                params['array_in'] is None):
            raise ValueError("Missing the required parameter `array_in` when calling `sort_array`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'array_in' in params:
            query_params.append(('arrayIn', params['array_in']))  # noqa: E501
            collection_formats['arrayIn'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/arrayops/sortArray', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sum_arrays(self, array_in1, array_in2, **kwargs):  # noqa: E501
        """sum_arrays  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sum_arrays(array_in1, array_in2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in1: (required)
        :param list[int] array_in2: (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sum_arrays_with_http_info(array_in1, array_in2, **kwargs)  # noqa: E501
        else:
            (data) = self.sum_arrays_with_http_info(array_in1, array_in2, **kwargs)  # noqa: E501
            return data

    def sum_arrays_with_http_info(self, array_in1, array_in2, **kwargs):  # noqa: E501
        """sum_arrays  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sum_arrays_with_http_info(array_in1, array_in2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] array_in1: (required)
        :param list[int] array_in2: (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['array_in1', 'array_in2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sum_arrays" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'array_in1' is set
        if ('array_in1' not in params or
                params['array_in1'] is None):
            raise ValueError("Missing the required parameter `array_in1` when calling `sum_arrays`")  # noqa: E501
        # verify the required parameter 'array_in2' is set
        if ('array_in2' not in params or
                params['array_in2'] is None):
            raise ValueError("Missing the required parameter `array_in2` when calling `sum_arrays`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'array_in1' in params:
            query_params.append(('arrayIn1', params['array_in1']))  # noqa: E501
            collection_formats['arrayIn1'] = 'multi'  # noqa: E501
        if 'array_in2' in params:
            query_params.append(('arrayIn2', params['array_in2']))  # noqa: E501
            collection_formats['arrayIn2'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/arrayops/addArrays', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

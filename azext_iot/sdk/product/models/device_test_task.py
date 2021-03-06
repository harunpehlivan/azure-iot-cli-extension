# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeviceTestTask(Model):
    """It represents an async operation associated with a
    Microsoft.Azure.IoT.TestKit.Models.DeviceTest.

    :param id: Id of a Microsoft.Azure.IoT.TestKit.Models.DeviceTestTask.
    :type id: str
    :param status: Task status a
     Microsoft.Azure.IoT.TestKit.Models.DeviceTestTask. Possible values
     include: 'Queued', 'Started', 'Running', 'Completed', 'Failed',
     'Cancelled'
    :type status: str or ~product.models.enum
    :param type: Task type. Possible values include: 'QueueTestRun',
     'GenerateTestCases'
    :type type: str or ~product.models.enum
    :param device_test_id: Id of Microsoft.Azure.IoT.TestKit.Models.DeviceTest
    :type device_test_id: str
    :param result_link: Task result link(relative url).
    :type result_link: str
    :param error:
    :type error: object
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'device_test_id': {'key': 'deviceTestId', 'type': 'str'},
        'result_link': {'key': 'resultLink', 'type': 'str'},
        'error': {'key': 'error', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(DeviceTestTask, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.status = kwargs.get('status', None)
        self.type = kwargs.get('type', None)
        self.device_test_id = kwargs.get('device_test_id', None)
        self.result_link = kwargs.get('result_link', None)
        self.error = kwargs.get('error', None)

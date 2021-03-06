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


class Reported(Model):
    """Reported.

    :param value: The current interface property value in a digitalTwin.
    :type value: object
    :param desired_state:
    :type desired_state: ~service.models.DesiredState
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
        'desired_state': {'key': 'desiredState', 'type': 'DesiredState'},
    }

    def __init__(self, **kwargs):
        super(Reported, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.desired_state = kwargs.get('desired_state', None)

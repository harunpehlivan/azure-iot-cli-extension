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


class TpmAttestation(Model):
    """Attestation via TPM.

    All required parameters must be populated in order to send to Azure.

    :param endorsement_key: Required.
    :type endorsement_key: str
    :param storage_root_key:
    :type storage_root_key: str
    """

    _validation = {
        'endorsement_key': {'required': True},
    }

    _attribute_map = {
        'endorsement_key': {'key': 'endorsementKey', 'type': 'str'},
        'storage_root_key': {'key': 'storageRootKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TpmAttestation, self).__init__(**kwargs)
        self.endorsement_key = kwargs.get('endorsement_key', None)
        self.storage_root_key = kwargs.get('storage_root_key', None)

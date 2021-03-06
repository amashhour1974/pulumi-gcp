# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class DefaultObjectACL(pulumi.CustomResource):
    bucket: pulumi.Output[str]
    """
    The name of the bucket it applies to.
    """
    role_entities: pulumi.Output[list]
    """
    List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
    """
    def __init__(__self__, __name__, __opts__=None, bucket=None, role_entities=None):
        """
        Creates a new default object ACL in Google Cloud Storage service (GCS). For more information see
        
        -> Note that for each object, its creator will have the `"OWNER"` role in addition
        to the default ACL that has been defined.
        
        For more information see
        [the official documentation](https://cloud.google.com/storage/docs/access-control/lists) 
        and 
        [API](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls).
        
        -> Want fine-grained control over default object ACLs? Use `google_storage_default_object_access_control`
        to control individual role entity pairs.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket it applies to.
        :param pulumi.Input[list] role_entities: List of role/entity pairs in the form `ROLE:entity`. See [GCS Object ACL documentation](https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls) for more details.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not bucket:
            raise TypeError('Missing required property bucket')
        __props__['bucket'] = bucket

        __props__['role_entities'] = role_entities

        super(DefaultObjectACL, __self__).__init__(
            'gcp:storage/defaultObjectACL:DefaultObjectACL',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


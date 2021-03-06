# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AccountIamMember(pulumi.CustomResource):
    billing_account_id: pulumi.Output[str]
    """
    The billing account id.
    """
    etag: pulumi.Output[str]
    """
    (Computed) The etag of the billing account's IAM policy.
    """
    member: pulumi.Output[str]
    """
    The user that the role should apply to.
    """
    role: pulumi.Output[str]
    """
    The role that should be applied.
    """
    def __init__(__self__, __name__, __opts__=None, billing_account_id=None, member=None, role=None):
        """
        Allows creation and management of a single member for a single binding within
        the IAM policy for an existing Google Cloud Platform Billing Account.
        
        > **Note:** This resource __must not__ be used in conjunction with
           `google_billing_account_iam_binding` for the __same role__ or they will fight over
           what your policy should be.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] billing_account_id: The billing account id.
        :param pulumi.Input[str] member: The user that the role should apply to.
        :param pulumi.Input[str] role: The role that should be applied.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not billing_account_id:
            raise TypeError('Missing required property billing_account_id')
        __props__['billing_account_id'] = billing_account_id

        if not member:
            raise TypeError('Missing required property member')
        __props__['member'] = member

        if not role:
            raise TypeError('Missing required property role')
        __props__['role'] = role

        __props__['etag'] = None

        super(AccountIamMember, __self__).__init__(
            'gcp:billing/accountIamMember:AccountIamMember',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


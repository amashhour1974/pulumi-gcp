# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class TopicIAMMember(pulumi.CustomResource):
    etag: pulumi.Output[str]
    """
    (Computed) The etag of the topic's IAM policy.
    """
    member: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    role: pulumi.Output[str]
    """
    The role that should be applied. Only one
    `google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
    `[projects|organizations]/{parent-name}/roles/{role-name}`.
    """
    topic: pulumi.Output[str]
    """
    The topic name or id to bind to attach IAM policy to.
    """
    def __init__(__self__, __name__, __opts__=None, member=None, project=None, role=None, topic=None):
        """
        Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:
        
        * `google_pubsub_topic_iam_policy`: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.
        * `google_pubsub_topic_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.
        * `google_pubsub_topic_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.
        
        > **Note:** `google_pubsub_topic_iam_policy` **cannot** be used in conjunction with `google_pubsub_topic_iam_binding` and `google_pubsub_topic_iam_member` or they will fight over what your policy should be.
        
        > **Note:** `google_pubsub_topic_iam_binding` resources **can be** used in conjunction with `google_pubsub_topic_iam_member` resources **only if** they do not grant privilege to the same role.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] member
        :param pulumi.Input[str] project: The project in which the resource belongs. If it
               is not provided, the provider project is used.
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        :param pulumi.Input[str] topic: The topic name or id to bind to attach IAM policy to.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not member:
            raise TypeError('Missing required property member')
        __props__['member'] = member

        __props__['project'] = project

        if not role:
            raise TypeError('Missing required property role')
        __props__['role'] = role

        if not topic:
            raise TypeError('Missing required property topic')
        __props__['topic'] = topic

        __props__['etag'] = None

        super(TopicIAMMember, __self__).__init__(
            'gcp:pubsub/topicIAMMember:TopicIAMMember',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


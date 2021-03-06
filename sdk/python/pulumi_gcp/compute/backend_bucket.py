# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class BackendBucket(pulumi.CustomResource):
    bucket_name: pulumi.Output[str]
    creation_timestamp: pulumi.Output[str]
    description: pulumi.Output[str]
    enable_cdn: pulumi.Output[bool]
    name: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    def __init__(__self__, __name__, __opts__=None, bucket_name=None, description=None, enable_cdn=None, name=None, project=None):
        """
        Backend buckets allow you to use Google Cloud Storage buckets with HTTP(S)
        load balancing.
        
        An HTTP(S) load balancer can direct traffic to specified URLs to a
        backend bucket rather than a backend service. It can send requests for
        static content to a Cloud Storage bucket and requests for dynamic content
        a virtual machine instance.
        
        
        To get more information about BackendBucket, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/latest/backendBuckets)
        * How-to Guides
            * [Using a Cloud Storage bucket as a load balancer backend](https://cloud.google.com/compute/docs/load-balancing/http/backend-bucket)
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=backend_bucket_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
            <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
          </a>
        </div>
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] bucket_name
        :param pulumi.Input[str] description
        :param pulumi.Input[bool] enable_cdn
        :param pulumi.Input[str] name
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not bucket_name:
            raise TypeError('Missing required property bucket_name')
        __props__['bucket_name'] = bucket_name

        __props__['description'] = description

        __props__['enable_cdn'] = enable_cdn

        __props__['name'] = name

        __props__['project'] = project

        __props__['creation_timestamp'] = None
        __props__['self_link'] = None

        super(BackendBucket, __self__).__init__(
            'gcp:compute/backendBucket:BackendBucket',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Environment(pulumi.CustomResource):
    config: pulumi.Output[dict]
    labels: pulumi.Output[dict]
    name: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    region: pulumi.Output[str]
    def __init__(__self__, __name__, __opts__=None, config=None, labels=None, name=None, project=None, region=None):
        """
        An environment for running orchestration tasks.
        
        Environments run Apache Airflow software on Google infrastructure.
        
        To get more information about Environments, see:
        
        * [API documentation](https://cloud.google.com/composer/docs/reference/rest/)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/composer/docs)
            * [Configuring Shared VPC for Composer Environments](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc)
        * [Apache Airflow Documentation](http://airflow.apache.org/)
        
        > **Warning:** We **STRONGLY** recommend  you read the [GCP guides](https://cloud.google.com/composer/docs/how-to)
          as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure, 
          including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
          Terraform will not be able to automatically find or manage many of these underlying resources. In particular:
          * It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some 
            errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
            error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid 
            against GCP Cloud Composer before filing bugs against the Terraform provider. 
          * **Environments create Google Cloud Storage buckets that do not get cleaned up automatically** on environment 
            deletion. [More about Composer's use of Cloud Storage](https://cloud.google.com/composer/docs/concepts/cloud-storage).
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[dict] config
        :param pulumi.Input[dict] labels
        :param pulumi.Input[str] name
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] region
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['config'] = config

        __props__['labels'] = labels

        __props__['name'] = name

        __props__['project'] = project

        __props__['region'] = region

        super(Environment, __self__).__init__(
            'gcp:composer/environment:Environment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


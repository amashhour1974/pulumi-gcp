# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class HttpHealthCheck(pulumi.CustomResource):
    check_interval_sec: pulumi.Output[int]
    creation_timestamp: pulumi.Output[str]
    description: pulumi.Output[str]
    healthy_threshold: pulumi.Output[int]
    host: pulumi.Output[str]
    name: pulumi.Output[str]
    port: pulumi.Output[int]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    request_path: pulumi.Output[str]
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    timeout_sec: pulumi.Output[int]
    unhealthy_threshold: pulumi.Output[int]
    def __init__(__self__, __name__, __opts__=None, check_interval_sec=None, description=None, healthy_threshold=None, host=None, name=None, port=None, project=None, request_path=None, timeout_sec=None, unhealthy_threshold=None):
        """
        An HttpHealthCheck resource. This resource defines a template for how
        individual VMs should be checked for health, via HTTP.
        
        
        > **Note:** google_compute_http_health_check is a legacy health check.
        The newer [google_compute_health_check](https://www.terraform.io/docs/providers/google/r/compute_health_check.html)
        should be preferred for all uses except
        [Network Load Balancers](https://cloud.google.com/compute/docs/load-balancing/network/)
        which still require the legacy version.
        
        
        To get more information about HttpHealthCheck, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/latest/httpHealthChecks)
        * How-to Guides
            * [Adding Health Checks](https://cloud.google.com/compute/docs/load-balancing/health-checks#legacy_health_checks)
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=http_health_check_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
            <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
          </a>
        </div>
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[int] check_interval_sec
        :param pulumi.Input[str] description
        :param pulumi.Input[int] healthy_threshold
        :param pulumi.Input[str] host
        :param pulumi.Input[str] name
        :param pulumi.Input[int] port
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[str] request_path
        :param pulumi.Input[int] timeout_sec
        :param pulumi.Input[int] unhealthy_threshold
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['check_interval_sec'] = check_interval_sec

        __props__['description'] = description

        __props__['healthy_threshold'] = healthy_threshold

        __props__['host'] = host

        __props__['name'] = name

        __props__['port'] = port

        __props__['project'] = project

        __props__['request_path'] = request_path

        __props__['timeout_sec'] = timeout_sec

        __props__['unhealthy_threshold'] = unhealthy_threshold

        __props__['creation_timestamp'] = None
        __props__['self_link'] = None

        super(HttpHealthCheck, __self__).__init__(
            'gcp:compute/httpHealthCheck:HttpHealthCheck',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


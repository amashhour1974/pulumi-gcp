# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RouterInterface(pulumi.CustomResource):
    ip_range: pulumi.Output[str]
    """
    IP address and range of the interface. The IP range must be
    in the RFC3927 link-local IP space. Changing this forces a new interface to be created.
    """
    name: pulumi.Output[str]
    """
    A unique name for the interface, required by GCE. Changing
    this forces a new interface to be created.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which this interface's router belongs. If it
    is not provided, the provider project is used. Changing this forces a new interface to be created.
    """
    region: pulumi.Output[str]
    """
    The region this interface's router sits in. If not specified,
    the project region will be used. Changing this forces a new interface to be
    created.
    """
    router: pulumi.Output[str]
    """
    The name of the router this interface will be attached to.
    Changing this forces a new interface to be created.
    """
    vpn_tunnel: pulumi.Output[str]
    """
    The name or resource link to the VPN tunnel this
    interface will be linked to. Changing this forces a new interface to be created.
    """
    def __init__(__self__, __name__, __opts__=None, ip_range=None, name=None, project=None, region=None, router=None, vpn_tunnel=None):
        """
        Manages a Cloud Router interface. For more information see
        [the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
        and
        [API](https://cloud.google.com/compute/docs/reference/latest/routers).
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] ip_range: IP address and range of the interface. The IP range must be
               in the RFC3927 link-local IP space. Changing this forces a new interface to be created.
        :param pulumi.Input[str] name: A unique name for the interface, required by GCE. Changing
               this forces a new interface to be created.
        :param pulumi.Input[str] project: The ID of the project in which this interface's router belongs. If it
               is not provided, the provider project is used. Changing this forces a new interface to be created.
        :param pulumi.Input[str] region: The region this interface's router sits in. If not specified,
               the project region will be used. Changing this forces a new interface to be
               created.
        :param pulumi.Input[str] router: The name of the router this interface will be attached to.
               Changing this forces a new interface to be created.
        :param pulumi.Input[str] vpn_tunnel: The name or resource link to the VPN tunnel this
               interface will be linked to. Changing this forces a new interface to be created.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['ip_range'] = ip_range

        __props__['name'] = name

        __props__['project'] = project

        __props__['region'] = region

        if not router:
            raise TypeError('Missing required property router')
        __props__['router'] = router

        if not vpn_tunnel:
            raise TypeError('Missing required property vpn_tunnel')
        __props__['vpn_tunnel'] = vpn_tunnel

        super(RouterInterface, __self__).__init__(
            'gcp:compute/routerInterface:RouterInterface',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


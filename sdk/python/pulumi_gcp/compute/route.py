# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Route(pulumi.CustomResource):
    description: pulumi.Output[str]
    dest_range: pulumi.Output[str]
    name: pulumi.Output[str]
    network: pulumi.Output[str]
    next_hop_gateway: pulumi.Output[str]
    next_hop_instance: pulumi.Output[str]
    next_hop_instance_zone: pulumi.Output[str]
    """
    (Optional when `next_hop_instance` is
    specified)  The zone of the instance specified in
    `next_hop_instance`.  Omit if `next_hop_instance` is specified as
    a URL.
    """
    next_hop_ip: pulumi.Output[str]
    next_hop_network: pulumi.Output[str]
    next_hop_vpn_tunnel: pulumi.Output[str]
    priority: pulumi.Output[int]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    tags: pulumi.Output[list]
    def __init__(__self__, __name__, __opts__=None, description=None, dest_range=None, name=None, network=None, next_hop_gateway=None, next_hop_instance=None, next_hop_instance_zone=None, next_hop_ip=None, next_hop_vpn_tunnel=None, priority=None, project=None, tags=None):
        """
        Represents a Route resource.
        
        A route is a rule that specifies how certain packets should be handled by
        the virtual network. Routes are associated with virtual machines by tag,
        and the set of routes for a particular virtual machine is called its
        routing table. For each packet leaving a virtual machine, the system
        searches that virtual machine's routing table for a single best matching
        route.
        
        Routes match packets by destination IP address, preferring smaller or more
        specific ranges over larger ones. If there is a tie, the system selects
        the route with the smallest priority value. If there is still a tie, it
        uses the layer three and four packet headers to select just one of the
        remaining matching routes. The packet is then forwarded as specified by
        the next_hop field of the winning route -- either to another virtual
        machine destination, a virtual machine gateway or a Compute
        Engine-operated gateway. Packets that do not match any route in the
        sending virtual machine's routing table will be dropped.
        
        A Route resource must have exactly one specification of either
        nextHopGateway, nextHopInstance, nextHopIp, or nextHopVpnTunnel.
        
        
        To get more information about Route, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/routes)
        * How-to Guides
            * [Using Routes](https://cloud.google.com/vpc/docs/using-routes)
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=route_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
            <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
          </a>
        </div>
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] description
        :param pulumi.Input[str] dest_range
        :param pulumi.Input[str] name
        :param pulumi.Input[str] network
        :param pulumi.Input[str] next_hop_gateway
        :param pulumi.Input[str] next_hop_instance
        :param pulumi.Input[str] next_hop_instance_zone: (Optional when `next_hop_instance` is
               specified)  The zone of the instance specified in
               `next_hop_instance`.  Omit if `next_hop_instance` is specified as
               a URL.
        :param pulumi.Input[str] next_hop_ip
        :param pulumi.Input[str] next_hop_vpn_tunnel
        :param pulumi.Input[int] priority
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] tags
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        if not dest_range:
            raise TypeError('Missing required property dest_range')
        __props__['dest_range'] = dest_range

        __props__['name'] = name

        if not network:
            raise TypeError('Missing required property network')
        __props__['network'] = network

        __props__['next_hop_gateway'] = next_hop_gateway

        __props__['next_hop_instance'] = next_hop_instance

        __props__['next_hop_instance_zone'] = next_hop_instance_zone

        __props__['next_hop_ip'] = next_hop_ip

        __props__['next_hop_vpn_tunnel'] = next_hop_vpn_tunnel

        __props__['priority'] = priority

        __props__['project'] = project

        __props__['tags'] = tags

        __props__['next_hop_network'] = None
        __props__['self_link'] = None

        super(Route, __self__).__init__(
            'gcp:compute/route:Route',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


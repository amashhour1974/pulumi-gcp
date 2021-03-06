// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Represents a VPN gateway running in GCP. This virtual device is managed
 * by Google, but used only by you.
 * 
 * 
 * To get more information about VpnGateway, see:
 * 
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways)
 * 
 * <div class = "oics-button" style="float: right; margin: 0 0 -15px">
 *   <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=target_vpn_gateway_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
 *     <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
 *   </a>
 * </div>
 * ## Example Usage - Target Vpn Gateway Basic
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const google_compute_address_vpn_static_ip = new gcp.compute.Address("vpn_static_ip", {
 *     name: "vpn-static-ip",
 * });
 * const google_compute_network_network1 = new gcp.compute.Network("network1", {
 *     name: "network1",
 * });
 * const google_compute_vpn_gateway_target_gateway = new gcp.compute.VPNGateway("target_gateway", {
 *     name: "vpn1",
 *     network: google_compute_network_network1.selfLink,
 * });
 * const google_compute_forwarding_rule_fr_esp = new gcp.compute.ForwardingRule("fr_esp", {
 *     ipAddress: google_compute_address_vpn_static_ip.address,
 *     ipProtocol: "ESP",
 *     name: "fr-esp",
 *     target: google_compute_vpn_gateway_target_gateway.selfLink,
 * });
 * const google_compute_forwarding_rule_fr_udp4500 = new gcp.compute.ForwardingRule("fr_udp4500", {
 *     ipAddress: google_compute_address_vpn_static_ip.address,
 *     ipProtocol: "UDP",
 *     name: "fr-udp4500",
 *     portRange: "4500",
 *     target: google_compute_vpn_gateway_target_gateway.selfLink,
 * });
 * const google_compute_forwarding_rule_fr_udp500 = new gcp.compute.ForwardingRule("fr_udp500", {
 *     ipAddress: google_compute_address_vpn_static_ip.address,
 *     ipProtocol: "UDP",
 *     name: "fr-udp500",
 *     portRange: "500",
 *     target: google_compute_vpn_gateway_target_gateway.selfLink,
 * });
 * const google_compute_vpn_tunnel_tunnel1 = new gcp.compute.VPNTunnel("tunnel1", {
 *     name: "tunnel1",
 *     peerIp: "15.0.0.120",
 *     sharedSecret: "a secret message",
 *     targetVpnGateway: google_compute_vpn_gateway_target_gateway.selfLink,
 * }, {dependsOn: [google_compute_forwarding_rule_fr_esp, google_compute_forwarding_rule_fr_udp4500, google_compute_forwarding_rule_fr_udp500]});
 * const google_compute_route_route1 = new gcp.compute.Route("route1", {
 *     destRange: "15.0.0.0/24",
 *     name: "route1",
 *     network: google_compute_network_network1.name,
 *     nextHopVpnTunnel: google_compute_vpn_tunnel_tunnel1.selfLink,
 *     priority: 1000,
 * });
 * ```
 */
export class VPNGateway extends pulumi.CustomResource {
    /**
     * Get an existing VPNGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VPNGatewayState, opts?: pulumi.CustomResourceOptions): VPNGateway {
        return new VPNGateway(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly creationTimestamp: pulumi.Output<string>;
    public readonly description: pulumi.Output<string | undefined>;
    public readonly name: pulumi.Output<string>;
    public readonly network: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project: pulumi.Output<string>;
    public readonly region: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink: pulumi.Output<string>;

    /**
     * Create a VPNGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VPNGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VPNGatewayArgs | VPNGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VPNGatewayState = argsOrState as VPNGatewayState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["network"] = state ? state.network : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
        } else {
            const args = argsOrState as VPNGatewayArgs | undefined;
            if (!args || args.network === undefined) {
                throw new Error("Missing required property 'network'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["network"] = args ? args.network : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
        }
        super("gcp:compute/vPNGateway:VPNGateway", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VPNGateway resources.
 */
export interface VPNGatewayState {
    readonly creationTimestamp?: pulumi.Input<string>;
    readonly description?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly network?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VPNGateway resource.
 */
export interface VPNGatewayArgs {
    readonly description?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly network: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
}

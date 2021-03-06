// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * VPN tunnel resource.
 * 
 * 
 * To get more information about VpnTunnel, see:
 * 
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels)
 * * How-to Guides
 *     * [Cloud VPN Overview](https://cloud.google.com/vpn/docs/concepts/overview)
 *     * [Networks and Tunnel Routing](https://cloud.google.com/vpn/docs/concepts/choosing-networks-routing)
 * 
 * > **Warning:** All arguments including the shared secret will be stored in the raw
 * state as plain-text.
 * [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 * 
 * <div class = "oics-button" style="float: right; margin: 0 0 -15px">
 *   <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=vpn_tunnel_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
 *     <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
 *   </a>
 * </div>
 * ## Example Usage - Vpn Tunnel Basic
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
export class VPNTunnel extends pulumi.CustomResource {
    /**
     * Get an existing VPNTunnel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VPNTunnelState, opts?: pulumi.CustomResourceOptions): VPNTunnel {
        return new VPNTunnel(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly creationTimestamp: pulumi.Output<string>;
    public readonly description: pulumi.Output<string | undefined>;
    public /*out*/ readonly detailedStatus: pulumi.Output<string>;
    public readonly ikeVersion: pulumi.Output<number | undefined>;
    public /*out*/ readonly labelFingerprint: pulumi.Output<string>;
    public readonly labels: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly localTrafficSelectors: pulumi.Output<string[]>;
    public readonly name: pulumi.Output<string>;
    public readonly peerIp: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project: pulumi.Output<string>;
    public readonly region: pulumi.Output<string>;
    public readonly remoteTrafficSelectors: pulumi.Output<string[]>;
    public readonly router: pulumi.Output<string | undefined>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink: pulumi.Output<string>;
    public readonly sharedSecret: pulumi.Output<string>;
    public /*out*/ readonly sharedSecretHash: pulumi.Output<string>;
    public readonly targetVpnGateway: pulumi.Output<string>;

    /**
     * Create a VPNTunnel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VPNTunnelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VPNTunnelArgs | VPNTunnelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VPNTunnelState = argsOrState as VPNTunnelState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["detailedStatus"] = state ? state.detailedStatus : undefined;
            inputs["ikeVersion"] = state ? state.ikeVersion : undefined;
            inputs["labelFingerprint"] = state ? state.labelFingerprint : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["localTrafficSelectors"] = state ? state.localTrafficSelectors : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["peerIp"] = state ? state.peerIp : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["remoteTrafficSelectors"] = state ? state.remoteTrafficSelectors : undefined;
            inputs["router"] = state ? state.router : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["sharedSecret"] = state ? state.sharedSecret : undefined;
            inputs["sharedSecretHash"] = state ? state.sharedSecretHash : undefined;
            inputs["targetVpnGateway"] = state ? state.targetVpnGateway : undefined;
        } else {
            const args = argsOrState as VPNTunnelArgs | undefined;
            if (!args || args.peerIp === undefined) {
                throw new Error("Missing required property 'peerIp'");
            }
            if (!args || args.sharedSecret === undefined) {
                throw new Error("Missing required property 'sharedSecret'");
            }
            if (!args || args.targetVpnGateway === undefined) {
                throw new Error("Missing required property 'targetVpnGateway'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["ikeVersion"] = args ? args.ikeVersion : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["localTrafficSelectors"] = args ? args.localTrafficSelectors : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["peerIp"] = args ? args.peerIp : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["remoteTrafficSelectors"] = args ? args.remoteTrafficSelectors : undefined;
            inputs["router"] = args ? args.router : undefined;
            inputs["sharedSecret"] = args ? args.sharedSecret : undefined;
            inputs["targetVpnGateway"] = args ? args.targetVpnGateway : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["detailedStatus"] = undefined /*out*/;
            inputs["labelFingerprint"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
            inputs["sharedSecretHash"] = undefined /*out*/;
        }
        super("gcp:compute/vPNTunnel:VPNTunnel", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VPNTunnel resources.
 */
export interface VPNTunnelState {
    readonly creationTimestamp?: pulumi.Input<string>;
    readonly description?: pulumi.Input<string>;
    readonly detailedStatus?: pulumi.Input<string>;
    readonly ikeVersion?: pulumi.Input<number>;
    readonly labelFingerprint?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    readonly localTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
    readonly name?: pulumi.Input<string>;
    readonly peerIp?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly remoteTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
    readonly router?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    readonly sharedSecret?: pulumi.Input<string>;
    readonly sharedSecretHash?: pulumi.Input<string>;
    readonly targetVpnGateway?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VPNTunnel resource.
 */
export interface VPNTunnelArgs {
    readonly description?: pulumi.Input<string>;
    readonly ikeVersion?: pulumi.Input<number>;
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    readonly localTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
    readonly name?: pulumi.Input<string>;
    readonly peerIp: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly remoteTrafficSelectors?: pulumi.Input<pulumi.Input<string>[]>;
    readonly router?: pulumi.Input<string>;
    readonly sharedSecret: pulumi.Input<string>;
    readonly targetVpnGateway: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to retrieve default service account for this project
func LookupDefaultServiceAccount(ctx *pulumi.Context, args *GetDefaultServiceAccountArgs) error {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["email"] = args.Email
		inputs["project"] = args.Project
	}
	_, err := ctx.Invoke("gcp:compute/getDefaultServiceAccount:getDefaultServiceAccount", inputs)
	return err
}

// A collection of arguments for invoking getDefaultServiceAccount.
type GetDefaultServiceAccountArgs struct {
	Email interface{}
	// The project ID. If it is not provided, the provider project is used.
	Project interface{}
}
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storage

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The DefaultObjectAccessControls resources represent the Access Control
// Lists (ACLs) applied to a new object within a Google Cloud Storage bucket
// when no ACL was provided for that object. ACLs let you specify who has
// access to your bucket contents and to what extent.
// 
// There are two roles that can be assigned to an entity:
// 
// READERs can get an object, though the acl property will not be revealed.
// OWNERs are READERs, and they can get the acl property, update an object,
// and call all objectAccessControls methods on the object. The owner of an
// object is always an OWNER.
// For more information, see Access Control, with the caveat that this API
// uses READER and OWNER instead of READ and FULL_CONTROL.
// 
// 
// To get more information about DefaultObjectAccessControl, see:
// 
// * [API documentation](https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/storage/docs/access-control/create-manage-lists)
// 
// <div class = "oics-button" style="float: right; margin: 0 0 -15px">
//   <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=storage_default_object_access_control_public&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
//     <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
//   </a>
// </div>
type DefaultObjectAccessControl struct {
	s *pulumi.ResourceState
}

// NewDefaultObjectAccessControl registers a new resource with the given unique name, arguments, and options.
func NewDefaultObjectAccessControl(ctx *pulumi.Context,
	name string, args *DefaultObjectAccessControlArgs, opts ...pulumi.ResourceOpt) (*DefaultObjectAccessControl, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.Entity == nil {
		return nil, errors.New("missing required argument 'Entity'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["bucket"] = nil
		inputs["entity"] = nil
		inputs["object"] = nil
		inputs["role"] = nil
	} else {
		inputs["bucket"] = args.Bucket
		inputs["entity"] = args.Entity
		inputs["object"] = args.Object
		inputs["role"] = args.Role
	}
	inputs["domain"] = nil
	inputs["email"] = nil
	inputs["entityId"] = nil
	inputs["generation"] = nil
	inputs["projectTeam"] = nil
	s, err := ctx.RegisterResource("gcp:storage/defaultObjectAccessControl:DefaultObjectAccessControl", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DefaultObjectAccessControl{s: s}, nil
}

// GetDefaultObjectAccessControl gets an existing DefaultObjectAccessControl resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDefaultObjectAccessControl(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DefaultObjectAccessControlState, opts ...pulumi.ResourceOpt) (*DefaultObjectAccessControl, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["bucket"] = state.Bucket
		inputs["domain"] = state.Domain
		inputs["email"] = state.Email
		inputs["entity"] = state.Entity
		inputs["entityId"] = state.EntityId
		inputs["generation"] = state.Generation
		inputs["object"] = state.Object
		inputs["projectTeam"] = state.ProjectTeam
		inputs["role"] = state.Role
	}
	s, err := ctx.ReadResource("gcp:storage/defaultObjectAccessControl:DefaultObjectAccessControl", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DefaultObjectAccessControl{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DefaultObjectAccessControl) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DefaultObjectAccessControl) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *DefaultObjectAccessControl) Bucket() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bucket"])
}

func (r *DefaultObjectAccessControl) Domain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domain"])
}

func (r *DefaultObjectAccessControl) Email() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["email"])
}

func (r *DefaultObjectAccessControl) Entity() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["entity"])
}

func (r *DefaultObjectAccessControl) EntityId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["entityId"])
}

func (r *DefaultObjectAccessControl) Generation() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["generation"])
}

func (r *DefaultObjectAccessControl) Object() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["object"])
}

func (r *DefaultObjectAccessControl) ProjectTeam() *pulumi.Output {
	return r.s.State["projectTeam"]
}

func (r *DefaultObjectAccessControl) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// Input properties used for looking up and filtering DefaultObjectAccessControl resources.
type DefaultObjectAccessControlState struct {
	Bucket interface{}
	Domain interface{}
	Email interface{}
	Entity interface{}
	EntityId interface{}
	Generation interface{}
	Object interface{}
	ProjectTeam interface{}
	Role interface{}
}

// The set of arguments for constructing a DefaultObjectAccessControl resource.
type DefaultObjectAccessControlArgs struct {
	Bucket interface{}
	Entity interface{}
	Object interface{}
	Role interface{}
}

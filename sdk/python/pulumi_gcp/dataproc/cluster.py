# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Cluster(pulumi.CustomResource):
    """
    Manages a Cloud Dataproc cluster resource within GCP. For more information see
    [the official dataproc documentation](https://cloud.google.com/dataproc/).
    
    
    !> **Warning:** Due to limitations of the API, all arguments except
    `labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updateable. Changing others will cause recreation of the
    whole cluster!
    """
    def __init__(__self__, __name__, __opts__=None, cluster_config=None, labels=None, name=None, project=None, region=None):
        """Create a Cluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if cluster_config and not isinstance(cluster_config, dict):
            raise TypeError('Expected property cluster_config to be a dict')
        __self__.cluster_config = cluster_config
        """
        Allows you to configure various aspects of the cluster.
        Structure defined below.
        """
        __props__['clusterConfig'] = cluster_config

        if labels and not isinstance(labels, dict):
            raise TypeError('Expected property labels to be a dict')
        __self__.labels = labels
        """
        The list of labels (key/value pairs) to be applied to
        instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
        which is the name of the cluster.
        """
        __props__['labels'] = labels

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the cluster, unique within the project and
        zone.
        """
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the `cluster` will exist. If it
        is not provided, the provider project is used.
        """
        __props__['project'] = project

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which the cluster and associated nodes will be created in.
        Defaults to `global`.
        """
        __props__['region'] = region

        super(Cluster, __self__).__init__(
            'gcp:dataproc/cluster:Cluster',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'clusterConfig' in outs:
            self.cluster_config = outs['clusterConfig']
        if 'labels' in outs:
            self.labels = outs['labels']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'region' in outs:
            self.region = outs['region']
from aws_cdk import core, aws_ec2, aws_iam, aws_eks


class CdkPyconEksStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # import default VPC
        #vpc = aws_ec2.Vpc.from_lookup(self, 'VPC', is_default=True)
        vpc = aws_ec2.Vpc(self, 'EKS-CDK-VPC', cidr='10.0.0.0/16', nat_gateways=1)

        # create an admin role
        eks_admin_role = aws_iam.Role(self, 'AdminRole',
                                      assumed_by=aws_iam.AccountPrincipal(
                                          account_id=self.account)
                                      )
        # create the cluster
        cluster = aws_eks.Cluster(self, 'cluster',
                                  masters_role=eks_admin_role,
                                  vpc=vpc,
                                  default_capacity=0,
                                  version='1.14',
                                  output_cluster_name=True
                                  )

        cluster.add_capacity('ondemand', instance_type=aws_ec2.InstanceType('t3.large'),
                             max_capacity=1,
                             bootstrap_options=aws_eks.BootstrapOptions(
                                 kubelet_extra_args='--node-labels myCustomLabel=od'
        )
        )

        cluster.add_capacity('spot', instance_type=aws_ec2.InstanceType('t3.large'),
                             max_capacity=1,
                             spot_price='0.1094',
                             bootstrap_options=aws_eks.BootstrapOptions(
                                 kubelet_extra_args='--node-labels myCustomLabel=spot'
        )
        )

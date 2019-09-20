from aws_cdk import core, aws_ec2, aws_ecs, aws_ecs_patterns


class CdkPyconFlaskStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # import default VPC
        #vpc = aws_ec2.Vpc.from_lookup(self, 'VPC', is_default=True)
        vpc = aws_ec2.Vpc(self, 'FargateFlaskVPC', cidr='10.0.0.0/16')

        # ECS cluster
        cluster = aws_ecs.Cluster(self, 'Cluster', vpc=vpc)
        svc = aws_ecs_patterns.ApplicationLoadBalancedFargateService(
            self, 'FargateService',
            cluster=cluster,
            image=aws_ecs.ContainerImage.from_asset('flask-docker-app'),
            container_port=5000,
            environment={
                'PLATFORM': 'AWS Fargate :-)'
            }
        )

        core.CfnOutput(self, 'SericeURL', value="http://{}".format(
            svc.load_balancer.load_balancer_dns_name))

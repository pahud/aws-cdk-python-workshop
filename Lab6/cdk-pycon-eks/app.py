#!/usr/bin/env python3

import os
from aws_cdk import core
from aws_cdk.core import Stack, Construct, Environment
from cdk_pycon_eks.cdk_pycon_eks_stack import CdkPyconEksStack


app = core.App()

ACCOUNT = app.node.try_get_context('account') or os.environ.get(
    'CDK_DEFAULT_ACCOUNT', 'unknown')
REGION = app.node.try_get_context('region') or os.environ.get(
    'CDK_DEFAULT_REGION', 'unknown')

AWS_ENV = Environment(region=REGION, account=ACCOUNT)

CdkPyconEksStack(app, "cdk-pycon-eks", env=AWS_ENV)

app.synth()

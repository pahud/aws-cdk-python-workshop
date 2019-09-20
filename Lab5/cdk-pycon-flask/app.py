#!/usr/bin/env python3

from aws_cdk import core

from cdk_pycon_flask.cdk_pycon_flask_stack import CdkPyconFlaskStack


app = core.App()
CdkPyconFlaskStack(app, "cdk-pycon-flask")

app.synth()

# Build and publish your AWS Lambda Layer to SAR(Serverless App Repository)

This sample walks you though building your **AWS CLI lambda layer** which has been published at [https://github.com/aws-samples/aws-lambda-layer-awscli](https://github.com/aws-samples/aws-lambda-layer-awscli).



# check out the repository

```bash
$ git clone https://github.com/aws-samples/aws-lambda-layer-awscli.git
$ cd aws-lambda-layer-awscli/
```



# create your S3 staging bucket

```bash
# Let's create a staging bucket in Tokyo region
$ aws --region ap-northeast-1 s3 mb 3://pahud-tmp-ap-northeast-1
```



# update Makefile

```bash
S3BUCKET ?= pahud-tmp-ap-northeast-1
LAMBDA_REGION ?= ap-northeast-1
```



# build, package and deploy your lambda layer

```bash
# build the layer from scratch 
$ make layer-build 

# package and deploy the layer with `SAM` CLI 
$ make sam-layer-package sam-layer-deploy 

# [OPTIONAL] destroy the layer 
$ make sam-layer-destroy
```



# publish your lambda layer

1. Update your package metadata in [sam-layer.yaml](https://github.com/aws-samples/aws-lambda-layer-awscli/blob/9cb12209fc174a3ec27f2e40a3292859c9ddb405/sam-layer.yaml#L3-L14)



2. publish to SAR 

```bash
$ make publish-new-version-to-sar
```

Your SAR will be published to `us-east-1` and  propagate to other regions.


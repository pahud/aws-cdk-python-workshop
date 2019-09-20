# Generate your customize buttons for SAR

In this Lab, we will walks you though building your custom SAR buttons like this:

|       Region       |                       Click and Deploy                       |
| :----------------: | :----------------------------------------------------------: |
| **ap-northeast-1** | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-northeast-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
| **ap-northeast-2** | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-northeast-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
| **ap-northeast-3** | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-northeast-3/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **ap-south-1**   | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-south-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
| **ap-southeast-1** | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-southeast-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
| **ap-southeast-2** | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-southeast-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|  **ca-central-1**  | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ca-central-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|  **eu-central-1**  | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-central-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **eu-north-1**   | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-north-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **eu-west-1**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-west-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **eu-west-2**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-west-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **eu-west-3**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-west-3/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **sa-east-1**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/sa-east-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **us-east-1**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-east-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **us-east-2**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-east-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **us-west-1**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-west-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |
|   **us-west-2**    | [![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-west-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli) |



# Prepare your SAR Application ARN

Get your SAR Application ARN from SAR console. Your ApplicationId should be in this format

```
arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli
```

Generaet now

```bash
# generate the icons with ge-sar-deploy-icons.sh
# Usage: bash gen-sar-deploy-icons.sh SAR_APP_ARN
$ bash gen-sar-deploy-icons.sh arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli

ap-northeast-1 ap-northeast-2 ap-northeast-3 ap-south-1 ap-southeast-1 ap-southeast-2 ca-central-1 eu-central-1 eu-north-1 eu-west-1 eu-west-2 eu-west-3 sa-east-1 us-east-1 us-east-2 us-west-1 us-west-2
|        Region        |                    Click and Deploy                     |
| :----------------: | :----------------------------------------------------------: |
|  **ap-northeast-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-northeast-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **ap-northeast-2**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-northeast-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **ap-northeast-3**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-northeast-3/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **ap-south-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-south-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **ap-southeast-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-southeast-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **ap-southeast-2**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ap-southeast-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **ca-central-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/ca-central-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **eu-central-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-central-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **eu-north-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-north-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **eu-west-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-west-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **eu-west-2**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-west-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **eu-west-3**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/eu-west-3/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **sa-east-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/sa-east-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **us-east-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-east-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **us-east-2**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-east-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **us-west-1**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-west-1/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
|  **us-west-2**  |[![](https://img.shields.io/badge/SAR-Deploy%20Now-yellow.svg)](https://deploy.serverlessrepo.app/us-west-2/?app=arn:aws:serverlessrepo:us-east-1:903779448426:applications/lambda-layer-awscli)|
```


Your SAR buttons in markdown format will be generated. 




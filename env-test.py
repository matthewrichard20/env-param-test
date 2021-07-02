import os
import sys
import json
import boto3
from dotenv import load_dotenv
env_path = '.env'
load_dotenv(dotenv_path=env_path)
# environment = os.getenv("ENV")
assume_role = os.getenv("ASSUME_ROLE")
export_role = os.getenv("EXPORT_ROLE")
kms_key = os.getenv("KMS_KEY")
# print(environment)
print(assume_role)
print(export_role)
print(kms_key)
# -*- coding: utf-8 -*-
from __future__ import print_function
import os, sys
import oss2
# 输入 AccessKeyId and AccessKeySecret
auth = oss2.Auth('LTAI6KwW70DAfUyD','tXNFt4nfNkts2I91HJxe5WbFVWexDd')
# 输入 Endpoint and Bucket name
bucket = oss2.Bucket(auth,'oss-cn-hangzhou.aliyuncs.com','wordpress-liutingshu')
# 本地文件路径
filePath = sys.argv[1]
fileName = filePath.split("/")[-1]
# 上传进度条
def percentage(consumed_bytes, total_bytes):
   if total_bytes:
     rate = int(100 * (float(consumed_bytes) / float(total_bytes))) 
     print('\r{0}%'.format(rate), end=filePath)
     sys.stdout.flush()
# 上传文件
oss2.resumable_upload(bucket, fileName, filePath, progress_callback=percentage)
print('\rUpload %s to OSS Success!' % filePath)

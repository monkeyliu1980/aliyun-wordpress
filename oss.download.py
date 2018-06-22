# -*- coding: utf-8 -*-
from __future__ import print_function
import os, sys
import oss2

# 百分比显示回调函数
def percentage(consumed_bytes, total_bytes):
     if total_bytes:
          rate = int(100 * (float(consumed_bytes)) / (float(total_bytes)))
          print('\r{0}%'.format(rate), end=saveFile)
          sys.stdout.flush()

auth = oss2.Auth('LTAI6KwW70DAfUyD', 'tXNFt4nfNkts2I91HJxe5WbFVWexDd')
bucket = oss2.Bucket(auth, 'oss-cn-hangzhou.aliyuncs.com', 'wordpress-liutingshu')

fileName = sys.argv[1]
saveFile = './' + fileName
oss2.resumable_download(bucket, fileName, saveFile,
     store = oss2.ResumableDownloadStore(root='/tmp'),
     multiget_threshold = 20 * 1024 * 1024,
     part_size = 10 * 1024 * 1024,
     num_threads = 5,
     progress_callback = percentage)

print('\rDownload %s to %s Success!' % (fileName, saveFile))

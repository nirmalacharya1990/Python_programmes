import boto3
import io
import json
s3=boto3.resource(service_name='s3',
                 region_name='ap-south-1',
                 aws_access_key_id='AKIAZ7E7Y63CVWLYW77N',
                 aws_secret_access_key='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'
                 )

""" bucketname = 'cybraicsnotebooks'
bucket = s3.Bucket(bucketname)
for obj in bucket.objects.all():
    s=obj.key
    print (s)
 """
a=0
for bucketname in s3.buckets.all():
#for bucketname in s3.get_objects():
    for obj in bucketname.objects.all():
    #for obj in bucketname.get_object():
     s= obj.key
     #print(s)
     #p= s.split()
     #print(p)
     x = obj.get()["Body"].read().decode()
     if "json" in s and  "sample1" in x:
       print(s)
       #x = obj.get()["Body"].read().decode()
       #x = obj.get()["Body"].read().decode()
       #print(x)

       #fileObject = open(x)
       #jsonContent = x.read()
       #if "sample1" in x:
       json_data = json.loads(x)
       print(bucketname)
       print(json_data)
       a=a+1
       print(a)
       #aList = json.loads(json_data)
       #if aList['fruit']=='Apple':
       #print(json_data['d']['key1']['nestkey']['subnestkey'])
       #print(x)
       #if aList['d']['key1']['nestkey']['subnestkey']=='sample1':
        #print('Do Something')
         
    #print (bucketname.name)"""
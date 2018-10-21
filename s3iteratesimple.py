import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)


bucket='securecheckin'

mybucket = s3.Bucket(bucket)

for object in mybucket.objects.all():
    print(object.key)

list1 = mybucket.objects.all()



import urllib.request
import os
import boto3

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/'

	urllib.request.urlretrieve(
		source_dataset_url + 'boro.csv', '/tmp/' + new_filename + '-boro.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'by-age.csv', '/tmp/' + new_filename + '-by-age.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'by-sex.csv', '/tmp/' + new_filename + '-by-sex.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'case-hosp-death.csv', '/tmp/' + new_filename + '-case-hosp-death.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'summary.csv', '/tmp/' + new_filename + '-summary.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'tests-by-zcta.csv', '/tmp/' + new_filename + '-tests-by-zcta.csv')

	urllib.request.urlretrieve(
		source_dataset_url + 'Deaths/probable-confirmed-dod.csv', '/tmp/' + new_filename + '-probable-confirmed-dod.csv')

	# uploading new s3 dataset
	s3 = boto3.client("s3")
	folder = "/tmp"

	asset_list = []

	for filename in os.listdir(folder):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + filename)
		asset_list.append({'Bucket': s3_bucket, 'Key': new_s3_key + filename})

	return asset_list
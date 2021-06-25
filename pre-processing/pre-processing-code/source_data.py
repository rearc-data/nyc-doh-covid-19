import os
import boto3
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from multiprocessing.dummy import Pool

def data_to_s3(endpoint):

	# throws error occured if there was a problem accessing data
	# otherwise downloads and uploads to s3

	source_dataset_url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/'

	try:
		response = urlopen(source_dataset_url + endpoint)

	except HTTPError as e:
		raise Exception('HTTPError: ', e.code, endpoint)

	except URLError as e:
		raise Exception('URLError: ', e.reason, endpoint)

	else:
		data_set_name = os.environ['DATASET_NAME']

		filename = data_set_name + '-' + endpoint.replace('/', '-')
		file_location = '/tmp/' + filename

		with open(file_location, 'wb') as f:
			f.write(response.read())

		# variables/resources used to upload to s3
		s3_bucket = os.environ['ASSET_BUCKET']
		new_s3_key = data_set_name + '/dataset/'
		s3 = boto3.client('s3')

		s3.upload_file(file_location, s3_bucket, new_s3_key + filename)

		print('Uploaded: ' + filename)

		# deletes to preserve limited space in aws lamdba
		os.remove(file_location)

		# dicts to be used to add assets to the dataset revision
		return {'Bucket': s3_bucket, 'Key': new_s3_key + filename}

def source_dataset():

	# list of enpoints to be used to access data included with product
	endpoints = [
		# totals
		'totals/antibody-by-age.csv',
		'totals/antibody-by-boro.csv',
		'totals/antibody-by-modzcta.csv',
		'totals/antibody-by-poverty.csv',
		'totals/antibody-by-sex.csv',
		'totals/by-age.csv',
		'totals/by-boro.csv',
		'totals/by-poverty.csv',
		'totals/by-race.csv',
		'totals/by-sex.csv',
		'totals/data-by-modzcta.csv',
		'totals/deaths-by-boro-age.csv',
		'totals/deaths-by-race-age.csv',
		'totals/deaths-by-underlying-conditions.csv',
		'totals/group-cases-by-boro.csv',
		'totals/group-data-by-boro.csv',
		'totals/group-death-by-boro.csv',
		'totals/group-hosp-by-boro.csv',
		'totals/probable-confirmed-by-age.csv',
		'totals/probable-confirmed-by-boro.csv',
		'totals/probable-confirmed-by-location.csv',
		'totals/probable-confirmed-by-race.csv',
		'totals/probable-confirmed-by-sex.csv',
		'totals/summary.csv',
        # trends
		'trends/antibody-by-week.csv',
		'trends/caserate-by-modzcta.csv',
		'trends/covid-like-illness.csv',
		'trends/data-by-day.csv',
		'trends/percentpositive-by-modzcta.csv',
		'trends/testing-by-age.csv',
		'trends/testing-turnaround.csv',
		'trends/testrate-by-modzcta.csv',
		'trends/tests.csv',
		# latest
		'latest/last7days-by-modzcta.csv',
		'latest/now-covid-like-illness.csv',
		'latest/now-data-by-day.csv',
		'latest/now-summary.csv',
		'latest/now-testing-by-age.csv',
		'latest/now-tests.csv',
		'latest/pp-by-modzcta.csv'
	]

	# multithreading speed up accessing data, making lambda run quicker
	with (Pool(7)) as p:
		asset_list = p.map(data_to_s3, endpoints)

	# asset_list is returned to be used in lamdba_handler function
	return asset_list

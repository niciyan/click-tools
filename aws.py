import boto3
from boto3.exceptions import Boto3Error
from helpers import handle_profiles, handle_subnets, handle_vpcs

class MyException(Exception):
    pass

def main():
    try:
        profiles = boto3.Session().available_profiles
        profile = handle_profiles(profiles)
        ec2 = boto3.Session(profile_name=profile).client('ec2')

        print('Fetching your vpcs. Wait a moment...')
        response = ec2.describe_vpcs()
        vpcs = response['Vpcs']
        your_vpc = handle_vpcs(vpcs)
        response = ec2.describe_subnets(
                Filters=[ { 'Name':'vpc-id', 'Values': [ your_vpc] }, ]
                )
        subnets = response['Subnets']
        handle_subnets(subnets)
        print('Done!')
    except Boto3Error as e:
        print('We got AWS error.')
        print(e)
    except Exception as e:
        print(e)
        # e.with_traceback()



if __name__ == '__main__':
    main()

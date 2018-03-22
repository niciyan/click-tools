import click, boto3

class MyException(Exception):
    pass

def main():
    try:
        ec2 = boto3.client('ec2')

        print('Fetching your vpcs. Wait a moment...')
        vpcs = ec2.describe_vpcs()['Vpcs']
        your_vpc = handle_vpcs(vpcs)
        response = ec2.describe_subnets(
                Filters=[ { 'Name':'vpc-id', 'Values': [ your_vpc] }, ]
                )
        subnets = response['Subnets']
        handle_subnets(subnets)
        print('\n----done.')
    except Exception as e:
        print(e)

def handle_vpcs(vpcs):
    if len(vpcs) == 0:
        raise MyException("No vpc available.")
    for vpc in vpcs:
        print('  * {}'.format(vpc['VpcId']))
    your_vpc = click.prompt('Input your vpc', type=click.Choice([ vpc['VpcId'] for vpc in vpcs ]))
    return your_vpc

def handle_subnets(subnets):
    if len(subnets) == 0:
        raise MyException("No subnet available.")
    for subnet in subnets:
        print('  * {}'.format(subnet['SubnetId']))


if __name__ == '__main__':
    main()

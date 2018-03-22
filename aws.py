import click, boto3

def main():
    ec2 = boto3.client('ec2')

    print('Fetching your vpcs. Wait a moment...')
    vpcs = ec2.describe_vpcs()['Vpcs']

    for vpc in vpcs:
        print('  * {}'.format(vpc['VpcId']))

    your_vpc = click.prompt('Input your vpc', type=click.Choice([ vpc['VpcId'] for vpc in vpcs ]))
    return

    response = ec2.describe_subnets(
            Filters=[
                {
                    'Name':'vpc-id',
                    'Values': [
                        your_vpc,
                        ]
                    },
                ]
            )

    subnets = response['Subnets']

    if len(subnets) > 0:
        for subnet in subnets:
            print('  * {}'.format(subnet['SubnetId']))
    else:
        print('No subnet available.')
        return

    print('\n----done.')

if __name__ == '__main__':
    main()

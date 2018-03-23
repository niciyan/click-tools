import click

def handle_profiles(profiles):
    if len(profiles) == 0:
        raise MyException("No profile available.")
    print('Choose Your AWS profile.')
    for profile in profiles:
        print("  * {}".format(profile))
    your_profile = click.prompt("Your profile", 
            default=profiles[0], 
            type=click.Choice(profiles)
            )
    return your_profile

def handle_vpcs(vpcs):
    if len(vpcs) == 0:
        raise MyException("No vpc available.")
    print('Your vpc list:')
    for i, vpc in enumerate(vpcs):
        print('  {} : {}'.format(i, vpc['VpcId']))
    number = click.prompt('Input your vpc', 
            default=0,
            type=click.IntRange(0, len(vpcs)))
    return vpcs[number]['VpcId']

def handle_subnets(subnets):
    if len(subnets) == 0:
        raise MyException("No subnet available.")
    print('Your subnet list:')
    for subnet in subnets:
        print('  * {} ( State:{}, AvailableIpAddressCount:{} )'.format(subnet['SubnetId'], subnet['State'], subnet['AvailableIpAddressCount']))



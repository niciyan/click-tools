import click ,requests ,pprint ,json, time

# @click.command()
@click.option('--name', prompt='Your name', default='World', help='The person to greet.')
@click.option('--security-group', prompt='Security Group', default='group', help='The Security Group.')
@click.option('--name', prompt='Your name', default='World', help='The person to greet.')
@click.option('--elasticip', prompt='ElasticIP', default='no', help='The Public IP Address.')
@click.option('--version', prompt='publish version', default=1, type=int)
def cmd(name, version, security_group, elasticip):
    msg = 'Hello, {name}'.format(name=name)
    click.echo(msg)

def fetch_data(url="https://google.com", method="GET"):
    response = requests.request(url=url, method=method)
    return response.headers

@click.command()
@click.option('--url', prompt='URL', default='https://google.com', help='The URL.')
@click.option('--method', prompt='Method', default='GET', help='Request Method.')
def cmd_fetch(url, method):
    for k, v in fetch_data(url, method).items():
        print("    {} : {}".format(k, v))

def get_api(url, method='GET'):
    response = requests.request(url=url, method=method)
    data = json.loads(response.text)
    return data

def main():
    # print(pprint.pprint(fetch_data(), indent=4))
    # for k, v in fetch_data():
    #     print("{} : {}".format(k, v))
    # cmd_fetch()
    url = "https://api.github.com/users/niciyan/repos"
    print('Fetching from {}'.format(url))
    data = get_api(url)
    print("Your repositories.")
    repos = [ item['name'] for item in data ]
    for item in data:
        print("  * ", item['name'])
    # time.sleep(1)
    repo = click.prompt('Enter repo name you want.', default=data[0]['name'], type=click.Choice(repos))
    print('you got {}'.format(repo))

    commit_url = "https://api.github.com/repos/niciyan/" + repo + "/commits"
    print("Fetching commits from {}".format(commit_url))
    commits = get_api(commit_url)
    for i, item in enumerate(commits):
        print("  {}  {}  {}".format(i, item['commit']['message'], item['commit']['author']['date']))
    # cmd()

if __name__ == '__main__':
    main()



from github import Github
import sys
import pandas as pd

def get_multi_clones(args):
    """
    Reads in the files and gets the unique users,
    then calls to get all repositories and clones of that user

    input: file_name type(string) -> the file string for the repo whitelist
    output: sum type(int) -> the total number of clones for all team members
    """
    file = pd.read_excel(args[1])
    database = pd.read_excel(args[2])

    sum = 0

    for num in range(len(database)):
        alias = database['Alias'][num]
        auth_code = database['Auth Code'][num]
        white_list = file[file['Alias'] == alias]['Repo Name']

        sum += get_single_account_clones(auth_code, list(white_list))

    return sum


def get_single_account_clones(token, white_list):
    """ 
    Get all the repositories under a single github auth token,
    Compare the repos gathered against those whitelisted, 
    and return the sum of all clones

    input: token type(string) -> the auth code for an individual account
    input: white_list type(list) -> the list of repositories we wish to measure
    output: sum type(int) -> the sum of all clones
    """
    g = Github(str(token))
    user = g.get_user()

    sum = 0

    for repo in user.get_repos():
        if repo.full_name in white_list:
            single_repo = repo.get_clones_traffic()
            sum += single_repo['count']

    return sum

if __name__ == "__main__":
    args = sys.argv

    total = get_multi_clones(args)

    print(total)
from typing import List
import git
from src.Importer import Importer
import os


def find_git_repos(directory) -> List[git.Repo]:
    git_repos = []
    for root, dirs, _files in os.walk(directory, followlinks=True):
        if '.git' in dirs:
            git_repos.append(git.Repo(root))
            dirs.remove('.git')

    return git_repos


repos = find_git_repos("/home/milesq/Desktop/dev/current/job")

non_gh_repos = [
    repo for repo in repos
    if repo.remotes
    and 'github' not in repo.remotes[0].url
]

mock_repo = git.Repo("./other-git-servers-mock")
mock_repo.remotes.append(git.Remote.add(mock_repo, "origin", "https://github.com/Milesq/other-git-servers-mock"))
importer = Importer(repos, mock_repo)
importer.set_author(['wmilosz88@gmail.com', 'milosz.wisniewski@ecreationmedia.tv'])
importer.import_repository()

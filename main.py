import git
from src.Importer import Importer
import os

def list_repos(parent_dir):
    return [git.Repo(os.path.join(parent_dir, path)) for path in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, path))]


repos = [
    *list_repos("/home/milesq/Desktop/dev/current/bbcs"),
    *list_repos("/home/milesq/Desktop/dev/current/uktv-compliance")
]

mock_repo = git.Repo("./other-git-servers-mock")

importer = Importer(repos, mock_repo)
importer.set_author(['wmilosz88@gmail.com', 'milosz.wisniewski@ecreationmedia.tv'])
importer.import_repository()

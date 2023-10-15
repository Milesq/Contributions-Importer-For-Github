import git
from git_contributions_importer.Importer import Importer

repos = [
    git.Repo("/home/milesq/Desktop/dlx1-p7-content-hierarchy")
]

mock_repo = git.Repo("./other-git-servers-mock")

importer = Importer(repos, mock_repo)
importer.set_author(['wmilosz88@gmail.com', 'milosz.wisniewski@ecreationmedia.tv'])
importer.import_repository()

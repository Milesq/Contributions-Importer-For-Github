#!/bin/bash
set -euxo pipefail

cd "$(dirname "$0")"

rm -rf other-git-servers-mock/
mkdir other-git-servers-mock/

git init other-git-servers-mock/

uv run main.py

cd other-git-servers-mock/

git push --force

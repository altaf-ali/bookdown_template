#!/bin/bash

set -ev

echo GIT_AUTHOR_NAME = ${GIT_AUTHOR_NAME}
echo GIT_AUTHOR_EMAIL = ${GIT_AUTHOR_EMAIL}

[ -z "${GITHUB_PAT}" ] && exit 0
[ "${TRAVIS_BRANCH}" != "master" ] && exit 0

git clone -b gh-pages https://${GITHUB_PAT}@github.com/${TRAVIS_REPO_SLUG}.git book-output

cd book-output
cp -r ../_book/* ./

git add --all *
git commit -m"Update the book" || true
git push origin gh-pages

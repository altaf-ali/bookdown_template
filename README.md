# Bookdown Template

[![Build Status](https://travis-ci.org/altaf-ali/bookdown_template.svg?branch=master)](https://travis-ci.org/altaf-ali/bookdown_template)

# Getting Started

- Generate new Personal Access Token on [GitHub](https://github.com/settings/tokens) with "repo" scope.

- Encrypt the token using the travis CLI:
    
    ```travis encrypt GITHUB_PAT=TOKEN```

- Make the following changes to each file:

    |Filename       |Changes|
    |---------------|----------------------------------|
    |.travis.yml    |Replace the `secure` key with the encrypted token|
    |.gitconfig     |Update `GIT_name` and `GIT_email`|
    |_bookdown.yml  |Update `rmd_files` as necessary|
    |DESCRIPTION    |Update `Package`, `Title`, `Version`, `Imports`, `Remotes`|
    |index.Rmd      |Update `title`, `github-repo`|
    |README.Rmd     |Update the **Build Status** link|

- Enable the repository on [Travis CI](https://travis-ci.org)

- Push all changes to GitHub

- Run `./bin/setup.sh'

# Acknowledgments

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


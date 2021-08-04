---
title: Project Organization
---

1. Anatomy of a Bioinformatics Project
    1. Computational environment (including external software)
    2. Scripts
    3. Raw data
    4. Processed data
2. Project Organization Challenges
    1. Raw/processed data can be large
    2. Scripts and external program parameters evolve over time
    3. Results evolve over time too!
    4. Only certain results must be tracked/maintained
    5. Code must be made available to others, ideally in an easily reproducible form
3. Project Organization Tools & Strategies
    1. Environment management software (e.g. conda)
    2. git+github
    3. README
4. Recommended Project Setup
    1. Choose a reasonable and descriptive project directory name
    2. Create a conda environment named the same as your project directory name
    3. `git init` - initialize directory as a git repository
    4. Create the following:
        1. `install_packages.sh` - script to store software install commands
        2. `README.md` - a readme that briefly describes the project and eventually
          instructions on how to run the code
        3. `analysis/` - directory that will contain all of your code
    5. `git add` and `git commit` the files in your repo
    6. Create parallel git repo on github/bitbucket, add as remote to your project
    7. `git push origin -u main` or whatever github/bitbucket tells you to do

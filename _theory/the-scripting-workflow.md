---
title: The Scripting Workflow
---

1. The Script: The Fundamental Unit of Bioinformatics Engineering
    1. A script is a file that contains code that can be executed
    2. Transforms a set of input files into one or more output files
    3. Scripts evolve: implement, execute, evaluate, repeat
    4. Workflows are composed of independent scripts that work together
2. The scripting environment
    1. Scripts combine *data* and *code*
    2. Your script must be able to access the data; your scripts must be stored in
    the same place where the data are
      1. If the data is not too large or protected, this could be a laptop
      2. Otherwise, you will use a compute cluster, or the cloud
    3. Computational environment: hardware+software
3. Writing scripts
    1. Scripts are *text files* that contain code understood by some language, e.g.
    bash, python, R, etc
    2. Scripts must be "run" or "executed"
    3. Scripts interact with external resources, e.g. file systems, web sites, etc
    4. Write incrementally, run and test often
4. Text/code editors
    1. CLI-based - nano, emacs, vim
    2. GUI-based - Atom, Sublime Text
    3. Notebooks: RStudio, Jupyter notebook/lab

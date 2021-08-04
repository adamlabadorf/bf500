---
title: Computational Environment Management
---

1. The Computational Environment
    1. The hardware+software context in which code runs
    2. An analysis is only reproducible if you also provide sufficient
    instructions about how to recreate the proper environment
    3. Strictly speaking, to *guarantee* reproducibility, must recreate
    *precisely* the same computational environment as when code was first run
    4. This is very, very hard!
2. Hardware
    1. Every computer has an architecture (AMD, intel, etc), memory (RAM), and
    storage (disk space)
    2. Some hardware is specialized for certain tasks (e.g. GPUs)
    3. Software written in "low level" languages like C must be compiled from
    source code so the computer can understand it
    4. Some algorithms require a certain amount of RAM to run (based on input
    size)
    5. Some analyses require input data that is very large, requiring large
    amounts of disk space
    6. These are all important aspects to specify about the hardware
    environment
3. Software
    1. Every piece of software requires other software to run
    2. Every piece of software has a *version* that changes over time
    3. Software often need *specific versions* of other software to run
    correctly
    4. Therefore, to recreate a complete software environment, must specify:
        1. Your own code
        2. The software package dependencies your code needs, and their versions
        3. The software dependencies of those dependencies, *and their versions...*
    5. And then another user must install exactly these versions in their environment
    6. This is very, very hard!
4. Software environment management solutions
    1. modules
    2. conda
    3. Containers

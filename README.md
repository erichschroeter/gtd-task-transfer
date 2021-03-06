# gtd-task-transfer

Contributors: Erich Schroeter

GTD Task Transfer is an application that allows GTD application users to transfer
their task data between other GTD applications.

## Description

The reason this exists is because I wanted to start using a GTD application, but
didn't want all my data to be stuck with that one application. So, I needed a way
to easily transfer data (if the GTD application supports exporting data to a CSV
format) from one app to another while I was trying out different GTD applications.

As of the last update of this README (2011-03-12), only importing data from a CSV
file into TaskWarrior is supported.  I have written the script in such a way that
it should be self-explanatory to add future functionality.

## Usage

Examples:

#### To list supported file types:

    ./gtd-task-transfer import -h

#### To list supported GTD applications:

    ./gtd-task-transfer import csv -h

#### To list supported TaskWarrior fields to import:

    ./gtd-task-transfer import csv /path/to/exported/tasks.csv taskwarrior -h

#### To preview what will be called to import tasks:

    ./gtd-task-transfer import --preview csv /path/to/exported/tasks.csv taskwarrior -d 0 -P 1 -p 2

#### To perform the import:

    ./gtd-task-transfer import csv /path/to/exported/tasks.csv taskwarrior -d 0 -P 1 -p 2
    
## Installation

I developed this project in Linux (Ubuntu 10.04) with Python 2.6.5 and 2.7. The
only installation is to copy the gtd-task-transfer.py file to a place you can
execute it, and follow the examples above.

### Install Python 2.7 in Ubuntu 10.04

1. download the tar from http://www.python.org/download/releases/2.7.1/
2. tar xzf Python-2.7.tgz
3. cd Python-2.7
4. ./configure
5. make
6. sudo make altinstall

### Prerequisites

The following libraries or programs were what I used.

- **Python 2.7**       _(perhaps > 2.7, but I haven't tested it)_
    - uses _argparse_ and _subprocess.call_


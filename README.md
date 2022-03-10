# What is this?

As I am practicing Python on [codechalleng.es](https://codechalleng.es) - check out my profile there: [tonmarton](https://codechalleng.es/profiles/tonmarton) - I need this repo to solve challenges - called Pybites - locally.

Below you can find how I set up my local environment and worked on Pybites.

## my PyBites badge:

With solving PyBites you receive points depending on the difficulty of the bites. These points get you badges - milestones. Here you can see my current badge: 
| belt image |  belt name  | personal certificate link |
| - | - | - | 
| <img src="https://codechalleng.es/static/img/honors/orange.73422678956e.png" width=60%> | **orange belt** | [cert link](https://codechalleng.es/badge/9e752512-2f4f-48eb-974a-c7f11ff3bb99) |   

# set-up

Using pipenv, since the environment variables can be supplied with a .env file this way. For this a couple of dependency versions are changed from the original [requirements.txt](https://github.com/pybites/platform-dependencies/blob/master/requirements.txt) - the ```requests``` and ```feedparser``` packages.

- add the environmental variables to a new .env file (this enables using the ```eatlocal``` package to automate the downloading and unzipping of Pybites). Use the .env-example file and rename it.
  
        PYBITES_USERNAME=<username>
        PYBITES_PASSWORD=<password>
        PYBITES_REPO=</path/to/local/repo>

- create the virtualenv and install the dependencies:
  
        pipenv install

- activate virtualenv:

        pipenv shell

    
# usage

- select a problem to solve on [codechalleng.es](https://codechalleng.es) and remember the number of the Pybite.
- download the problem with ```eatlocal```:

        eatlocal download <bite number>

- write a solution in the ```<bite name>.py```:
- run tests:

        pytest

- submit solution with ```eatlocal```:

        eatlocal submit <bite number>






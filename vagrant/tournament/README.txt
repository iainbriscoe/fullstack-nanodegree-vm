Tournaments 

Requirements: 
- machine with python installed. 
- machine with vagrant installed.
- install virtual box on your machine.
- internet access.


Starting:

Vagrant- 
vagrant can be downloaded from this website https://www.vagrantup.com/downloads.html 
-> once downloaded run the installer and follow the on screen steps which which install vagrant on your machine.

Virtual Box - 
virtual box can be downloaded from this website https://www.virtualbox.org/wiki/Downloads 
-> once downloaded run the installer and follow the on screen steps which which install virtual box on your machine.

Python -  
Python can be downloaded and installed from: https://www.python.org/downloads/
-> once download run the installer and follow the on screen steps which will instal python on your machine.

Once python is installed on your machine. You will now have a program title IDLE. 

To start running the program on your machine navigate to terminal(mac) or command prompt(windows) then follow these steps: 
type: cd desktop/fullstack/vagrant
comment: this will be the directory to get you to into your vagrant folder contained within the project folder
type: vagrant up
comment: will begin to download content and set up a virtual machine connection
type: vagrant ssh 
type cd /vagrant/tournament 
comment: This time the directory is changed using cd / instead of just cd
type: psql
type: \i tournament.sql
type: \c 
type: \q 
comment: this set of comments logs in to psql -> creates the tournaments database -> connect to the database -> quit psql(leaves the database running but exits psql to bring you back to the vagrant prompt)
type: python tounament_test.py

When the tournament_test comment is run it runs the tournament_test.py file which checks each function in tournament.py against the database created in the previous steps 

You should expect to see steps 1 - 8 detailing the passed tests.
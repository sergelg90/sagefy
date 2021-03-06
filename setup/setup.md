Local Development Setup
=======================

These instructions assume you are using Mac OS X.

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
2. Install [Vagrant](http://downloads.vagrantup.com/)
3. Install Vagrant Guest Additions: `vagrant plugin install vagrant-vbguest`
4. Clone the Repository: `git clone https://github.com/heiskr/sagefy.git`
5. Enter the directory: `cd sagefy`
6. `vagrant up`
7. `sudo nano /etc/hosts`, and add `192.168.122.114 doris`
8. In your browser, visit `http://doris/`

Common Vagrant commands
-----------------------

- Enter Vagrant: `vagrant ssh`
- Put Vagrant to sleep: `vagrant suspend`
- Make a new Vagrant: `vagrant destroy; vagrant up`

Tailing the Log
---------------

    sudo tail -F /var/log/nginx/error.log
    sudo tail -F /tmp/uwsgi.log

Working with the UI
-------------------

    cd ~/Sites/sagefy/ui
    gulp

Push gh-pages to Github Pages
-----------------------------

    git subtree push --prefix gh-pages origin gh-pages

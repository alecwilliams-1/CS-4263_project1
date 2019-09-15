This is a Django-based website that serves a single random number basically naked in HTML

Requirements:

note: it may work on more systems and configurations than those listed, but we here at team
Apple guarantee nothing other than what is stated here.

software requirements:
Ubuntu Server 18.04
Python 3 (it may coexist with an installation of python 2, however all python commands must explicitly state "Python3".  it tends to come preinstalled in Ubuntu, but can be manually installed with "sudo apt install python3")
Django (it can be installed using "pip install Django=2.2.5". you may need to run the command as superuser)


To run, navigate to the folder this readme is in, and enter "sudo python manage.py runserver 0:80"
alternatively, script files "startPython3.sh" and "startPython2-3.sh" are provided, however we make no guarantees about these, and are solely for convenience.
these are for systems with only python 3 and both python 3 and python 2 respectively.

once running, the server can be accessed through a web browser via its external IP address.
# python-cicd
Personal repository for playing around with Python CI-CD process

## Reminders for myself:

### setup.py
setup.py develop  # installs all dependencies and the library itself to allow
                  # running and testing the script easily
setup.py develop -u # --uninstall, removes the develop files
setup.py build    # build the package
setup.py clean -a # clean all files from /build

The setup.cfg file contains default options for commands of the setup.py script

### pip
pip install -r requirements.txt     # install all required libraries

# python-cicd
Personal repository for playing around with Python CI-CD process

## Reminders for myself:

### setup.py

Installing all dependencies and the library itself to allow running and testing the script easily:
```bash
setup.py develop
```

Remove the development installation
```bash
setup.py develop -u | --uninstall
```

Build the package
```bash
setup.py build
setup.py bdist_wheel    # binary distribution, needs `wheel` installed first
setup.py sdist          # source distribution
```

Clean all files from /build
```bash
setup.py clean -a
```

The setup.cfg file contains default options for commands of the setup.py script

### pip
pip install -r requirements.txt     # install all required libraries

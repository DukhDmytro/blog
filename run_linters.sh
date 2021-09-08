#!/bin/bash
# Disable C0115: Missing class docstring
# Disable R0903: Too few public methods (0/2)
# Because class Meta is commonly used in Django
echo 'PYLINT'
# pylint --disable=C0115,R0903 *.py **/*.py
pylint *.py **/*.py
echo ''
echo 'FLAKE8'
flake8 --exclude 'migrations'
echo ''
echo 'MYPY'
mypy . --ignore-missing-imports

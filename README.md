# Setup
- Install python 3.7
- Install library:
    - pip install pipenv
    - pipenv shell (to start a new shell session with the virtualenv)
    - pipenv install --ignore-pipfile (install packages from Pipfile.lock, skip Pipfile)

- If you are Pycharm's user:
    Go to Preferences > Project Interpreter > Add > Pipenv Environment > Ok
    (refer https://www.jetbrains.com/help/pycharm/pipenv.html for more details)


# Run test in parallel with pytest-xdist lib:
    pytest -n=2 --alluredir=./allure --clean-alluredir --driver chrome


# Generate report:
Make sure you have allure installed (or install by running: brew install allure)
    allure generate "./allure/" -o ./reports/ --clean


# Useful link:
- https://realpython.com/pipenv-guide/#pipenv-introduction
- https://pipenv-fork.readthedocs.io/en/latest/basics.html
- https://docs.pytest.org/en/latest/contents.html
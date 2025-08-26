For the creation of a library:

- A directory is needed (name of directory is not relevant).
- Inside the directory there should be a folder named 'src'. 
- Inside this folder, a folder with the name of the packet or various if the library has various packages. 
- Inside this folder there should be a folder with the name '__init__.py', and as many other scripts as we want with the funtions we want the packet we have.
- In the '__init__.py' script we will call the functions we want the packet to have in this way: 'from .script_with_functions import function1, function2...'. ALso inside this '__init__.py' script, a variale called '__all__' is needed with a list of the name of the functions included in that packet.


- Going back to the main directory, outside of 'src', a file named pyproject.toml is needed for the building of the library.
- The structure of this file include build instructions, project metadata (name of the library, version), dependencies, tests...

- Other scripts and folders are recomended as standard structure.
- tests folder with scripts to test the functions and df examples.
- LICENSE
- README.md


- For this build:

We used python -m build
This creates a folder with .whl adn .gz. The distribuible files that can be used to distribute the packet, in the python public index or in github or internaly...

- Upload in public index python repository (anyone can do pip install...)

Create account in PyPI and: 
python -m twine upload dist/*
will ask for a token

- Updates?: 

If changes are made in code, in the pyproject.toml file, version is changed, we build again and upload to pypi.
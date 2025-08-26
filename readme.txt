"When importing a module, it searches through all paths contained in sys.path. sys.path contains default paths like the location of the Python installation's standard library and the location pip installs packages to, plus any paths in the PYTHONPATH environment variable. One additional path is added upon invocation of a script, either the directory that that script is in if you do python script.py or the current working directory if you do python -m script."

For this repo, absolute import statements are used so that:
1. modules that import other modules can be imported into top-level scripts succesfully
2. modules can be executed directly using the -m switch AS LONG AS the top-level directory is the working directory (current location)
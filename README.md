#Instructins for Virtual Environment and local dependency management

1) Create a new virtual environment 
 "py -m venv .venv"
2) Activate virtual environment (GitBash on windows)
 Powershell:
 ".venv/Scripts/activate"                                           
 GitBash
 "source .venv/Scripts/activate"     

What the terminal should look like using PowerShell
 ---> "(.venv) ..."                              
 
3) Confirm activation (GitBash for example. Should list the env directory)
 Powershell
 "which python"
 GitBash
 "where python"

4) Generate requirements.txt file with existing dependencies
"pip freeze > requirements.txt"

6) Install required dependencies from requirements.txt
"pip install -r requirements.txt"

7) Create requirements.txt for existing files
"pipreqs ./<dir>"

Create a file directory containing project files and refer to this for dependencies

8) How to exit env
"deactivate"
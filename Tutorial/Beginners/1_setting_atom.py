#########################################
# Checking Default Installed Packages ###
#########################################

# file->settings (or ctrl+shift+p and type settings),
# In packages side tab,
# check in installed package for a core package,
# "language-python" - syntax highlighting, code completion etc
# click on the package to edit/add new feature

print("Hello world")

##################
# Run the code ###
##################

# Run the code on windows terminal in Atom ###
# file->settings, In Install side tab,
# "platformio-ide-terminal"
# Packages-> platformio-ide-terminal->New terminal ( or ctrl+shift+p ..)
# by default the current directory comes
# type "python .\1.setting_atom.py"


# Run the code in Atom ###
# Install package "script"
# ctrl+shift+b - run the code

# Run in a different python version ###
# In script:run options, in command type the path "usr/bin/python2.7"
# if you want you can save as profile with a profile name
# have to repeat each time you run


x = 5
print("the value is : ")
print(x)

###############################
# packages to Improve Style ###
###############################

# "file-icons" - improves file icons in the tree
# "minimap" - mini map view of the program near the scroll

#####################################
# packages to Improve Performance ###
#####################################

# Debugger for break point ###
# Install package "python-debugger"
# alt+r - python debugger
# alt+shift+r - set break point on the line

# Auto-Complete ###
# disable some core packages which is not python friendly
# disable "autocomplete-plus" and "autocomplete-snippet"
# install "autocomplete-python"
# enable/install "kite" for more

# Auto-Format ###
# "python-autopep8" - formats the lines and spacing on save (turn on check box)
#  also on terminal need to "pip install autopep8" - need to install on system

# Check error ###
# install "linter-flake8"
# and its dependencies - linter,linter-ui-default, intentions, busy-signal
# also on terminal need to "pip install flake8"

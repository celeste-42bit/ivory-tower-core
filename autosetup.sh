python3 -m venv env
source ./env/bin/activate

#Make sure python3 and pip are installed
    # if not, check for sudo privileges and install python3 and pip

# create venv and install reqirements.txt using pip

if [[ -z "$VIRTUAL_ENV" ]]; then
    exit
fi

pip3 install -r ./requirements.txt > /dev/null 2>&1
if [[ $? -eq 0 ]]; then
    echo "Done."
else
    echo "Ups. Something went ded. Rip."
fi

# check if required file structure exists
    # if not, create required directory structure and add required config files with default content

# Finish and close

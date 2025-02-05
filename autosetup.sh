python3 -m venv env
source ./env/bin/activate

if [[ -z "$VIRTUAL_ENV" ]]; then
    exit
fi

pip3 install -r ./requirements.txt > /dev/null 2>&1
if [[ $? -eq 0 ]]; then
    echo "Done."
else
    echo "Ups. Something went ded. Rip."
fi

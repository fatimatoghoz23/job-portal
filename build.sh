set -o errexit
python3 -m pip install -r requirements.txt
# pip install  requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
echo "BUILD START"
python3 -m pip install -r requirements.txt
python backend/manage.py collectstatic --noinput
echo "BUILD END"
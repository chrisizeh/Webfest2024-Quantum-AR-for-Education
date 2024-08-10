# For development use (simple logging, etc):
pip3 install flask
python3 -m flask --app server run
# For production use:
# gunicorn server:app -w 1 --log-file -

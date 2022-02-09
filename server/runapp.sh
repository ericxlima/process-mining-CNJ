export FLASK_APP=app.py
# export SECRET_KEY='2f7ac045-92d5-43d6-9d5b-ee068d4b9974'
#  Development mode ON make CORS error 
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0

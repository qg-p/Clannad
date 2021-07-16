cd project
docker build .
docker run -p 5000:5000 -it chatrobot python app.py
FROM python:3.5-onbuild
ENV FLASK_APP=reconcile.py
#CMD [ "flask", "run" ]
CMD [ "python", "test.py" ]

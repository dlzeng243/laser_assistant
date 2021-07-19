# #!/bin/bash

if [ ! -d "/svgpathtools" ] 
then
  git clone https://github.com/mathandy/svgpathtools
  python3 svgpathtools/setup.py install
fi


pip3 install --user -r requirements.txt
python3 laser_flask.py

# export FLASK_APP=laser_flask.py
# flask run
# Introduction:
This project is a tool that will help make coding accessible to everyone.
It can convert flowcharts to python3 code
It can parse google documents and spreadsheets
It can use the power of AI to make working with excel sheets more intuitive.

# Working overview
This project contains two versions of the ‘Flow Chart Parser’:

Flow2Code: 
This project uses Graph theory to represent a flowchart in a computer's memory. Then by using various algorithms the flowchart is converted to Python3 code. The code generated can be executed on the server or can be downloaded to be executed locally.

SmartFlow
This project uses the same underlying concepts used in the ‘Flow2Code’ but adds a layer of NLP on top of it to make the tool more intuitive to use.

# Installation and Launching
Installing python 3.6.9
wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
tar -xvf Python-3.6.9.tgz
cd Python-3.6.9
./configure
make
make altinstall

Create virtual environment
python3.6 -m venv env_FCP

Activate environment and install dependencies:
source env_FCP/bin/activate
pip install -r requirements.txt(.../drag-drop-gui/ABFL Branding/requirements.txt)

Launching app
cd ‘ABFL Branding/BackEnd’
python routes_main.py ( by default the app will launch on port 8013 )
	
Endpoints
use /flow2code endpoint for Flowchart to Python3 converter.
Ex: localhost:8013/flow2code
use /smartflow endpoint for Smart FCP.
Ex: localhost:8013/smartflow

# Directory Structure
Inside ‘ABFL Branding/Backend’:
AI Models:
                  -     finalized_model.sav: This model is used to classify the instructions into functions.
Ex: If the input is “add all elements in the column points” will be classified as “sum”
 glove.6B.50d.txt: Is the Stanford generated word embeddings.
admin_api.py: helper file for routes_main.py, contains different classes that lead to different results.
AIUtil.py: This is a helper file for SmartFlow.py this has all the preprocessing and prediction methods required for the NLP classification.
conv.py: This module is used to convert json received from the front end to graph data.
FlowData2Code.py: This module is used to convert the graph data to python3 code. This is the module being used when you are accessing the ‘/flow2code’ endpoint.
routes_main.py: This is the main module. This module defines all the endpoints for the API.
settings.py: used to define the port number of the application
SmartFlow.py: This module is used to parse various gsuit elements using NLP. This is the module being used when you are accessing the ‘/smartflow’ endpoint.
tokenizer.py: It is a helper module for the FlowData2Code.py and SmartFlow.py module.

Inside ‘ABFL Branding/Frontend’:
mxgraph: This directory contains many example projects for the mxgraph library. ( a JS library used for the frontend of the project )
static: this directory contains all the static files that can be accessed using the API
IndexFlow2Code.html: This is the page that is loaded up when the user accesses the ‘/flow2code’ endpoint.
IndexSmartFlow.html: This is the page that is loaded up when the user accesses the ‘/smartflow’ endpoint.

All generated files are generated in the ‘ABFL Branding’ directory.

‘ABFL Branding/gsuitutil’ and ‘ABFL Branding/mailutil’ directories contain all modules required for accessing google APIs and mails.

# Demo Videos
Demo video for FCP: 
https://drive.google.com/file/d/102fj6df-VdfdT-ExSi7a5FpO_8rFlu9S/view?usp=sharing

Demo video for SmartFlow FCP: 
https://drive.google.com/file/d/1eWn0ImHzg3WMKHdovcuTpKhh1YxQYigG/view?usp=sharing

# How to train/retrain the NLP model?
Installing python 3.8.5
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
tar -xvf Python-3.8.5.tgz
cd Python-3.8.5
./configure
make
make altinstall

Create virtual environment inside the ‘Training Model’ dir
python3.8 -m venv env_Train

Activate environment and install dependencies:
source env_Train/bin/activate
pip install -r requirements.txt (.../drag-drop-gui/Training Model/requirements.txt)

Put all the training data into the .../Training Model/classes
With file name as the label and the content of the file as the data points

Launch the ‘training.ipynb’ by writing the command jupyter-notebook ‘training.ipynb’ and launching the whole notebook sequentially.

The model is saved in the ‘../Training Model/models’.

# Demo Video for FCP
https://drive.google.com/file/d/102fj6df-VdfdT-ExSi7a5FpO_8rFlu9S/view?usp=sharing

# Demo Video for Smart FCP
https://drive.google.com/file/d/1eWn0ImHzg3WMKHdovcuTpKhh1YxQYigG/view?usp=sharing

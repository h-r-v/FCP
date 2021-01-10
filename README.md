**# Introduction:**

This project is a tool that will help make coding accessible to everyone.

- It can convert flowcharts to python3 code
- It can parse google documents and spreadsheets
- It can use the power of AI to make working with excel sheets more intuitive.

**# Working overview**

This project contains two versions of the &#39;Flow Chart Parser&#39;:

1. Flow2Code:

This project uses Graph theory to represent a flowchart in a computer&#39;s memory. Then by using various algorithms the flowchart is converted to Python3 code. The code generated can be executed on the server or can be downloaded to be executed locally.

1. SmartFlow

This project uses the same underlying concepts used in the &#39;Flow2Code&#39; but adds a layer of NLP on top of it to make the tool more intuitive to use.

**# Installation and Launching**

1. Installing python 3.6.9

- wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
- tar -xvf Python-3.6.9.tgz
- cd Python-3.6.9
- ./configure
- make
- make altinstall

2. Create virtual environment

- python3.6 -m venv env\_FCP

3. Activate environment and install dependencies:

- source env\_FCP/bin/activate
- pip install -r requirements.txt(.../drag-drop-gui/ABFL Branding/requirements.txt)

4. Launching app

- cd &#39;ABFL Branding/BackEnd&#39;
- python routes\_main.py ( by default the app will launch on port 8013 )

5. Endpoints

- use /flow2code endpoint for Flowchart to Python3 converter.

Ex: localhost:8013/flow2code

- use /smartflow endpoint for Smart FCP.

Ex: localhost:8013/smartflow

**# Directory Structure**

Inside &#39;ABFL Branding/Backend&#39;:

- AI Models:

- finalized\_model.sav: This model is used to classify the instructions into functions.

Ex: If the input is &quot;add all elements in the column points&quot; will be classified as &quot;sum&quot;

- glove.6B.50d.txt: Is the Stanford generated word embeddings.

- admin\_api.py: helper file for routes\_main.py, contains different classes that lead to different results.
- py: This is a helper file for SmartFlow.py this has all the preprocessing and prediction methods required for the NLP classification.
- py: This module is used to convert json received from the front end to graph data.
- py: This module is used to convert the graph data to python3 code. This is the module being used when you are accessing the &#39;/flow2code&#39; endpoint.
- routes\_main.py: This is the main module. This module defines all the endpoints for the API.
- py: used to define the port number of the application
- py: This module is used to parse various gsuit elements using NLP. This is the module being used when you are accessing the &#39;/smartflow&#39; endpoint.
- py: It is a helper module for the FlowData2Code.py and SmartFlow.py module.

Inside &#39;ABFL Branding/Frontend&#39;:

- mxgraph: This directory contains many example projects for the mxgraph library. ( a JS library used for the frontend of the project )
- static: this directory contains all the static files that can be accessed using the API
- html: This is the page that is loaded up when the user accesses the &#39;/flow2code&#39; endpoint.
- html: This is the page that is loaded up when the user accesses the &#39;/smartflow&#39; endpoint.

All generated files are generated in the &#39;ABFL Branding&#39; directory.

&#39;ABFL Branding/gsuitutil&#39; and &#39;ABFL Branding/mailutil&#39; directories contain all modules required for accessing google APIs and mails.

**# Demo Videos**

- Demo video for FCP:

https://drive.google.com/file/d/102fj6df-VdfdT-ExSi7a5FpO\_8rFlu9S/view?usp=sharing

- Demo video for SmartFlow FCP:

https://drive.google.com/file/d/1eWn0ImHzg3WMKHdovcuTpKhh1YxQYigG/view?usp=sharing

**# How to train/retrain the NLP model?**

1. Installing python 3.8.5

- wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
- tar -xvf Python-3.8.5.tgz
- cd Python-3.8.5
- ./configure
- make
- make altinstall

2. Create virtual environment inside the &#39;Training Model&#39; dir

- 8 -m venv env\_Train

3. Activate environment and install dependencies:

- source env\_Train/bin/activate
- pip install -r requirements.txt (.../drag-drop-gui/Training Model/requirements.txt)

4. Put all the training data into the .../Training Model/classes

- With file name as the label and the content of the file as the data points

5. Launch the &#39;training.ipynb&#39; by writing the command jupyter-notebook &#39;training.ipynb&#39; and launching the whole notebook sequentially.

6. The model is saved in the &#39;../Training Model/models&#39;.

**# Demo Video for FCP**

[https://drive.google.com/file/d/102fj6df-VdfdT-ExSi7a5FpO\_8rFlu9S/view?usp=sharing](https://drive.google.com/file/d/102fj6df-VdfdT-ExSi7a5FpO_8rFlu9S/view?usp=sharing)

**# Demo Video for Smart FCP**

[https://drive.google.com/file/d/1eWn0ImHzg3WMKHdovcuTpKhh1YxQYigG/view?usp=sharing](https://drive.google.com/file/d/1eWn0ImHzg3WMKHdovcuTpKhh1YxQYigG/view?usp=sharing)

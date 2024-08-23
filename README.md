# Karbon-SDE-Internship-Hackathon
This challenge involves developing a financial analysis model and creating a web application to utilize it.

## Features
The web application has been built using Streamlit, an open-source framework to rapidly build interactive apps. It uses 3 files:-

1. rules.py -> Financial analysis model uses rules defined in this file.
2. model.py -> uses rules defined in rules.py to output results in json format.
3. data.json -> data file used in rules.

The streamlit app consists of two pages or sections :-

Page 1 - On this page, upload the data file data.json and click on submit.

Page 2 - On this page, view results got from model.py

## Installation

1.Clone the Repo

git clone https://github.com/pranavvb03/Karbon-SDE-Internship-Hackathon.git

2. Install requirements.txt
   
Ensure streamlit is installed

4. Run the streamlit app

Run the command given below in the terminal

streamlit run app.py

## Results
The expected results are to displayed in JSON format, having following fields:-

"flags": {
            "TOTAL_REVENUE_5CR_FLAG": total_revenue_5cr_flag_value,
            "BORROWING_TO_REVENUE_FLAG": borrowing_to_revenue_flag_value,
            "ISCR_FLAG": iscr_flag_value,
        }
        
where each flag belongs to a single class given by color codes as follows,

GREEN = 1
AMBER = 2
RED = 0
MEDIUM_RISK = 3 
WHITE = 4 
        
Link to streamlit application - https://karbon-sde-internship-hackathon-eurss5ktpzxa9wzpivswmp.streamlit.app/

Link to sequence diagram part A - https://drive.google.com/file/d/149I5MxGIc1eM_TYwcGxPAzKmvIxt0i1A/view?usp=sharing

Loom link - https://www.loom.com/share/cd1105aec0b844cca0242af972c7ce11?sid=a5420249-9c44-449f-85c4-f620033e19d2

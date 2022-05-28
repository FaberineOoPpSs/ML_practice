--README--

1. Use 200968186_MiniProject_PHASE_I.ipynb file for EDAs

2. Use 200968186_MiniProject_PHASE_II.ipynb file for ML models and model evaluation

3. main.py contains fastAPI implementation. To run the api follow the steps:
	1. Open the cmd.exe prompt from Anaconda
	2. Change directory to location of the folder in which project is stored
	3. Type uvicorn main:app --reload (as given in line 38 of main.py file)
	4. Copy the http://127.0.0.1:8000 and add '/docs' like this: http://127.0.0.1:8000/docs once 
	   it shows 'Application startup complete.'
	5. select '/moviePred_user_based' and press 'Try it out' and then enter user_id and then 
	   press 'Execute' you will see the predicted movies.
	6. similar process can be done for '/moviePred_item_based' but instead of user_id type movie_name
	   to see the prediction of similar movies
4. frontend.py contains streamlit implementation for ui experience. To run the ui on local host follow the steps:
	1. Run fastAPI on terminal using steps written above.
	2. Open new cmd.exe prompt from Anaconda and change the diretory to the path of file
	3. Type streamlit run frontend.py
	4. And voila the page will load automatically on your default browser.

5. itemRecommender.py(use spyder to view file) file contains recommender function that is used in main.py
	for recommending similar movies w.r.t given movie ml model used is briefly 
	described and analyzed in 200968186_MiniProject_PHASE_II.ipynb file.

6. userRecommender.py(kindly use spyder to view file) file contains recommender function that is used in main.py
	for recommending similar movies w.r.t to similar user preferences the function
	uses model described and analyzedf breifly in 
	200968186_MiniProject_PHASE_II.ipynb file

PROJECT BY 
	Yashaswi Aryan
	200968186
	Batch-IV

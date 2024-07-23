Clinical Research Assistants are solely responsible for the entry of lab results, which are often recorded on books, making way for unwanted errors. We have created a program that can simplify the process of data entry and minimize the room for errors. We can input data manually to the program or upload a scanned PDF, which the program will easily recognise and store in a database. Further, the program will use the data to find the Local Lab Reference Range which can be very useful for further experiments. And, this can be accessed by other labs across the world. They can add their data to this database as well, which will be used by the app to calculate multiple Local Lab Reference Ranges which can all be compiled together. This document will explore the program completely, explaining its functioning.

![image](https://github.com/Christian74D/Lab-ranges/assets/112863270/a67d6d8a-d8f6-4f72-bed7-e5c37206a578)


Methodology:

	The Model involves getting Lab test records either as Manual Entry or by PDF Upload from the user.
	The uploaded PDF is converted into a CSV File using an AI Model
which gets converted to a Pandas Dataframe.Similarly, the Manual Entry done by the user in table form from the interface is also converted into a 
Pandas Dataframe.
	The Dataframe is uploaded into a FireBase database where records from Laboratories across the world can be stored and accessed simultaneously.
	To analyze the ranges , data is retrieved and Local Ranges is calculated separately for each lab.Entire Global Ranges of Test record parameters is also calculated for all labs after removing outliers using IQR 


![image](https://github.com/Christian74D/Lab-ranges/assets/112863270/05b61e6a-071e-4b5d-a567-414e074aa7cc)


Refer Redifining Precision.docx for detailed documentation


List of Files
app.py
db_manager.py
helper_functions.py
range.calculator.py
keys.py
README.md
<firebase.json>




Dependencies 
PIL
pdf2image
pytesseract
pandas
seaborn
matplotlib.pyplot
firebase_admin
gradio
Pathlib
openai



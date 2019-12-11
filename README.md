# FINAL project

This is the final project of the course. I used Django to develop it, and it allows me to draw the Electroencephalograms of different patients that are in my database. You can choose between a healthy and a sick patient, with Alzheimer Disease. Also, you can pick the trial of the patient you want to see, and the number of channels of the EEG that you want. Each channel represent one electrode placed in the scalp. In this database, we used 16 electrodes.

The views page have all the functions used to extract the data from the database, and send it to the html files to use them, as well as allowing javascript to use this data.

In the templates we can find this:
*base.html: which is the page that have information that will be available in all the other pages
*patients.html: Webpage where you can choose the patient you want to see. Each one has different states (sick or healthy)
*trial.html: Page to choose the trial and the features you want to see.

In models.py you can find the models created in the database, and in import.py you can find the code for importing data in the database.
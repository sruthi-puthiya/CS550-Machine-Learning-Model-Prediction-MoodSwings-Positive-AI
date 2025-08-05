# CS550-Machine-Learning-Model-Prediction-MoodSwings-Positive-AI
The vision is to empower people across the world by providing a tool that can identify symptoms through conversations and guide them immediately towards the proper professional help by alerting the medical providers. 


About Dataset
This dataset is collected from Keggle.com, it has a usability score of 10. And dataset seems to cover a wide range of linguistic, psychological, and behavioral attributes, potentially suitable for analyzing mental health-related topics in online communities or text data. With a wide range of features, including sentiment analysis scores and psychological indicators, the dataset offers opportunities for developing predictive models to identify or predict mental health outcomes based on textual data. This can be useful for early intervention and support.
Brief description of each column:
•	Timestamp: The date and time when the respondent submitted the survey.
•	Gender: The respondent’s gender identity.
•	Country: The country where the respondent resides.
•	Occupation: The respondent’s job role or profession.
•	self_employed: Indicates if the respondent is self-employed (Yes/No).
•	family_history: Whether the respondent has a family history of mental illness (Yes/No).
•	past_treatment: Whether the respondent has ever sought treatment for a mental health condition (Yes/No)
•	Days_Indoors: How many days the respondent stayed indoors recently, possibly due to external stressors.
•	Growing_Stress: Indicates if the respondent feels their stress levels are increasing.
•	Changes_Habits: Reports any noticeable changes in habits or routines.
•	Mental_Health_History: Indicates if the respondent has a past diagnosis or history of mental health issues.
•	Mental_Disorder: Whether the respondent experiences sudden or frequent mood changes.
•	Coping_Struggles: Whether the respondent struggles to cope with everyday stress or pressure.
•	Work_Interest: Level of interest or engagement the respondent has in their work.
•	Social_Weakness: Difficulty in maintaining or engaging in social interactions.
•	mental_health_consultation_before: Whether the respondent interested to take a evaluation on the same.
•	care_options: Awareness of available mental health care resources or options.
•	Target: Mental_Disorder
•	Multi-class classification, class= Medium, Low, High
•	 Features: ['Gender', 'Country', 'Occupation', 'self_employed', 'family_history',
       'past_treatment', 'Days_Indoors', 'Growing_Stress', 'Changes_Habits',
       'Mental_Health_History', 'Coping_Struggles', 'Work_Interest',
       'Social_Weakness', 'mental_health_interview', 'care_options']
•	Total of 292364 data is available
•	Shape : (292364, 17)
•	Duplicates: 1487 (Removed)
•	Null values : 5167 – handle later
•	Data type is int64 for one column and others are Objects
•	Timestamp is not useful to build the model - drop column timestamp



Project Environment setup:
•	Programming Language: Python 3.13.5
•	IDE: Visual Studio Code (VS Code)
•	Operating System: Windows 11 Pro
•	Processor: 12th Gen Intel® Core™ i5-1235U @ 1.30 GHz
•	Python Libraries : scikit-learn (sklearn), pandas, numpy, matplotlib, seaborn



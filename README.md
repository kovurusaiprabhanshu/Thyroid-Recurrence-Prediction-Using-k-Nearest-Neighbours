# Thyroid Reccurence Prediction Using k-Nearest Neighbours 
Performing **kNN analysis** of Thyroid patient dataset, and exploring what **algorithms**, **hyperparameters** and **metrics** are optimal for predicting reccurence of Thyroid Cancer.

## Description
Using concepts of **k-Nearest-Neighbors** to predict Thyroid Cancer Recurrence. We shall use **KD-Tree**, **Ball-Tree** and **Brute Force** algortithms for indexing. Various **distance metrics** are also explored. **Hyperparameters** are tuned. 

## Techniques Used

- **Machine Learning Modeling**: The abstraction of the Supervised Learning paradigm implemented. Collected data, in the form of a CSV, is loaded into the model. 
- **Data Visualization**: Representation of complex data into a simpler, visual format (such as graphs).   
- **Data Preprocessing**: Filtering and transforming raw data into a consistent, usable format.  
- **Performance Evaluation**: Appraisal of model through various metrics to evaluate the effectiveness and usefulness of the model. 

## Algorithms used 

#### KD-Tree Algorithm  
- Sophisticated data structure for indexing
-  Partitions the data space using hyperplanes that are perpendicular to the coordinate axes, creating a binary tree structure
#### Ball-Tree Algorithm
- Sophisticated data structure for spatial indexing
- The structure is constructed as a binary tree, where each non-leaf node represents a hypersphere containing a subset of the data, and each leaf node corresponds to a small subset of points
#### Brute Force
-  The most naive neighbor search implementation
-  Efficient brute-force neighbors searches can be very competitive for small data samples

## Evaluation Metrics

### Accuracy
**Accuracy** is a fundamental metric used for evaluating the performance of a classification model. It tells us the proportion of correct predictions made by the model out of all predictions.

*`Accuracy = No. of Correct Predictions/Total No. of Predictions`*

## Precison 
**Precision** measures how many of the positive predictions made by the model are actually correct. It's useful when the cost of false positives is high such as in medical diagnoses where predicting a disease when it’s not present can have serious consequences.

*`Precision = TP/(TP+FP)`* 

## Sensitivity (Recall) 
**Sensitivity** measures how many of the actual positive cases were correctly identified by the model. It is important when missing a positive case (false negative) is more costly than false positives

*`Sensitivity (Recall) = TP/(TP+FN)`*

## F-1 Score
**F-1 Score** is the harmonic mean of precision and recall. It is useful when we need a balance between precision and recall as it combines both into a single number. 

## Use Cases 
*  **Prediction of new reccurences of Thyriod Cancer cases**: The model is capable of predicting trends of reccurences and risks on an individual basis. 
* **National Health Evaluation**: Gives insights into the condition of the state's medical infrastructre. 
* **Template**: Acts as a primary template for medical forecasting, and a powerful tool for medical analytics.  

## Workflow 
1. **Data Loading and Preparation**
*  Load `Thyroid_Diff.csv`
*  Format the data 
2. **Data Preprocessing and Visualization**
* Create a new dataframes as per requirement  
* Plot the data on a graph for interpretation
* Split the data for testing and training
3. **Model Training** 
* Using aforementioned algorithms and paradigms, fit the training data into each model of kNN
4. **Evaluation** 
* Calculate Accuracy for each model
* Compute F-1 Score for each model
* Calculate Precision, Sensitivity and Specificity through Confusion Matrix
* Evaluate the performance for each model

## Project Components
| Component| Feature | Description| 
| ------------- | ------ | ------|
| Dataset  | `Thyroid_Diff.csv` | Contains all data. Downloaded from Kaggle.com
| Environment| `Thyroid_Reccurence_Prediction.ipynb` | Jupyter Lab Notebook with workflow
| Documentation   | `Readme.md`| Overview of the project and additional information

## Libraries and Technologies Used
*  Python 3 (Programming Language) 
*  Jupyter Notebook (Environment) 
*  Pandas (Data Frames) 
*  Numpy (Data Preprocessing) 
*  Scipy (Scientific Calculations) 
*  Matplotlib (Data Visualization) 
*  Scikit-Learn (Data Preprocessing and ML model designing) 

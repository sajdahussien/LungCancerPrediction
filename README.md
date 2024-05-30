Investigating the Role of miRNA Editing in Lung Adenocarcinoma Classification using Machine Learning Models


This project explores the role of microRNA (miRNA) editing in classifying lung adenocarcinoma using machine learning models. The dataset comprises miRNA expressions across 38 samples, with 19 samples from individuals diagnosed with lung adenocarcinoma and 19 samples from healthy controls.

Key Steps:

Exploratory Data Analysis (EDA) and Preprocessing: Conducted EDA to understand the dataset and preprocessing to handle missing values, remove duplicates, and scale features.

Machine Learning Model Development: Utilized various machine learning algorithms including XGBoost, K-Nearest Neighbors (KNN), Random Forest (RF), Support Vector Machine (SVM), Logistic Regression, Gradient Boosting, and Decision Tree to develop predictive models for lung adenocarcinoma classification.

Model Fine-Tuning: Fine-tuned the Random Forest (RF) algorithm to optimize its performance using techniques such as GridSearch.

Model Deployment: Deployed the best-performing model using Streamlit, providing an interactive platform for real-time lung adenocarcinoma classification.

Results:

The Random Forest (RF) algorithm achieved the highest accuracy of 97% when deployed on selected features.
Hyperparameter tuning did not lead to further improvements in RF model accuracy.

Limitations:

The limited number of samples (19 lung adenocarcinoma and 19 healthy controls) may restrict the generalizability of the findings.
Risk of overfitting due to the small sample size.
Future Directions
Incorporate larger and more diverse datasets to validate the robustness of the developed models.
Explore additional features and data sources to enhance predictive performance.
Investigate advanced machine learning techniques for handling imbalanced datasets and improving model interpretability.

Contributors:

Sajda Hussien 

License:

This project is licensed under the MIT License - see the LICENSE file for details. As a student at college, you are encouraged to modify and use the code for educational purposes.







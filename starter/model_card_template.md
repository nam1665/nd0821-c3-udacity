# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a model that utilizes a Random Forest Classifier to determine whether a person's salary is greater than 50k or not. The following features are used for this determination:

* age
* workclass
* fnlgt
* education
* education-num
* marital-status
* occupation
* relationship
* race
* sex
* capital-gain
* capital-loss
* hours-per-week
* native-country

## Intended Use
This model is designed to classify an employee's salary as either <=50K or >50K based on their information. Users can input their employee information in the predefined format and receive a salary prediction based on the model's classification.

## Training Data
The data and related information (primary use, etc.) can be found [here](https://archive.ics.uci.edu/ml/datasets/census+income)


## Evaluation Data
The initial dataset undergoes preprocessing before being divided into training and evaluation data sets. The evaluation data set comprises 20% of the total data.


## Metrics
Here we selected the following metrics to measure the accuracy of the model:
* **Precision**:  0.74 
* **Recall**:  0.63
* **Fbeta**:  0.68

## Ethical Considerations
* Relying on features such as sex, ethnicity and race: While these features may be meaningful, they may not be the most effective for accurately determining an individual's salary. For example, if a hiring manager uses this model to decide whether to offer a salary above or below 50k for a job, relying on these features could result in bias towards minorities, who have historically earned less money.

## Caveats and Recommendations
This model was trained on data primarily consisting of people from the United States. Therefore, it is not advisable to use this model to predict salary types for individuals from other regions of the world, as these regions may have significantly different feature distributions.

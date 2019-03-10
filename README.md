This is an implementation of the random forest algorithm. The purpose of this project is an excercise to help me to develop my python programming skills.
The goal is to develop an object oriented implementation of the random forest algorithm with permuation importance using numpy as the only dependency.
I also aim to use Numba to accelerate the code and compile it for GPU as an interesting experiment.

**Background**
The initial plan for this project was to first write a decision tree class, then create a random forest class that instantiates a number of decision tree objects and estimates using some methods.
My thinking looked something like this 

class decision_tree:

  with methods:
  
  __init__(self, input_dataframe)
  
  train(self)
  
  predict(self)

class random_forest:

  with methods:

  __init__(self,input_dataframe)

  create_dataframe_with_random_column_subset_and_bagged_samples(self)
  
  train_forest(self)
  
  combine_predictions(self)

However, before beginning to write the code for this project I began to contribute to scikit-learn and began to read the code base and realised that scikit learn uses an estimator class as a base class. My goal as a programmer is to be good enough to write scikit-learn, so it makes sense for me to base my work on the architecture of scikit-learn. In order to mimic the experience of implementing a novel algorithm I will base my architecture of the other scikit-learn predictors (e.g. SVM).

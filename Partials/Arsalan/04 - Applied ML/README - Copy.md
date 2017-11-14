## Question 2: Applied ML

We are going to build a classifier of news to directly assign them to 20 news categories. Note that the pipeline 
that you will build in this exercise could be of great help during your project if you plan to work with text!

[TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), short for term frequency–inverse document frequency, 
is of great help when if comes to compute textual features. Indeed, it gives more importance to terms that are 
more specific to the considered articles (TF) but reduces the importance of terms that are very frequent in 
the entire corpus (IDF). 

Compute TF-IDF features for every article using 
[TfidfVectorizer](
http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). 
Then, split your dataset into a training, a testing and a validation set (10% for validation and 10% for testing). 
Each observation should be paired with its corresponding label (the article category).


2. Train a random forest on your training set. Try to fine-tune the parameters of your predictor on your 
validation set using a simple grid search on the number of estimator "n_estimators" and the max depth of the 
trees "max_depth". Then, display a confusion matrix of your classification pipeline. Lastly, once you assessed 
your model, inspect the `feature_importances_` attribute of your random forest and discuss the obtained results.



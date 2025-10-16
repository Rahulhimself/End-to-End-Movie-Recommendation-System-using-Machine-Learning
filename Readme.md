# Movie Recommendation System Using Machine learning

<img src="images\main image.jpg" alt="Movie Recommendation System main poster" width="800" height="400">

###
Recommendation systems have become an indispensable necessity in our intensely busy, modern world. Given the overwhelming volume of choices and the constant constraint of limited time, these systems are vital tools that conserve a user's valuable cognitive resources by eliminating the need for exhaustive searching and decision-making.

At its core, a recommendation system is an Artificial Intelligence-based algorithm designed to personalize discovery. It achieves this by performing predictive modeling and applying sophisticated heuristics to vast datasets. The system actively analyzes numerous factors, including an individual's historical behavior (browsing/search history), their user profile, and the behavior patterns of demographically or behaviorally similar users ("collaborative filtering"). By synthesizing this information, the system efficiently skims through all possible content options to generate a highly customized and relevant list of items, effectively bridging the gap between a user's desire for specific content and the noise of the global catalog.
###

<hr>

## About the Project

### Discover similar films instantly! This Streamlit app provides personalized movie recommendations. ###
## Check live demo of the application ##

<a href="https://rb-movie-recommendation-system-using-machine-learning.streamlit.app/">RB_streamlit_app_demo</a>
<hr>
<img src="images\image1.png" alt="Movie Recommendation System main poster" width="600" height="300">
<hr>
<img src="images\image2.PNG" alt="Movie Recommendation System main poster" width="600" height="300">
<hr>

## Dataset used ##

<a href="https://www.kaggle.com/datasets/sakshisemalti/movies-dataset-with-posters">Dataset</a>
<hr>

## Concept used to build the model.pkl file : cosine_similarity ##

###
1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : <a href="https://www.learndatasci.com/glossary/cosine-similarity/">Click here</a>

### 
<hr>

## How to run ##

### follow the steps ###

### clone the repository ###

```bash
https://github.com/Rahulhimself/End-to-End-Movie-Recommendation-System-using-Machine-Learning
```
### STEP 01- Create a conda environment after opening the repository ###

```bash
conda create -n movie python=3.7.10 -y
```
```bash
conda activate movie
```
### STEP 02- install the requirements ###

```bash
pip install -r requirements.txt
```

```bash
#run this file to generate the models

MR_test.ipynb
```
### run with this ###
```bash
streamlit run app.py
```

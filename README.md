# Cat-REST
## Table of Contents
- [About] (#about)
- [Motivations] (#motivations)
  - [Why CatBoost?] (#why-cat-boost)
  - [Why Flask-CORS?] (#why-flask-cors)
  - [Why Meyer's Reset] (#why-meyers-reset)
## About
This is a small project which I started to teach myself a bit more about REST APIs and deploying machine learning models outside of CLI interfaces. I've been working through The Odin Project and decided to make a front-end for the API as a replacement for the sign-up form project suggested.

## Motivations
### Why CatBoost?
I mostly chose CatBoost because I wanted a model for API testing purposes. CatBoost models can be trained very quickly and require minimal data preprocessing compared to LightGBM and XGBoost. Although CatBoost was only chosen for speed in this project, gradient boosted decision trees can yield good predictions for tabular data when combined with carefully considered EDA and data preprocessing.
### Why Flask-CORS?
I had no problems using curl to test the API but I quickly learned about same-origin policy when I tried to make an AJAX request from the browser. Flask-CORS is a simple to use Flask extension to enable cross-origin AJAX.
### Why Meyer's Reset?
I had issues trying to position the black main div box because browser default margins. A CSS reset seemed to be best way to unspecified prevent browser-default behaviours.
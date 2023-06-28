
assessment1
==============================
**ADSI- ASSESSMENT-1_ SHIVANI NANDKISHOR NIPANE**



**NBA LONGETIVTITY DATASET**

The NBA dataset used in this project consists of player statistics and career information for NBA rookies. The dataset includes 21 columns, with features such as games played, minutes played, points per game, field goals made/attempts, three-pointers made/attempts, free throws made/attempts, rebounds, assists, steals, blocks, turnovers, and more. The target variable, "TARGET_5Yrs," indicates whether a rookie player lasted at least 5 years in the NBA.

The goal of the project is to build a predictive model that can anticipate a rookie player's career longevity based on their stats. The project involves data cleaning, exploratory data analysis, feature engineering, and model training using different algorithms, including XGBoost, LightGBM, and Logistic Regression. Hyperparameter tuning is performed for each model to optimize their performance, evaluated using the AUROC (Area Under ROC) metric.

The results indicate that the Logistic Regression model achieved the highest AUROC score after hyperparameter tuning. However, it's important to consider other factors such as model interpretability and computational efficiency when selecting the best model.

Overall, this project aims to provide insights into the relationship between rookie player statistics and their career longevity, which can be valuable for NBA teams and decision-makers in player recruitment, development, and long-term planning.

**RUNNING ENVIROMENT:**

**Replace the main folder adsi_24622969 to adsi while running the zip folder**

->Install packages with pipenv
pipenv install pandas==2.0.1
pipenv install jupyterlab==3.6.3
pipenv install scikit-learn==1.2.2
pipenv install yellowbrick==1.5
pipenv install seaborn
pipenv install xgboost
pipenv install lightgbm

-> pipenv run pip freeze >> requirements.txt

**SET PYTHONPATH**

echo PYTHONPATH="/Users/adsi/assessment1".env

**Launch Jupyter Lab from your virtual environment**

pipenv run jupyter lab

Project Organization
---------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

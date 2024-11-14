# SpaceX Rocket Landing Success Analysis

## Explore
- How payload mass, launch site, number of flights, and orbits affect first-stage landing success
- Rate of successful landings over time
- Best predictive model for successful landing (binary classification)

## Executive Summary
This research aims to identify the factors contributing to a successful rocket landing. To achieve this, the following methodologies were applied:

1. **Data Collection**: Gathered data using SpaceX REST API and web scraping techniques.
2. **Data Wrangling**: Created success/fail outcome variable.
3. **Data Exploration**: Visualized data based on payload, launch site, flight count, and yearly trends.
4. **Data Analysis**: Calculated statistics such as total payload, payload range for successful launches, and total number of successful vs. failed outcomes.
5. **Launch Site Analysis**: Explored launch site success rates and proximity to geographical markers.
6. **Visualization**: Displayed the launch sites with the most success and identified successful payload ranges.
7. **Predictive Modeling**: Used logistic regression, SVM, decision tree, and K-nearest neighbor models to predict landing outcomes.

## Results
### Exploratory Data Analysis
- **Launch Success**: The success rate of launches has improved over time.
- **Top Site**: KSC LC-39A shows the highest success rate among landing sites.
- **Orbit Success**: Orbits ES-L1, GEO, HEO, and SSO have a 100% success rate.

### Visualization / Analytics
- **Launch Sites**: Most are located near the equator and close to coastlines.

### Predictive Analytics
- All models performed similarly on the test set, with the decision tree model slightly outperforming others on `.best_score_`.

## Methodology
### Data Collection - API
- **API Requests**: Fetched rocket launch data from the SpaceX API.
- **Data Parsing**: Used `.json()` and `.json_normalize()` to decode API response and convert it into a DataFrame.
- **Launch Data Filtering**: Filtered to include only Falcon 9 launches.
- **Data Cleaning**: Replaced missing Payload Mass values with the calculated `.mean()`.
- **Data Export**: Saved the cleaned data to a CSV file.

### Data Collection - Web Scraping
- **Request Data**: Retrieved Falcon 9 launch data from Wikipedia.
- **Data Parsing**: Used BeautifulSoup to parse HTML tables and extract data.
- **Data Structuring**: Created a DataFrame and exported it to a CSV file.

### Data Wrangling
- Converted landing outcomes to binary: `1` for success and `0` for failure.

### Exploratory Data Analysis (EDA) with Visualization
- Created charts to visualize relationships and comparisons between variables.

### SQL-Based EDA
- Queried data to gain insights into payload ranges and launch outcomes.

### Mapping with Folium
- Created maps to visualize launch sites, outcomes, and distances to proximities.

### Dashboard with Plotly Dash
- Built an interactive dashboard:
  - **Pie Chart**: Shows successful launch rate.
  - **Scatter Chart**: Shows Payload Mass vs. Success Rate by Booster Version.

### Predictive Analytics
- **Data Preparation**: Created a NumPy array from the Class column, standardized the data with `StandardScaler`, and split it using `train_test_split`.
- **Model Tuning**: Used `GridSearchCV` with `cv=10` for parameter optimization.
- **Model Evaluation**: Applied `GridSearchCV` on logistic regression, SVM, decision tree, and KNN models. Evaluated model accuracy with `.score()` and confusion matrices.
- **Best Model Identification**: Compared models using `Jaccard_Score`, `F1_Score`, and accuracy metrics.

---

This project provides a comprehensive analysis of factors influencing rocket landing success and explores predictive models to improve future landings.

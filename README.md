# TZ-Gaming-Optimal-Targeting-of-Mobile-Ads

### Project Description:
In this detailed project, I undertook the task of improving mobile advertisement targeting for TZ Gaming, a mobile game development company. The goal was to leverage data science techniques to optimize ad targeting strategies through the Vneta ad-network, enhancing customer acquisition and retention. My responsibilities included analyzing provided data, estimating logistic regression models, and evaluating the performance of different targeting strategies.

### Technology Stack:
- **Data Analysis and Modeling:** Python, pandas, pyrsm, Matplotlib
- **Statistical and Machine Learning Techniques:** Logistic Regression
- **Data Visualization:** Matplotlib, seaborn
- **Version Control:** Git for source code management

### Key Accomplishments:

#### Data Analysis and Preprocessing:
- **Data Loading and Filtering:** Loaded the dataset from a parquet file and segmented it into training and test sets to ensure a robust evaluation of the models.
- **Exploratory Data Analysis:** Performed initial analysis to understand the distribution and relationship of features within the data.

#### Model Development and Evaluation:
- **Logistic Regression Modeling:** Developed multiple logistic regression models to predict the probability of ad clicks (`click`) using various features such as app type, mobile OS, and user behavior metrics.
- **Statistical Testing and Evaluation:** Utilized Chi-square tests and Pseudo R-squared values to assess the models' goodness of fit and explanatory power.
- **Importance and Prediction Analysis:** Analyzed the importance of different features using permutation importance and evaluated the predictive performance using prediction plots.

#### Strategic Analysis for Ad Targeting:
- **Decile Analysis:** Implemented decile analysis to categorize users based on the predicted probability of clicking on an ad, which helps in focusing efforts on the most promising user segments.
- **Gains and Lift Analysis:** Created gains and lift charts to visualize the effectiveness of the logistic regression model in comparison to random targeting.
- **Cost-Benefit Analysis:** Conducted a detailed cost-benefit analysis to compare different ad targeting strategies, assessing their potential profitability and return on marketing expenditure (ROME).

#### Predictive Performance and Recommendations:
- **Model Comparison:** Compared the performance of different models including a random baseline, logistic regression, and Vneta's proprietary model, using metrics such as accuracy and ROME.
- **Profitability Analysis:** Calculated expected profits and ROME for various scenarios, providing actionable insights on which ad targeting strategy would be most beneficial for TZ Gaming in terms of profitability and cost-efficiency.

### Key Outcomes:
- **Enhanced Targeting Efficiency:** The logistic regression model provided a significant improvement in targeting efficiency, leading to higher click-through rates and better allocation of advertising budget.
- **Increased ROI:** Demonstrated through detailed financial analysis that targeted advertising using predictive modeling significantly increases the return on investment compared to random targeting.
- **Strategic Business Recommendations:** Based on the analysis, recommended the adoption of sophisticated data-driven targeting strategies over traditional methods or the existing random targeting approach, highlighting the benefits in terms of increased user engagement and profitability.

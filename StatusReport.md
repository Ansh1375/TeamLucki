Our project aims to analyze the relationship between crime rates and socioeconomic factors such as income and poverty across Chicago community areas from 2020 to 2024. So far, we have completed data acquisition, data quality assessment, data cleaning and integration process, and visualization.

Week 1:
We created our GitHub repository and collected our two datasets, the Chicago Crime Dataset from the Chicago Data Portal, and various datasets from the United States Census Bureau. However, we found it difficult to connect the two datasets and changed our source from the United States Census Bureau to the Chicago Health Atlas, which had better information on income and poverty rates in the City of Chicago.

Week 2:
We assessed the quality of the data, using Python to look for missing values and potential duplicate entries in the data. We identified missing values in various columns and dropped the necessary rows. Some columns that were not important had missing values, so we decided not to drop these. We also dropped duplicate rows to make sure the data is clean and our analysis is accurate. While assessing the quality of the data, we made sure that the datasets were compatible.

Week 3:
We merged the datasets using the community_id variable. The merge was not successful initially because there were null values after the merge. To fix this, we had to standardize the data types before the merge. After this, the merge was successful, and we made sure to check the merged dataset for missing values or duplicated rows.

Week 4:
We used Python to visualize the merged dataset in various ways. We compared crime counts against median household income and poverty rate using scatterplots. We also looked at which communities had the highest crime counts and looked at crime counts across different income groups. Finally, we looked at how the different crime types were composed across the ten communities with the highest crime rates.

Week 5: 
We have not started yet; however, we are going to get started on workflow automation and reproducibility, making sure the project is reproducible and everything is easy and clear to follow. We are also going to work on analyzing the data and understanding what we can learn from it.

Week 6:
The final report will be worked on once every other step is completed.

Updated Timeline:
Week 1 (Data Acquisition): Completed
Week 2 (Data Quality Assessment): Completed
Week 3 (Data Cleaning & Integration): Completed
Week 4 (Data Visualization): Completed
Week 5 (Data Analysis & Workflow Automation/Reproducibility): In Progress
Week 6 (Final Report): Not Started

Changes:
We have made a few changes to our project as we have been working on it. We switched one data source from the United States Census Bureau to the Chicago Health Atlas. We also switched our time frame from 2000 to 2024 to 2020 to 2024, as we believe it better reflects the current relationship between socioeconomic factors and crime rates in Chicago. We also decided to focus more on income and poverty, rather than other socioeconomic factors. After our initial plan was uploaded, it was recommended that we describe the variables better and think about time x geography matching. I will describe the variables below. In terms of time x geography matching, it is difficult to combine the two as demographic data is taken per year and crime data is taken when it is reported/occured. The datasets are integrated on the geographic identifier and we have to assume that socioeconomic conditions are relatively stable over the time period we are using.

Data Description:
Date: When the crime occurred
Primary Type: Category of crime
Block: location Description
community_id: Geographic identifier
INC_2020-2024: Median household income
POV_2020-2024: Poverty rate (%)
community_id: Geographic identifier

Challenges and Solutions:
    Missing community_id:
        Some crime records were not linked to any community, so we dropped those rows as they could not be used in the analysis.
    Large number of merge mismatches:
        There were null values after we merged the datasets, and this was because community_id was stored as a float in one dataset and an int in another. To fix this, we standardized the data types and reran the merge.
    Duplicate records:
        There were duplicate crime entries, which inflated crime counts. We removed these rows using key identifying columns to clean the data and make sure it is accurate.
    Misleading null values:
        Location had a high null count. We deemed this irrelevant to the analysis and decided to remove the column.
    Large dataset:
        The dataset from the Chicago Data Portal was extremely large, making it impossible to upload to git. This is a problem that we are unsure of how to fix at this moment, but we will work on fixing it as soon as possible.

Individual Contributions:
Maksim Mihajlovic:
I was responsible for assessing the quality of both datasets and ensuring they were suitable for analysis. I conducted detailed data quality checks, including identifying and evaluating missing values, duplicate records, and inconsistencies in key variables. Then, I cleaned the datasets by removing rows with missing community identifiers, eliminating duplicate crime records based on key attributes, and addressing formatting issues, including inconsistent data types.

I also played a key role in debugging and improving the dataset integration process. After the initial merge, I identified mismatches caused by differences in the formatting of the community_id field and resolved them by standardizing data types across both datasets. I also verified the integrity of the merged dataset by confirming that income and poverty rate were correctly aligned with the crime data and contained no missing values.

Overall, my contributions focused on ensuring the data was accurate, consistent, and fully prepared for reliable analysis in the next stages of the project.
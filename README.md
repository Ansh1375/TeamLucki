# TeamLucki
Chicago Crime and Poverty: A Data-Driven Analysis of Community Area Trends

Contributors:
    Maksim Mihajlovic
    Ansh Bera

Summary:
The motivation for this project comes from the lasting question of the relationship between socioeconomic factors and public safety. While it is commonly believed that poverty drives crime, this project seeks to quantify the relationship within the city of Chicago. Our primary research question asks, to what extent does the poverty rate of a community area in Chicago correlate to its total reported crime count between 2020 and 2024? We chose Chicago because not only is it our home city, but it is also a large and diverse city that has historically been known to have a higher crime rate. It also contains many unique districts with their own demographics and cultures. By focusing on the period between 2020 and 2024, we are analyzing an important shift in urban history. This timeframe captures the immediate and long-term societal shifts following the COVID-19 pandemic, a time period where many cities across the country reported higher crime rates and economic stress. The world changed heavily due to COVID-19, and by using this time period, we can more accurately represent the current state of the world.

To answer this, we developed a data pipeline that integrates two distinct datasets: the City of Chicago's reported crime incidents and a socioeconomic dataset from Chicago containing income and poverty indicators. This project used a programmatic approach to data integration, ensuring that raw incident-level data could be accurately collected by community ID and merged with socioeconomic indicators. While these datasets contain vast amounts of information, they were not ready to be analyzed without any work being done on them. The crime dataset contains millions of rows and dozens of columns, with each row representing an individual incident with a time stamp and coordinate. Some of these rows were duplicates, and we had to ensure that the data was clean prior to working with it. In contrast, the socioeconomic dataset is aggregated by community area. This meant we had to bind the datasets despite the different specificities. We had to group the crime dataset by community_id to generate a crime count for each neighborhood. This data was then merged with the socioeconomic dataset, which contained the poverty rate and median income. We then had to clean the data by handling missing values and data type inconsistencies to ensure its accuracy. Finally, we automated this process by creating a run-all script. This script manages the execution flow and cleans and merges the data before visualization.

Our findings indicate a slight, but not statistically significant, positive correlation between poverty rates and crime density. The project successfully automated the transition from data acquisition to a final visualization, proving that the analysis can be repeated as new data comes to fray. By providing this framework, we hope to contribute a tool that allows for ongoing analysis into this question, and we hope to move the conversation from subjective evidence to data-driven insights.

Reproducing:
To reproduce this analysis, follow the steps below.
1. Prerequisites
    Ensure you have Python 3.12.2 or later and the pip package manager installed on your system
2. Environment Setup
    Install the necessary software dependencies using the provided requirements.txt and/or environment_dump.txt files. You can run pip install -r requirements.txt.
3. Data Acquisition
    Ensure that the crime.csv (Incident-level data from the Chicago Data Portal) and ses_data.csv (Socioeconomic indicators data from the Chicago Health Atlas).
    Note: The crime.csv file is very large, so install it from the provided Box link.
4. Execute the Workflow
    The entire analysis is executed via a single run_all.py script
5. Verification
    Upon successful completion, the script will output the crime_with_ses.csv and poverty_correlation.png artifacts into the project folder.
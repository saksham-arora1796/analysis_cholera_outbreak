Python Code

#Importing all Libraries and Dependencies
import pandas as pd  
import os 
import matplotlib.pyplot as plt
import re
import numpy as np

#Setting the Work Directory
os.getcwd()
os.chdir('E:/GMU SEM 2/AIT 580/AIT - 580 - Final Data Analysis Project - Saksham Arora - G01157124')
os.getcwd()

#Reading the file using Pandas in Python
dataframe = pd.read_csv("CholeraOutbreak.csv")
print(dataframe)

#Showing Data with columns having Null Values
print("\nShowing Total Number of null values in each column : ")
print(dataframe.isnull().sum())

#Dealing with Nulll values in the dataset
dataframe.fillna(0, inplace=True)
print(dataframe)
print(dataframe.dtypes)

#Conversion of String(Default) columns to Numeric Colums for Analysis
dataframe["Date"] = pd.to_datetime(dataframe["Date"], errors='coerce')

dataframe["Cases"] = pd.to_numeric(dataframe["Cases"], errors='coerce')
dataframe["Cases"] = dataframe["Cases"].fillna(dataframe["Cases"].mean()).astype(np.int64)

dataframe["Deaths"] = pd.to_numeric(dataframe["Deaths"], errors='coerce')
dataframe["Deaths"] = dataframe["Deaths"].fillna(dataframe["Deaths"].mean()).astype(np.int64)

dataframe["CFR (%)"] = pd.to_numeric(dataframe["CFR (%)"], errors='coerce')
dataframe["CFR (%)"] = dataframe["CFR (%)"].fillna(dataframe["CFR (%)"].mean())

dataframe["Attack Rate (per 1000)"] = pd.to_numeric(dataframe["Attack Rate (per 1000)"], errors='coerce')
dataframe["Attack Rate (per 1000)"] = dataframe["Attack Rate (per 1000)"].fillna(dataframe["Attack Rate (per 1000)"].mean())

#dataframe["COD Gov Pcode"] = pd.to_numeric(dataframe["COD Gov Pcode"], errors='coerce')
print("Mean = ",dataframe["COD Gov Pcode"].mean())
dataframe["COD Gov Pcode"] = dataframe["COD Gov Pcode"]
dataframe["COD Gov Pcode"] = dataframe["COD Gov Pcode"].replace(0,dataframe["COD Gov Pcode"].mean()).astype(np.int64)

#Checking the Null value status again after dealing with Null Values
print("\nValues of the columns after replacing the null values with the mean value for each column : ")
print(dataframe.isnull().sum())
print(dataframe.dtypes)
print(dataframe)


#Statistical Summary
print("Statistic Summary for the Dataset - Yemen Cholera Epidemiology : ")
print(dataframe.describe())

dataframe.to_csv('AIT-580-FinalProject.csv', index=False, encoding='utf-8')

#Plot 1 : Governorate VS Deaths
plt.scatter(dataframe['Deaths'],dataframe['CFR (%)'], color='red', marker='.')
plt.title('Plot 1: CFR (%) Versus Death ', color='black')
plt.xlabel('Deaths due to Cholera', color='black')
plt.xticks(rotation=45)
plt.ylabel('CFR (%)', color='black')
plt.show()

#Plot 2 : Governorate VS Cases
plt.scatter(dataframe['Cases'],dataframe['CFR (%)'], color='blue', marker='.')
plt.title('Plot 2: CFR (%) Versus Cases ', color='black')
plt.xlabel('Cases of Cholera', color='black')
plt.ylabel('CFR (%)', color='black')
plt.show()

R and R Studio

#Setting Work Directory
setwd("~/Documents/AIT 580/AIT - 580 - Final Data Analysis Project - Saksham Arora - G01157124 ")

#Reading the file into R
library(readr)
AIT_580_FinalProject <- read_csv("AIT-580-FinalProject.csv")

#Regression Model - 1 
model1 <- lm(AIT_580_FinalProject$`Attack Rate (per 1000)`~Cases + Deaths, data = AIT_580_FinalProject)
summary(model1)
layout(matrix(c(1,2,3,4),2,2))
plot(model1)


#Regression Model - 2 
model2 <- lm(AIT_580_FinalProject$`CFR (%)`~Cases + Deaths, data = AIT_580_FinalProject)
layout(matrix(c(1,2,3,4),2,2))
plot(model2)


#Correaltion between Cases and Deaths
cor(AIT_580_FinalProject$Cases,AIT_580_FinalProject$Deaths, method = 'spearman')

#Correaltion between Cases and Attack Rate (per 1000)
cor(AIT_580_FinalProject$Cases,AIT_580_FinalProject$`Attack Rate (per 1000)`, method = 'kendall')

#Correaltion between Cases and Case Fatality Ratio Percentage
cor(AIT_580_FinalProject$Cases,AIT_580_FinalProject$`CFR (%)`, method = 'kendall')

#Correaltion between Deaths and Case Fatality Ratio Percentage
cor(AIT_580_FinalProject$Deaths,AIT_580_FinalProject$`CFR (%)`, method = 'spearman')

#Correaltion between Deaths and Attack Rate (per 1000)
cor(AIT_580_FinalProject$Deaths,AIT_580_FinalProject$`Attack Rate (per 1000)`, method = 'spearman')


a) Single Variable T-test Hypothesis

t.test(AIT_580_FinalProject$Deaths)
t.test(AIT_580_FinalProject$Cases)
t.test(AIT_580_FinalProject$`CFR (%)`)
t.test(AIT_580_FinalProject$`Attack Rate (per 1000)`)

b) Correlation Hypothesis
#Running Correlation Hypothesis between Deaths and Cases
cor.test(AIT_580_FinalProject$Deaths, AIT_580_FinalProject$Cases)

#Running Correlation Hypothesis between Deaths and Case Fatality Ratio Percentage
cor.test(AIT_580_FinalProject$Deaths, AIT_580_FinalProject$`CFR (%)`)

#Running Correlation Hypothesis between Cases and Case Fatality Ratio Percentage
cor.test(AIT_580_FinalProject$Cases, AIT_580_FinalProject$`CFR (%)`)

#Running Correlation Hypothesis between Deaths and Cases
cor.test(AIT_580_FinalProject$Cases, AIT_580_FinalProject$`Attack Rate (per 1000)`)

#Running Correlation Hypothesis between Deaths and Cases
cor.test(AIT_580_FinalProject$Deaths, AIT_580_FinalProject$`Attack Rate (per 1000)`)



PostgreSQL

1. Find the total number of cases of Cholera 
SELECT SUM(Cases) as "Total Cases of Cholera"  from cholera;
 Total Cases of Cholera 

2. Find the deaths among the total number of cases
SELECT SUM(Deaths) as "Total Cases of Cholera which resulted in Deaths"  from cholera;

3. Find the rate of attack of cholera in each governorate with the total number of deaths 
select governorate, attack_rate_per_1000, deaths from cholera;

4. Find the goverate(s) which were the most affected by number of Cholera Cases
select governorate as "Most Affected Governorates", cases as "Number of Cases" from cholera where cases = (select MAX(cases) from cholera) group by governorate,cases;

5. Find the maximum number  of cases in each of the distinct governorates
select governorate as "Most Affected Governorates",MAX(Cases) as "Number of Cases" from cholera group by governorate;

6. Find the Governorate Code for the governorate where maximum number of people died
select cod_gov_code as "Government PCode", deaths as "Total number of Deaths" from cholera where deaths = (select MAX(deaths) from cholera) group by deaths,cod_gov_code; 

7. Find the dates and name of governorate when there were maximum number of cases and maximum number of deaths
select date, governorate,cases,deaths from cholera where cases = (select MAX(cases) from cholera) OR deaths = (select MAX(deaths) from cholera) group by date, governorate,cases,deaths;

8. Find all the governorates and their max deaths.
select governorate as 'Distinct Governorate', MAX(Deaths) as 'Number of Deaths' FROM cholera GROUP BY governorate;

9. Find the name of the governorate, date and total number of deaths that happened on 13th July 2017.
select date, governorate, deaths from cholera where date = '2017-07-13';

10. Find all the records where the case fatality ratio is less than 0.15% and date was 30th October 2017
select * from cholera where cfr_percent < 0.15 and date = '2017-10-30';
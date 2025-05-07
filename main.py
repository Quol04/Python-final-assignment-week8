
# 🧩 Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px

# Optional: Configure visuals
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# 📥 Step 2: Load Dataset
df = pd.read_csv('owid-covid-data.csv')  # Make sure the file is in your working directory
df.head()

# 🧾 Step 3: Explore Data Structure
print("Columns:\n", df.columns)
print("\nMissing Values:\n", df.isnull().sum())


# 🧼 Step 4: Data Cleaning
# Filter for selected countries
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Drop critical rows with missing values
df = df.dropna(subset=['date', 'total_cases'])

# Fill missing values (forward fill)
df.fillna(method='ffill', inplace=True)
df.head()


# 📊 Step 5: Total Cases Over Time
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# 📈 Step 6: New Daily Cases Comparison
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['new_cases'], label=country)

plt.title('New Daily COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.show()


# ☠️ Step 7: Death Rate Analysis
df['death_rate'] = df['total_deaths'] / df['total_cases']

# Plot death rate for selected countries
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['death_rate'], label=country)

plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.show()


# 💉 Step 8: Vaccination Progress
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_vaccinations'], label=country)

plt.title('COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()




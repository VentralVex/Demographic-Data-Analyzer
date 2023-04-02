import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("adult.data.csv")

  # Number of each race and their percentage of the total population
  race_count = df["race"].value_counts()
  race_percentages = race_count / df.shape[0] * 100

  # Average age of men
  average_age_men = df.loc[df["sex"] == "Male", "age"].mean().round(1)

  # Percentage of people who have a Bachelor's degree
  percentage_bachelors = df["education"].value_counts(
    normalize=True).loc["Bachelors"] * 100
  percentage_bachelors = percentage_bachelors.round(1)

  # Percentage of people with higher education that earn >50K
  higher_education = df.loc[df["education"].isin(
    ["Bachelors", "Masters", "Doctorate"])]
  higher_education_rich = (higher_education["salary"] == ">50K").mean() * 100
  higher_education_rich = higher_education_rich.round(1)

  # Percentage of people without higher education that earn >50K
  lower_education = df.loc[~df["education"].
                           isin(["Bachelors", "Masters", "Doctorate"])]
  lower_education_rich = (lower_education["salary"] == ">50K").mean() * 100
  lower_education_rich = lower_education_rich.round(1)

  # Min work time
  min_work_hours = df["hours-per-week"].min()

  # Percentage of rich among those who work minimum hours
  num_min_workers = df[df["hours-per-week"] == min_work_hours]
  rich_percentage = (num_min_workers["salary"] == ">50K").mean() * 100
  rich_percentage = rich_percentage.round(1)

  # Highest earning country
  highest_earning_country = (df.loc[df["salary"] == ">50K",
                                    "native-country"].value_counts(
                                      normalize=True).idxmax())

  # Percentage of highest earning country
  highest_earning_country_percentage = (
    df.loc[df["native-country"] == highest_earning_country,
           "salary"].value_counts(normalize=True).loc[">50K"] * 100)
  highest_earning_country_percentage = highest_earning_country_percentage.round(
    1)

  # Print results
  if print_data:
    print("Number of each race:\n", race_count)
    print("Percentage of each race:\n", race_percentages)
    print("Average age of men:", average_age_men)
    print("Percentage with Bachelors degrees:", percentage_bachelors)
    print("Percentage with higher education that earn >50K:",
          higher_education_rich)
    print("Percentage without higher education that earn >50K:",
          lower_education_rich)
    print("Min work time:", min_work_hours, "hours/week")
    print("Percentage of rich among those who work minimum hours:",
          rich_percentage)
    print("Highest earning country:", highest_earning_country)
    print("Percentage of highest earning country:",
          highest_earning_country_percentage)

  # Return a dictionary containing all the calculated values
  return {
    "race_count": race_count,
    "race_percentages": race_percentages,
    "average_age_men": average_age_men,
    "percentage_bachelors": percentage_bachelors,
    "higher_education_rich": higher_education_rich,
    "lower_education_rich": lower_education_rich,
    "min_work_hours": min_work_hours,
    "rich_percentage": rich_percentage,
    "highest_earning_country": highest_earning_country,
    "highest_earning_country_percentage": highest_earning_country_percentage
  }

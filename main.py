import yaml
import datetime


class Country:

    def __init__(self, name, num_seasons):
        self.name = name
        self.num_seasons = num_seasons
        self.start_dates = []
        self.end_dates = []

    def __str__(self):
        return f'country={self.name}\n' \
               f'num seasons = {self.num_seasons}\n' \
               f'start dates = {str(self.start_dates)}\n' \
               f'end dates = {str(self.end_dates)}\n'


countries_to_visit = []

with open("countries.yaml", "r") as f:

    # One doc represents a country
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    # For country in country list
    for doc in docs:
        # k is the country name
        # v is the start and end date
        for k, v in doc.items():
            # Add country to list of country objects
            country = Country(k, len(v))
            # Append start dates and append end dates to country
            # object lists
            for i in range(1, len(v) + 1):
                country.start_dates.append(v[f'season {i}']["start"])
                country.end_dates.append(v[f'season {i}']["end"])
            # Append country list object to list
            # of country objects
            countries_to_visit.append(country)
            print(country)


date = datetime.date(2021, 8, 31)

curr_country = countries_to_visit[0]


if curr_country.start_dates[0] <= date <= curr_country.end_dates[0]:
    print("in date range")
else:
    print("not in range")



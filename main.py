from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("results.csv")

data = dataset.dropna()

print("There are " + str(data.shape[0]) + " tuples in the dataset")

labelEncoder = LabelEncoder()
dataTourn = labelEncoder.fit_transform(data["tournament"])

print("There are " + str(max(dataTourn)) + " tournaments in this dataset")

data['date'] = pd.to_datetime(data['date'])
matches = data[data['date'].dt.year == 2018].shape[0]

print("There are " + str(matches) + " matches in 2018")

homeWins = data[data["home_score"] > data["away_score"]].shape[0]
homeLosses = data[data["home_score"] < data["away_score"]].shape[0]
homeDraws = data[data["home_score"] == data["away_score"]].shape[0]

print("Home team wins:", homeWins)
print("Home team losses:", homeLosses)
print("Home team draws:", homeDraws)

labels = ["Wins", "Losses", "Draws"]
sizes = [homeWins, homeLosses, homeDraws]
plt.pie(sizes, labels=labels)
plt.show()

neutral = [(data["neutral"] == False).sum(), (data["neutral"] == True).sum()]
label = ["Non-Neutral", "Neutral"]
plt.pie(neutral, labels=label)
plt.show()

uniqueTeams = len(pd.concat([data['home_team'], data['away_team']]).unique())

print("There are "+ str(uniqueTeams) + " unique teams")


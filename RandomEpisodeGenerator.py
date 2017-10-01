from random import randint
import json

def selectRandomEpisode(root, fileName, seasons):
	episodes = selectEpisodesWithHighestPriority(root, fileName, seasons)

	index = randint(0, len(episodes) - 1)

	return episodes[index]


def selectEpisodesWithHighestPriority(root, fileName, seasons):
	#all episodes within the selected seasons
	episodes = []

	if seasons == "all":
		low = 0
		high = root["totalSeasons"]
	else:
		low = int(seasons[0])
		high = int(seasons[len(seasons) - 1])

	#itterate through series in the root object and get all episodes in the selected seasons
	for i in range(low, high):
		episodes.extend(root["seasons"][i]["episodes"])

	#caculate highest priority group from selected episodes
	highestPriority = 3
	for i in range(0, len(episodes)):
		if episodes[i]["priority"] < highestPriority:
			highestPriority = int(episodes[i]["priority"])

	#select highest priority episodes from selected episodes
	priorityEpisodes = []
	for i in range(0, len(episodes)):
		if episodes[i]["priority"] == highestPriority:
			priorityEpisodes.append(episodes[i])

	return priorityEpisodes

def printEpisode(episode):
	print("Season " + str(episode["seasonNumber"]) + ", Episode " + str(episode["number"]))
	print(episode["title"])
	print(episode["description"])
	print("Priority Group: " + str(episode["priority"]))

#update episode with updated priority and save to file
def updatePriority(root, fileName, episode, priority):
	root["seasons"][episode["seasonNumber"]-1]["episodes"][episode["number"]-1]["priority"] = priority
	
	with open(fileName, "w") as outFile:    
		json.dump(root, outFile)

if __name__ == '__main__':
	name = input("Enter series title: ")
	seasons = input("List seasons to select from (Enter 'all' for all seasons): ")

	#parse episodes string to a list
	if not seasons.lower() == "all":
		seasons = seasons.split()
	else:
		seasons = seasons.lower()

	#create fileName from provided series name
	fileName = name.lower().replace(" ", "_") + ".json"

	with open(fileName) as seriesData:    
		root = json.load(seriesData)

	while True:
		episode = selectRandomEpisode(root, fileName, seasons)

		printEpisode(episode)

		priority = int(input("Assign priority (1 highest - 3 lowest): "))

		updatePriority(root, fileName, episode, priority)

		satisfied = input("Continue? (Y/N): ")

		if not (satisfied.lower() == "y" or satisfied.lower() == "yes") :
			break


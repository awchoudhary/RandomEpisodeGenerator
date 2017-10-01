#######################################################################################################################################
# A script to scrape episode data for a series from IMDB and load it into a json file. 
# Paramter 1: IMDB ID for Series (which is the number beginning with 'tt' in url for series in IMDB)
# Paramter 2: Number of seasons to extract. If a number greater than the total seasons for a series is provided, all episodes for the 
# series are extracted.
#######################################################################################################################################

# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json



def extractSeries(id, numSeasons):
	#Root document object
	root = {}
	#list of season json objects
	seasons = []
	#list of seasons extracted so far
	seasonsExtracted = []
	totalSeriesEpisodes = 0

	for num in range(1, numSeasons+1):
		#encapsulates season number and episodes
		seasonData = {}
		seasonData["seasonNum"] = num
		totalSeasonEpisodes = 0

		#create and load url
		url = "http://www.imdb.com/title/" + id + "/episodes?season=" + str(num)
		page = urlopen(url)
		soup = BeautifulSoup(page, "html.parser")

		#if we have extracted all seasons for the series and are reloading the page for the last season, break out
		#current season can be found in the season select dropdown
		currentSeasonNum = soup.find("select", {"id" : "bySeason"}).find("option", {"selected" : "selected"})["value"]
		if int(currentSeasonNum) in seasonsExtracted:
			break

		#get series name if we don't have it already
		if "seriesName" not in root:
			root["seriesName"] = soup.find("h3", {"itemprop" : "name"}).find("a").text.strip()

		# Find all episode divs in page
		divs = soup.findAll("div", { "class" : "list_item" })

		#loop through and get all episode info as list
		episodes = []
		for div in divs:
			number = div.find("meta")['content']
			title = div.find("a")["title"]
			description = div.find("div", {"class" : "item_description"}).text.strip()

			episode = {"seasonNumber" : num, "number": int(number), "title": title, "description": description, "priority": 1}
			
			episodes.append(episode)

			totalSeriesEpisodes += 1
			totalSeasonEpisodes += 1

		seasonData["totalNumberOfEpisodes"] = totalSeasonEpisodes
		seasonData["episodes"] = episodes

		seasons.append(seasonData)
		seasonsExtracted.append(num)

	root["totalSeasons"] = len(seasonsExtracted)
	root["totalEpisodes"] = totalSeriesEpisodes
	root["seasons"] = seasons

	#write root to a file
	outfileName = root["seriesName"].lower().replace(" ", "_") + ".json"
	outfile = open(outfileName, "w")
	json.dump(root, outfile)

	print("Created " + outfileName)


if __name__ == '__main__':

	id = input("Enter IMDB ID: ")

	#keep trying to get valid number of seasons
	while True:
		try:
			numSeasons = int(input("Enter Number of Seasons: "))
			if numSeasons > 0:
				break
			else:
				print("Invalid Input")
		except:
			print("Invalid Input")

	extractSeries(id, numSeasons)
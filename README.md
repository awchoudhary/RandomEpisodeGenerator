# Scripts to get details for a random episode of any TV series on IMDB

The motivation for this was to choose a random episode to re-watch for popular Sitcoms.

Here's how to use it:

1. Clone the repo.
2. Run `ScrapeEpisodes.py` to create a json file with episode details for a series. You must provide the IMDB ID for the series you wish to scrape, which is the string that starts with "tt" in the URL for the IMDB page of the series.
3. Run `RandomEpisodeGenerator.py` to get episode details for a random episode.

You must assign an episode a priority group (1 being the highest and 3 the lowest), after selecting an episode. You always get a random episode from the highest priority group.

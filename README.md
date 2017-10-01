# Scripts to get random episode details for any TV series on IMDB

The motivation for this was to choose a random episode to re-watch for popular Sitcoms.

Here's how to use it:

1. Clone the repo.
2. Run `ScrapeEpisodes.py` to create a json file with episodes for a series.
3. Run `RandomEpisodeGenerator.py` to get episode details for a random episode.

You must assign an episode a priority group (1 being the highest and 3 the lowest), after selecting an episode. You always get a random episode from the highest priority group.

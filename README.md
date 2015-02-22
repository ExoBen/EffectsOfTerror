# EffectsOfTerror
STACS Hack 2015 (St Andrews University Hackathon): Palantir and Bloomberg challenges project (by using Bloomberg APIs, present insightful data in a useful way).

This project aims to highlight what effects terrorist attacks and terrorism in general have on local economy, imports/exports, immigration/emigration.

Structure
===
Django Web Server, calling egrep and a Haskell results parser on a local copy of the Global Terrorism Database (http://www.start.umd.edu/gtd/) in order to find terrorist events matching the search.

The results of this are then used to generate multiple queries to the Bloomberg HTTP API for related financial and population data in the time interval of one year before and after the event, highliting what effects the event had.

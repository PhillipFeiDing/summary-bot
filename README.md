# Introduction

This project trains a summarybot model to summarize the activities and contents involved in everyday converstaions. It accepts a dialogue transcript as an input and is supposed to output a gist of what is happening.

# Progress

- By Sept. 3th, corpus (transcripts and summaries) has been collected from FRIENDS series; some data cleaning has been done as well.

# Contents

## Data
- I have run the scripts before so all data has been collected from sites and cleaned in a json file. It is stored as a dictionary under folder src/data/FRIENDS/transcript/transcript.json and src/data/FRIENDS/summary/summary.json.
- Each key is in the format "\d\d\d\d", where the first two digits are the season number and the next two represent the episode. This is useful when matching transript to summary

## Scripts
- Crawling source codes are under src folder. They are defined as functions for separate tasks and ecah only works for specific sites and data since each site has different structure for storing data. If you want more data from different sources you can write more scripts. Make sure you have Beautiful Soup 4 installed if you run the existing scripts.

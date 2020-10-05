# Project 2: Social Media Analyzer

## Restaurant Comparison Tool
This tool utilizes Twitter and Google NLP API to compare sentiment towards two restaurants. When run, the script `proj2.py` prompts the user to enter two different restaurant names. It then searches for tweets based on the names entered and calculates the average sentiment scores for each restaurant across the lists of tweets obtained. The resulting output displays which restaurant people seem to prefer more based on these average scores. An example output is shown below.

![wendys_mcds](https://github.com/hubertlin1/ec601-proj2/blob/master/output.PNG)

## Experimenting with API
I went through tutorials and tried to implement them to reproduce the results locally on my machine. I was able to successfully call multiple functions contained within the Google Language API and was able to use them to perform basic sentiment analysis on my own generated text files. I was also able to utilize tweepy to successfully authenticate with Twitter and grab tweets based on search word, popularity, and time of posting. I included some of these example scripts as well.

## Potential User Stories & Use Cases
* Everyday consumers might want suggestions when deciding what restaurant to go to

* Businesses might want to see how customers feel after visiting

* Businesses might want to see how their public reception compares to the competition

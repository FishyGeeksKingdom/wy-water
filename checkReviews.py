import sys
import json

if __name__== "__main__":

  reviews_raw = sys.argv[1]
  teams_raw = sys.argv[2]

  reviews = json.loads(reviews_raw)["data"]["organization"]["repository"]["pullRequest"]["reviews"]["edges"]
  teams = json.loads(teams_raw)

  print(reviews)
  print(teams)


  print("Hello World from the Devops repo!")
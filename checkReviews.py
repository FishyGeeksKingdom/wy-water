import sys
import json

if __name__== "__main__":

  reviews_raw = sys.argv[1]
  teams_raw = sys.argv[2]

  teamMap = {}
  reviews = json.loads(reviews_raw)["data"]["organization"]["repository"]["pullRequest"]["reviews"]["edges"]
  teams = json.loads(teams_raw)["data"]["organization"]["team"]["members"]["edges"]

  for member in teams:
      teamMap[member["node"]["id"]] = member["node"]["login"]

  print(reviews)
  print(teamMap)

  approvedReviews = []
  readyToPublish = False
  for review in reviews:
    if review["node"]["state"] == 'APPROVED' and review["node"]["author"]["id"] in teamMap:
      readyToPublish = True
      # approvedReviews.append(review["node"])
      print('yay')
  
  
  if not readyToPublish:
    print("A merge into main requires a review approval from one of the following team members: " + ', '.join(teamMap.values()))
  else:
    print("Send it")


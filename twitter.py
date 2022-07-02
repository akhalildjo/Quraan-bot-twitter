import tweepy


auth = tweepy.OAuthHandler("QJwFw2QXQhOedHXOsGFvguZ0a","XHjyVC5XwhBIkfIJkV3e0YprG2kZmoBFJRKo2fqiXhC36PZPTE")
auth.set_access_token("1517563251739004928-fwesulPbeKeOXb5UrgomRAh3bQWGA2","IsmRXtskedttEAjRYp5T6wwf8dWwCHe3KGwMTBRdAfHSN")

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print ("ok")
except: 
    print("erreur de connexion")
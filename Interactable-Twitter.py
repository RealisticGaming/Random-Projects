import tweepy
import config
import configparser
import pandas as pd
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img1 = cv2.imread('person.jpg')
img2 = cv2.imread('fruit.jpg')
img3 = cv2.imread('babypandas.jpg')

choices = int(input("Please Choose an image. \n1. Person\n2. Fruit\n3. Pandas\n4. Face Recognition\n5. Shut Down\n"))
while choices > 5 or choices < 1:
   choices = int(input("Please Choose an image. \n1. Person\n2. Fruit\n3. Pandas4. Face Recognition\n5. Shut Down\n"))
else:
   while 4 >= choices >= 1:
       if choices == 1:
           cv2.imshow('person', img1)

           key = cv2.waitKey(5000)
           cv2.destroyAllWindows()

           confi = configparser.ConfigParser()
           confi.read('config.ini')

           api_key = confi['twitter']['api_key']
           api_key_secret = confi['twitter']['api_key_secret']

           access_token = confi['twitter']['access_token']
           access_token_secret = confi['twitter']['access_token_secret']

           # authentication
           auth = tweepy.OAuthHandler(api_key, api_key_secret)
           auth.set_access_token(access_token, access_token_secret)


           client = tweepy.Client(consumer_key=config.api_key,
                                  consumer_secret=config.api_key_secret,
                                  access_token=config.access_token,
                                  access_token_secret=config.access_token_secret)
           api = tweepy.API(auth)
           # Intro to menu
           wel = str(input("Welcome to the main menu. What is the name that you would like to be addressed by? "))
           menu = "\n1.Create a post\n2.Display my posts\n3.Display followers\n4.Display followed\n5.Go back to previous menu\n"
           # While loop for menu
           choice = int(input(str(wel) + ", please select from the following choices:" + menu))
           while choice > 5 or choice < 1:
               choice = int(input(str(wel) + ", please select from the following choices:" + menu))
           else:
               while 4 >= choice >= 1:
                   if choice == 1:
                       post = client.create_tweet(text=input(" "))
                       print(post)
                   elif choice == 2:
                       time = api.user_timeline()
                       columns = ['Time', 'Tweet']
                       data = []
                       for tweet in time:
                           data.append([tweet.created_at, tweet.text])
                       df = pd.DataFrame(data, columns=columns)
                       print(df)
                   elif choice == 3:
                       follow = api.get_followers()
                       column = ['User']
                       data = []
                       for id in follow:
                           data.append([id.screen_name])
                       fl = pd.DataFrame(data, columns=column)
                       print(fl)
                   elif choice == 4:
                       friend = api.get_friends()
                       column = ['User']
                       data = []
                       for id in friend:
                           data.append([id.screen_name])
                       dl = pd.DataFrame(data, columns=column)
                       print(dl)
                   choice = int(input(str(wel) + ", please select a new choice:" + menu))
               else:
                   print("Goodbye!")
       elif choices == 2:
           cv2.imshow('fruit', img2)

           key = cv2.waitKey(5000)
           cv2.destroyAllWindows()

           print("That looks great, but you need to choose a person.")
       elif choices == 3:
           cv2.imshow('pandas', img3)

           key = cv2.waitKey(5000)
           cv2.destroyAllWindows()

           print("Aren't they adorable, but you need to choose a person.")
       elif choices == 4:
           cap = cv2.VideoCapture(0)

           while True:
               _, img = cap.read()

               gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

               faces = face_cascade.detectMultiScale(gray, 1.1, 4)

               for (x, y, w, h) in faces:
                   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

               cv2.imshow('img', img)

               k = cv2.waitKey(30) & 0xff
               if k == 27:
                   break
               else:
                   cv2.waitKey(5000)
                   cv2.destroyAllWindows()
               confi = configparser.ConfigParser()
               confi.read('config.ini')

               api_key = confi['twitter']['api_key']
               api_key_secret = confi['twitter']['api_key_secret']

               access_token = confi['twitter']['access_token']
               access_token_secret = confi['twitter']['access_token_secret']

               # authentication
               auth = tweepy.OAuthHandler(api_key, api_key_secret)
               auth.set_access_token(access_token, access_token_secret)

               client = tweepy.Client(consumer_key=config.api_key,
                                      consumer_secret=config.api_key_secret,
                                      access_token=config.access_token,
                                      access_token_secret=config.access_token_secret)
               api = tweepy.API(auth)
               # Intro to menu
               wel = str(input("Welcome to the main menu. What is the name that you would like to be addressed by? "))
               menu = "\n1.Create a post\n2.Display my posts\n3.Display followers\n4.Display followed\n5.Go back to previous menu\n"
               # While loop for menu
               choice = int(input(str(wel) + ", please select from the following choices:" + menu))
               while choice > 5 or choice < 1:
                   choice = int(input(str(wel) + ", please select from the following choices:" + menu))
               else:
                   while 4 >= choice >= 1:
                       if choice == 1:
                           post = client.create_tweet(text=input(" "))
                           print(post)
                       elif choice == 2:
                           time = api.user_timeline()
                           columns = ['Time', 'Tweet']
                           data = []
                           for tweet in time:
                               data.append([tweet.created_at, tweet.text])
                           df = pd.DataFrame(data, columns=columns)
                           print(df)
                       elif choice == 3:
                           follow = api.get_followers()
                           column = ['User']
                           data = []
                           for id in follow:
                               data.append([id.screen_name])
                           fl = pd.DataFrame(data, columns=column)
                           print(fl)
                       elif choice == 4:
                           friend = api.get_friends()
                           column = ['User']
                           data = []
                           for id in friend:
                               data.append([id.screen_name])
                           dl = pd.DataFrame(data, columns=column)
                           print(dl)
                       choice = int(input(str(wel) + ", please select a new choice:" + menu))
                   else:
                       print("Goodbye!")
               break

       choices = int(input("Please Choose an image. \n1. Person\n2. Fruit\n3. Pandas\n4. Face Recongition\n5. Shut Down\n"))
   else:
       print("Thank you for stopping by!")

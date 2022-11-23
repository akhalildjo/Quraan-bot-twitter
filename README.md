![alt text][basmalah]


# Athar el quraan


A program that will automatically share on twitter the translated verses of the Quraan in a "random" way every day at 10 am.

## Requirements

* Python 3.6 +
* [Heroku account](https://dashboard.heroku.com/)
* [Zapier account](https://zapier.com/app/dashboard)
* [HCTI account](https://htmlcsstoimage.com/)
* [Uploadcare account](https://uploadcare.com/)

## Installing 

First of all, you will need to fork this project.

Once cloned or forked, i'd suggest you to set your environnement variabeles (Background image link, API keys etc..), for API keys, you will need to create an account on HCTI and Uploadcare.

Create a new Heroku workflow, sync it with your github account, choose the forked project with your own variables and modifications if any, then choose the current branch. For the Build you can pick Python one.

You will also need to add an Add-on for your worflow, to set a crontask, you must add "Heroku Scheduler" Add-on then set this command `python3 main.py` at time you want !
The last step is the most important, you will need to create a Zapier account, then create a new zap, choose Uploadcare as a trigger (it will ask you to link you account with API keys), then for actions, choose twitter : tweet an image ! 

(Before doing all of that, don't forget to test the project localy to make sure it's working, after dewonloading python depedencies with command `pip3 install -r requirements.txt`)

## Special thanks

I'd like to thank AbdulBaqi for inspiration, his code helped me a lot, I also recommand his [website](http://abdulbaqi.io/tag/technology/) treating about new technologies and interesting concepts ! 
thanks to [Abderrahman](https://www.instagram.com/ansary.sahrawi/) for background font and templating the concept, he's the best Web designer i've ever seen ! & finaly to Aymene for the code review and for helping me to host my app ! 


[basmalah]: https://github.com/akhalildjo/atharelquraan/blob/0dfbf759926a89f2c4a88752298f5142777c5030/athar-basmalah.png "BismiLah ar-rahman ar-rahim"

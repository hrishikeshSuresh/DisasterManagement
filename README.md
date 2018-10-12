# Disaster Relief Management

#### Problem Statement

+ Efficient allocation and management of resources between relief camps and shelters to avoid wastage of important resources during disaster relief operations.
+ Help NGOs to respond to various needs of individuals in an affected area and maintain effective co-ordination between government, NGOs and general public to aid the relief operations.


#### Inspiration

During the recent events of Kerala Floods (2018), a lot of important necessities like medicine, food etc.
were wasted. Read [here](https://www.thehindu.com/news/national/kerala/medical-relief-ops-lack-a-centralised-system/article24763621.ece) .


#### Idea

We will create an automated and centralized management system that will coordinate work between relief camps and provide aid to where it is needed the most. Governmental shelters and NGOs can be approached by private parties and other NGOs by simply tweeting with hashtags related to a particular natural disaster.They can tweet with the amount of resources they have like:    
![example_tweet](https://github.com/redlegblackarm/DisasterManagement/blob/master/tweet.png)

Now we will extract this data. The database will contain the number of people, the number of volunteers, the rough number of resources it needs and the current resources it has. We will manage a database centrally where we will schedule these tweets in the database,at the shelters where resources are needed the most.Then an automated query will be sent to the twitter handle asking for confirmation. 
	
If they reply within a stipulated time, then the resources that were promised will be added to the database. It will be useful if the handles share their location as we can also choose the closest aid provider. If a particular handle does not keep its promise, it will be black-listed with a warning.

If any particular shelter is over-crowded, authorities can put in a tweet requesting for more shelter spaces. A nearby NGO or person can sponsor the shelter by tagging the location of the proposed shelter and also mentioning other facilities that are available at the spot. The system will check if the location is safe by making use of remote-sensing so that the shelter doesn't get affected the natural disaster. 

![flow_chart](https://github.com/redlegblackarm/DisasterManagement/blob/master/Codefundo%20-%20Flowchart.png)

	
We are also looking at mining twitter data constantly, looking for disaster-specific topics and hashtags. We plan to do disaster-specific summarizations by analyzing this data and using this to generate reports related to sub-topics of a disaster. These kind of summarizations in food, medicines or infrastructure could be of use to different interest groups like rescue workers, government agencies, field experts or common people, which could help them in making informed decisions.

Since the volume of such data can be really high,**Microsoft Azure can help us manage and store this data effectively and help us train our models efficiently at the same time.**


#### Overview
	
The proposed centralized relief management system will:
+ Help in quick co-ordination and relief, as the resources would reach the right place, at the right time and in correct quantities
+ Prevent wastage of resources
+ Collect data continuously to help in serving the requests with the right resources, also verifying and identifying safe relief camps to manage crowd.


	


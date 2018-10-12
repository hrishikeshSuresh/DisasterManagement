# Disaster Relief Management

#### Problem Statement

+ Efficient allocation and management of resources between relief camps and shelters to avoid wastage of important resources during disaster relief operations.
+ Help NGOs to respond to various needs of individuals in an affected area and maintain effective co-ordination between government, NGOs and general public to aid the relief operations.


#### Inspiration

During the recent events of Kerala Floods (2018), a lot of important necessities like medicine, food etc.
were wasted.Read [here](https://www.thehindu.com/news/national/kerala/medical-relief-ops-lack-a-centralised-system/article24763621.ece) This inspired us to come up with this idea, and Microsoft Azure can provide a huge kickstart to our plans.



#### Idea

We will create an automated and centralized management system that will coordinate work between relief camps and provide aid to where it is needed the most. Governmental shelters and NGOs can be approached by private parties and other NGOs by simply tweeting with hashtags related to a particular natural disaster.They can tweet with the amount of resources they have, as shown below.</p>    
![example_tweet](https://github.com/redlegblackarm/DisasterManagement/blob/master/tweet.png)
<p>Now we will extract this data. The database will contain the number of people, the number of volunteers, the rough number of resources it needs and the current resources it has. We will manage a database centrally where we will schedule these tweets in the database,at the shelters where resources are needed the most.</p><p>Then an automated query will be sent to the twitter handle asking for confirmation. 
If they reply within a stipulated time, then the resources that were promised will be added to the database. It will be useful if the handles share their location as we can also choose the closest aid provider. The database will be open to the public. If a particular handle does not keep its promise, it will be black-listed with a warning.</p><p>If any particular shelter is over-crowded, the chief in-charge of the shelter can request for a shelter, then a tweet will be put out from the system's twitter handle. A nearby NGO or person can sponsor the shelter by tagging the location of the proposed shelter and also mentioning other facilities that are available at the spot. The system will check if the location is safe by making use of remote-sensing so that the shelter doesn't get affected the natural disaster. The best location will be chosen and the chosen shelter will be approved.</p>
<p>We are also looking at mining twitter data constantly and looking for disaster-specific topics and hashtags. We plan to do disaster-specific summarizations by analyzing this data and using this to generate reports related to sub-topics of a disaster. These kind of summarizations in -food, medicines or infrastructure, could be of use to different interest groups like rescue workers, government agencies, field experts, or common people, which could help them in making informed decisions.</p>
<p>Since the volume of such data can be really high, Microsoft Azure can help us manage and store this data effectively and help us train our models efficiently at the same time.</p>


#### Overview
	
The proposed centralized relief management will
+ Help in quick co-ordination and relief, as the resources would reach the right place, at the right time and in correct quantities
+ Save resources and prevent their wastage
+ Regular surveys and data collections will help to serve the demands with the right resources, area surveys will help determine safe points after disasters and also be able to determine correct locations to set-up health camps
	


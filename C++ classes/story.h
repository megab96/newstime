//A story is a collection of events that follow a narrative or common theme.
//The story class consists mainly of a list of events and pointers to 
//related stories. A story could be searched by its keywords, title, startdate/
//enddate or event.

#ifndef STORY_H
#define STORY_H

#include <iostream>
#include <string>
#include <list>
class event;		//never done forward defs before

class story:
{
public:
	story(){};
	story(int start = 0, int end = 0, string title);
	int getStartDate();
	int getEndDate();
	string getTitle();
	event * getEventByName(string nameOfEvent);		//pointer to head of eventList
	string * getKeywordsList();						//pointer to head of keywordsList
	story * getStoriesList();							//pointer to head of storiesList
private:
	int startDate, endDate;				//date format: 20160301 for now
	string title;						//e.g. catalonia independence
	list<event*> eventList;
	list<string*> keywordsList;
	list<story*> relatedStoryList;
};

#endif
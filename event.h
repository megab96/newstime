#ifndef EVENT_H
#define EVENT_H

#include<iostream>
#include<string>
#include<list>
#include"story.h"

class event:
{
public:
	event(){};
	event(int date, string title);
	int getDate();
	string getTitle();
	event * getRelatedEventsList();
	string * getLinksList();
private:
	int date;
	string title;
	list<string> linksList;
	list<event*> relatedEventsList;
	story * parentStory;
};

#endif
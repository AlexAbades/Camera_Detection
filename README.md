# Camera_Detection

Project where I try to detect in real life the prices from the products using camera detection. 


Do we really need to take in consideration all the possible problems of real life detection ?
We are trying to detect the price, and we can have problems of brightness and reflection but the problems with:

- Non-Planar objects
- Unknown layout

Almost al the prices are in a standard layout, white with black letters or either in orange or other color for 
the offers. 

- How we detect the language of the etiquete:
	- Take a look on how google translate does it 

- How we detect an offer? 
	- Color of the etiquete 
	- Crossed price (normal one) 
	- 2 prices: Normal one and the offer price.

- How we detect the store were we are buying? 
	- Are we buying at netto, Aldi, Fotex...?
	Are the etiquets universal or there are some differences from one store to another? 

- Should we access the location? 
	- We can't be sure that the store where we are buying will have the etiquets in the same language
	 of the country. 
	- Same with the currency. 
	- We can ease some tasks with location. Store, language 
	- Expensive for memory and battery.

- Create a database to store the products.
	- We have to store the label, specifies which product we are buying
	- Price of the product
	- Store where we are buying it 
	- Date when we bought it. We don't want to compare a product that has been bought one year ago. 
	(Is it necessary if we update the products each time we buy them? Yes, because some product might be 
	bought with little frecuency, so the price of the product we are scanning should have a referece in our 
	data base).

- Should we send messages of Nutritional aspect?
	- If they are scanning biscuits, show the amount of suggar, fat... 
	- We should acses to a food data base (My fitnesPal) 
	- Will be more complicated, buy more interactive for the users
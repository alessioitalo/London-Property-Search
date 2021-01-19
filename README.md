# London-Property-Search

This simple script uses BeautifulSoup to scrape Rightmove.co.uk in order to find properties for rent.

The properties are filtered from the Rightmove main page: the link I am using is showing one bedrooms flats in West London, within a 1100-1400£ per month range. This settings can be changed by using a different url in the LINK constant.

The data is stored in three separate lists (addresses, prices per month, links) and is then uploaded in a Google Form using selenium.

A new form can be created from https://docs.google.com/forms/u/0/

# Reporting STLs
[Public Callout from CATU Galway: Report Illegal Short-Term Lets](https://catuireland.org/airbnb/2025/04/30/how-to-report-illegal-short-term-lets/)
(30 April 2025)
Google Doc: [Airbnb Reporting Workflow](https://docs.google.com/document/d/1dJ9pLyHGGaqsroIJK6dkNMUtFdlGg_EjPLygFtY9JUo/edit?usp=sharing)
1. Take listings from Google Sheet "Airbnb Power Hour" tab "Entire Homes" (572 entries)
- City, Latitude, Longitude, Type, Address, Description
- Presence/Lack of permission, Has action been taken
- Check date that this data was scraped
- Suggest addition of date column so we know when things were submitted to GCC
- Look into Apify tri_angle/airbnb-scraper
- Create own scraper of Airbnb
- Including Title, Coordinates, Address and/or Eircode (maybe later extracted via regex), Description, Property Type, Date of Listing
- May need to run several queries (1, 2, 4, 6 guests; weekend, week, month; specific months) then check for duplicates (and determine if running several times is necessary)
- Note map projection of coordinates, potentially reproject
- Create shapefile/ pointfile of results
2. Look for planning permission via City Council Planning Map on ArcGIS
- Potential Layers of interest: Planning Applications (Last 10 Years), Unauthorised Developments
- Export layers of interest
- Determine date range of data
- Check for updated dataset
- Planning Application Sites: Reference Number, Application Type, Status, Details (address), Description (permission type), Date Received, Date Due
- Filter to only have planning permission data of short-term lets(?)
3. In QGIS
- Create visualisation of maps
- First check if Airbnb coordinates fall within planning permission boundaries
- Then check if Airbnb coordinates are near (10m threshold?) with planning permission points
4. Find the property owner via Form 17 (landdirect.ie)
- Search by address, Eircode, coordinate
- Look for site to tell Eircode from coordinate?
- Click on property, get folio number
- If Form 17 exists in folio, get owner name from form
- If Form 17 does not exist, folio may need to be purchased
5. Populate the complaint form and send to Galway Planning and GCC //  Populate CATU's Google Form Report an STL
6. Evaluate automated method against existing dataset
7. Start on Google Sheet "Airbnb Power Hour" tab "Booking.com reporting" (11 entries)
Create own scraper of Booking.com


Instead of scraping airbnb, since it blocks both scrapy and selenium
https://insideairbnb.com/get-the-data
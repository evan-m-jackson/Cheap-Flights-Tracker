# Cheap-Flights-Tracker

This program will either text or email the user a list of cheap flights for any locations that they want to travel to.  All the user has to do is fill out a Google Sheets doc that has 3 columns (City, IATA Code, Max Price).  The code will then either text or email the user any flights for those locations that are less than the Max Price.  The flights are found using the Tequila API and text messages are sent using the Twilio API.

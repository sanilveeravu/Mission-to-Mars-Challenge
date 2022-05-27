# Mission to Mars

## Overview of the Project

With lot of sites having information on Mars, this application was build to consolidate all the interesting information and images into a website. The application would allow the users to scrape new content from each of these siates to get the latest and greatest information.

## Resources
- Data Source: https://redplanetscience.com, https://spaceimages-mars.com, https://galaxyfacts-mars.com, https://marshemispheres.com
- Software: Python 3.9.7, Jupyter Notebook, flask, mongo, bootstrap, html
---

## Results

A new website was built using flask with the scrape option. The overall page looks as below:
![FullScreenImage](Resources/FullScreenImage.png)

### Application Flow

- The scrape button in turn runs the web scraping process in python using splinter and beautiful soup. 

- The collected data from the scraping process is stored into mongodb in the same process.

- The index html page is then rendered through flask collecting the data from mongo.

### Additional Styling

1. The new components added were put also into grids. Added a new feature of using offset to get the required spacing.

    ![Grid](Resources/Grid.png)

2. The scrape button was added to span across the screen.

    ![Button](Resources/Button.png)

3. The table was styled using bootstrap table class.

    ![Table](Resources/Table.png)

4. The tile was updated to use lead

    ![Lead](Resources/Lead.png)

---

## Summary

The application was able to collect all the necessary details about Mars and show an impressive effort even to NASA.



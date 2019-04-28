# canvas-student-list
Bash and Python code that uses Canvas LMS API to create pdf sign-in sheets (student lists) for class sections. Codebase relies on a modified version of https://github.com/dkloz/canvas-api-python api-wrapper.

## Usage

+ Obtain a Canvas API key. 

Go to Canvas account settings. Press the "New Access Token" button.


Enter the Token expiration date and press "Generate Token". Expiration date should be set at or later than the classs end date if you want your script to be functional for the whole duration of the class. Copy down the token shown.

+ Modify the getdata.py script as follows

Enter your API key (Token) by assigning it to *APIkey* variable

Modify the dictionary of GSIs (variable *gsis*) by entering all class sections and corresponding GSI names. This dictionary will be used to match class sections to GSI names. Script assumes that last three letters of section name contain the section number. If your university uses another section naming format, modify the script accordingly.


Go to Canvas and open the courses you want to process. Notice the course numbers at the end of the URLs.


Add these numbers into *class_numbers* list as string variables. Script will loop over these class numbers to generate student lists for all of them.

+ Run *makepdfs.sh*



## Requirements


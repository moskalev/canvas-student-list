# canvas-student-list
Bash and Python code that uses Canvas LMS API to create pdf sign-in sheets (student lists) for class sections. Codebase relies on a modified version of https://github.com/dkloz/canvas-api-python api-wrapper.

## Usage

+ Obtain a Canvas API key. 

Go to Canvas account settings. Press the "New Access Token" button.

![New Access Token](https://user-images.githubusercontent.com/1658661/56871696-35aad880-69ef-11e9-886e-91a3e40fa513.png)

Enter the Token expiration date and press "Generate Token". Expiration date should be set at or later than the class end date if you want your script to be functional for the whole duration of the class.

![Expiration Date](https://user-images.githubusercontent.com/1658661/56871706-5a06b500-69ef-11e9-8faf-cdb2ccaf9a2e.png)

Copy down the token shown.

![Copy down the token](https://user-images.githubusercontent.com/1658661/56871711-6c80ee80-69ef-11e9-9a0b-60dff0eef07d.png)

+ Modify the *getdata.py* script as follows

Enter your API key (Token) by assigning it to *APIkey* variable

Modify the dictionary of GSIs (variable *gsis*) by entering all class sections and corresponding GSI names. This dictionary will be used to match class sections to GSI names. Script assumes that last three letters of section name contain the section number. If your university uses another section naming format, modify the script accordingly.

Go to Canvas and open the courses you want to process. Notice the course numbers at the end of the URLs.

![Canvas course number](https://user-images.githubusercontent.com/1658661/56871718-7c98ce00-69ef-11e9-8176-862c0eb671e1.png)

Add these numbers into *class_numbers* list as string variables. Script will loop over these class numbers to generate student lists for all of them.

+ Run *makepdfs.sh*

Script will create a folder *pdfs* where it will operate with tex/pdf files. 

## Requirements

**lualatex** is used to generate pdfs from tex files. A rather unusual font is set in *tabletemplate.tex*. If your system does not have the fonts needed, replace the font name accordingly.

**pdfunite** is used to form a single pdf out of individual sections' pdfs.

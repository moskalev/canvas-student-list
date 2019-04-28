from read import CanvasReader
from subprocess import call

APIkey = '' # enter your API key here

gsis = {'409' : 'GSI 2', 
'502' : 'GSI 3', 
'407' : 'GSI 4', 
'408' : 'GSI 5', 
'501' : 'GSI 2', 
'507' : 'GSI 6', 
'410' : 'GSI 5', 
'509' : 'GSI 7', 
'508' : 'GSI 8', 
'510' : 'GSI 7', 
'511' : 'GSI 8', 
'401' : 'GSI 9', 
'504' : 'GSI 9', 
'503' : 'GSI 6', 
'403' : 'GSI 1', 
'505' : 'GSI 3', 
'506' : 'GSI 4'
} # all sections need to be represented

class_numbers = ['266735', '265784'] # in string format

reader = CanvasReader(APIkey, 'https://umich.instructure.com', '/api/v1')


def generatepdfs(classnum):
    
    sections = reader.get_sections(classnum)

    for section in sections:
        print('processin section', section['id'])
        secinfo = reader.get_section_info(classnum, section['id'])
        
        secstudents = secinfo[0]['students']
        
        if(len(secstudents) > 40):
            continue;
        
        enrolledstudents = []
        for stud in secstudents:
            if stud['enrollments'][0]['enrollment_state'] == 'active':
                enrolledstudents.append(stud)
        sortedsecstudents = sorted(enrolledstudents, key=lambda k: k['sortable_name'])
        tabledata = ''
        for student in sortedsecstudents:
            tabledata = tabledata + student['sortable_name'] + " &  \\\\  \hline\n"
            
        f = open("tabletemplate.tex","r")
        latex = f.read()
        
        latex = latex.replace('%SECTIONSTRING', section['name'] + ', ' + gsis[section['name'][-3:]])
        latex = latex.replace('%TABLEDATA', tabledata)
        f.close()
        
        f = open("pdfs/" + section['name'][-3:] + ".tex","w")
        f.write(latex)
        f.close()
        
        print('lualatex ')
        
        call(["lualatex", "--jobname=pdfs/" + section['name'][-3:], "pdfs/" + section['name'][-3:] + ".tex"])
    
        print(len(sortedsecstudents))
        

## Generates pdfs for sections
for class_num in class_numbers:
    generatepdfs(class_num)

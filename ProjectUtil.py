import csv
import os

class Project():
    #Unsure if anything needs to be done on init here.
    def __init__(self):
        pass
    
    #name is the name of the file within the ProjectFiles folder.
    #members, risks, riskstatus, and requirements must be a list object with strings inside, even if there is only one element in the list.
    #all other arguments are strings.
    #In the case of an existing file with the same name, the old file will be overwritten.
    #In the event of there being more than one row, all 'blank' elements will be filled with an empty string.
    def createFile(self, name, owner, members, description, risks, riskStatus):
        if(members == ''):
            self.members = ['']
        elif(',' in members):
            self.members = members.split(',')
        else:
            self.members = [members]
        if(risks == ''):
            self.risks = ['']
        elif(',' in risks):
            self.risks = risks.split(',')
        else:
            self.risks = [risks]
        if(riskStatus == ''):
            self.riskStatus = ['']
        elif(',' in riskStatus):
            self.riskStatus = riskStatus.split(',')
        else:
            self.riskStatus = [riskStatus]
        self.name = name
        self.path = str(os.path.dirname(os.path.realpath(__file__))) + '\\ProjectFiles\\' + name + '.csv'
        self.owner = owner
        self.description = description
        with open(self.path, mode = 'w') as projectFileWrite:
            writer = csv.writer(projectFileWrite, delimiter = ',', lineterminator = '\n')
            row1 = ['Project Name', 'Project Owner', 'Members', 'Description', 'Risks', 'Risk Status', 'Functional Requirements', 'Nonfunctional Requirements', 'Week Number', 'Person Hours Total', 'Requirements Analysis Hours', 'Designing Hours', 'Coding Hours', 'Testing Hours', 'Project Management Hours']
            writer.writerow(row1)
            row2 = [self.name, self.owner, self.members[0], self.description, self.risks[0], self.riskStatus[0], '', '', '', '', '', '', '', '', '']
            writer.writerow(row2)
            lengths = []
            lengths.append(len(self.members))
            lengths.append(len(self.risks))
            lengths.append(len(self.riskStatus))
            lengths.sort()
            longestList = lengths[-1]
            #I'm sure this can be cleaned up in some way later but for now whatever it works.
            for x in range(1, longestList):
                addingList = ['', '']
                if(x < len(self.members)):
                    addingList.append(self.members[x])
                else:
                    addingList.append('')
                addingList.append('')
                if(x < len(self.risks)):
                    addingList.append(self.risks[x])
                else:
                    addingList.append('')
                if(x < len(self.riskStatus)):
                    addingList.append(self.riskStatus[x])
                else:
                    addingList.append('')
                addingList.append('')
                addingList.append('')
                addingList.append('')
                addingList.append('')
                addingList.append('')
                addingList.append('')
                addingList.append('')
                writer.writerow(addingList)
    
    #The file name passed in MUST exist in ProjectFiles for this to work.
    #This function returns a dictionary object containing a rows and columns list.
    #These are both two dimensional.
    #The rows list contains a list with each element containing the next row in the csv
    #The columns list contains a list with each element containing the next column in the csv.
    def readFile(self, name):
        self.path = str(os.path.dirname(os.path.realpath(__file__))) + '\\ProjectFiles\\' + name + '.csv'
        with open(self.path, mode ='r') as projectFileRead:
            reader = csv.reader(projectFileRead, delimiter = ',', lineterminator = '\n')
            rows = []
            columns = []
            for row in reader:
                rows.append(row)
                if(len(columns) == 0):
                    for x in range(len(row)):
                        columns.append([])
                for x in range (len(row)):
                    columns[x].append(row[x])
            csvContents = {
                'rows': rows,
                'columns': columns
            }
            return csvContents
    
    #This funtion returns the row specified with rowNum, from the file specified by name within ProjectFiles.
    #The file name MUST exist in ProjectFiles for this to work.
    #May be taken out later, as everything that you get from this function you can get from readFile, but with extra information.
    def getRow(self, name, rowNum):
        self.path = str(os.path.dirname(os.path.realpath(__file__))) + '\\ProjectFiles\\' + name + '.csv'
        with open(self.path, mode ='r') as projectFileRead:
            reader = csv.reader(projectFileRead, delimiter = ',', lineterminator = '\n')
            rows = [r for r in reader]
            return rows[rowNum]

    #The file name MUST exist in ProjectFiles for this to work.
    #This function rewrites a csv file with the new row you want to exist in the csv, in the rowNum you specify.
    def editRow(self, name, rowNum, newRow):
        data = self.readFile(name = name)
        rows = data['rows']
        rows[rowNum] = newRow
        with open(self.path, mode = 'w') as projectFileWrite:
            writer = csv.writer(projectFileWrite, delimiter = ',', lineterminator = '\n')
            writer.writerows(rows)
            
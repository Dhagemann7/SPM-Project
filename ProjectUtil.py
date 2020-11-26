import csv
import os

class Project():
    def __init__(self, name, owner, members, description, risks, riskStatus, requirements):
        self.name = name
        self.path = str(os.path.dirname(os.path.realpath(__file__))) + '\\ProjectFiles\\' + name + '.csv'
        self.owner = owner
        self.members = members
        self.description = description
        self.risks = risks
        self.riskStatus = riskStatus
        self.requirements = requirements
        self.createFile()

    def createFile(self):
        with open(self.path, mode = 'w') as projectFile:
            writer = csv.writer(projectFile, delimiter = ',')
            row1 = ['Project Name', 'Project Owner', 'Members', 'Description', 'Risks', 'Risk Status', 'Requirements', 'Person Hours Total', 'Requirements Analysis Hours', 'Design Hours', 'Coding Hours', 'Testing Hours', 'Project Management Hours']
            writer.writerow(row1)
            row2 = [self.name, self.owner, self.members[0], self.description, self.risks[0], self.riskStatus[0], self.requirements[0], '0', '0', '0', '0', '0', '0']
            writer.writerow(row2)

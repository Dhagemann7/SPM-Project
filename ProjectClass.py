class Project:
    def __init__(self, name,owner,members,description,risks,fRequirements,nfRequirements,hours):
        self.name = name
        self.owner = owner
        self.members = members
        self.description = description

    #risks, requirements, hours to be implemented as arrays - hours array is an array of week objects

    def addRisk(self,riskName, riskStatus):
        #add risk to array of risks - append

        return
    
    def addRequirement(self,rtype, requirement):
        #add requirement to array of requirements depending on type

        #if (rtype == 'functional'):
            #add requirement to array of functional requirements - append

        #if (rtype == 'nonfunctional'):
            #add requirement to array of nonfunctional requirements - append

        return

    def addWeekHours(self,week,requirementsHours,designHours,codingHours,testingHours,projManagementHours):
        
        #newWeek = Week(week,requirementsHours,designHours,codingHours,testingHours,projManagementHours)
        
        #add week/hours object to week/hours array - append

        return
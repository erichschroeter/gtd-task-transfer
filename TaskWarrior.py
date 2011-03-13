import re

'''
This class encapsulates information supported by TaskWarrior 
(http://taskwarrior.org/projects/show/taskwarrior/)
'''
class TaskWarriorTask(object):

    # Properties
    def getDescription(self):
        return self.__description

    def setDescription(self, value):
        if value is None:
            #raise ValueError('The description must be specified')
            value = ''
        alpha_numeric = re.compile('[\W_]+')
        value = alpha_numeric.sub(' ', value)
        value = value.lstrip()
        value = value.rstrip()
        self.__description = value

    description = property( getDescription, setDescription )

    def getProject(self):
        return self.__project

    def setProject(self, value):
        if value is None:
            value = ''
        alpha_numeric = re.compile('[\W_]+')
        value = alpha_numeric.sub('-', value)
        value = value.lstrip('-')
        value = value.rstrip('-')
        self.__project = value

    project = property( getProject, setProject )

    def getPriority(self):
        return self.__priority

    def setPriority(self, value):
        if value is None:
            value = ''
        elif value == '':
            value = ''
        elif value != 'H' or value != 'M' or value != 'L':
            raise ValueError('Priority must have a value of H, M, L, or blank. ' + str(value) + ' was given.')
        self.__priority = value

    priority = property( getPriority, setPriority )

    def getStatus(self):
        return self.__status

    def setStatus(self, value):
        if value is None:
            value = 'pending'
        self.__status = value

    status = property( getStatus, setStatus )

    def getEntered(self):
        return self.__entered

    def setEntered(self, value):
        if value is None:
            value = ''
        self.__entered = value

    entered = property( getEntered, setEntered )

    def __init__(self, description=None, project=None, priority=None, status=None, entered=None):
        self.description = description
        self.project = project
        self.priority = priority
        self.status = status
        self.entered = entered

    def __repr__(self):
        return "[" + \
                " description='" + self.description + "' " + \
                " project='" + self.project + "' " + \
                " priority='" + self.priority + "' " + \
                " status='" + self.status + "' " + \
                " entered='" + self.entered + "' ]"


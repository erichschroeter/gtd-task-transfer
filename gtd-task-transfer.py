import os
import sys
import csv
import argparse
from subprocess import call
from TaskWarrior import TaskWarriorTask

def main():
    parser = argparse.ArgumentParser(prog='gtd-task-transfer', description='Transfer your task data from one GTD application to another')

    # Create subparsers for subcommands
    subparsers = parser.add_subparsers(title='Commands')

    ''' Stub for additional commands '''
    # COMMAND   --------------------------------------- START
    # COMMAND   ----------------------------------------- END

    # IMPORT    ---------------------------------------- START
    # Create a parser for importing tasks to different GTD apps (i.e. ThinkingRock, TaskWarrior, etc)
    parser_import = subparsers.add_parser('import', help='Import task data to a GTD application')
    parser_import.add_argument('--preview', help='Preview what will be imported', action='store_true', default=False)
    parser_import.add_argument('--confirm', help='Confirm each task that will be imported', action='store_true', default=False)

    # Create a subparser for each file type to support
    file_type_list = parser_import.add_subparsers(title='Import file type', description='Supported file types')

    #                   SUPPORTED FILE TYPES
    
    # Create a subparser for CSV file
    parser_csv = file_type_list.add_parser('csv')
    parser_csv.add_argument('file', help='The CSV file. (including headers in row 0)')
    
    # TODO add iCal support

    #                   APPLICATIONS

    # Create a subparser for each GTD application that supports CSV
    application_list = parser_csv.add_subparsers(title='GTD Applications', description='available applications')

    # Create a parser for importing into TaskWarrior
    parser_taskwarrior = application_list.add_parser('taskwarrior', description='Import task data from a CSV file into TaskWarrior. The column values are 0 based. Make sure to include the Headers in row 0.')
    parser_taskwarrior.set_defaults(command=import_to_taskwarrior_wrapper)
    parser_taskwarrior.add_argument('-d', '--description', help='The column with the text representing the task', type=int)
    parser_taskwarrior.add_argument('-P', '--project', help='The column representing the project', type=int)
    parser_taskwarrior.add_argument('-p', '--priority', help='The column representing the priority', type=int)
    parser_taskwarrior.add_argument('-s', '--status', help='The column representing the status. (NOT SUPPORTED YET)', type=int)
    parser_taskwarrior.add_argument('-e', '--entered', help='The column representing when the date when entered. (NOT SUPPORTED YET)', type=int)

    # TODO add ThinkingRock support

    # IMPORT    ------------------------------------------ END
    
    args = parser.parse_args()

    # call the specified command
    args.command(args)

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
#   Command Wrappers                                                        #
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #

def import_to_taskwarrior_wrapper(args):
    map = {}
    map[args.description] = 'description'
    map[args.project] = 'project'
    map[args.priority] = 'priority'
    #map[args.status] = 'status'
    #map[args.entered] = 'entered'
    tasks = get_tasks_from_csv(args.file, map)
    import_to_taskwarrior(tasks, args.confirm, args.preview)

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
#   Commands                                                                #
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
def import_to_taskwarrior(tasks, confirm=False, preview=False):
    '''
    Imports the given list of tasks into TaskWarrior.

    @param tasks A list of Task objects.
    '''

    '''
    description = tasks[0].description
    project = 'project:' + tasks[0].project
    priority = 'priority:' + tasks[0].priority
    call(['task', 'add', description, project, priority])
    '''
    num_imported = 0
    for task in tasks:
        description = task.description
        project = 'project:' + task.project
        priority = 'priority:' + task.priority
        if preview:
            print 'task add ' + description + ' ' + project + ' ' + priority
        else:
            if confirm:
                response = raw_input('add <' + description + '>? (y/n)')
                if response == 'y':
                    call(['task', 'add', description, project, priority])
                    num_imported += 1
            else:
                call(['task', 'add', description, project, priority])
                num_imported += 1
    
    if preview:
        print str(len(tasks)) + ' tasks will be imported into TaskWarrior'
    else:
        print str(num_imported) + ' tasks imported into TaskWarrior'

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
#   Helpers                                                                 #
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #

# TODO fix link for supported attributes
def get_tasks_from_csv(file, map):
    '''
    Returns a list of Tasks. This simply reads the given CSV file converting each
    row into a Task object.

    The map is a map between the column number (0 based) and the supported task
    attribute. See <FIXME> for supported task attributes.

    @param file The CSV file exported from ThinkingRock
    @param map A mapping of columns to task attributes
    '''
    reader = csv.reader(open(file, 'rb'))
    reader.next()

    tasks = []
    
    for i, row in enumerate(reader):
        #sys.stdout.write( '(' + str(i) + ')' )
        #print row
        task = TaskWarriorTask()
        for column, attribute in map.items():
            #print str(column) + ' --> ' + attribute
            setattr(task, attribute, row[column])
            #print attribute + ' -->\t' + getattr(task, attribute)

        tasks.append(task)

    return tasks

if __name__ == "__main__":
    main()

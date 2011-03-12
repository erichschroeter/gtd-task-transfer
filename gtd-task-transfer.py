import os
import sys
import cvs
import argparse

def main():
    parser = argparse.ArgumentParser(prog='gtd-task-transfer', description='Transfer your task data from one GTD application to another')

    # Create subparsers for subcommands
    subparsers.parser.add_subparsers(title='Commands')

    ''' Stub for additional commands '''
    # COMMAND   --------------------------------------- START
    # COMMAND   ----------------------------------------- END

    # IMPORT    ---------------------------------------- START
    # Create a parser for importing tasks to different GTD apps (i.e. ThinkingRock, TaskWarrior, etc)
    parser_import = subparsers.add_parser('import', help='Import task data to a GTD application')
    parser_import.add_argument('task', help='The task text')
    
    # Create a subparser for each GTD application
    application_list = parser_import.add_subparsers(title='GTD Applications', description='available applications')

    # Create a parser for importing into TaskWarrior
    parser_taskwarrior = application_list.add_parser('taskwarrior')
    parser_taskwarrior.set_defaults(command=import_to_taskwarrior_wrapper)

    # IMPORT    ------------------------------------------ END

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
#   Command Wrappers                                                        #
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #

def import_to_taskwarrior_wrapper(args):
    map = {}

    tasks = get_tasks_from_csv(args.file, map)
    import_to_taskwarrior(tasks)

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
#   Commands                                                                #
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #
def import_to_taskwarrior(tasks):
    '''
    Imports the given list of tasks into TaskWarrior.

    @param tasks A list of Task objects.
    '''
    for task in tasks:
        print task

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
    
    for i, row in enumerate(reader):
        sys.stdout.write( '(' + str(i) + ')' )
        print row
        for column, attribute in map.items():
            print str(column) + ' --> ' + attribute

if __name__ == "__main__":
    main()

import argparse
import getpass
import logging

import tableauserverclient as TSC


def main():
    parser = argparse.ArgumentParser(description='This function will refresh a specific datasouce based on its name')
    parser.add_argument('--server', '-s', required=True, help='server address')
    parser.add_argument('--username', '-u', required=True, help='username to sign into server')
    # This is useful to avoid prompting user to enter password:
    parser.add_argument('-pw', default=None)
    parser.add_argument('--site', '-S', default=None)
    parser.add_argument('--datasource_name', '-dn', required=True, help='datasource name')
    parser.add_argument('--logging-level', '-l', choices=['debug', 'info', 'error'], default='error',
                        help='desired logging level (set to error by default)')
    
    args = parser.parse_args()   

    if args.pw is None:
        password = getpass.getpass("Password: ")
    else:
        password = args.pw

     # Set logging level based on user input, or error by default
    logging_level = getattr(logging, args.logging_level.upper())
    logging.basicConfig(level=logging_level)

    # SIGN IN
    tableau_auth = TSC.TableauAuth(args.username, password, args.site)
    server = TSC.Server(args.server)
    server.use_highest_version()
    with server.auth.sign_in(tableau_auth):

        #Get datasource specified by name
        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                 TSC.RequestOptions.Operator.Equals,
                                 args.datasource_name))
        matching_datasources, pagination_item = server.datasources.get(req_option)

        #get all server tasks and get id of matching_datasource
        # example task formatted as string
        # <Task#c04bb70f-922a-4b7e-812e-bc4c95a77da5 RefreshExtractTask pri(50) failed(0) schedule_id(83e2c10e-9642-449b-aa1e-4577bcc66c34) target(<Target#eb4e72e2-0c0d-4287-a1fe-090b599a1d1a, datasource>)>

        tasks, pagination = server.tasks.get()                
        if len(matching_datasources) > 0:
            for task in tasks:
                #print(task)
                if ("{}".format(task)).find(matching_datasources[0].id) > -1:
                    task_id = ("{}".format(task))[6:42]
                    print("Found a refresh job for datasource: " + args.datasource_name + ", task id: " + task_id )
                    print("")
                    print("Running the refresh job now (asynchronously)...")
                    print("")
                        
                    # run refresh task
                    print(server.tasks.run(task))
                # else:
                #     print("Can't find a refresh Task for datasource: " + args.datasource_name )
        else:
            print("Datasource " + args.datasource_name + " not found")

if __name__ == '__main__':
    main()
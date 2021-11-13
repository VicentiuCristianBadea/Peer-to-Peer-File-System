import tinydb
import Client


class DBHelper:
    def __init__(self):
        self.query = tinydb.Query()
        self.db = tinydb("server.json")
        self.clients_table = self.db.table("clients")

    # Registration
    def REGISTER(self, client):
        try:
            # TODO check for existing client
            if self.does_client_exist(client) is None:
                self.clients_table.insert(client)
                return True, None
            else:
                return False, "Already registered."
        except Exception as e:
            print(e)
            return False, "Database error."

    def DE_REGISTER(self, client):
        try:
            if self.does_client_exist(client) is None:
                return True
            else:
                if type(client) == str:
                    self.clients_table.remove(self.query.name == client)
                    return True
                elif type(client) == Client or type(client) == dict:
                    self.clients_table.remove(self.query.name == client['name]'])
                    return True
                else:
                    return False
        except Exception as e:
            print(e)
            return False

    # File Related
    def PUBLISH(self, client, files):
        try:
            existing_client = self.does_client_exist(client)
            if existing_client is None:
                return False, "Client not registered."
            else:
                existing_client = existing_client[0]
                existing_files = existing_client['files']
            try:
                assert type(files) == list
            except:
                files = [files]
            for file in files:
                if file in existing_files:
                    continue
                else:
                    existing_files.append(file)
            self.clients_table.update({'files': existing_files}, self.query.name == client['name'])
            return True, None
        except Exception as e:
            print(e)
            return False, "Database Error"
        pass

    def REMOVE(self, client, files):
        try:
            existing_client = self.does_client_exist(client)
            if existing_client is not None:
                existing_client = existing_client[0]
                client_files = existing_client['files']
                for file in files:
                    if file in client_files:
                        client_files.remove(file)
                existing_client['files'] = client_files
                self.update_client_data(existing_client)
                return True, None
            else:
                return False, "Client not registered."
        except Exception as e:
            print(e)
            return False, "Database error."

    # Retrieving Information

    def RETRIEVE_ALL(self):
        list_of_everything = {}
        try:
            all_clients = self.clients_table.all()
            all_clients_stripped = []
            for client in all_clients:
                all_clients_stripped.append(client.get_client_data())
            list_of_everything['clients'] = all_clients_stripped
            files_dict = self.get_file_dict()
            list_of_everything['files'] = files_dict
            return True, list_of_everything
        except Exception as e:
            print(e)
            return False, "Database error."

    def SEARCH_FILE(self, name):
        client_list = []
        try:
            clients = self.clients_table.search(self.query.files.any([name]))
            for client in clients:
                client_list.append(client.get_client_connection())
            return True, client_list
        except Exception as e:
            print(e)
            return False, "Database error."

    def RETRIEVE_INFOT(self, name):
        try:
            existing_client = self.does_client_exist(name)
            if existing_client is not None:
                existing_client = existing_client[0]
                existing_client = existing_client.get_client_data()
                return True, existing_client
            else:
                return False, "Client not registered."
        except Exception as e:
            print(e)
            return False, "Database error."

    # Helper Functions
    def does_client_exist(self, client):
        if type(client) == Client:
            client = client['name']
        elif type(client) == str:
            pass
        else:
            print(f"does_client_exist expecting Client or String, received {type(client)}")
            return None
        found_client = self.clients_table.search(self.query.name == client)
        if len(found_client) == 1:
            return found_client[0]
        else:
            return None

    def update_client_data(self, client):
        existing_client = self.does_client_exist(client)
        try:
            if existing_client is not None:
                self.clients_table.remove(existing_client['name'])
                self.clients_table.insert(client)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_file_dict(self):
        files_dict = {}
        try:
            clients = self.clients_table.all  # Get full list of all clients and their files
            for client in clients:
                files = client['files']   # Get a list of all files from that client
                for file in files:
                    file_name = file['name']
                    if file_name in files_dict:  # If the file has been added to the list already
                        clients_with_file = files_dict[file_name]  # Get the list of clients associated with the file
                        clients_with_file.append(client.get_client_connection())  # Append the new client to the list
                        files_dict[file_name] = clients_with_file  # Reassign the list of clients
                    else:
                        files_dict[file_name] = [client.get_client_connection()]  # put the first client in a list
        except Exception as e:
            print(e)
        finally:
            return files_dict

import tinydb
#import Client


class DBHelper:
    def __init__(self):
        self.query = tinydb.Query()
        self.db = tinydb("server.json")
        self.clients_table = self.db.table("clients")

    def add_file(self, client, files):
        try:
            existing_client = self.clients_table.search(self.query.name == client['name'])
            if len(existing_client) == 1:
                existing_client = existing_client[0]
                existing_files = existing_client['files']
            else:
                return False
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
        except Exception as e:
            print(e)
        pass

    def rem_file(self, client, files):
        try:
            if type(files) == dict:
                files = [files]
            for file in files:
                pass
        except Exception as e:
            print(e)
        pass

    def get_file_list(self):
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

    def get_one_file(self, name):
        client_list = []
        try:
            clients = self.clients_table.search(self.query.files.any([name]))
            for client in clients:
                client_list.append(client.get_client_connection())
        except Exception as e:
            print(e)
        finally:
            return client_list

    def add_client(self, client):
        try:
            # TODO check for existing client
            self.clients_table.insert(client)
            return True
        except Exception as e:
            print(e)
            return False

    def rem_client(self, client):
        try:
            self.clients_table.remove(self.query.name == client['name]'])
        except Exception as e:
            print(e)
        pass

    def get_client_list(self):
        try:
            return self.clients_table.all
        except Exception as e:
            print(e)
        pass

    def get_one_client(self, name):
        pass



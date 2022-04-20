from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.soap = self.app.config["web"]
        self.client = Client(self.soap["baseURL"] + 'api/soap/mantisconnect.php?wsdl')

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        list = []
        result = self.client.service.mc_projects_get_user_accessible(
            self.app.config['web_admin']['username'], self.app.config['web_admin']['password'])
        for row in result:
            list.append(
                Project(id=row.id, name=row.name, status=row.status.name, view_state=row.view_state.name,
                        description=row.description))

        return list

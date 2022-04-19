import string
import random

from model.project import Project


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app, db):
    project = Project(name=(random_project_name("project_", 10)))
    old_projects_list = db.get_project_list()
    app.project.create_project(project)
    new_projects_list = db.get_project_list()
    old_projects_list.append(project)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)

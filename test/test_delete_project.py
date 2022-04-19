from model.project import Project
import random


def test_delete_some_group(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(name='test'))
    old_projects_list = db.get_project_list()
    project = random.choice(old_projects_list)
    app.project.delete_project_by_id(project.id)
    new_projects_list = db.get_project_list()
    assert len(old_projects_list) - 1 == len(new_projects_list)
    old_projects_list.remove(project)
    assert sorted(new_projects_list, key=Project.id_or_max) == sorted(old_projects_list, key=Project.id_or_max)

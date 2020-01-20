import json
    
_managers = dict()
_watchers = dict()

file = open('D:\workspace\source_file.json')
file_data = json.loads(file.read())

#sort all projects
file_data = sorted(file_data,  key=lambda x: x.get('priority'))

for project_info in file_data:
    
    project_name = project_info.get('name')
    project_priority = project_info.get('priority')

    for manager in project_info.get('managers', []):
        
        if manager not in _managers.keys():
            _managers[manager] = []

        _managers[manager].append({'project_name': project_name, 'priority': project_priority})

    for watcher in project_info.get('watchers', []):
        if watcher not in _watchers.keys():
            _watchers[watcher] = []

        _watchers[watcher].append({'project_name': project_name, 'priority': project_priority})



with open('managers.json', 'w') as m:
    json.dump(_managers, m)

with open('watchers.json', 'w') as w:
    json.dump(_watchers, w)

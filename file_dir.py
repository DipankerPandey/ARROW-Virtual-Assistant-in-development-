from windows_tools.installed_software import get_installed_software
a=[]
for software in get_installed_software():
    print(software['name'])
    a.append(software['name'])

for r in a:
    print(r)

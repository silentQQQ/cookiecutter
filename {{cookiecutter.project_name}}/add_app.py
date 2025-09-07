# When running the script, the user inputs the app name as a parameter. If no input is provided, show a prompt
# Copy the demo folder and its files to the apps folder, and modify the folder name
# - Replace 'demo' with the user-provided app name
# - Replace 'demo' under templates\demo with templates\app
# - Modify the settings.py file in the project folder, adding the app name to the INSTALLED_APPS list
# - Modify the urls.py file in the project folder, adding the app's URL configuration

import os
import sys
import shutil

# When running the script, the user inputs the app name as a parameter. If no input is provided, show a prompt
if len(sys.argv) < 2:
    print("Please input app name")

# Copy the demo folder and its files to the apps folder, and modify the folder name
# argv can read many app names
for i in range(1, len(sys.argv)):
    app_name = sys.argv[i]
    # Replace folder name    
    demo_folder = './apps/demo'
    app_folder = os.path.join('apps', app_name)
    if not os.path.exists(app_folder):
        shutil.copytree(demo_folder, app_folder)
    
    # Replace demo\templates\demo with templates\app_name
    template_folder = os.path.join(app_folder, 'templates/demo')
    if os.path.exists(template_folder):
        os.rename(template_folder, os.path.join(app_folder, 'templates', app_name))

    # From the first line of the readme.md file in the same directory, get the project name
    readme_file = 'readme.md'
    readme_path = os.path.join(os.getcwd(), readme_file)
    with open(readme_path, 'r',encoding='utf-8') as f:

        first_line = f.readline()
        project_name = first_line.split(' ')[1].strip()

    # In the project_name folder, get the path to the settings.py file
    settings_path = os.path.join(os.getcwd(), project_name, 'settings.py')
    # Add the app name to the INSTALLED_APPS list, open the file in read/write mode
    content = ''
    with open(settings_path, 'r',encoding='utf-8') as f:

        content = f.read()
        # Replace 'apps.demo' with 'apps.app_name'
        content = content.replace('apps.demo', f"apps.demo',\n\t'apps.{app_name}")

    with open(settings_path, 'w',encoding='utf-8') as f:
        f.write(content)


    # Replace 'apps.demo.urls' with 'apps.app_name.urls'
    urls_path = os.path.join(os.getcwd(), project_name, 'urls.py')
    lines = []
    with open(urls_path, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        # Find the line in lines that contains 'path('apps.demo/', include('apps.demo.urls')),\n'
        cur_index = 0
        for index,line in enumerate(lines):
            if 'apps.demo' in line:
                cur_index = index
                break
        # Add a line after cur_index
        lines.insert(cur_index+1, \
            f"\tpath('{app_name}/', include('apps.{app_name}.urls',namespace='{app_name}')),\n")

    with open(urls_path, 'w',encoding='utf-8') as f:
        f.writelines(lines)

    # Replace 'Demo' with app_name, capitalized, and 'demo' with app_name in apps.py
    apps_path = os.path.join(os.getcwd(), 'apps', app_name, 'apps.py')
    with open(apps_path, 'r',encoding='utf-8') as f:
        content = f.read()
        # Replace 'Demo' with app_name, capitalized
        content = content.replace('Demo', app_name.capitalize())
        # Replace 'demo' with app_name
        content = content.replace('demo', app_name)
        # Write to file
        with open(apps_path, 'w',encoding='utf-8') as f:
            f.write(content)
    
    
    # Replace 'apps.urls'->app_label 'demo' with app_name
    urls_path = os.path.join(os.getcwd(),'apps',app_name,'urls.py')
    with open(urls_path, 'r',encoding='utf-8') as f:
        content = f.read()
        content = content.replace('demo',app_name)
    
    with open(urls_path, 'w',encoding='utf-8') as f:
        f.write(content)

    print(f"App {app_name} has been added to project {project_name}")
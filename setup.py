import argparse
from datetime import date
import os

subproject_default_folders = ["include", "src", "test"]


def EOF():
    if os.name == "nt":
        return "\r\n"
    else:
        return "\n"


def new_readme(project_name, path):
    f = open(f"{path}/README.md", "w")
    f.write(f"# {project_name.upper()}{EOF()}")
    f.write(f"{EOF()}")
    f.write(f"{EOF()}")
    f.write(f"## Library Supports{EOF()}")
    f.write(f"| Name | Description |{EOF()}")
    f.write(f"|---|---|{EOF()}")
    f.write(f"{EOF()}")
    f.write(f"## License{EOF()}")
    f.write(f"This project is licensed under the [Apache License](../LICENSE){EOF()}")
    f.close()


def detect_end_of_line_char(line):
    if "\r\n" in line:
        return "\r\n"
    else:
        return "\n"


def update_project_readme(project_name, path):
    f = open(f"./README.md", 'r+')
    contents = f.readlines()
    eol = detect_end_of_line_char(contents[0])

    subprojects_index = contents.index(f"## Sub Libraries{eol}")
    subproject_info_insert_index = contents.index(eol, subprojects_index)
    contents.insert(subproject_info_insert_index, f"| [{project_name.upper()}]({path}/README.md) |   |{eol}")

    version_history_index = contents.index(f"## Version History{eol}")
    license_index = contents.index(f"## License{eol}")
    for i in range(version_history_index, license_index, 1):
        wip_version_history_index = i
        if "WIP" in contents[i]:
            break
    wip_version_history_insert_index = contents.index(eol, wip_version_history_index)
    contents.insert(wip_version_history_insert_index, f"- Create New Sub Library {project_name.upper()}{eol}")

    f.seek(0)
    f.writelines(contents)
    f.close()

def create_new_subproject(project_name):
    print(f"Creating new subproject {project_name}")
    subproject_path = f"./{project_name}"
    subproject_datasheets_path = f"./Documents/Datasheets/{project_name}"
    if not os.path.exists(subproject_path):
        os.makedirs(subproject_path)
        for folder in subproject_default_folders:
            os.makedirs(f"{subproject_path}/{folder}")

        subproject_name = project_name.replace("_", " ").upper()
        new_readme(subproject_name, subproject_path)

        update_project_readme(subproject_name, subproject_path)

        if not os.path.exists(subproject_datasheets_path):
            os.makedirs(subproject_datasheets_path)

        print(f"Created new subproject {project_name}")
    else:
        print(f"subproject {project_name} is already exist")


def generate_file_document(name):
    file_documents = []
    file_documents.append(f"/**{EOF()}")
    file_documents.append(f" ******************************************************************************{EOF()}")
    file_documents.append(f" * @file {name}{EOF()}")
    file_documents.append(f" * @brief <discription>{EOF()}")
    file_documents.append(f" *{EOF()}")
    file_documents.append(f" * @dauthor Zhen Wei{EOF()}")
    file_documents.append(f" * @date {date.today().strftime("%m/%d/%Y")}{EOF()}")
    file_documents.append(f" ******************************************************************************{EOF()}")
    file_documents.append(f" * @copyright{EOF()}")
    file_documents.append(f" * Copyright (c) {date.today().year}{EOF()}")
    file_documents.append(f" * All rights reserved.{EOF()}")
    file_documents.append(f" *{EOF()}")
    file_documents.append(f" ******************************************************************************{EOF()}")
    file_documents.append(f" */{EOF()}")
    return file_documents


def create_new_header_file(name, project):
    file_path = f"./{project}/include/{name}.h"
    print(f"Creating {file_path}")
    if not os.path.exists(file_path):
        file_containts = generate_file_document(f"{name}.h")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"#ifndef {name.upper()}_H__{EOF()}")
        file_containts.append(f"#define {name.upper()}_H__{EOF()}")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"// Includes{EOF()}")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"#ifdef __cplusplus{EOF()}")
        file_containts.append(f"extern \"C\" {"{"}{EOF()}")
        file_containts.append(f"#endif{EOF()}")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"// Header file body{EOF()}")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"#ifdef __cplusplus{EOF()}")
        file_containts.append(f"{"}"}{EOF()}")
        file_containts.append(f"#endif{EOF()}")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"#endif /* {name.upper()}_H__ */{EOF()}")

        f = open(file_path, "w")
        f.writelines(file_containts)
        f.close()
    else:
        print(f"file {file_path} is already exist")
        exit()


def create_new_src_file(name, project):
    file_path = f"./{project}/src/{name}.c"
    print(f"Creating {file_path}")
    if not os.path.exists(file_path):
        file_containts = generate_file_document(f"{name}.c")
        file_containts.append(f"{EOF()}")
        file_containts.append(f"#include <stdio.h>{EOF()}")
        file_containts.append(f"#include \"{name}.h\"{EOF()}")

        f = open(file_path, "w")
        f.writelines(file_containts)
        f.close()
    else:
        print(f"file {file_path} is already exist")
        exit()


def new_subproject(args):
    create_new_subproject(args.name) 


def new_library(args):
    print(f"Creating new library {args.name}")
    subproject_path = f"./{args.project}"
    if not os.path.exists(subproject_path):
        create_new_subproject(args.project)
    
    create_new_header_file(args.name, args.project)
    create_new_src_file(args.name, args.project)

    f = open(f"./README.md", 'r+')
    contents = f.readlines()
    eol = detect_end_of_line_char(contents[0])

    version_history_index = contents.index(f"## Version History{eol}")
    license_index = contents.index(f"## License{eol}")
    for i in range(version_history_index, license_index, 1):
        wip_version_history_index = i
        if "WIP" in contents[i]:
            break
    wip_version_history_insert_index = contents.index(eol, wip_version_history_index)
    contents.insert(wip_version_history_insert_index, f"- Add library for {args.name}{eol}")

    f.seek(0)
    f.writelines(contents)
    f.close()

    f = open(f"{subproject_path}/README.md", 'r+')
    contents = f.readlines()
    eol = detect_end_of_line_char(contents[0])

    library_supports_index = contents.index(f"## Library Supports{eol}")
    library_supports_insert_index = contents.index(eol, library_supports_index)
    contents.insert(library_supports_insert_index, f"| [{args.name}](./Documents/Datasheets/{args.name}.pdf) |   |{eol}")

    f.seek(0)
    f.writelines(contents)
    f.close()


def main():
    parser = argparse.ArgumentParser(
        prog='setup',
        description=''
    )
    subparser = parser.add_subparsers()

    new_subproject_parser = subparser.add_parser('new_subproject')
    new_subproject_parser.add_argument('-n', '--name', metavar='subproject_name', type=str, help='The name of the subproject', required=True)
    new_subproject_parser.set_defaults(func=new_subproject)

    new_library_parse = subparser.add_parser('new_library')
    new_library_parse.add_argument('-n', '--name', metavar='library_name', type=str, help='The name of the library', required=True)
    new_library_parse.add_argument('-p', '--project', metavar='subproject_name', type=str, help='The name of the subproject', required=True)
    new_library_parse.set_defaults(func=new_library)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
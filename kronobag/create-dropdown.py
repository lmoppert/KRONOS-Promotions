#!/usr/bin/env python3

import csv

GRADE_BLOCK = """              <div id="KRONOS{grade}" class="collapse" data-parent="#GradeDetails">
                <table class="table -striped table-hover table-sm">
                  <thead>
                    <tr class="table-light"><th colspan="4">KRONOS {grade}</th></tr>
                    <tr class="table-warning"><th>Weight</th><th>Type</th><th>Height</th><th class="px-3">&nbsp;</th></tr>
                  </thead>
                  <tbody>
                    {packages}
                  </tbody>
                </table>
              </div>"""
TABLE_ROW = """<tr class="linked-row" data-target="media/KRONOBag_{etype}-{height}.pdf" title="KRONOBag_{etype}-{height}.pdf">
                      <td>{weigth} kg</td><td>{etype}</td><td>{height} cm</td><td class="text-center"><i class="far fa-file-pdf"></i></td>
                    </tr>\n                    """

with open('grades.csv', 'r') as csvfile:
    packages = csv.reader(csvfile, delimiter=";")
    grade = ""
    package_list = ""
    for package in packages:
        if package[0] != grade:
            if grade != "":
                print(GRADE_BLOCK.format(
                    grade=grade, packages=package_list[:-21]))
            grade = package[0]
            package_list = ""
        package_list += TABLE_ROW.format(
            weigth=package[3], etype=package[1], height=package[2])

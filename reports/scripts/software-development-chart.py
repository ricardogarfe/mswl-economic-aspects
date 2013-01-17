# Copyright(c) 2013 by Ricardo Garcia Fernandez <ricardogarfe@gmail.com>
#
# This file is part of SCMAnalay.
#
# PyCha is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyCha is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with PyCha.  If not, see <http://www.gnu.org/licenses/>.
import cairo
import pycha.bar
import pycha.line
import sys
import pycha.pie
import pycha.stackedbar

def optionsAndLabels(labels):

    options = {
        'legend': {
            'hide': False,
            'position': {
                'top': 20,
                'left': 80,
            },
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': 'blue',
            },
        },
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=l) for i, l in enumerate(labels)],
                'label': 'Demanded',
            },
            'y': {
                'tickCount': 4,
                'label': 'Percentage',
            }
        },
        'padding': {
            'top': 20,
            'left': 40,
            'right': 20,
            'bottom': 40
        }
    }

    return options

def renderTotalsGraph():

    # Requested Profiles
    lines = (
        ('Functional analysis applications', 25.9),
        ('Web-application programming', 16.2),
        ('Structured programming', 15.2),
        ('Leadership of projects', 4.7),
        ('Software-Architecture', 4.5),
        ('Prototyping and web-layout', 3.5),
    )

    dataSet = [(line[0], [[0, line[1]]]) for line in lines]

    dataSet_labels = ((line[0]) for line in lines)

    options = optionsAndLabels(dataSet_labels)

    pieChart('requested-profiles-piechart.png', dataSet, options)

    # Requested Programming Languages
    lines = (
        ('Java', 12.4),
        ('PL/SQL', 10.8),
        ('J2EE', 10.6),
        ('HTML', 4.6),
        ('SQL', 4.6),
    )

    dataSet = [(line[0], [[0, line[1]]]) for line in lines]

    dataSet_labels = ((line[0]) for line in lines)

    options = optionsAndLabels(dataSet_labels)

    pieChart('requested-programming-language-piechart.png', dataSet, options)


def pieChart(output, dataSet, options):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 800, 800)

    chart = pycha.pie.PieChart(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(output)

if __name__ == '__main__':

    # Requested data from http://orientacion-laboral.infojobs.net/competencias-mas-demandadas-informatica-telecomunicaciones
    renderTotalsGraph()


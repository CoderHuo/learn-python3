from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json, pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def index(request):
    return bar_chart(request)

def bar_chart(request):
    return python_projects_bar()


def line_chart(request):
    return python_projects_line()


def get_project_start():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    print("Status code:", r.status_code)

    response_dict = r.json()
    repo_dicts = response_dict['items']
    names, stars = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])
    return names, stars


def python_projects_bar():
    names, stars = get_project_start()
    # 绘图
    my_style = LS('#333366', base_style=LCS)
    # 设置图标样式
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 24
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    bar_chart = pygal.Bar(my_config, style=my_style)
    bar_chart.title = 'Most-Starred Python Projects on GitHub'
    bar_chart.x_labels = names
    bar_chart.add('', stars)
    return bar_chart.render_django_response()


def python_projects_line():
    names, stars = get_project_start()
    # 绘图
    my_style = LS('#333366', base_style=LCS)
    # 设置图标样式
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 24
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.show_x_guides = True
    my_config.width = 1000

    line_chart = pygal.Line(my_config, style=my_style)
    line_chart.title = 'Most-Starred Python Projects on GitHub'
    line_chart.x_labels = names
    line_chart.add('', stars)
    return line_chart.render_django_response()

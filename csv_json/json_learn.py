#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

__author__ = 'Mr.Huo'


def main():
    # file_dir = os.getcwd()
    file_name = 'diameter.json'
    with open(file_name) as f:
        data = json.load(f)
    # print(data)

    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    print("Status code:", r.status_code)

    response_dict = r.json()
    print(response_dict.keys())

    print("Total repositories:", response_dict['total_count'])
    repo_dicts = response_dict['items']
    print("Repositories returned:", len(repo_dicts))

    repo_dict = repo_dicts[0]
    print("Keys:", len(repo_dict))
    for key in sorted(repo_dict):
        print(key)
    print("\nSelected information about first repository:")
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])

    names, stars = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

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
    #my_config.show_x_guides = True
    my_config.width = 1000

    # bar_chart = pygal.Bar(style=my_style, x_label_rotation=45)
    bar_chart = pygal.Bar(my_config, style=my_style)
    bar_chart.title = 'Most-Starred Python Projects on GitHub'
    bar_chart.x_labels = names
    bar_chart.add('', stars)
    bar_chart.render_to_file('C:\\Users\\zhuosha\\PycharmProjects\\python_repos_bar.svg')

    line_chart = pygal.Line(style=my_style, x_label_rotation=45)
    line_chart.title = 'Most-Starred Python Projects on GitHub'
    line_chart.x_labels = names
    line_chart.add('', stars)
    line_chart.render_to_file('C:\\Users\\zhuosha\\PycharmProjects\\python_repos_line.svg')


if __name__ == '__main__':
    main()

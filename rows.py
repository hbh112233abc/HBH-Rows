#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'huangbinghe@gmail.com'

import sublime
import sublime_plugin
from collections import Counter



class MaxCountCommand(sublime_plugin.TextCommand):

    def run(self, edit, without_empty_line=1):
        setting = sublime.load_settings("HBH-Rows.sublime-settings")
        # 获取页面内容
        content = self.view.substr(sublime.Region(0, self.view.size()))
        lines = content.split('\n')
        print(lines)
        if without_empty_line:
            lines = filter(lambda x: x,lines)
        print(lines)
        cnt = Counter(lines)
        print(cnt)
        print(cnt.most_common(1))
        max_line = cnt.most_common(1)[0]
        max_line_str = ':'.join(map(str,max_line))
        print(max_line_str)
        self.view.replace(edit,sublime.Region(0, self.view.size()),max_line_str)

class RepeatLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, repeat_count=2, without_empty_line=1):
        setting = sublime.load_settings("HBH-Rows.sublime-settings")
        # 获取页面内容
        content = self.view.substr(sublime.Region(0, self.view.size()))
        lines = content.split('\n')
        print(lines)
        if without_empty_line:
            lines = filter(lambda x: x,lines)
        print(lines)
        cnt = Counter(lines)
        print(cnt)
        repeat_lines = []
        for s,c in cnt.items():
            if c < repeat_count:
                continue
            repeat_lines.append((s,c))
        repeat_lines = sorted(repeat_lines,key=lambda x:x[1],reverse=1)
        print(repeat_lines)
        repeat_lines_str = '\n'.join(map(lambda x:'{}:{}'.format(x[0],x[1]),repeat_lines))
        self.view.replace(edit,sublime.Region(0, self.view.size()), repeat_lines_str)

class MergeLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        setting = sublime.load_settings("HBH-Rows.sublime-settings")

        # 获取页面内容
        content = self.view.substr(sublime.Region(0, self.view.size()))
        lines = content.split('\n')
        print(lines)

        content_lines = []
        n = 1
        for line in lines:
            if len(content_lines) < n:
                content_lines.append([])
            if not line:
                n += 1
                continue
            content_lines[n-1].append(line)
        content_lines = list(filter(lambda x: x,content_lines))
        print(content_lines)

        content_lines = list(zip(*content_lines))
        print(content_lines)

        merge_lines_str = '\n'.join(map(lambda x:','.join(x),content_lines))
        print(merge_lines_str)

        self.view.replace(edit,sublime.Region(0, self.view.size()), merge_lines_str)
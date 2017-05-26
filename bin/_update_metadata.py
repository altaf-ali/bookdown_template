#!/usr/bin/env python

import argparse
import fileinput
import re
import subprocess

class MetadataFixer:
  def __init__(self):
    self.user = None
    self.repo = None
    self.title = None

  def parse_args(self):
      arg_parser = argparse.ArgumentParser(description='update_project.py')
      arg_parser.add_argument('--title', required=True, help='project title')
      args = arg_parser.parse_args()
      self.title = args.title

  def fetch_config(self):
    result = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
    print("returned from subproces")
    origin_regex = '^(git@|https:\/{2})github.com[:\/]([0-9a-zA-Z-]*?)\/(.*?)\.git$'
    m = re.match(origin_regex, result.stdout.decode("utf-8"))
    if (len(m.groups()) == 3):
      self.user = m.group(2)
      self.repo = m.group(3)

  def update_description(self):
    with fileinput.FileInput("DESCRIPTION", inplace=True) as file:
      for line in file:
        line = re.sub("(?<=^Title:)(.*)$", " " + self.title, line)
        line = re.sub("(?<=^Package:)(.*)$", " " + self.repo, line)
        print(line, end = '')

  def update_index_rmd(self):
    with fileinput.FileInput("index.Rmd", inplace=True) as file:
      for line in file:
        line = re.sub("(?<=^title:)(.*)$", ' "%s"' % self.title, line)
        line = re.sub("(?<=^github-repo:)(.*)$", ' %s/%s' % (self.user, self.repo), line)
        print(line, end = '')

  def update_readme_md(self):
    with fileinput.FileInput("README.md", inplace=True) as file:
      for line in file:
        line = re.sub('(?<=https\:\/{2}travis-ci.org\/)(.*?)(?=.svg|\))', '%s/%s' % (self.user, self.repo), line)
        print(line, end = '')

  def run(self):
    self.fetch_config()
    print("    username: %s" % self.user)
    print("  repository: %s" % self.repo)
    self.parse_args()
    print("       title: %s" % self.title)

    self.update_description()
    self.update_index_rmd()
    self.update_readme_md()

MetadataFixer().run()

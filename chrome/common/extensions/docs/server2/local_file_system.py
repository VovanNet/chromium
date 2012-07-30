# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os

import file_system
from future import Future

class LocalFileSystem(file_system.FileSystem):
  """FileSystem implementation which fetches resources from the local
  filesystem.
  """
  def __init__(self, base_path):
    self._base_path = self._ConvertToFilepath(base_path)

  def _ConvertToFilepath(self, path):
    return path.replace('/', os.sep)

  def _ReadFile(self, filename, binary):
    with open(os.path.join(self._base_path, filename), 'r') as f:
      contents = f.read()
      if binary:
        return contents
      return file_system._ProcessFileData(contents, filename)

  def _ListDir(self, dir_name):
    all_files = []
    full_path = os.path.join(self._base_path, dir_name)
    for path in os.listdir(full_path):
      if path.startswith('.'):
        continue
      if os.path.isdir(os.path.join(full_path, path)):
        all_files.append(path + '/')
      else:
        all_files.append(path)
    return all_files

  def Read(self, paths, binary=False):
    result = {}
    for path in paths:
      if path.endswith('/'):
        result[path] = self._ListDir(self._ConvertToFilepath(path))
      else:
        result[path] = self._ReadFile(self._ConvertToFilepath(path), binary)
    return Future(value=result)

  def Stat(self, path):
    return self.StatInfo(os.stat(os.path.join(self._base_path, path)).st_mtime)

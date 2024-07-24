#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""The __init__ module/file used in this case to start/initialize
our storage engine
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()  # Fs: Created a file storage instance
storage.reload()

# set this to your module directory, using forward slashes (/) not backward slashes (\):
export_dir = "C:/Program Files (x86)/Steam/steamapps/common/MountBlade Warband/Modules/PN_1.0"

import os
import sys

if not os.path.isdir(export_dir) or not os.access(export_dir, os.W_OK):
  sys.exit("ERROR: unable to write to module export directory '" + export_dir + "'.")

def export_path(file_name):
  return os.path.join(export_dir, file_name)

scan_module_textures = 1
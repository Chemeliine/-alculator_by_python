[app]

# (str) Title of your application
title = induperator

# (str) Package name
package.name = altan

# (str) Package domain (needed for android/ios packaging)
package.domain = altanschool.com

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ogg, kivy

# (list) List of inclusions using pattern matching
source.include_patterns = data/*.png, sound/*.ogg

# (str) Application versioning (method 1)
version = 0.1

docker run -it -v "$(pwd)":/home/user/hostcwd kivy/buildozer android debug

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
presplash.filename = %(source.dir)s/images/Logo-altan-general-light.png

# (str) Icon of the application
icon.filename = %(source.dir)s/images/Logo-altan-lp-icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.10.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = black

# (list) Permissions
android.permissions = INTERNET,CHANGE_WIFI_MULTICAST_STATE,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# (int) Android API to use
# see https://developer.android.com/distribute/best-practices/develop/target-sdk
android.api = 27

# (int) Android SDK version to use
android.sdk = 23

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

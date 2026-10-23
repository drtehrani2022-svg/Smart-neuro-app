[app]

# (str) Title of your application
title = SmartMed Test

# (str) Package name
package.name = smartmedtest

# (str) Package domain (needed for android/ios packaging)
package.domain = org.smartmed

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) Application requirements
requirements = python3,kivy==2.3.0,Cython==0.29.36

# (str) Application versioning (method 1)
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (bool) If True, then the application will be compiled for multiple archs.
android.accept_sdk_license = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist the application root
#android.whitelist =

# (str) Path to the whitelist file
#android.whitelist_src =

# (str) Path to the blacklist file
#android.blacklist_src =

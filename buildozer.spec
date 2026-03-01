[app]
title = My Application
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.1
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[buildozer:android]
android.accept_sdk_license = True
android.sdk_path = /home/runner/.android
android.ndk_path = /home/runner/.android/ndk
android.sdk_manager_tools_version = 9477386
android.ndk = 25b
android.sdk = 33
android.build_tools = 33.0.2
android.api = 33
android.minapi = 21
android.gradle_dependencies = 'androidx.core:core:1.9.0'

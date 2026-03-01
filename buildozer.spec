[app]
title = My Application
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[buildozer:android]
android.accept_sdk_license = True
android.ndk = 25b
android.sdk = 33
android.build_tools = 33.0.2  # 👈 الأهم هنا
android.api = 33
android.minapi = 21
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk

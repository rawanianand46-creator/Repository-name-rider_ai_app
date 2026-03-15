[app]

title = RiderAI
package.name = riderai
package.domain = org.rider

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1

[app:android]

android.api = 33
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET

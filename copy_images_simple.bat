@echo off
echo Copying image files...
for %%f in ("2025素材\2025素材\*.jpg") do copy /Y "%%f" "images\"
for %%f in ("2025素材\2025素材\*.mp4") do copy /Y "%%f" "images\"
echo Done.
dir /b images | find /c ".jpg"
echo JPG files copied.


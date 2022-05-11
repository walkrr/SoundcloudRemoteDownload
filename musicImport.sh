#!/bin/bash
touch post.sh
for dir in /home/mason/Utilities/tmp/*/
do
  echo $dir
  for file in "$dir"*.mp3
  do
    echo $file
    echo eyeD3 --add-lyrics "\"${file:0: -4}.lrc"\":sync "\"$file"\" >> post.sh
  done
  echo beet import -A "\"$dir"\" >> post.sh
  echo rm -r "\"$dir"\" >> post.sh
done
chmod +x post.sh
./post.sh
rm post.sh

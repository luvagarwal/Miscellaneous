# USAGE: download youtube playlists
# open the playlist in the browser and save the page. Now run this script with argument as the path to the save html page.

v=$(grep -no '<a href="https://.* class="playlist-video clearfix  spf-link "' "$1")

urls=$(echo $v | sed 's/[0-9]\+:/\n/g' | sed 's/<a href=\"\(.*\)\" class=\".*\"/\1/g')

for url in $urls; do youtube-dl $url; done


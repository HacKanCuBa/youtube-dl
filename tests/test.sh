#!/usr/bin/env bash
testurl=https://www.youtube.com/watch?v=zsVgoO65ykQ
tmp=$(mktemp -d -t ytdltest_XXXXXX)
echo '
-f "best[height <=? 480]"
--restrict-filenames
--embed-thumbnail
--no-mtime
--audio-quality 6
' > $tmp/test-config
echo "-o $tmp/%(title)s_%(id)s.%(ext)s
" >> $tmp/test-config

youtube-dl --config-location $tmp/test-config $testurl
echo conversion runs done.
echo =================================
file $tmp/*
youtube-dl --version
echo =================================
rm -r $tmp
echo cleaning up
echo all done.

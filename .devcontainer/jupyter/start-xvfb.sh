#!/bin/bash
Xvfb :99 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset &
export DISPLAY=:99
sleep 5
exec "$@"

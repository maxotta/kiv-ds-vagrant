#!/bin/bash
set -e
LOG_TAG="<*> container-startup: "
echo "$LOG_TAG Entry point STARTING."
echo "$LOG_TAG number of arguments: $#"
echo "$LOG_TAG arguments: '$@'"
# Start the OpenSSH daemon

if [ $# -eq 0 ]; then
    echo "$LOG_TAG Starting sshd (not detached)."
    /usr/sbin/sshd -D
else
    echo "$LOG_TAG Starting sshd (detached daemon)."
    /usr/sbin/sshd
    if [ ! -z "$STARTUP_DELAY" ] ; then
        echo "Startup delay is set to: $STARTUP_DELAY. Going to sleep for a while..."
        sleep $STARTUP_DELAY
    fi
    exec "$@"
fi
# reached only if a service dies
echo "$LOG_TAG Entry point TERMINATED."
# EOF

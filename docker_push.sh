#!/bin/bash
tag="latest"
#$(date +%s)
echo "qLtqP-nuwET6BC6EYSJh" | docker login registry.gitlab.com -u  "dewmal" --password-stdin
docker tag ceylonapp/fx-agent-engine "registry.gitlab.com/dewmal/fx_agent_platform/fx-agent-engine-image:${tag}"
docker push "registry.gitlab.com/dewmal/fx_agent_platform/fx-agent-engine-image"
#
#echo "dewmal91" | docker login -u "ceylonapp" --password-stdin
#docker push 'ceylonapp/fx-engine-base'
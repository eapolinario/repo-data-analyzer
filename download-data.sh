#!/bin/bash

for COMPONENT in flyte flyteidl flyteplugins flyteadmin flytecopilot datacatalog flytepropeller flytestdlib flytekit flyteconsole flytesnacks stow; do
	echo "Handling $COMPONENT" >&2
	REPO="flyteorg/$COMPONENT"
	gh pr list --repo "$REPO" --state merged --json number,title,mergedAt --limit 5000 | jq -r --arg prefix $COMPONENT '.[] | [$prefix, .number, .title, .mergedAt] | @csv'
done

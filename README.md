Code used to generate data about the flyte repositories.

In order to refresh data:

```
make download-data
```

This is going to write to `data/list.csv` data that looks like:

```
"flyte",1224,"Added kustomize support in docker sandbox","2021-07-26T06:22:52Z"
"flyte",1975,"Fix Docker image unambiguity in the getting started guide","2021-12-25T22:37:14Z"
"flytekit",512,"Implement fast register for pod tasks v2","2021-06-11T16:17:32Z"
"flytekit",1525,"Backport to 1.2 - Flytekit Auth system overhaul and pretty printing upgrade (#1458)","2023-02-28T19:54:30Z"
"flytepropeller",292,"Construct subnode DataDir to be under parent's node OutputDir to keep behavior consistent across","2021-07-14T02:36:41Z"
"flytekit",625,"0.15 pin idl to <0.20","2021-08-30T20:32:49Z"
"flyteadmin",87,"Remove todo comment","2020-04-07T16:57:43Z"
"flytesnacks",321,"Map pod task example","2021-07-06T18:55:15Z"
"flytepropeller",571,"Not stripping structure from literal types","2023-06-07T12:56:36Z"
"flytesnacks",921,"Reduces docs build warnings to 0","2022-11-15T19:21:11Z"
"flyteplugins",177,"Removed literals.go from flyteplugins and reusing it from flyteidl","2021-05-28T05:52:04Z"
"flyteidl",270,"Add workflow execution JSON schema","2022-04-07T05:56:36Z"
"flytepropeller",140,"bug; abort called for not started nodes","2020-05-30T00:10:24Z"
"flyte",4085,"move memverge doc","2023-09-28T19:24:50Z"
"flytesnacks",962,"Add DD integration details","2023-03-17T12:32:05Z"
"flyte",2398,"Updated launchplans.rst","2022-04-22T08:57:03Z"
"flyte",1907,"Make TLS secret name configurable","2021-12-07T20:23:32Z"
"flytekit",1593,"Backfill should fill in the right input vars","2023-04-21T20:41:31Z"
"flyteadmin",227,"add missing go.sum","2021-07-29T20:15:20Z"
"flyte",1118,"Update index.rst","2021-06-10T17:36:19Z"
```

Then run:

```
make generate-graphs
```

To refresh the final graphs (also in the data directory).

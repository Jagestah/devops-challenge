# devops-challenge
A quick challenge for incumbent DevOps Engineers

Your company has tasked you with writing an integration for the [Star Wars API](https://swapi.co/). The input of the integration will be similar to `input.yaml`. Write a script in Go or Python that will call out to the [Star Wars API](https://swapi.co/) and gather information on each object in `input.yaml`. The output should be in JSON format so that it can be ingested by another service, to be created in the future. An example of what the future service will expect has been provided as `output.json`.

Some criteria for the project:
- The output should be written to a file `swapi-output.json`.
- Build and include alternative `input.yaml` files.
- The script should be dockerized.
- The docker container should be deployable to Kubernetes via a Helm Chart
- Results should be posted to a public Github repo with an associated Pull Request.
- Send us a link to the PR.

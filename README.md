# devops-challenge
A quick challenge for incumbent DevOps Engineers

Write a script in Go or Python that will call out to the [Star Wars API](https://swapi.co/) and gather information on each object in `input.yaml`.

- a `.json` file should be created for each object in `input.yaml`.
- the naming convention should match `<object.name>.json` for each object.
- The script should be dockerized and be able to run alternative `input.yaml` files.
- The docker container should be deployable to Kubernetes via a Helm Chart
- Results should be posted to a public Github repo with an associated Pull Request.

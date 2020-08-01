# TrackLog

By Google Summer Product Sprint GCN Team #2

## Setup Development Environment

### Required Softwares

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/downloads/)
- [Pipenv (optional)](https://github.com/pypa/pipenv)
- [Node](https://nodejs.org/)
- [Yarn](https://yarnpkg.com/getting-started/install)
- [Cloud SDK (optional)](https://cloud.google.com/sdk/docs)

### Install Dependencies

Setup and use Python virtual environment:

```
$ pipenv install --dev
$ pipenv shell
```

or use a traditional way to install dependencies:

```
$ pip install -r requirements.txt
```

Install Node.js dependencies:

```
$ yarn install
```

### Run Applications

```
$ flask init-db
$ flask run
$ yarn serve
```

Flask will run on port 5000 and Vue will serve on port 8080.

### Continuous Deployment

The project is now configured with Cloud Build. After a PR to `master` branch being merged, Cloud Build will automatically trigger a build and deploy the updated contents. There is no need to deploy the site yourself.

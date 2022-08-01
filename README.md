# interview-algorand

Interview project for Algorand

# Objective

> Coding Exercise:
> In your language of choice. Please write a program that uses the GitHub API to return as a JSON of open issues with their labels from a GitHub repository.
> It should take a parameter of the repository to query.

# Quick Start

## With pip

### Install the package

```bash
pip install ./interview_algorand-0.1.0-py3-none-any.whl
```

### Run the program

```bash
export ALGORAND_GH_USER=<your-github-username>
export ALGORAND_GH_TOKEN=<your-github-token>
gh_issues_cli --repo <repository>
```

(where <repository> is the name of the repository you want to query)

## With Poetry

If you have [Poetry](https://python-poetry.org/docs/master/) installed, you can run the following commands:

### Install the package

```bash
poetry install
```

### Run the program

```bash
export ALGORAND_GH_USER=<your-github-username>
export ALGORAND_GH_TOKEN=<your-github-token>
poetry run gh_issues_cli --repo <your-github-repo>
```

## With Docker

If you have [Docker](https://www.docker.com/) installed, you can run the following commands:

```bash
docker build -t 'algorand-interview:latest' .
docker run -it --rm -e ALGORAND_GH_USER=<your-github-username> -e ALGORAND_GH_TOKEN=<your-github-token> algorand-interview:latest
/home/runtime/.local/bin/gh_issues_cli --repo <your-github-repo>
```

Or even uninteractive:

```bash
docker run --rm -e ALGORAND_GH_USER=<your-github-username> -e ALGORAND_GH_TOKEN=<your-github-token> algorand-interview:latest /home/runtime/.local/bin/gh_issues_cli --repo <your-github-repo>
```

# Configuration

Set the environment variables ALGORAND_GH_USER and ALGORAND_GH_TOKEN.

```bash
export ALGORAND_GH_USER=<your-github-username>
export ALGORAND_GH_TOKEN=<your-github-token>
```

You can also use `.env` file to set the environment variables.

# Caveats

* Python-Poetry is new to me, I've been using [pipenv](https://pipenv.pypa.io/en/latest/) for a while, but Poetry seems
  to be the new direction of package management.
* I'm very much under-utilising pydantic, but it has nice settings helpers.
* Tests? There's probably another round of refactoring that can be done with tests. I YOLO'd it this time :-/...

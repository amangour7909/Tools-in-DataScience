# Learning UV and Example Project

## Steps to Learn UV

1. **Install UV**
   - Download the UV installer from the official website.
   - Run the installer and follow the on-screen instructions.
   - Restart your computer after installation is complete.

2. **Set Up Example Project**
   - Create a new directory for your project.
   - Initialize a new UV project using `uv init`.

3. **Write Your First UV Script**
   - Create a new file `hello.uv`.
   - Write a simple script to print a message.

4. **Run Your UV Script**
   - Use the command `uv run hello.uv` to execute your script.

5. **Explore UV Features**
   - Experiment with different UV commands and features.
   - Refer to the UV documentation for more advanced usage.

## Example Project

This project contains a simple script to demonstrate UV usage.

## Frequently Used Commands

- `uv init`: Initialize a new UV project.
- `uv run <file.uv>`: Run a UV script.
- `uv build`: Build the UV project.
- `uv test`: Run tests for the UV project.
- `uv remove` 
- `uv tree`: view all dependencies

## UV Ecosystem

### Virtual Environments (venv)

UV supports virtual environments to manage project-specific dependencies. You can create a virtual environment using the command:

```sh
uv venv create
```

### pyproject.toml

The `pyproject.toml` file is used to configure the UV project. It contains metadata about the project, dependencies, and build instructions. Here is an example of a `pyproject.toml` file:

```toml
[tool.uv]
name = "example_project"
version = "0.1.0"
description = "An example project to learn UV"

### uv sync
    create uv ecosystem for existing uv project
    it ensures all the project dependencies are installed and up to date

### add inline script metadata and dependencies 
    add dependencies in script with metadata in same file that program need to run.
    /// script
    requires-python = ">=3.11"
    dependencies = [
        "requests"
    ]
    ///
    uv run file.py

    - add script from console
    `uv add --script file.py 'requests'`

### virtual environment
    - when we create project with uv it automatically creates venv when we add dependencies
    - `uv venv` to create venv manually
    - `./venv/Scripts/activate` to activate

### How to set parameters to http request
    - curl "http://example.com/api/resource?param1=value1&param2=value2"
    - import requests

        params = {
            'param1': 'value1',
            'param2': 'value2'
        }
        response = requests.get('http://example.com/api/resource', params=params)
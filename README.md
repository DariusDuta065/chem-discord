# Welcome to your CDK Python project

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory. To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

- `cdk ls` list all stacks in the app
- `cdk synth` emits the synthesized CloudFormation template
- `cdk deploy` deploy this stack to your default AWS account/region
- `cdk diff` compare deployed stack with current state
- `cdk docs` open CDK documentation

## Dev tools

- Trigger lambda locally using SAM

  - requires `homebrew` & `sam-cli` to be installed
  - requires `docker` for the Lambda runtime container
  - run `cdk synth` every time there are changes to functions
  - `sam local invoke -t cdk.out/DiscordLambda-dev.template.json DiscordBotLambda`

- Invoke Lambda with custom events & payloads

  ```bash
    sam local invoke \
      -t cdk.out/DiscordLambda-dev.template.json \
      -e ./discord_bot/events/general_message.json \
      DiscordBotLambda
  ```

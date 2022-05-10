#!/usr/bin/env python3
import aws_cdk as cdk
from discord_lambda.discord_lambda_stack import DiscordLambdaStack

from config import get_config

app = cdk.App()

context_env = app.node.try_get_context("env")
config = get_config(context_env if context_env else "dev")
env = cdk.Environment(account=config.account_id, region=config.region)

DiscordLambdaStack(
    app, f"DiscordLambda-{config.env}",
    env=env,
    config=config
)

app.synth()

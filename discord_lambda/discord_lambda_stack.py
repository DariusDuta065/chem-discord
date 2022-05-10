from os import path, getcwd

from aws_cdk import (
    BundlingOptions,
    DockerImage,
    Stack,
    Duration,
    CfnOutput,
    aws_lambda as _lambda
)

from constructs import Construct

from config import Config


class DiscordLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, config: Config, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        discord_bot_fn = _lambda.Function(
            self, "DiscordBotLambda",
            memory_size=2048,
            handler="discord_bot.handler",
            timeout=Duration.seconds(10),
            runtime=_lambda.Runtime.PYTHON_3_9,
            architecture=_lambda.Architecture.ARM_64,
            environment={
                "DISCORD_BOT_TOKEN": config.bot_token
            },
            code=_lambda.Code.from_asset(
                path.join(getcwd(), "discord_bot"),
                bundling=BundlingOptions(
                    image=DockerImage.from_registry("python:3.9-alpine"),
                    command=[
                        "sh", "-c", "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
                    ]
                )
            ),
        )

        discord_bot_fn_url = discord_bot_fn.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
            cors=_lambda.FunctionUrlCorsOptions(
                allowed_origins=['*'],
                allowed_headers=['*'],
                allowed_methods=[_lambda.HttpMethod.ALL]
            )
        )

        CfnOutput(
            self, "DiscordBotLambdaURL",
            value=discord_bot_fn_url.url
        )

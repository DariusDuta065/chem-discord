import os
import json
import requests

bot_token = os.getenv('DISCORD_BOT_TOKEN', None)

channels = {
    "general": "912446110394642445",
    "logging": "912449228683497482",
    "events": "912449246354079754"
}


def send_message(message: str, channel: str):
    if channel not in channels:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'Requested channel not found'
            })
        }

    channel_snowflake = channels[channel]
    print(f"Sending to {channel_snowflake}: {message}")

    res = requests.post(
        f"https://discord.com/api/v9/channels/{channel_snowflake}/messages",
        data={
            "content": message
        },
        headers={
            "Authorization": bot_token
        }
    )

    if res.status_code == 200:
        return {
            'statusCode': 200,
            'body': {
                'success': f'Message sent to {channel}'
            }
        }

    return {
        'statusCode': res.status_code,
        'body': {
            'error': 'Message not sent'
        }
    }


def validate_req(event) -> tuple[bool, dict]:
    if not 'body' in event:
        return False, None, {
            'statusCode': 405,
            'body': {
                'error': 'POST request required'
            }
        }

    body = json.loads(event['body'])

    if not 'channel' in body or not 'message' in body:
        return False, None, {
            'statusCode': 400,
            'body': json.dumps({
                'error': "Provide valid 'channel' and 'message'"
            })
        }

    return True, body, None


def handler(event, _):
    is_valid, body, err = validate_req(event)

    if not is_valid:
        return err

    return send_message(body['message'], body['channel'])

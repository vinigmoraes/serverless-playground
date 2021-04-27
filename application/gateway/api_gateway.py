import json


def parse_json(event: dict):
    try:
        possible_body = event.get("body", "{}")
        return json.loads(possible_body)
    except Exception:
        return dict()


class ApiGatewayEvent:
    def __init__(self, event, context):
        self.query = event.get("queryStringParameters", {})
        self.body = parse_json(event)
        self.headers = event.get("headers", {})
        self.request_id = context.aws_request_id

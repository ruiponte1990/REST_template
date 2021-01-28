import json
import logging
import Event
import Response
from service import service
from exceptions import BadRequestException, NotFoundException, UnauthorizedException, \
    MethodNotAllowedException, ConflictException, NoContentException

def handler(event, context):
    action_map = {
        "service" : service.service
    }
    event = Event(event)
    response = Response()
    paths = event.get_path()
    method = event.get_request_method()
    if method == "OPTIONS":
        return response.no_content()
    for path in paths:
        if path in action_map:
            try:
                data = action_map[path](event)
                return response.success(content=json.dumps(data))
            except BadRequestException as ex:
                logging.error(ex)
                return response.bad_request(content=str(ex), escape=True)
            except UnauthorizedException as ex:
                logging.error(ex)
                return response.unauthorized(escape=True)
            except MethodNotAllowedException as ex:
                logging.error(ex)
                return response.method_not_allowed(escape=True)
            except ConflictException as ex:
                logging.error(ex)
                return response.conflict(escape=True)
            except NoContentException as ex:
                logging.error(ex)
                return response.no_content(escape=True)
            except Exception as ex:
                logging.error(ex)
                return response.error(escape=True)
    return response.not_found(escape=True)
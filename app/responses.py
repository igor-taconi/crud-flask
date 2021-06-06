from typing import Any, Dict, Tuple, Union

ExtraInfo = Dict[Any, Any]
StatusCode = int
Status = Dict[str, Union[int, bool]]
Message = Dict[str, Union[str, Status]]
Response = Tuple[Message, StatusCode]


def create_response(data: Message, status_code: StatusCode) -> Response:
    return data, status_code


def create_message(
    message: str,
    error: bool,
    success: bool,
    status_code: int,
    extra_info: ExtraInfo = None
) -> Message:
    data = {
        'status': {
            'code': status_code,
            'success': success,
            'error': error
        },
        'mensage': message,
    }
    if isinstance(extra_info, dict):
        data.update(extra_info)

    return data


def create_error_response(
    message: str, status_code: int = 400, extra_info: ExtraInfo = None
) -> Response:
    data = create_message(
        message=message,
        error=True,
        success=False,
        status_code=status_code,
        extra_info=extra_info
    )

    return create_response(data, status_code)


def create_success_response(
    message: str, status_code: int = 200, extra_info: ExtraInfo = None
) -> Response:
    data = create_message(
        message=message,
        error=False,
        success=True,
        status_code=status_code,
        extra_info=extra_info
    )

    return create_response(data, status_code)

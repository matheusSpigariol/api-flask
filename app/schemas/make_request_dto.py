from app.schemas.dtos.request_dto import RequestDTO


def make_request_dto(data, **kwatgs) -> RequestDTO:
    request_data = RequestDTO(
        name=data['name'],
        email=data['email']
    )

    return request_data

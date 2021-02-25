from exceptions import BadRequestException, UnauthorizedException, NotFoundException, ConflictException, \
    UnprocessableException, PayloadTooLarge


def test_bad_request_exception(app_context):
    with app_context:
        ex = BadRequestException()
        assert ex.code == 400
        assert ex.description == 'Bad Request Exception'


def test_unauthorized_exception(app_context):
    with app_context:
        ex = UnauthorizedException()
        assert ex.code == 401
        assert ex.description == 'Unauthorized Exception'


def test_not_found_exception(app_context):
    with app_context:
        ex = NotFoundException()
        assert ex.code == 404
        assert ex.description == 'Not Found Exception'


def test_conflict_exception(app_context):
    with app_context:
        ex = ConflictException()
        assert ex.code == 409
        assert ex.description == 'Conflict Exception'

def test_unprocessable_exception(app_context):
    with app_context:
        ex = UnprocessableException()
        assert ex.code == 422
        assert ex.description == 'Unprocessable Exception'

def test_payload_to_large_exception(app_context):
    with app_context:
        ex = PayloadTooLarge()
        assert ex.code == 413
        assert ex.description == 'Payload Too Large'

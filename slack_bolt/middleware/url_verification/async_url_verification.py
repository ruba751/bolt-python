from typing import Callable, Awaitable

from slack_bolt.logger import get_bolt_logger
from .url_verification import UrlVerification
from slack_bolt.middleware.async_middleware import AsyncMiddleware
from slack_bolt.request.async_request import AsyncBoltRequest
from slack_bolt.response import BoltResponse


class AsyncUrlVerification(UrlVerification, AsyncMiddleware):
    def __init__(self):
        self.logger = get_bolt_logger(AsyncUrlVerification)

    async def async_process(
        self,
        *,
        req: AsyncBoltRequest,
        resp: BoltResponse,
        next: Callable[[], Awaitable[BoltResponse]],
    ) -> BoltResponse:
        if self._is_url_verification_request(req.payload):
            return self._build_success_response(req.payload)
        else:
            return await next()
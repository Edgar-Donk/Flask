Status Codes
============

The flask server in development mode shows status codes after every operation.

Informational - 1xx
-------------------

This class of status code indicates a provisional response::

   HTTP_100_CONTINUE
   HTTP_101_SWITCHING_PROTOCOLS

Successful - 2xx
----------------

This class of status code indicates that the client's request was successfully 
received, understood, and accepted::

   HTTP_200_OK
   HTTP_201_CREATED
   HTTP_202_ACCEPTED
   HTTP_203_NON_AUTHORITATIVE_INFORMATION
   HTTP_204_NO_CONTENT
   HTTP_205_RESET_CONTENT
   HTTP_206_PARTIAL_CONTENT

Redirection - 3xx
-----------------

This class of status code indicates that further action needs to be taken by 
the user agent in order to fulfill the request::

   HTTP_300_MULTIPLE_CHOICES
   HTTP_301_MOVED_PERMANENTLY
   HTTP_302_FOUND
   HTTP_303_SEE_OTHER
   HTTP_304_NOT_MODIFIED
   HTTP_305_USE_PROXY
   HTTP_306_RESERVED
   HTTP_307_TEMPORARY_REDIRECT

Client Error - 4xx
------------------

The 4xx class of status code is intended for cases in which the client seems 
to have erred. Except when responding to a HEAD request, the server SHOULD 
include an entity containing an explanation of the error situation, and whether 
it is a temporary or permanent condition::

   HTTP_400_BAD_REQUEST
   HTTP_401_UNAUTHORIZED
   HTTP_402_PAYMENT_REQUIRED
   HTTP_403_FORBIDDEN
   HTTP_404_NOT_FOUND
   HTTP_405_METHOD_NOT_ALLOWED
   HTTP_406_NOT_ACCEPTABLE
   HTTP_407_PROXY_AUTHENTICATION_REQUIRED
   HTTP_408_REQUEST_TIMEOUT
   HTTP_409_CONFLICT
   HTTP_410_GONE
   HTTP_411_LENGTH_REQUIRED
   HTTP_412_PRECONDITION_FAILED
   HTTP_413_REQUEST_ENTITY_TOO_LARGE
   HTTP_414_REQUEST_URI_TOO_LONG
   HTTP_415_UNSUPPORTED_MEDIA_TYPE
   HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
   HTTP_417_EXPECTATION_FAILED
   HTTP_428_PRECONDITION_REQUIRED
   HTTP_429_TOO_MANY_REQUESTS
   HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE

Server Error - 5xx
------------------

Response status codes beginning with the digit "5" indicate cases in which 
the server is aware that it has erred or is incapable of performing the request. 
Except when responding to a HEAD request, the server SHOULD include an entity 
containing an explanation of the error situation, and whether it is a temporary 
or permanent condition::

   HTTP_500_INTERNAL_SERVER_ERROR
   HTTP_501_NOT_IMPLEMENTED
   HTTP_502_BAD_GATEWAY
   HTTP_503_SERVICE_UNAVAILABLE
   HTTP_504_GATEWAY_TIMEOUT
   HTTP_505_HTTP_VERSION_NOT_SUPPORTED
   HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
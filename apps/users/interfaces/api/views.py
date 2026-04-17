import logging
import traceback

from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status

from apps.users.application.use_cases.login_user import LoginUser
from apps.users.application.use_cases.register_user import RegisterUser
from apps.users.application.use_cases.logout_user import LogoutUser
from apps.users.application.dto.login_dto import LoginDTO
from apps.users.application.dto.register_dto import RegisterDTO
from apps.users.domain.exceptions.auth_exceptions import InvalidCredentials, UserAlreadyExists

from apps.users.infrastructure.repositories.django_user_repository import DjangoUserRepository
from apps.users.infrastructure.repositories.django_token_repository import DjangoTokenRepository
from apps.users.infrastructure.repositories.django_session_repository import DjangoSessionRepository

from apps.users.infrastructure.serializers.user_serializer import LoginSerializer, RegisterSerializer, LogoutSerializer
from apps.audit.infrastructure.services.ip_resolver import get_client_ip


logger = logging.getLogger(__name__)


def _ok(data=None, message="OK", pagination=None):
    return {"message": message, "data": data if data is not None else {}, "pagination": pagination, "error": None}


def _fail(message, detail=None):
    return {"message": message, "data": {}, "pagination": None, "error": detail if detail is not None else message}


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    try:
        # 🔐 VALIDACIÓN
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                _fail("Invalid data", serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )

        data = serializer.validated_data

        # DTO limpio
        dto = LoginDTO(
            email=data['email'],
            password=data['password'],
            ip=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT')
        )

        service = LoginUser(
            DjangoUserRepository(),
            DjangoTokenRepository(),
            DjangoSessionRepository()
        )

        result = service.execute(dto)
        from apps.audit.infrastructure.services.audit_logger import log_session_login
        log_session_login(
            user_id=result["user_id"],
            session_started_at=result.get("session_started_at"),
            ip_address=get_client_ip(request),
        )

        return Response(_ok(result, "Inicio de sesion correcto"), status=status.HTTP_200_OK)

    except InvalidCredentials:
        logger.warning(
            f"Login failed for email: {request.data.get('email')}"
        )

        return Response(
            _fail("Invalid credentials"),
            status=status.HTTP_401_UNAUTHORIZED
        )

    except Exception as e:
        logger.error(traceback.format_exc())

        return Response(
            _fail("Internal server error", str(e)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    try:
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                _fail("Invalid data", serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )

        data = serializer.validated_data
        dto = RegisterDTO(
            email=data["email"],
            password=data["password"],
            username=data.get("username"),
        )

        service = RegisterUser(DjangoUserRepository())
        result = service.execute(dto)
        from apps.audit.infrastructure.services.audit_logger import log_user_registered
        log_user_registered(
            user_id=result["id"],
            email=result["email"],
            ip_address=get_client_ip(request),
        )

        return Response(_ok(result, "Usuario registrado"), status=status.HTTP_201_CREATED)

    except UserAlreadyExists:
        return Response(
            _fail("User already exists"),
            status=status.HTTP_409_CONFLICT
        )

    except Exception as e:
        logger.error(traceback.format_exc())
        return Response(
            _fail("Internal server error", str(e)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    try:
        serializer = LogoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                _fail("Invalid data", serializer.errors),
                status=status.HTTP_400_BAD_REQUEST
            )

        refresh = serializer.validated_data["refresh"]
        service = LogoutUser(
            DjangoTokenRepository(),
            DjangoSessionRepository(),
        )
        result = service.execute(refresh)

        from apps.audit.infrastructure.services.audit_logger import log_session_logout
        log_session_logout(
            user_id=result["user_id"],
            session_started_at=result.get("session_started_at"),
            session_ended_at=result.get("session_ended_at"),
            ip_address=get_client_ip(request),
        )

        return Response(
            _ok(
                {
                    "user_id": result["user_id"],
                    "session_started_at": result["session_started_at"],
                    "session_ended_at": result["session_ended_at"],
                },
                "Sesion cerrada",
            ),
            status=status.HTTP_200_OK
        )

    except Exception as e:
        logger.error(traceback.format_exc())
        return Response(
            _fail("Internal server error", str(e)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
import logging
import os
from django.shortcuts import render
from constantClassApp.constant_creator import constant_class_creator
from .constants import LoggedUserAttributes, ErrorMessage, SuccessMessage
from .models import LoggedUser
from django.http import JsonResponse

logging.basicConfig(
    filename= os.environ.get("SERVER_LOG"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'
)

logger = logging.getLogger(__name__)


def sign_up(request):
    """
    API for user sign up.
    :param request:
    :return: render template:
    """
    if request.method == 'GET':
        return render(
            request,
            template_name="constantClassApp/sign_up.html",
            status=200
        )
    if request.method == 'POST':
        try:
            email = request.POST.get(LoggedUserAttributes.EMAIL, LoggedUserAttributes.EMPTY_STRING)
            password = request.POST.get(LoggedUserAttributes.PASSWORD, LoggedUserAttributes.EMPTY_STRING)
            if email == LoggedUserAttributes.EMPTY_STRING or password == LoggedUserAttributes.EMPTY_STRING:
                return render(
                    request,
                    template_name='constantClassApp/sign_up.html',
                    status=200
                )
            if (LoggedUser.objects.filter(email=email).exists()):
                logger.error(ErrorMessage.USER_ALREADY_EXISTS)
                return render(
                    request,
                    template_name='constantClassApp/sign_up.html',
                    context= ErrorMessage.USER_ALREADY_EXISTS,
                    status=400
                )
            else:
                LoggedUser.objects.create(email=email, password=password)
                return render(
                    request,
                    template_name='constantClassApp/sign_in.html',
                    context=SuccessMessage.USER_CREATED,
                    status=201
                )
        except Exception as error:
            logger.exception(error)
            return render(
                request,
                template_name="constantClassApp/internal_server_error.html",
                status=500
            )


def get_user_count(request):
    """
    API to fetch user count.
    :param request:
    :return JSON:
    """
    if request.method == 'GET':
        try:
            total_users = LoggedUser.objects.count()
            return JsonResponse(
                {LoggedUserAttributes.COUNT: total_users},
                status=200
            )
        except Exception as error:
            logger.error(error)
            return JsonResponse(
                {LoggedUserAttributes.ERROR: LoggedUserAttributes.INTERNAL_SERVER_ERROR},
                status=500
            )

def sign_in(request):
    """
    API for user sign in.
    :param request:
    :return render template:
    """
    if request.method == 'GET':
        return render(
            request,
            template_name='constantClassApp/sign_in.html',
            status=200
        )

    if request.method == 'POST':
        email = request.POST.get(LoggedUserAttributes.EMAIL, LoggedUserAttributes.EMPTY_STRING)
        password = request.POST.get(LoggedUserAttributes.PASSWORD, LoggedUserAttributes.EMPTY_STRING)
        try:
            if email == LoggedUserAttributes.EMPTY_STRING or password == LoggedUserAttributes.EMPTY_STRING:
                return render(
                    request,
                    template_name='constantClassApp/sign_in.html',
                    status=200
                )
            user_object = LoggedUser.objects.get(email=email)
            if user_object.validate_password(password):
                request.session[LoggedUserAttributes.EMAIL] = email
                return render(
                    request, context=SuccessMessage.SIGN_IN_SUCCESSFUL,
                    template_name='constantClassApp/operations.html',
                    status=200
                )
            else:
                logger.exception(ErrorMessage.INCORRECT_PASSWORD)
                return render(
                    request,
                    context=ErrorMessage.INCORRECT_PASSWORD,
                    template_name='constantClassApp/sign_in.html',
                    status=404
                )
        except LoggedUser.DoesNotExist:
            logger.error(LoggedUser.DoesNotExist)
            return render(
                request,
                context=ErrorMessage.USER_DOES_NOT_EXISTS,
                template_name='constantClassApp/sign_in.html',
                status=404
            )

        except Exception as error:
            logger.exception(error)
            return render(
                request,
                template_name="constantClassApp/internal_server_error.html",
                status=500
            )
    else:
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=500
        )

def sign_out(request):
    """
    API for sign out a session.
    :param request:
    :return render template:
    """
    try:
        request.session.pop(LoggedUserAttributes.EMAIL)
        return render(
            request,
            template_name="constantClassApp/sign_in.html",
            context=SuccessMessage.SIGN_OUT_SUCCESSFUL,
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=500
        )

def constant_class_create(request):
    """
    API to create key of constants.
    :param request:
    :return render template:
    """
    if request.method == 'POST':
        try:
            data = request.POST.get(LoggedUserAttributes.DATA)
            constant_class_string = constant_class_creator.check_and_create_constant_class(data)
            if constant_class_string:
                CONST_DICT = {"success": True, "message": constant_class_string}
                return render(
                    request,
                    template_name="constantClassApp/operations.html",
                    context=CONST_DICT,
                    status=200
                )
            else:
                return render(
                    request,
                    template_name="constantClassApp/operations.html",
                    context=ErrorMessage.INVALID_FORMAT,
                    status=400
                )
        except Exception as error:
            logger.error(error)
            return render(
                request,
                template_name="constantClassApp/internal_server_error.html",
                status=500
            )


def home(request):
    """
    API for home page.
    :param request:
    :return render template:
    """
    try:
        return render(
            request,
            template_name="constantClassApp/index.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=500
        )

def handle_unknown_routes(request):
    """
    API to handle unknown routes.
    :param request:
    :return render template:
    """
    try:
        return render(
            request,
            template_name="constantClassApp/unknown_routes.html",
            status=200
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=500
        )













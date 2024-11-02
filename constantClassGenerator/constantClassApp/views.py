import logging
import os
from django.shortcuts import render
from rest_framework import status
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
    if request.method == 'GET':
        return render(
            request,
            template_name="constantClassApp/sign_up.html",
            status=status.HTTP_200_OK
        )
    if request.method == 'POST':
        try:
            email = request.POST.get(LoggedUserAttributes.EMAIL, LoggedUserAttributes.EMPTY_STRING)
            password = request.POST.get(LoggedUserAttributes.PASSWORD, LoggedUserAttributes.EMPTY_STRING)
            if email == LoggedUserAttributes.EMPTY_STRING or password == LoggedUserAttributes.EMPTY_STRING:
                return render(
                    request,
                    template_name='constantClassApp/sign_up.html',
                    context=SuccessMessage.USER_CREATED,
                    status=status.HTTP_200_OK
                )
            if (LoggedUser.objects.filter(email=email).exists()):
                logger.error(ErrorMessage.USER_ALREADY_EXISTS)
                return render(
                    request,
                    template_name='constantClassApp/sign_up.html',
                    context= ErrorMessage.USER_ALREADY_EXISTS,
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                LoggedUser.objects.create(email=email, password=password)
                return render(
                    request,
                    template_name='constantClassApp/sign_in.html',
                    context=SuccessMessage.USER_CREATED,
                    status=status.HTTP_201_CREATED
                )
        except Exception as error:
            logger.exception(error)
            return render(
                request,
                template_name="constantClassApp/internal_server_error.html",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def get_user_count(request):
    if request.method == 'GET':
        try:
            total_users = LoggedUser.objects.count()
            return JsonResponse(
                {LoggedUserAttributes.COUNT: total_users},
                status=status.HTTP_200_OK
            )
        except Exception as error:
            logger.error(error)
            return JsonResponse(
                {LoggedUserAttributes.ERROR: LoggedUserAttributes.INTERNAL_SERVER_ERROR},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

def sign_in(request):
    if request.method == 'GET':
        return render(
            request,
            template_name='constantClassApp/sign_in.html',
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        email = request.POST.get(LoggedUserAttributes.EMAIL, LoggedUserAttributes.EMPTY_STRING)
        password = request.POST.get(LoggedUserAttributes.PASSWORD, LoggedUserAttributes.EMPTY_STRING)

        print(request.method)
        try:
            if email == LoggedUserAttributes.EMPTY_STRING or password == LoggedUserAttributes.EMPTY_STRING:
                return render(
                    request,
                    template_name='constantClassApp/sign_up.html',
                    context=SuccessMessage.USER_CREATED,
                    status=status.HTTP_200_OK
                )
            user_object = LoggedUser.objects.get(email=email)
            if user_object.validate_password(password):
                request.session[LoggedUserAttributes.EMAIL] = email
                return render(
                    request, context=SuccessMessage.SIGN_IN_SUCCESSFUL,
                    template_name='constantClassApp/operations.html',
                    status=status.HTTP_200_OK
                )
            else:
                logger.exception(ErrorMessage.INCORRECT_PASSWORD)
                return render(
                    request,
                    context=ErrorMessage.INCORRECT_PASSWORD,
                    template_name='constantClassApp/sign_in.html',
                    status=status.HTTP_404_NOT_FOUND
                )
        except LoggedUser.DoesNotExist:
            logger.error(LoggedUser.DoesNotExist)
            return render(
                request,
                context=ErrorMessage.USER_DOES_NOT_EXISTS,
                template_name='constantClassApp/sign_in.html',
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as error:
            logger.exception(error)
            return render(
                request,
                template_name="constantClassApp/internal_server_error.html",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def sign_out(request):
    try:
        request.session.pop(LoggedUserAttributes.EMAIL)
        return render(
            request,
            template_name="constantClassApp/sign_in.html",
            context=SuccessMessage.SIGN_OUT_SUCCESSFUL,
            status=status.HTTP_200_OK
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def constant_class_create(request):
    if request.method == 'POST':
        try:
            data = request.POST.get(LoggedUserAttributes.DATA)
            print(data)
            if data:
                constant_class_string = constant_class_creator.create_constant_class(data)
                CONST_DICT = {"success": True, "message": constant_class_string}
                return render(
                    request,
                    template_name="constantClassApp/operations.html",
                    context=CONST_DICT,
                    status=status.HTTP_200_OK
                )
            else:
                return render(
                    request,
                    template_name="constantClassApp/operations.html",
                    context=ErrorMessage.EMPTY_DATA,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as error:
            logger.error(error)
            return render(
                request,
                template_name="constantClassApp/internal_server_error.html",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def home(request):
    try:
        return render(
            request,
            template_name="constantClassApp/index.html",
            status=status.HTTP_200_OK
        )
    except Exception as error:
        logger.error(error)
        return render(
            request,
            template_name="constantClassApp/internal_server_error.html",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )













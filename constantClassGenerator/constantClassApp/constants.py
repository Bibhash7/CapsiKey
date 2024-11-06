class LoggedUserAttributes:
    EMAIL = 'email'
    PASSWORD = 'password'
    EMPTY_STRING = ""
    DATA = "data"
    COUNT = "count"
    ERROR = "error"
    INTERNAL_SERVER_ERROR = "internal server error."
class ErrorMessage:
    USER_ALREADY_EXISTS = {"success": False, "message": "User already exists in DB."}
    NOT_A_ALPHA_STRING = {"success": False, "message": "Only alpha string with _ is allowed."}
    INCORRECT_PASSWORD = {"success": False, "message": "Invalid username or password."}
    USER_DOES_NOT_EXISTS = {"success": False, "message": "User does not exists, please sign up."}
    INVALID_FORMAT = {"success": False, "message": "Provide a string of alphabetic characters only, allowing underscores; comma, space or newline-separated."}

class SuccessMessage:
    USER_CREATED = {"success": True, "message": "User Created."}
    CONSTANT_CLASS_GENERATED ={"success": True,"message": "Constant class generated."}
    SIGN_IN_SUCCESSFUL = {"success": True, "message": "Successfully signed in."}
    SIGN_OUT_SUCCESSFUL = {"success": True, "message": "Successfully signed out."}

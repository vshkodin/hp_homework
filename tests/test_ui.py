def test_sign_in(holistiplan):
    """
    Test case to ensure that user can be authenticated.
    """
    # Authenticate user
    holistiplan.login_logout.sign_in()


def test_logout(holistiplan):
    """
    Test case to ensure that user can Log out.
    """
    # Authenticate user
    holistiplan.login_logout.sign_in()

    # Logout User
    holistiplan.login_logout.sign_out()


def test_reset_password(holistiplan):
    """
    Test case to ensure that user reset password.
    """

    # Validate forgot password page
    holistiplan.login_logout.validate_forgot_password_page()


def test_validate_signup_link_on_signin_page(holistiplan):
    """
    Test case to ensure signup link is working on sign in page.
    """

    # Validate forgot password page
    holistiplan.login_logout.validate_signup_link()



# def test_sign_up(holistiplan):
#     """
#     Test case to ensure that user can Log out.
#     """
#     # Authenticate user
#     holistiplan.login()
#
#     # Validate authentication
#     holistiplan.check_user_authentication()
#
#
# def test_profile_change_name(holistiplan):
#     """
#     Test case to ensure that user can Log out.
#     """
#     # Authenticate user
#     holistiplan.login()
#
#     # Validate authentication
#     holistiplan.check_user_authentication()
#
#     # Logout User
#     holistiplan.change_user_name("Vlad")
#
#     holistiplan.change_user_name("Vlad")
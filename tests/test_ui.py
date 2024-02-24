import pytest


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


def test_validate_signup(holistiplan):
    """
    Test case to ensure signup is working on sign in page.
    """

    # Validate signup
    holistiplan.signup.sign_up()


def test_validate_password_check(holistiplan):
    """
    Test case to ensure password checks are working.
    """

    # Update name of user
    holistiplan.signup.validate_password_check()


def test_update_name_user(holistiplan):
    """
    Test case to ensure that user can update name.
    """
    # Authenticate user
    holistiplan.login_logout.sign_in()

    # Update name of user
    holistiplan.profile.update_name_of_user()


def test_redeem_points(holistiplan):
    """
    Test case to ensure that user can Redeem points.
    """
    holistiplan.home.redeem_points()


def test_clear_points(holistiplan):
    """
    Test case to ensure that user clear points.
    """
    holistiplan.home.clear_points()

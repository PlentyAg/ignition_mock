# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Utility module."""

__all__ = [
    'get_function_name',
    'set_locale',
    'validate_form'
]

import traceback

import system.util
from incendium import constants


def get_function_name():
    """Returns the name of the function last called.

    Returns:
        str: Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]


def set_locale(user):
    """Sets the Locale to the user's default Language. If none is
    configured, the default will be English (US).

    Args:
        user (_User): The User.
    """
    locale = constants.DEFAULT_LANGUAGE

    if user and user.get_locale():
        locale = user.get_locale()

    system.util.setLocale(locale)


def validate_form(strings=None, numbers=None, collections=None):
    """Performs a form validation.

    Args:
        strings (dict): A dictionary containing all strings which must
            not be empty. Optional.
        numbers (dict): A dictionary containing all numbers which must
            be greater than zero. Optional.
        collections (dict): A dictionary containing all collections
            which must at least contain an element. Optional.

    Returns:
        tuple: A tuple containing:
            is_valid (bool): True if all validation tests have passed,
                False otherwise.
            error_message (str): Error message in case any validation
                test has failed.
    """
    # Initialize variables.
    is_valid = True
    error_message = constants.EMPTY_STRING

    if strings:
        for k, v in strings.iteritems():
            if not v:
                error_message += constants.NEW_TABBED_LINE + k
                is_valid = False
    if numbers:
        for k, v in numbers.iteritems():
            if v is None or v <= 0:
                error_message += constants.NEW_TABBED_LINE + k
                is_valid = False
    if collections:
        for k, v in collections.iteritems():
            if v is None or v <= 0:
                error_message += constants.NEW_TABBED_LINE + k
                is_valid = False

    return is_valid, error_message

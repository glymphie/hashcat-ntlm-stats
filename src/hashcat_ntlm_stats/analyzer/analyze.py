from .password_patterns import find_custom_patterns, find_zxcvbn_patterns


def analyze(list_of_cracked_users):
    """Analyze password patterns and add labels to each cracked user."""

    for user in list_of_cracked_users:
        if not user.cracked:
            continue

        patterns = set()
        patterns.update(find_custom_patterns(user.cracked_password))
        patterns.update(find_zxcvbn_patterns(user.cracked_password))

        user.password_patterns = sorted(patterns)

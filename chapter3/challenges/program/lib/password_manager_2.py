# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():

    def __init__(self):
        self.password_manager = {}

    # Abstraction func to check password is valid
    def is_password_valid(self, password):
        special_chars = '!@$%&'
        return len(password) > 7 and any(i in password for i in special_chars)

    # Abstraction func to return True if password argument doesn't already exist in password_manager - used in both add() and update() funcs
    def is_password_unique(self, password):
        if self.password_manager != {}:
            # Finds any password already in password manager that is a duplicate of password argument
            password_duplicate = list(filter(lambda item: item[1]['password'] == password, self.password_manager.items()))
            return password_duplicate == []
        return True

    def add(self, service, password):
        if self.is_password_unique(password) and self.is_password_valid(password):
            self.password_manager[service] = {
                'password': password,
                'added_on': datetime.now()
            }
        
    def list_services(self):
        return list(self.password_manager.keys())

    def remove(self, service):
        self.password_manager.pop(service)
        
    def update(self, service, password):
        if self.is_password_unique(password) and self.is_password_valid(password):
            self.password_manager[service]['password'] = password

    # Returns password of service, if service exists, otherwise .get() method returns 'None' as default
    def get_for_service(self, service):
        # First link of .get() chain provides default value of empty dict if no such service found.
        # Without default, would throw error on moving to second .get() link as you can't call .get() on value None
        return self.password_manager.get(service, {}).get('password')
    
    # Defines function with arbitrary positional argument 'reversed' to accept 'reverse' option
    def sort_services_by(self, sort_by, *reversed):
        # 'is_reversed' = True if 'reverse' option included.
        is_reversed = reversed == ('reverse',)
        if sort_by == 'service':
            return sorted(self.password_manager.keys(), reverse=is_reversed)
        else:
            # Creates dict with only service names and corresponding 'added_on' times
            dict_to_sort = {k: v['added_on'] for k, v in self.password_manager.items()}
            # Sorts above dictionary by added_on value (kvpair[1]) and reverses if required
            sorted_tuples_list = sorted(dict_to_sort.items(), key=lambda kvpair: kvpair[1], reverse=is_reversed)
            return [item[0] for item in sorted_tuples_list]

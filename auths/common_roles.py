from auths.models import User
def is_superagent(user):
    if user.role:
        if user.role.perm:
            if user.role.perm.filter(perm_name__iexact='is_superagent').exists():
                return True
    return False

def is_agent(user):
    if user.role:
        if user.role.perm:
            if user.role.perm.filter(perm_name__iexact='is_agent').exists():
                return True
    return False
def is_admin(user):
    if user.role:
        if user.role.perm:
            if user.role.perm.filter(perm_name__iexact='is_admin').exists():
                return True
    return False

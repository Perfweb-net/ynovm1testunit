import re

def is_valid_email(email):
    """Valide une adresse email."""
    if not isinstance(email, str):
        raise TypeError("L'email doit être une chaîne")
    
    if email.count('@') != 1:
        return False
    
    local_part, domain = email.split('@')
    
    # Validation partie locale (1-64 caractères alphanumériques/points/tirets)
    if not re.match(r'^[a-zA-Z0-9._-]{1,64}$', local_part):
        return False
    
    # Validation domaine avec extension 2-4 lettres
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', domain):
        return False
    
    return True

def validate_password_strength(password):
    """Évalue la force d'un mot de passe."""
    if not isinstance(password, str):
        raise TypeError("Le mot de passe doit être une chaîne")
    
    result = {
        'is_valid': False,
        'score': 0,
        'missing_criteria': []
    }
    
    # Critères de validation
    criteria = {
        'Longueur >= 8': len(password) >= 8,
        'Au moins 1 majuscule': any(c.isupper() for c in password),
        'Au moins 1 minuscule': any(c.islower() for c in password),
        'Au moins 1 chiffre': any(c.isdigit() for c in password),
        'Au moins 1 caractère spécial': any(c in '!@#$%^&*' for c in password)
    }
    
    # Calcul du score et des critères manquants
    for criterion, is_met in criteria.items():
        if is_met:
            result['score'] += 1
        else:
            result['missing_criteria'].append(criterion)
    
    result['is_valid'] = result['score'] >= 4
    return result 
class ExternalServiceError(Exception):
    """Raised when a call to an external API or service fails."""


class AuthenticationError(Exception):
    """Raised when JWT tokens or API‐keys fail validation."""


class ValidationError(Exception):
    """Raised when input data fails business or schema validation."""
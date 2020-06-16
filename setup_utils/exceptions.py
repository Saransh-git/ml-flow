class VersionException(Exception):
    def __init__(self, reason=None):
        self.reason = reason
        self.description = 'Version not defined'
        super().__init__(self.description, self.reason)

    def __str__(self):
        return f"VersionException: {self.description} - {self.reason}"

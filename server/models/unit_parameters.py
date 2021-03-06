from modules.model import Model
from modules.validations import is_required, is_string


class UnitParameters(Model):
    tablename = 'units_parameters'

    schema = dict(Model.schema.copy(), **{
        'entity_id': {  # TODO-3 validate foreign
            'validate': (is_required, is_string),
        },
    })

    def get_learners(self):
        """

        """

    def get_difficulty(self):
        """

        """

    def get_quality(self):
        """

        """

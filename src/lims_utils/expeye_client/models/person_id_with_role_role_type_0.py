from enum import StrEnum


class PersonIdWithRoleRoleType0(StrEnum):
    ALTERNATE_CONTACT = "Alternate Contact"
    ASSOCIATE = "Associate"
    CO_INVESTIGATOR = "Co-Investigator"
    DATA_ACCESS = "Data Access"
    ERA_ADMIN = "ERA Admin"
    LOCAL_CONTACT = "Local Contact"
    LOCAL_CONTACT_2 = "Local Contact 2"
    PRINCIPAL_INVESTIGATOR = "Principal Investigator"
    STAFF = "Staff"
    TEAM_LEADER = "Team Leader"
    TEAM_MEMBER = "Team Member"

    def __str__(self) -> str:
        return str(self.value)

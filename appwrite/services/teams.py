from appwrite.service import Service


class Teams(Service):

    def update_team(self, collection_id, name, read="[]", write="[]", rules="[]"):
        """Update Team"""
        pass

    def list_teams(self, search='', limit=25, offset=0, order_type='ASC'):
        """List Teams"""
        pass

    def create_team(self, name, roles="[\"owner\"]"):
        """Create Team"""
        pass

    def get_team(self, team_id):
        """Get Team"""
        pass

    def update_team(self, team_id, name):
        """Update Team"""
        pass

    def delete_team(self, team_id):
        """Delete Team"""
        pass

    def get_team_members(self, team_id):
        """Get Team Members"""
        pass

    def create_team_membership(self, team_id, email, roles, redirect, name=''):
        """Create Team Membership"""
        pass

    def delete_team_membership(self, team_id, invite_id):
        """Delete Team Membership"""
        pass

    def create_team_membership_resend(self, team_id, invite_id, redirect):
        """Create Team Membership (Resend Invitation Email)"""
        pass

    def update_team_membership_status(self, team_id, invite_id, user_id, secret, success='', failure=''):
        """Update Team Membership Status"""
        pass

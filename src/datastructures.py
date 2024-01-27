
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name,):
        self.last_name = last_name
        # example list of members
        self._members = []
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member: dict):
        if "id" not in member:
            member["id"] = self._generateId()
        # member["last_name"] = self.last_name
        self._members.append(member)
        # fill this method and update the return
        # pass

    def delete_member(self, id):
        # self.members = list(
        #     filter(lambda member : member["id"] != id, self._members)
        # )
        # pass
        for member in self._members:
            if id == member["id"]:
                return self._members.remove(member)

    # def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id

        # pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        # member = list(
        #     filter(lambda member: member["id" == id, self._members])
        # )
        # return member[0]
        # pass
        for member in self._members:
            if id == member["id"]:
                return member


    def get_all_members(self):
        return self._members
        
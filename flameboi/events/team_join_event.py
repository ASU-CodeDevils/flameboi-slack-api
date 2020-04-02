from flameboi.common.IEvent import Event

class TeamJoinEvent(Event):

    def __init__(self, payload):
        super().__init__(payload)

    def get_details(self) -> dict:
        return {
            'user_id': self.event.get('user', {}).get('id')
        }
        

    # assert theBot.send_onboarding_DM(user_id)["ok"]
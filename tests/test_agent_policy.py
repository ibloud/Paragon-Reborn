import unittest

from security.agent_policy import Action, Authorization, Decision, Observation, State, authorize, transition

GOOD = Authorization(True, True, True, True, True)


class AgentPolicyTests(unittest.TestCase):
    def test_missing_authorization_fails_closed(self):
        auth = Authorization(True, True, True, False, True)
        self.assertEqual(authorize(auth, Action.READ, Observation()), Decision.STOP)

    def test_missing_identity_fails_closed(self):
        auth = Authorization(False, True, True, True, True)
        self.assertEqual(authorize(auth, Action.READ, Observation()), Decision.STOP)

    def test_unknown_is_not_authorized(self):
        self.assertEqual(authorize(GOOD, Action.READ, Observation(unknown=True)), Decision.STOP)

    def test_suspicious_contains(self):
        self.assertEqual(authorize(GOOD, Action.READ, Observation(suspicious=True)), Decision.CONTAIN)

    def test_forbidden_denies_immediately(self):
        self.assertEqual(authorize(GOOD, Action.ACT, Observation(forbidden=True)), Decision.DENY)

    def test_normal_action_continues_only_with_complete_authority(self):
        self.assertEqual(authorize(GOOD, Action.READ, Observation()), Decision.CONTINUE)

    def test_invalid_containment_transition_fails_closed(self):
        with self.assertRaises(ValueError):
            transition(State.NORMAL, State.RELEASED)

    def test_containment_requires_review_before_release(self):
        self.assertEqual(transition(State.CONTAINED, State.REVIEWED), State.REVIEWED)
        with self.assertRaises(ValueError):
            transition(State.CONTAINED, State.RELEASED)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.gemini_metatron_core.workflow import WorkflowManager

class TestWorkflowManager(unittest.TestCase):
    def test_workflow_execute_success(self):
        manager = WorkflowManager()
        result = manager.execute("test_workflow")
        self.assertTrue(result)

    def test_workflow_execute_empty_name(self):
        manager = WorkflowManager()
        with self.assertRaises(ValueError) as context:
            manager.execute("")
        self.assertEqual(str(context.exception), "Workflow name cannot be empty.")

    def test_workflow_execute_none_name(self):
        manager = WorkflowManager()
        with self.assertRaises(ValueError) as context:
            manager.execute(None)
        self.assertEqual(str(context.exception), "Workflow name cannot be empty.")

if __name__ == '__main__':
    unittest.main()

import unittest
from src.gemini_metatron_core.engine import Engine

class TestEngine(unittest.TestCase):
    def test_engine_start_success(self):
        engine = Engine()
        result = engine.start()
        self.assertTrue(result)
        self.assertTrue(engine.is_running)

    def test_engine_start_already_running(self):
        engine = Engine()
        engine.start()
        with self.assertRaises(RuntimeError) as context:
            engine.start()
        self.assertEqual(str(context.exception), "Engine is already running.")

if __name__ == '__main__':
    unittest.main()

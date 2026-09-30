import unittest
from src.gemini_metatron_core.mcp import MCPServer

class TestMCPServer(unittest.TestCase):
    def test_mcp_connect_success(self):
        server = MCPServer()
        result = server.connect()
        self.assertTrue(result)
        self.assertTrue(server.connected)

    def test_mcp_connect_already_connected(self):
        server = MCPServer()
        server.connect()
        with self.assertRaises(ConnectionError) as context:
            server.connect()
        self.assertEqual(str(context.exception), "Already connected to an MCP server.")

if __name__ == '__main__':
    unittest.main()

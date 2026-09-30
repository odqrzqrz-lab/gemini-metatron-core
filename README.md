# gemini-metatron-core

Central engine for Gemini-powered metacognitive workflows, MCP server integrations, and next-gen agent architectures.

## Architecture

This project provides the core components necessary to build metacognitive, Gemini-powered AI workflows. The architecture is modular and built on three primary components:

1.  **Metatron Engine (`src.gemini_metatron_core.engine.Engine`)**: The central orchestrator that manages the state of the system.
2.  **MCP Server Integration (`src.gemini_metatron_core.mcp.MCPServer`)**: A robust integration module designed to interface seamlessly with Model Context Protocol (MCP) servers, enabling advanced contextual data handling.
3.  **Metacognitive Workflow Manager (`src.gemini_metatron_core.workflow.WorkflowManager`)**: Provides the logic to execute and manage multi-step metacognitive reasoning workflows.

Each module includes robust error handling to ensure stability when running complex operations.

## Setup Instructions

### Prerequisites

*   Python 3.8+

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gemini-metatron-core.git
    cd gemini-metatron-core
    ```
2.  Install dependencies (currently only testing dependencies are needed):
    ```bash
    pip install -r requirements.txt
    ```

## Usage Examples

Here is a basic example of how you can use the core components together in your Python application:

```python
import logging
from src.gemini_metatron_core.engine import Engine
from src.gemini_metatron_core.mcp import MCPServer
from src.gemini_metatron_core.workflow import WorkflowManager

logging.basicConfig(level=logging.INFO)

# 1. Initialize and start the Engine
engine = Engine()
try:
    engine.start()
except RuntimeError as e:
    print(f"Error starting engine: {e}")

# 2. Connect to an MCP Server
mcp_server = MCPServer(host="localhost", port=8000)
try:
    mcp_server.connect()
except ConnectionError as e:
    print(f"Error connecting to MCP server: {e}")

# 3. Execute a Metacognitive Workflow
workflow_manager = WorkflowManager()
try:
    workflow_manager.execute("analyze_context_workflow")
except ValueError as e:
    print(f"Error executing workflow: {e}")
```

## Running Tests

Unit tests are written using the standard `unittest` framework. To run the tests, execute the following command from the root directory:

```bash
python -m unittest discover tests/
```

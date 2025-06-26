# mcp-tutorial

1. Install [`devbox`](https://www.jetify.com/docs/devbox/installing_devbox/) to set this project up in an isolated environment, or use another virtual environment manager like `venv`, `conda`, `uv`.
2. If using devbox, start the environment defined in `devbox.json` using `devbox shell`.
3. An example MCP server is defined in `calculator.py` with the tool: `add` to add two numbers.
4. The MCP server can be run using `uv python run calculator.py`.
5. In `devbox.json`, I have defined a custom run script `mcp-run-calculator` to invoke the server.
6. Add MCP server to an MCP client like Claude Desktop by editing its config file. On MacOS, its location is `~/Library/Application Support/Claude/claude_desktop_config.json`.
7. The following code in the config file will attach the `add` tool to Claude Desktop:
   ```
   {
     "mcpServers": {
       "calculator": {
         "command": "devbox",
         "args": [
           "-c",
           "/location/of/mcp-tutorial",
           "run",
           "mcp-run-calculator"
         ]
       }
     }
   }
   ```
8. After restarting Claude Desktop, the tool should appear as `calculator` in the toggle box of the text input.
   <img width="707" alt="Image" src="https://github.com/user-attachments/assets/1e48d190-7bbc-4df5-97c4-abc6155903ba" />
9. Test the tool by typing a prompt like - "add 42 and 999".
10. Build your own MCP server!
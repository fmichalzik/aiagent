# aiagent
A toy version of Claude Code using Google's free Gemini API!

Building an LLM-powered command-line program capable of reading, updating, and running Python code using the Gemini API. <br>
Guided by the [Boot.dev course - Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python), the goal is to learn how LLMs and agentic coding tools work.

> [!CAUTION]  
> Remember, it is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code.
> Even their tools aren't perfectly secure, so be careful what you give it access to, and don't give this code away to anyone else to use.

#### What Does the Agent Do?

1. Accepts a coding task (e.g., "strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽")
2. Chooses from a set of predefined functions to work on the task, for example:
      - Scan the files in a directory
      - Read a file's contents
      - Overwrite a file's contents
      - Execute the python interpreter on a file
3. Repeats step 2 until the task is complete (or it fails miserably, which is possible)

#### Learning Goals
Learn how LLMs and agentic coding tools work. <br>
Practice Python and functional programming skills.

#### Setup
Create a virtual environment at the top level of the project. <br>
```python3 -m venv venv```

Activate the virtual environment. <br>
```source venv/bin/activate```

Install the requirements. <br>
```pip install -r requirements.txt```

#### Usage
From the terminal, start the main script by passing the prompt as an argument ('--verbose' optional).
Example:
```python main.py "How do I build a calculator app?" --verbose```

The scope (working directory) for the predefined functions can be set in the config file. Do not give an LLM broader access to you maschine!  

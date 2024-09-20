## Using the `llms-ctx.txt` file

The easiest way to get started with AI assistance is to use the `llms-ctx.txt` file. This file contains a context overview in a format that can be easily navigated by LLMs.

It follows the structure outlined by FastAi to provide LLM's with an easily understood/ navigatable context all in a single file. A full reference can be found <a href="https://llmstxt.org/" target="_blank">here.</a>

To implement this file in Cursor for example, type `@doc` or navigate to _Cursor Settings>Features>Docs_. Then, choose “Add new doc” and add a reference to the `llms-ctx.txt` file below:

> <a href="https://www.shad4fasthtml.com/llms-ctx.txt">llms-ctx.txt</a>

This can then be referenced in Cursor using the `@doc` command, giving it access to the full context of the project - including all current component documentation.

Further experimentation is required to properly optimize this file for LLM use, and I will continue to update it as test new methods and formats.

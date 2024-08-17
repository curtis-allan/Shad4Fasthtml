## Quick Start Guide

### Setup & Installation

Getting started with Shadcn UI for FastHTML is quick and easy. Follow these simple steps to set up your project:

1. Copy the `shadcn.py` file from the GitHub repository into your FastHTML project directory.

   > **Note:** A pip module will be available in the near future. This is a temporary solution.

2. Add the following import statements to the top of the file where you want to use the components:

   ```python
   from fasthtml import *
   from shadcn import *
   ```

3. Include the Shadcn headers in your FastHTML headers and disable the default Pico.css header, as shown below:

   ```python
   app, rt = fast_app(
       pico=False,
       hdrs=(ShadHead(),),
   )
   ```

### You're All Set!

Congratulations! You've successfully set up Shadcn UI for your FastHTML project. You're now ready to start using the UI components in your app.

## Using Components

To implement Shadcn UI components in your codebase, refer to the relevant component documentation. Each component has its own set of properties and usage guidelines.

## Need Help?

If you encounter any issues or have questions, please open an issue on the GitHub repository and either myself or a member of the community will try to help.

Happy coding!

---

*This documentation is a work in progress. I appreciate your patience and feedback as I continue to build upon the repo and this readme. All credits go to <a href="https://x.com/shadcn" target="blank">@Shadcn</a> for the component styles and <a href="https://x.com/jeremyphoward" target="_blank">@JeremyPHoward</a> for the fastHtml framework.*
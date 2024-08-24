*This documentation is a work in progress. I appreciate your patience and feedback as I continue to build upon the repo. All credits go to <a href="https://x.com/shadcn" target="_blank">@Shadcn</a> for the component styles and <a href="https://x.com/jeremyphoward" target="_blank">@JeremyPHoward</a> for the fastHtml framework.*

## Quick Start Guide

### Setup & Installation

Getting started with Shadcn UI for FastHTML is quick and easy. Follow these simple steps to set up your project:

1. Copy the `shadcn.py` file from the GitHub repository into your FastHTML project directory.

> [!NOTE]
>A pip module will be available in the near future. This is a temporary solution.

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

### Configuration

#### Tailwind Configuration

Shadcn-ui components use TailwindCSS for styling by default. Shad4FastHtml now uses the Tailwind CSS standalone package by default, replacing the CDN version. This change allows for minification and bundling of used styles, optimizing the bundle size for production. If you wish to use the CDN instead, set the `tw_link` parameter to `True` in the `ShadHead` function.

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(tw_link=True),),
)
```

>[!TIP]
> Refer to the <a hx-boost="true" href="/getting-started/tailwind-setup">Tailwind Setup Guide</a> for more information.

#### Lucide Icons

As a preference, I have chosen to use Lucide icons for the project. If you wish to use another icon library or wish to ommit the lucide import and script elements, you can do so by setting the `lucide_link` parameter to `False` in the `ShadHead` function.

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(lucid=False),),
)
```

### You're All Set!

Congratulations! You've successfully set up Shad4FastHtml for your project! You're now ready to start using the UI components in your app.

>[!WARNING]
> This project is still in its youth. If you encounter any bugs or issues, please open an issue on the GitHub repository.

## Using Components

To implement Shadcn UI components in your codebase, refer to the relevant component documentation. Each component has its own set of properties and usage guidelines.

## Known Issues

* Using Lucide via the cdn is not an ideal solution, as there are two seperate url's recommended for `dev` and `prod` environments. Will either implement a solution to automate the import or try to find a better solution.

* Toast: Client side render + mobile touch handling. Currently relies on htmx server endpoints for rendering, which is not great for a client-focused UI component. Will update this soon to use the same JS solution as the `dialog` and `sheet` components.

* Add type assertions for all component attributes, with proper error handling and documentation.

* Table demo - theme toggle fix

* **IN PROGRESS** Documentation fixing and cleaning up.

## Need Help?

If you encounter any issues or have questions, please reach out either through the <a href="https://github.com/curtis-allan/shadcn-fasthtml-framework" target="_blank">Github</a> repo or send me a dm on<a href="https://x.com/CurtisJAllan" target="_blank">X aka twitter</a> and either myself or a member of the community will try to help out.